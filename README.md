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

I ran three test profiles (High-Energy Pop, Chill Lofi, Deep Intense Rock) and compared the results to my own musical intuition.

**Why Sunrise City ranked first for the pop profile.** It's the only song in the catalog that is both pop AND happy, so it hit every scoring term at once: +2.0 for the exact genre, +1.0 for the mood, +1.47 for energy being nearly dead-on (0.82 vs the 0.8 target), and +0.41 for the acousticness fit. A score of 4.88 out of 5.00 feels right to me. If someone says "I want upbeat happy pop," that is exactly what this song is.

**Does it feel right overall?** Mostly yes. Three different songs topped the three lists (Sunrise City, Library Rain, Storm Runner), so no single song is dominating and the genre weight isn't overpowering the other features. For the Chill Lofi profile, Library Rain beat Midnight Coding 4.85 to 4.82 even though both are lofi/chill. The tiebreaker was acousticness (0.86 vs 0.71). That felt plausible: the dreamier, more acoustic song edging out the one that's closer to background noise.

**Where it felt wrong.** In Deep Intense Rock, Iron Cathedral (metal, aggressive, 0.97 energy) ranked 5th, below a pop song and an edm track. Intuitively a metal song is the closest thing to rock in the catalog, and "aggressive" is basically "intense." But the scoring treats genre and mood as exact string matches, so metal gets zero genre points and aggressive gets zero mood points. The weights are fine; the problem is the tags are too literal.

**Did one song keep topping every list?** No, which tells me the 2.0 genre weight is balanced. Genre did decide one close call though: for the Chill Lofi profile, Focus Flow (lofi/focused) ranked above Spacewalk Thoughts (ambient/chill) purely because of genre. You could argue either is the better pick for someone who wants chill, so that's a judgment call rather than a bug.

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

My biggest learning moment was realizing the math isn't the hard part. Adding up weighted points took an afternoon. Deciding what deserves points, and figuring out that "closeness" matters more than raw values, took way longer. The empty genre string bug drove this home: my fuzzy match was handing out free points to every song in the catalog, and I only caught it because I tested a weird profile on purpose.

Using AI tools helped most with the research side. Learning how Spotify and YouTube actually do this made my tiny version make sense as a simplified version of the real thing. But I had to double-check constantly. The AI suggested features and weights that sounded smart on paper, and I still had to run the profiles myself to see if they held up. The bugs I found, like the whitespace issue and the empty string exploit, came from running the code, not from the suggestions.

What surprised me is how alive a simple point system feels. There is no learning, no model, just addition. But when Gym Hero kept showing up for the happy pop user, it felt like a real recommendation quirk, the same way Spotify pushes an odd pick sometimes. That's when it clicked that recommendations that feel intelligent are mostly just decent data plus a sensible scoring rule.

If I extended this project, I would add listening history so profiles build themselves instead of being typed in, a genre similarity map so metal counts for rock fans, and asymmetric energy scoring since "too hyped" feels worse than "too chill" for most people.



