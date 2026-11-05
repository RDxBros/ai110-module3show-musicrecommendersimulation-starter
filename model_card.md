# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

VibeMatch recommends the top 5 songs from a small catalog based on a user's stated preferences. It assumes the user can describe what they want up front: a favorite genre, a mood, an energy level, and whether they like acoustic music. This is a classroom project for learning how recommenders work. It is not meant for real users or real music libraries.  

---

## 3. How the Model Works  

The recommender works like a friend who knows your taste and is flipping through a stack of songs, giving each one a grade. Every song in the catalog gets scored against the user's profile: their favorite genre, the mood they want, how much energy they're looking for, and whether they like acoustic-sounding music.

Points work like this. A song gets +2 for matching the genre exactly, or +1 for a close genre (like "indie pop" when you asked for "pop"). Matching mood earns +1. Then the song earns up to +1.5 based on how close its energy level is to what the user wanted, and up to +0.5 based on how well its acousticness fits. The best a song can do is 5 points. After every song gets a grade, the system sorts them from highest to lowest and hands back the top five.

Genre counts the most because it's usually the steadiest part of someone's taste. Mood counts less since it changes day to day. The number-based features matter for a different reason: they reward closeness, so a song that's slightly calmer than you wanted still scores okay, while a song way off your energy target gets almost nothing. That also means a song can still rank decently even when its genre doesn't match, as long as the feel is right.

Compared to the starter code, the main thing I added was the actual scoring rule (the starter just returned the first few songs in the list), plus partial credit for related genres so users with niche tastes don't get shut out.

---

## 4. Data  

The catalog has 18 songs in a CSV file. The starter file had 10 songs and I added 8 more to cover genres and moods that were missing, like metal, classical, hip hop, and country. Each song has a genre, a mood, and numbers for energy, tempo, valence, danceability, and acousticness. What the data cannot capture: lyrics, artist reputation, how popular a song is, or what the user listened to before. Taste is more than a row in a table.  

---

## 5. Strengths  

The system works best for users with clear, single tastes. The Chill Lofi profile got exactly the top three lofi songs, and the pop and rock profiles each got their best match first. Mood matching does a nice job bridging genres, like recommending an ambient song to a chill-seeking lofi fan. The explanations are a real strength too: every point in the score traces back to a feature, so you can always see why a song won.  

---

## 6. Limitations and Bias 

The biggest weakness I found is that the energy scoring quietly favors people with extreme tastes over people with moderate ones. My formula measures the distance between the user's target energy and the song's energy, so a user who wants energy at 0.95 creates a huge spread between songs, but a user who wants 0.5 gets almost identical scores for half the catalog. On top of that, the formula treats "too energetic" and "not energetic enough" as equally bad, when most listeners feel one direction is worse. There's also a genre imbalance in the data: lofi has three songs while most genres only have one, so fans of well-represented genres have more chances to score the +2.0 bonus than everyone else.  

---

## 7. Evaluation  

I tested three normal profiles (High-Energy Pop, Chill Lofi, Deep Intense Rock) and the results matched intuition: the lofi songs swept the Chill Lofi list, and exact genre+mood matches always won. Then I tried some "adversarial" profiles to see if the scoring could be tricked.

**Comparing the normal profiles to each other**

- High-Energy Pop vs Chill Lofi: the lists are mirror images. Every song the pop profile recommends has energy above 0.75 and low acousticness; every song the lofi profile recommends has energy below 0.45 and high acousticness. Same scoring rule, completely different results, which means the energy target and acoustic flag are actually steering the output instead of just decorating it.
- High-Energy Pop vs Deep Intense Rock: both users want energy around 0.9, but the winners are different because the tags are different (Sunrise City for pop, Storm Runner for rock). The interesting one is Gym Hero showing up in both lists. It is a pop song with the "intense" mood and the highest energy in the catalog, so it bridges both profiles. For the happy pop user it ranks second even though its mood says "intense," because two strong feature matches (pop + energy) outweigh one miss. A real listener would probably feel Gym Hero is fine for a workout but weird as a "happy" pick, so this is where a one-word mood tag falls short of real understanding.
- Chill Lofi vs Deep Intense Rock: zero shared songs. The acoustic flag splits them cleanly: the lofi list is all 0.7+ acousticness, the rock list is all under 0.10. The two users basically live in different halves of the catalog, which is exactly what you would expect from a chill-studier versus a headbanger.

**Edge case 1: Conflicted user** (sad mood + very high energy + acoustic)

```
1. Neon Requiem (classical/melancholic) - 3.88
   genre match (classical) +2.0, mood match (melancholic) +1.0, energy closeness +0.41, acousticness fit +0.47
2. Fog Harbor Blues (blues/melancholic) - 2.08
   mood match (melancholic) +1.0, energy closeness +0.65, acousticness fit +0.44
3. Gym Hero (pop/intense) - 1.50
   energy closeness +1.47, acousticness fit +0.03
```

The system handles this okay. The mood+genre match still wins even though the energy fit is terrible, which is arguably the right call. But notice a "happy workout pop" song lands at #3 for a user who said they want sad music. That's what happens when you can only express one mood.

**Edge case 2: Ghost profile** (genre "folk" and mood "dreamy" are not in the catalog)

```
1. Blue Hour Ballad (r&b/romantic) - 1.77
   energy closeness +1.50, acousticness fit +0.28
2. Midnight Coding (lofi/chill) - 1.52
   energy closeness +1.38, acousticness fit +0.15
3. Night Drive Loop (synthwave/moody) - 1.52
   energy closeness +1.12, acousticness fit +0.39
```

When neither tag matches anything, the ranking is driven entirely by the numbers. The results aren't wrong exactly, but they feel random because the two strongest signals are dead. This is the cold-start problem in miniature.

**Edge case 3: Genre hacker** (empty genre string)

```
1. Library Rain (lofi/chill) - 3.85
   related genre (lofi) +1.0, mood match (chill) +1.0, energy closeness +1.42, acousticness fit +0.43
2. Midnight Coding (lofi/chill) - 3.82
   related genre (lofi) +1.0, mood match (chill) +1.0, energy closeness +1.47, acousticness fit +0.35
3. Spacewalk Thoughts (ambient/chill) - 3.78
   related genre (ambient) +1.0, mood match (chill) +1.0, energy closeness +1.32, acousticness fit +0.46
```

Found a real bug. An empty genre string is technically "contained in" every genre, so every single song gets +1.0 free points as a "related genre." It doesn't change the ranking between songs since they all get the same bonus, but it inflates scores and produces a fake "related genre" reason on every recommendation. A strip/empty check before scoring would fix it.

**Edge case 4: Sloppy input** (genre is " pop" with a leading space)

```
1. Sunrise City (pop/happy) - 3.88
   related genre (pop) +1.0, mood match (happy) +1.0, energy closeness +1.47, acousticness fit +0.41
2. Rooftop Lights (indie pop/happy) - 3.77
   related genre (indie pop) +1.0, mood match (happy) +1.0, energy closeness +1.44, acousticness fit +0.33
3. Gym Hero (pop/intense) - 2.78
   related genre (pop) +1.0, energy closeness +1.30, acousticness fit +0.47
```

An untrimmed space silently downgrades an exact match to a fuzzy one. Sunrise City still wins here but loses a full point. The fix is just calling .strip() on inputs, but it shows how fragile string matching is.

---

## 8. Future Work  

First, fix the input bugs my tests found: strip whitespace and ignore empty strings before scoring. Second, give the system a map of related genres and moods so "metal" counts for a rock fan and "aggressive" counts as "intense." Right now the string matching is too literal. Third, let a profile hold more than one target, since real people like multiple opposite things. Last, I would add a listening history so the system can learn instead of being told, which is what real recommenders like Spotify actually do.  

---

## 9. Personal Reflection  

The biggest thing I learned is that a recommender is mostly just a scoring rule plus a ranking, and the hard part is not the math but deciding what deserves points. I was surprised that my bias problems came from the data, not the weights. Lofi got an advantage just because it had more songs in the file. It changed how I think about apps like Spotify: when a recommendation feels off, it is probably not a broken algorithm, it is the system faithfully scoring whatever data it has.  
