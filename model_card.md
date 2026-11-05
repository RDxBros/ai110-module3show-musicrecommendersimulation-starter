# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

The recommender works like a friend who knows your taste and is flipping through a stack of songs, giving each one a grade. Every song in the catalog gets scored against the user's profile: their favorite genre, the mood they want, how much energy they're looking for, and whether they like acoustic-sounding music.

Points work like this. A song gets +2 for matching the genre exactly, or +1 for a close genre (like "indie pop" when you asked for "pop"). Matching mood earns +1. Then the song earns up to +1.5 based on how close its energy level is to what the user wanted, and up to +0.5 based on how well its acousticness fits. The best a song can do is 5 points. After every song gets a grade, the system sorts them from highest to lowest and hands back the top five.

Genre counts the most because it's usually the steadiest part of someone's taste. Mood counts less since it changes day to day. The number-based features matter for a different reason: they reward closeness, so a song that's slightly calmer than you wanted still scores okay, while a song way off your energy target gets almost nothing. That also means a song can still rank decently even when its genre doesn't match, as long as the feel is right.

Compared to the starter code, the main thing I added was the actual scoring rule (the starter just returned the first few songs in the list), plus partial credit for related genres so users with niche tastes don't get shut out.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
