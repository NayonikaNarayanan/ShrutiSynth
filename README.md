# ShrutiSynth: AI-Powered Carnatic Music Generator

***PS-1 internship project at Swecha Tech, May–July 2025***
***Summer internship project at FLWSTUDIO, May–July 2026***

ShrutiSynth is an AI application that generates Carnatic classical music using digital signal processing and a custom audio synthesis engine. Built as a foundational prototype for Swecha's broader Indian-language AI roadmap, the project addresses a gap in existing tools: no AI product on the market is built specifically for Carnatic music, and none serve the intermediate student who already has foundations and wants to explore the tradition independently.

The application allows users to select traditional ragas, instruments, and moods, and generates expressive compositions with varied tempo and gamaka ornamentation. It includes an integrated learning module covering raga theory and instrument context.

## Who It's For

ShrutiSynth is built for intermediate Carnatic music students: students who already have strong foundations, can maintain thalam, and know their first ragas, but whose guru isn't always available and who want to keep exploring the tradition on their own terms.

It is not designed for absolute beginners. Without foundational technique built under a guru, a generative tool can reinforce incorrect habits or cause confusion. ShrutiSynth's purpose is to support the stage after foundations are in place, where independent musical exploration becomes both possible and important.

**North Star:** ShrutiSynth exists so that no intermediate Carnatic music student ever has to stop exploring the tradition just because their guru isn't in the room.

## Problem Statement

Intermediate Carnatic music students struggle to explore independently because existing frameworks for the tradition weren't designed for self-directed, digital learning. There's a gap between the depth of knowledge that exists and what this generation can actually access on their own.

## Project Background

ShrutiSynth originated from a conversation during my internship at Swecha Tech (May–July 2025). As a trained Carnatic classical vocalist of 14 years with additional training in Robindro Sangeet (Bengali classical vocals), I was interested in what tools actually exist for classical music learners at the intermediate level, and what I found was a market gap that is both specific and unoccupied.

I surveyed the major products in the Indian classical music learning space: Riyaz, SwarShala, Shankar Mahadevan Academy, NaadSadhana, Artium Academy, and Acharyanet. Every single one either covers Carnatic as one module within a broader Indian classical or multi-genre platform, or optimises for beginner onboarding and live guru access. Not one is built specifically around the theory, grammar, and exploration needs of a student who already has their foundations.

The raga library across every competitor illustrated this most clearly. Even the strongest products offered surface-level coverage (notes, arohana/avarohana, maybe a recording) with no relational context. No melakarta system. No gamaka logic per raga. No sense of how ragas connect to each other. The raga library is treated as a catalogue, not as an explorable system.

This matters beyond a technical gap. As younger generations increasingly turn to AI tools, the absence of tools that reflect the depth of Indian classical traditions risks the next generation of students losing access to the structure and grammar of what they're learning. ShrutiSynth is a first step toward filling that gap, starting with Carnatic music, with architecture designed to extend to other Indian classical traditions in future iterations.

The project was developed during a 5-day rapid prototyping sprint and involved competitive analysis of existing tools, definition of MVP scope and accuracy benchmarks, and validation of generated outputs against domain expertise in Carnatic vocals, including evaluation of raga scales, gamaka ornamentations, and instrument-specific harmonic characteristics. The current implementation uses a custom Python audio synthesis engine, with an AudioCraft / MusicGen abstraction layer built into the architecture to support future integration of larger generative models.

## Features

- **Raga-based composition** supporting ragas including Kalyani, Sankarabharanam, Kharaharapriya, Todi, Bhairavi, and more
- **Instrument selection** across traditional instruments such as Veena, Flute, Violin, Tabla, and Nadaswaram
- **Mood-driven note weighting** with prompt structures for forms such as alapana, korvai, and bhajan
- **Streamlit-based interface** with multi-page navigation, real-time playback, waveform visualization, and WAV export
- **Integrated learning module** providing context on ragas, instruments, and Carnatic music theory
- **Modular generator core** that handles raga logic, tempo, and instrument synthesis

## Project Structure

| File | Description |
|------|-------------|
| `Home.py` | Streamlit landing page with project overview and feature highlights |
| `pages/Music_Generator.py` | Main interface for raga, instrument, and mood selection with waveform visualization |
| `pages/02_Education.py` | Educational guide covering Carnatic music theory, ragas, and instruments |
| `complete_carnatic_generator.py` | Core generation engine implementing raga and instrument logic |
| `.streamlit/config.toml` | Streamlit server configuration |
| `pyproject.toml` | Python project metadata and dependencies |

## Folder Layout

```
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
```

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

- Replace hardcoded raga data with a verified JSON database to eliminate intonation errors and prevent scale hallucination
- Build a Raga Map showing relationships between ragas (melakarta parents, janya children, parallel ragas) to support structured independent exploration
- Add a foundations checklist or onboarding gate so the app can communicate its assumptions to users and reinforce that it is not for beginners
- Fix known synthesis gaps: percussion instruments (Tabla, Ghatam, Kanjira), pentatonic raga crashes, unused temperature parameter
- Surface raga theory and relational context within the interface, not just in the education module
- Add granular playback controls
- Integrate larger generative models through the existing AudioCraft / MusicGen abstraction layer

## Contributors

- Nayonika Narayanan
- Anushka Doodipala [2025 internship, code contributions]
