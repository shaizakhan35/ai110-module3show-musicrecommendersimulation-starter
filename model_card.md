# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

MoodTunes 1.0

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

MoodTunes 1.0 is designed for classroom exploration of how content-based music recommenders work. It generates song
recommendations based on a user's preferred genre, mood,
energy level, and valence. It assumes the user has one
clear genre and mood preference. This is not built for
real users or real platforms, it is a learning simulation.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Each song gets a score based on how well it matches the user.
Genre and mood are either a match or not; genre is worth 2.0
points and mood is worth 1.5 points. Energy and valence use
proximity scoring, meaning a song closer to the user's preferred
level scores higher. All songs are scored, sorted from highest
to lowest and the top 5 are returned. The maximum score is 5.5.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog has 20 songs across 11 genres including pop, lofi,
rock, jazz, metal, R&B, country, and classical. Moods include
happy, chill, intense, sad, romantic, and melancholic. The data
was created manually for this simulation and does not reflect
real listening data. Some genres like jazz and classical only
have one song each.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users whose preferred genre and mood
are both in the catalog. A lofi/chill user received Midnight
Coding as the top result with a score of 5.44, which felt
accurate. The reason strings also make every recommendation
transparent and easy to understand.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system over-prioritizes genre because it carries a weight
of 2.0 out of a maximum score of 5.5, which is strong enough
to override mood and valence entirely. During testing, a user
who wanted sad music received Gym Hero, a high-energy happy pop
song, as the top recommendation simply because the genre matched.The catalog is also uneven; genres like rock and classical only have one song each, so users with niche tastes get very limited options, while users with missing genres like salsa never receive the genre bonus at all. The system also ignores tempo and acousticness and has no way to handle conflicting preferences or cultural context.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested four user profiles: a default pop/happy profile, a 
conflicting pop/sad profile, a missing genre profile using salsa, and an indecisive profile with no genre or mood specified. For each one I checked whether the top results felt emotionally correct and whether the reason strings explained the ranking clearly. The default profile worked well and matched my intuition, but the most surprising result was that a user who asked for sad music received Gym Hero, a high-energy happy pop song, as the top recommendation simply because the genre matched. I also ran a weight shift experiment where I lowered the genre weight from 2.0 to 1.0 and doubled the energy weight, which caused Midnight Skyline, a sad hip hop song, to jump from 3 to 1 for the same profile, proving that the weights have a big impact on what the system thinks is a good recommendation.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

-Add collaborative filtering to recommend based on what similar
users liked. 
-Allow users to specify more than one genre or mood.
-Add more songs per genre so niche users get better variety.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I did not expect to care this much about a music recommender.
The moment that hit me hardest was when a user who asked for
sad music got a gym workout song back. That was my biggest
learning moment. Algorithms do not feel anything, they just
follow numbers. Using AI tools helped me move faster, but I
still had to stop and check if I actually understood what was
being generated. The AI gave me formulas and code, but it could
not tell me whether the weights made sense for my data. That
part I had to figure out myself.

What surprised me most is how something so simple can actually
feel like it knows you. When Midnight Coding showed up as the
top result for a chill lofi user, it genuinely felt right. I
did not expect a math formula to produce something that felt
human. If I kept going, I would make it learn from real people
and add mood detection so the system could ask how you are
feeling today instead of always assuming the same preference.