# ShrutiSynth — AI-Powered Carnatic Music Generator
PS-1 internship project at Swecha Tech - May-July 2025

ShrutiSynth is an AI application that generates Carnatic classical music using digital signal processing and a custom audio synthesis engine. Built as a foundational prototype for Swecha's broader Indian-language AI roadmap, the project addresses a gap in existing AI music tools, which are largely built around Western music frameworks and lack support for the structural and tonal grammar of Carnatic music.

The application allows users to select traditional Carnatic Indian ragas, instruments, and moods, and generates expressive compositions with varied tempo and gamaka ornamentation. It is designed to be accessible to non-musicians while remaining grounded in the musicological conventions of the form.

## Project Background

ShrutiSynth was developed during a 5-day rapid prototyping sprint as part of an internship at Swecha Tech (May–July 2025). The work involved competitive analysis of existing AI music generators, definition of MVP scope and accuracy benchmarks, and validation of generated outputs against domain expertise in Carnatic vocals — including evaluation of raga scales, gamaka ornamentations, and instrument-specific harmonic characteristics.

The current implementation uses a custom Python audio synthesis engine. An AudioCraft / MusicGen abstraction layer is built into the architecture to support future integration of larger generative models.

## Features

- **Raga-based composition** supporting ragas including Kalyani, Sankarabharanam, Kharaharapriya, Todi, Bhairavi, and more
- **Instrument selection** across traditional instruments such as Veena, Flute, Violin, Tabla, and Nadaswaram
- **Mood-driven note weighting** with prompt structures for forms such as alapana, korvai, and bhajan
- **Streamlit-based interface** with multi-page navigation, real-time playback, waveform visualization, and WAV export
- **Integrated learning module** providing context on ragas, instruments, notable compositions, and legendary Carnatic artists
- **Modular generator core** that handles raga logic, tempo, and instrument synthesis

## Project Structure

| File | Description |
|------|-------------|
| `Home.py` | Streamlit landing page with project overview and feature highlights |
| `pages/Music_Generator.py` | Main interface for raga, instrument, and mood selection with waveform visualization |
| `pages/02_Education.py` | Educational guide covering Carnatic music theory, ragas, instruments, and notable composers |
| `complete_carnatic_generator.py` | Core generation engine implementing raga and instrument logic |
| `.streamlit/config.toml` | Streamlit server configuration |
| `pyproject.toml` | Python project metadata and dependencies |

## Folder Layout
ShrutiSynth/
├── Home.py
├── complete_carnatic_generator.py
├── logo.png
├── pyproject.toml
├── pages/
│   ├── 02_Education.py
│   └── Music_Generator.py
└── .streamlit/
└── config.toml

## Setup and Usage

**1. Clone the repository**
```bash
git clone https://github.com/NayonikaNarayanan/ShrutiSynth.git
cd ShrutiSynth
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv shrutienv
source shrutienv/bin/activate
```

**3. Install dependencies**
```bash
pip install -e .
```

**4. Run the application**
```bash
streamlit run Home.py
```

## Requirements

- Python 3.11 or higher
- Streamlit >= 1.46.0
- NumPy, SciPy, SoundFile
- Torch, Torchaudio
- Accelerate, Transformers
- Audiocraft (optional, for extended model support)

## Roadmap

- Improve raga detection and generation accuracy
- Add granular playback controls
- Surface contextual information about each selected raga within the interface
- Integrate larger generative models through the existing AudioCraft / MusicGen abstraction layer

## Contributors

- Nayonika Narayanan
- Anushka Doodipala
