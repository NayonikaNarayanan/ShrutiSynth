import streamlit as st

st.set_page_config(page_title="Indian Classical Music", layout="wide")

st.title("🎓 ShrutiSynth Guide to Indian Classical Music")

# 🌸 What is Indian Classical Music?
st.header("🌸 What is Indian Classical Music?")
st.write("""
Indian classical music is a centuries-old tradition rooted in deep emotional expression and complex melodic structures. It is not merely entertainment, but a form of devotion, meditation, and a cultural lifeline that has evolved over thousands of years. There are three major classical styles in India — **Carnatic**, **Hindustani**, and **Rabindra Sangeet** — each with its own system of ragas, rhythms, and aesthetics.

**Carnatic music**, predominant in South India, is deeply structured and centered around fixed compositions like varnams and kritis. It emphasizes a tight grammar of raga (melody) and tala (rhythm), allowing intricate improvisation within defined boundaries. It is known for devotional themes and spiritual intensity.

**Hindustani music**, practiced in North India, is more improvisational and is often performed in the context of ragas that evolve slowly through long alap sections. It developed under significant Persian and Mughal influence and features gharanas (lineages), each with a distinct style.

**Rabindra Sangeet**, originating in Bengal, is a semi-classical genre created by Nobel Laureate Rabindranath Tagore. It draws inspiration from Indian ragas, folk music, and Western classical, blending melody with deep literary expression. It speaks to the human soul — of nature, freedom, and love.
""")

# 🎼 Understanding Raga in Indian Classical Music
st.header("🎼 Understanding Raga in Indian Classical Music")
st.write("""
A **raga** is far more than a scale — it is a melodic personality that defines how a sequence of notes should be approached, emphasized, ornamented, and emotionally delivered. Each raga has an **Arohanam** (ascending structure) and **Avarohanam** (descending structure), but also possesses characteristic phrases called **pakads**, key notes like **vadi** and **samvadi**, and an emotional flavor or time of performance.

Ragas are associated with specific moods, times of the day, or even seasons — they can invoke peace, pathos, courage, or love. In Carnatic music, ragas are built from 72 Melakarta parent scales, each spawning numerous **janya ragas** with unique rules.
""")

# 🎶 Popular Ragas in ShrutiSynth
st.header("🎶 Popular Ragas in ShrutiSynth")
st.markdown("""
- **Kalyani** – is a major raga known for its majestic and auspicious nature. Its Arohanam is Sa Re Ga Ma# Pa Dha Ni Sa and its Avarohanam is Sa Ni Dha Pa Ma# Ga Re Sa. Kalyani is frequently used in compositions of grandeur and devotion. 
- **Sankarabharanam** – resembles the Western major scale and is extremely versatile. It ascends as Sa Re Ga Ma Pa Dha Ni Sa and descends as Sa Ni Dha Pa Ma Ga Re Sa. It lends itself equally to intricate compositions and lively improvisations.  
- **Kharaharapriya** – is a soulful raga that allows fluid gamakas. It follows Sa Re Ga Ma Pa Dha Ni Sa in both ascent and descent. Tyagaraja composed extensively in this raga to express devotion and introspection. 
- **Mayamalavagowla** – is taught to beginners due to its symmetrical structure and clearly defined swaras. Its Arohanam is Sa Re1 Ga Ma Pa Dha1 Ni Sa, and its Avarohanam is Sa Ni Dha1 Pa Ma Ga Re1 Sa. Though simple, it forms the backbone of Carnatic learning.
- **Mohana** – is a bright pentatonic raga that skips Ma and Ni. It ascends Sa Re Ga Pa Dha Sa and descends Sa Dha Pa Ga Re Sa. Despite its simplicity, it is highly melodic and used in bhajans and folk-tinged pieces.
- **Hindolam** –  is another pentatonic raga that excludes Re and Pa. Its Arohanam is Sa Ga1 Ma Dha1 Ni1 Sa, and Avarohanam is Sa Ni1 Dha1 Ma Ga1 Sa. It is introspective and tranquil, often used in meditative pieces.
- **Bilahari** –  is a derivative of Sankarabharanam that is cheerful and energetic. It ascends as Sa Re Ga Pa Ma Pa Dha Ni Sa and descends as Sa Ni Dha Pa Ma Ga Re Sa. It is often used in brisk varnams and kritis.
- **Shanmukhapriya** –  is known for its striking character and rich gamaka potential. Its Arohanam is Sa Ri2 Ga2 Ma1 Pa Dha1 Ni2 Sa, and Avarohanam is Sa Ni2 Dha1 Pa Ma1 Ga2 Ri2 Sa. It suits vibrant, energetic compositions. 
- **Charukesi** – is an emotionally charged raga with a plaintive character. Its scale is Sa Ri2 Ga2 Ma1 Pa Dha1 Ni2 Sa ascending, and Sa Ni2 Dha1 Pa Ma1 Ga2 Ri2 Sa descending. It is widely used in pieces that express longing and devotion.
- **Kamboji** –  is majestic and spacious. Its ascent is Sa Re Ga Pa Dha Sa and descent is Sa Ni Dha Pa Ma Ga Re Sa. It is deeply associated with traditional compositions and temple rituals.
- **Harikambhoji** –  is a full-scale raga that resembles the Mixolydian mode. Its ascent and descent are Sa Re Ga Ma Pa Dha Ni Sa and Sa Ni Dha Pa Ma Ga Re Sa, respectively. It is associated with folkish charm and joy.
- **Natabhairavi** – mirrors the natural minor scale. It uses Sa Re Ga Ma Pa Dha Ni Sa in both ascent and descent. It evokes gravity and is often used in devotional or melancholic compositions.
- **Todi** –  is a profound and highly gamaka-rich raga. Its Arohanam is Sa Ri1 Ga3 Ma1 Pa Dha1 Ni3 Sa and its Avarohanam is Sa Ni3 Dha1 Pa Ma1 Ga3 Ri1 Sa. Considered difficult, it is prized for its emotive depth.
- **Bhairavi** – is both classical and versatile. It uses Sa Ri1 Ga1 Ma Pa Dha1 Ni1 Sa and Sa Ni1 Dha1 Pa Ma Ga1 Ri1 Sa. It supports light classical pieces and complex ragam-tanam-pallavi as well.
""")

# 📜 Popular Carnatic Compositions
st.header("📜 Popular Carnatic Compositions")
st.write("""
Among the most iconic compositions is *Vatapi Ganapatim Bhajeham* in Hamsadhwani by Muthuswami Dikshitar — a powerful invocation to Lord Ganesha.  
*Endaro Mahanubhavulu* in Sri by Tyagaraja is one of the five Pancharatna Kritis, honoring all great saints.  
*Nagumomu Ganaleni* in Abheri showcases longing and devotion in its purest form, while *Bhajare Re Chitta* in Kalyani by Mysore Vasudevacharya offers meditative surrender.  
Another favorite is *Brochevarevarura* in Khamas, a staple of light classical concerts known for its lilting melody.
""")

# 🧑‍🎤 Legendary Artists of Carnatic Music
st.header("🧑‍🎤 Legendary Artists of Carnatic Music")
st.write("""
**Tyagaraja** is considered the heart of Carnatic music. His hundreds of devotional kritis in Telugu are filled with philosophical depth and musical sophistication. He rarely performed publicly and composed entirely as an offering to Lord Rama.

**Muthuswami Dikshitar**, the most scholarly of the Carnatic trinity, composed in Sanskrit, weaving together mythology, astrology, and intricate raga structure. His works often include the name of the deity and location of temples.

**Syama Sastri** was known for rhythmic mastery and his compositions in praise of Goddess Kamakshi. His kritis are fewer but deeply revered for their lyrical elegance and technical difficulty.

**MS Subbulakshmi**, the first musician to receive the Bharat Ratna, brought Carnatic music to the global stage. Her voice became synonymous with bhakti (devotion) and cultural pride.

**Lalgudi Jayaraman** was a violin maestro who redefined instrumental Carnatic music with lyrical phrasing. He composed varnams and tillanas that are now staples for students and performers alike.
""")

# 🎻 Traditional Instruments in ShrutiSynth
st.header("🎻 Traditional Instruments in ShrutiSynth")
st.write("""
- **🎻 Violin** – though of Western origin, was fully Indianized in the 19th century by Baluswami Dikshitar. In Carnatic music, it is played seated with the scroll resting on the ankle, allowing for continuous pitch modulation. Tuned to the tonic and fifth, it is capable of replicating intricate gamakas and now holds a central place in both accompaniment and solo performances. 
- **🎼 Veena** – or more specifically the Saraswati Veena, is a plucked string instrument native to South India with a history dating back to the Vedas. With its carved jackfruit-wood body, fretted neck, and sympathetic strings, it represents both divinity and discipline. It is played using a plectrum and is closely associated with Goddess Saraswati.
- **🎶 Flute** – known as venu, is one of India’s most ancient instruments. The bamboo Carnatic flute, made popular by T.R. Mahalingam (Flute Mali), is keyless and requires sophisticated control over breath and tongue to shape gamakas. It is sweet, expressive, and associated with both Lord Krishna and meditative artistry.
- **🎷 Nadaswaram** – is a double-reed wind instrument from Tamil Nadu, known for its loud, powerful tone. Traditionally played in temples and auspicious occasions, it is believed to be one of the world’s loudest non-brass instruments. It is usually accompanied by the thavil and played using circular breathing.  
- **🥁 Mridangam** – is the primary percussion instrument in Carnatic concerts, made from jackfruit wood with dual playing surfaces. Its design allows it to produce both treble and bass sounds, and it is the foundation of rhythmic improvisation and structure. 
- **🪘 Ghatam** – is a clay pot with metal filings mixed into the clay to enhance resonance. Played with fingers and palms while held against the stomach, it is deceptively simple in appearance and offers a wide range of tonal variety and rhythmic complexity. 
- **🪈 Kanjira** – is a hand-held frame drum native to Tamil Nadu, traditionally made with monitor lizard skin and a single jingle. Played with one hand, it adds brightness and sparkle to the rhythmic ensemble and is known for pitch bends and crisp articulation.
- **🪕 Tabla** – though primarily from Hindustani tradition, is recognized across India. It consists of two drums — the treble dayan and the bass bayan. While not a part of traditional Carnatic concerts, it features in jugalbandi (fusion) and devotional settings.
""")

# 📝 Footer Prompt
st.markdown("---")
st.markdown("Would you like to learn more or explore each raga through generated music? Visit the Music Generator page!")


