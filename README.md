# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

My recommender works like "describe the song" in Spotify. Each song has attributes like genre, mood, energy, and acousticness, and each user profile lists what they're looking for. The system scores every song by closeness to the profile: genre counts most, then mood, then the numbers. It recommends the top scorers. It only knows ten songs and can't learn from other listeners, so it's a simplified version of the real thing.

Each Song has:
- id and title so we can identify it (not used for scoring)
- artist (just for display)
- genre (like pop, lofi, or rock)
- mood (like happy, chill, or intense)
- energy on a 0 to 1 scale
- tempo_bpm (bpm)
- valence on a 0 to 1 scale (how positive the song feels)
- danceability on a 0 to 1 scale
- acousticness on a 0 to 1 scale

Each UserProfile stores:
- favorite_genre (the genre they're most into)
- favorite_mood (the vibe they're looking for)
- target_energy (how much energy they want, 0 to 1)
- likes_acoustic (yes or no)

Each song earns points based on how close it is to the user profile:

+2.0 for an exact genre match (+1.0 for a close one, like "indie pop" vs "pop")
+1.0 for a mood match
up to +1.5 based on how close the song's energy is to the target (closer = more points)
up to +0.5 based on how acoustic it is (acoustic fans want high values, others want low)

The best possible score is 5.0. Genre counts the most because it's the steadiest part of someone's taste. Mood is next since it matters but changes day to day. The numbers (energy and acousticness) break ties and can lift a song even when the labels don't match. After every song gets scored, the system sorts them highest to lowest and returns the top few.

Where bias could show up

Because genre is worth the most, the system might skip over a great song that matches the user's mood and energy just because it's in a different genre. It also can't handle someone who likes two opposite things at once, since it scores everything against one target. And with only 18 songs, a user whose favorite genre isn't in the data gets recommendations based mostly on mood and energy, which might feel random to them.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
User profile: genre=pop, mood=happy, energy=0.8, acoustic=False

Loading songs from data/songs.csv...
Loaded songs: 18

Top 5 Recommendations
========================================

1. Sunrise City - Neon Echo
   Genre: pop | Mood: happy
   Score: 4.88 / 5.00
   Why: genre match (pop) +2.0, mood match (happy) +1.0, energy closeness +1.47, acousticness fit +0.41

2. Gym Hero - Max Pulse
   Genre: pop | Mood: intense
   Score: 3.78 / 5.00
   Why: genre match (pop) +2.0, energy closeness +1.30, acousticness fit +0.47

3. Rooftop Lights - Indigo Parade
   Genre: indie pop | Mood: happy
   Score: 3.77 / 5.00
   Why: related genre (indie pop) +1.0, mood match (happy) +1.0, energy closeness +1.44, acousticness fit +0.33

4. Moon Festival - Kira Tanabe
   Genre: j-pop | Mood: playful
   Score: 2.92 / 5.00
   Why: related genre (j-pop) +1.0, energy closeness +1.50, acousticness fit +0.42

5. Block Party Anthem - DJ Cornerstone
   Genre: hip hop | Mood: euphoric
   Score: 1.89 / 5.00
   Why: energy closeness +1.43, acousticness fit +0.46
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



