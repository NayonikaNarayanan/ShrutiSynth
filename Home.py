import streamlit as st

# Configure page
st.set_page_config(
    page_title="Home - ShrutiSynth",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply Nexa font and styling
st.markdown("""
<style>
@import url('https://fonts.cdnfonts.com/css/nexa');

.stApp {
    background: radial-gradient(circle at center, #ede9ff 0%, #e6e3ff 50%, #ddd6fe 100%);
    font-family: 'Nexa', 'Helvetica Neue', Arial, sans-serif !important;
    padding-top: 0rem !important;
    margin-top: 0rem !important;
}

.main > div {
    padding-top: 0rem !important;
}

.block-container {
    padding-top: 0rem !important;
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

.center-content {
    text-align: center;
    margin: 1rem 0;
    padding-top: 1rem;
}
.compact-section {
    margin: 0.5rem 0;
}

.feature-card {
    background: rgba(255, 255, 255, 0.1);
    padding: 1rem;
    border-radius: 10px;
    margin: 0.5rem 0;
    border-left: 4px solid #6b46c1;
}

.feature-item {
    text-align: center;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    margin: 0.5rem;
    border: 1px solid rgba(107, 70, 193, 0.1);
}
</style>
""", unsafe_allow_html=True)

# Centered welcome section
st.markdown('<div class="center-content">', unsafe_allow_html=True)
st.title("Welcome to")

# Logo centered and optimized size
try:
    st.image("logo.png", width=380)
except:
    st.markdown("🎵 **ShrutiSynth**")

# Statement below logo with enhanced styling
st.markdown("### AI-Powered Carnatic Music Generator")
st.markdown("*Experience the timeless beauty of Indian classical music through modern AI*")

# Short description
st.markdown("")
st.write("Create authentic Carnatic classical compositions instantly with AI. Choose from traditional ragas, select instruments like Veena or Violin, and generate high-quality music that honors centuries-old musical traditions while embracing cutting-edge technology.")
st.markdown('</div>', unsafe_allow_html=True)

# Key Features Section
st.markdown("#### Key Features")
feature_items = [
    "Authentic Carnatic compositions",
    "15+ traditional instruments", 
    "Classical ragas and talas",
    "AI-powered generation"
]

# Display features in columns
feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)
for i, text in enumerate(feature_items):
    with [feat_col1, feat_col2, feat_col3, feat_col4][i]:
        st.markdown(f"<div class='feature-item'><strong>{text}</strong></div>", unsafe_allow_html=True)

st.markdown("")
if st.button("🎼 Start Creating Music", type="primary", use_container_width=True):
    st.switch_page("pages/Music_Generator.py")