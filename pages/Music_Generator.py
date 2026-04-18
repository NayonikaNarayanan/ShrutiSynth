import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import io
import time
import wave
import struct
import base64
from datetime import datetime
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure page
st.set_page_config(
    page_title="ShrutiSynth - Music Generator",
    page_icon="🎼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply Nexa font and styling
st.markdown("""
<style>
@import url('https://fonts.cdnfonts.com/css/nexa');

.stApp {
    background: linear-gradient(135deg, #f0efff 0%, #e6e3ff 100%);
    font-family: 'Nexa', 'Helvetica Neue', Arial, sans-serif !important;
    padding-top: 0rem !important;
}

.main > div {
    padding-top: 0rem !important;
}

.block-container {
    padding-top: 1.5rem !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Nexa', 'Helvetica Neue', Arial, sans-serif !important;
    font-weight: bold;
    color: #6b46c1;
}

.stMarkdown, .stText, p, span, div {
    font-family: 'Nexa', 'Helvetica Neue', Arial, sans-serif !important;
}

.stButton > button {
    font-family: 'Nexa', 'Helvetica Neue', Arial, sans-serif !important;
    font-weight: 600;
}

.stSelectbox label, .stSlider label, .stTextArea label {
    font-family: 'Nexa', 'Helvetica Neue', Arial, sans-serif !important;
    font-weight: 500;
}

.stSidebar {
    font-family: 'Nexa', 'Helvetica Neue', Arial, sans-serif !important;
}

.generation-status {
    background: linear-gradient(135deg, rgba(107, 70, 193, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
    border: 2px solid rgba(107, 70, 193, 0.3);
    border-radius: 15px;
    padding: 1.5rem 2rem;
    margin: 2rem 0;
    color: #6b46c1;
    font-weight: 600;
    text-align: center;
    backdrop-filter: blur(10px);
    font-size: 1.1rem;
}
</style>
""", unsafe_allow_html=True)

def extract_waveform_data(audio_data, num_bars=64):
    """Extract waveform data for visualization from audio signal."""
    if hasattr(audio_data, 'flatten'):
        audio_flat = audio_data.flatten()
    else:
        audio_flat = np.array(audio_data)
    
    # Calculate chunk size
    chunk_size = max(1, len(audio_flat) // num_bars)
    waveform_data = []
    
    for i in range(num_bars):
        start_idx = i * chunk_size
        end_idx = min(start_idx + chunk_size, len(audio_flat))
        
        if start_idx < len(audio_flat):
            chunk = audio_flat[start_idx:end_idx]
            # Calculate RMS amplitude for this chunk
            rms = np.sqrt(np.mean(chunk**2)) if len(chunk) > 0 else 0
            # Scale to pixel height (15-60px range for compact display)
            height = max(15, min(60, int(rms * 80 + 15)))
            waveform_data.append(height)
        else:
            waveform_data.append(15)
    
    return waveform_data

# Header with optimized logo
st.markdown("")  # Add top spacing
col_logo, col_spacer = st.columns([1.2, 3.8])
with col_logo:
    try:
        st.image("logo.png", width=180)
    except:
        st.markdown("🎵")

# Main interface
col1, col2 = st.columns([1.8, 1.2])

with col1:
    st.markdown('<h3 style="color: #6b46c1; font-family: \'Nexa\', \'Helvetica Neue\', Arial, sans-serif; font-weight: bold;">Compose Your Music</h3>', unsafe_allow_html=True)
    
    # Raga selection
    ragas = [
        "Any Raga",
        "Kalyani", "Sankarabharanam", "Kharaharapriya", "Mayamalavagowla",
        "Mohana", "Hindolam", "Bilahari", "Shanmukhapriya", "Charukeshi",
        "Kambhoji", "Harikambhoji", "Natabhairavi", "Todi", "Bhairavi"
    ]
    
    selected_raga = st.selectbox("Choose Raga:", ragas)
    
    # Instrument selection
    instruments = [
        "Any Instrument",
        "Violin", "Veena", "Flute", "Sitar", "Mridangam", 
        "Tabla", "Ghatam", "Kanjira", "Vocal", "Nadaswaram"
    ]
    
    selected_instrument = st.selectbox("Choose Instrument:", instruments)
    
    # Check if an example prompt was selected
    default_prompt = ""
    if "selected_prompt" in st.session_state:
        default_prompt = st.session_state.selected_prompt
        del st.session_state.selected_prompt
    
    prompt = st.text_area(
        "Describe additional details (optional):",
        value=default_prompt,
        height=100,
        placeholder="Add specific style, tempo, or mood details..."
    )
    
    # Parameters
    col_a, col_b = st.columns(2)
    with col_a:
        duration = st.slider("Duration (seconds)", 5, 60, 15, 5)
    with col_b:
        tempo = st.selectbox("Tempo", ["Slow", "Medium", "Fast"], index=1)

with col2:
    st.markdown("#### Musical Techniques")
    st.markdown("*Click to enhance your composition*")
    
    example_prompts = [
        " Soulful alapana improvisation",
        " Intricate korvai rhythms", 
        " Traditional gamaka ornaments",
        " Melodic violin passages",
        " Percussive mridangam beats",
        " Devotional bhajan style"
    ]
    
    for i, example in enumerate(example_prompts):
        if st.button(example, key=f"example_{i}", use_container_width=True):
            style_text = example.split(" ", 1)[1]
            st.session_state.selected_prompt = style_text
            st.rerun()
    
    # Add mood selection
    st.markdown("#### Mood")
    mood = st.selectbox("Select Mood:", [
        "Peaceful", "Devotional", "Energetic", "Melancholic", 
        "Celebratory", "Meditative", "Romantic", "Heroic"
    ], key="mood_select")

# Generate button (outside columns)
if st.button("🎵 Generate Music", type="primary", use_container_width=True):
    # Create comprehensive prompt combining all selections
    instrument_text = selected_instrument if selected_instrument != "Any Instrument" else "traditional instrument"
    raga_text = selected_raga if selected_raga != "Any Raga" else "classical raga"
    
    full_prompt = f"{instrument_text} in {raga_text}, {tempo.lower()} tempo, {mood.lower()} mood"
    if prompt.strip():
        full_prompt += f", {prompt}"
        
    with st.spinner("Generating your Carnatic music composition..."):
        try:
            # Try to import and use the generator
            from complete_carnatic_generator import MusicGen, torch
            
            # Initialize AudioCraft MusicGen model
            device = torch.device('cpu')
            model = MusicGen.get_pretrained('facebook/musicgen-medium', device)
            
            # Set AudioCraft generation parameters
            model.set_generation_params(
                duration=duration,
                temperature=1.0,
                top_k=250,
                top_p=0.9,
                cfg_coeff=3.0,
                selected_raga=selected_raga if selected_raga != "Any Raga" else "Sankarabharanam",
                selected_instrument=selected_instrument if selected_instrument != "Any Instrument" else "Violin"
            )
            
            start_time = time.time()
            with torch.no_grad():
                generated = model.generate([full_prompt], progress=True)
                audio_data = generated[0].cpu().numpy()
                sample_rate = 22050
            
            # Convert to audio bytes for download
            def save_audio(audio_data, sample_rate):
                buffer = io.BytesIO()
                if len(audio_data.shape) > 1:
                    audio_data = audio_data.flatten()
                audio_int16 = (audio_data * 32767).astype(np.int16)
                with wave.open(buffer, 'wb') as wav_file:
                    wav_file.setnchannels(1)
                    wav_file.setsampwidth(2)
                    wav_file.setframerate(sample_rate)
                    wav_file.writeframes(audio_int16.tobytes())
                buffer.seek(0)
                return buffer.getvalue()
            
            audio_bytes = save_audio(audio_data, sample_rate)
            st.session_state.generated_audio = audio_bytes
            st.session_state.audio_data = audio_data
            st.session_state.sample_rate = sample_rate
            st.session_state.generation_time = time.time() - start_time
            st.session_state.last_prompt = full_prompt
            st.session_state.last_raga = selected_raga
            st.session_state.last_instrument = selected_instrument
            st.session_state.last_mood = mood
            st.session_state.last_duration = duration
            st.session_state.last_temperature = 1.0
            
            st.success(f"Generated: {full_prompt}")
            st.info(f"Using: {selected_raga} raga with {selected_instrument} in {mood.lower()} mood")
            
        except ImportError:
            st.error("Carnatic Generator not found. Please ensure complete_carnatic_generator.py is available.")
        except Exception as e:
            st.error(f"Generation failed: {str(e)}")

# Display generated audio
if 'generated_audio' in st.session_state and st.session_state.generated_audio is not None:
    st.markdown("---")
    st.markdown("#### 🎧 Generated Music")
    
    # Display track info and waveform visualization
    if 'audio_data' in st.session_state and 'sample_rate' in st.session_state:
        # Display track info
        raga_display = st.session_state.last_raga if hasattr(st.session_state, 'last_raga') else "Generated"
        instrument_display = st.session_state.last_instrument if hasattr(st.session_state, 'last_instrument') else "Composition"
        
        col_info1, col_info2 = st.columns([3, 1])
        with col_info1:
            st.markdown(f"**🎵 {raga_display} - {instrument_display}**")
        with col_info2:
            st.markdown("*ShruthiSynth AI*")
        
        # Create animated waveform visualization
        waveform_data = extract_waveform_data(st.session_state.audio_data, num_bars=60)
        
        # Create animated wave bars using CSS keyframes
        wave_html = '<div style="display: flex; align-items: end; justify-content: center; height: 100px; gap: 2px; padding: 20px; background: linear-gradient(135deg, rgba(255, 255, 255, 0.4) 0%, rgba(107, 70, 193, 0.05) 100%); border-radius: 15px; margin: 20px 0; border: 1px solid rgba(107, 70, 193, 0.2); overflow: hidden; box-shadow: 0 4px 12px rgba(107, 70, 193, 0.1);">'
        
        for i, height in enumerate(waveform_data):
            delay = (i * 0.05) % 2.0  # Stagger animation delays
            wave_html += f'''
            <div style="
                width: 4px; 
                height: {height}px; 
                background: linear-gradient(to top, #6b46c1 0%, #8b5cf6 50%, #a855f7 100%);
                border-radius: 2px;
                animation: wave-pulse 2s ease-in-out infinite;
                animation-delay: {delay}s;
                box-shadow: 0 2px 4px rgba(107, 70, 193, 0.2);
                transform-origin: bottom;
            "></div>'''
        
        wave_html += '</div>'
        
        # Add custom CSS for wave animation
        animation_css = """
        <style>
        @keyframes wave-pulse {
            0%, 100% { 
                transform: scaleY(0.3);
                opacity: 0.6; 
            }
            25% { 
                transform: scaleY(0.8);
                opacity: 0.8; 
            }
            50% { 
                transform: scaleY(1.2);
                opacity: 1; 
            }
            75% { 
                transform: scaleY(0.9);
                opacity: 0.9; 
            }
        }
        </style>
        """
        
        # Display animated waveform
        st.markdown(animation_css + wave_html, unsafe_allow_html=True)
        
        # Standard audio player
        st.audio(st.session_state.generated_audio, format="audio/wav")
    else:
        # Fallback to basic player
        st.audio(st.session_state.generated_audio, format="audio/wav")
    
    # Info and download in columns
    col_info1, col_info2, col_info3, col_info4 = st.columns(4)
    
    with col_info1:
        if hasattr(st.session_state, 'last_duration'):
            st.metric("Duration", f"{st.session_state.last_duration}s")
    with col_info3:
        if hasattr(st.session_state, 'generation_time'):
            st.metric("Generated in", f"{st.session_state.generation_time:.1f}s")
    with col_info4:
        if hasattr(st.session_state, 'last_raga'):
            st.metric("Raga", st.session_state.last_raga)
    
    # Download button
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"carnatic_music_{timestamp}.wav"
    
    col_download1, col_download2 = st.columns([1, 1])
    with col_download1:
        st.download_button(
            label="💾 Download Audio",
            data=st.session_state.generated_audio,
            file_name=filename,
            mime="audio/wav"
        )