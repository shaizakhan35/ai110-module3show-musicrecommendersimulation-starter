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

My recommender compares each song's attributes to the user's taste profile and scores them. The highest scoring songs get recommended.

Song features:
- 'genre' - style of music (pop, lofi, rock, jazz)
- 'mood' - emotional feel (happy, chill, intense, moody)
- 'energy' - calm to intense (0.0 to 1.0)
- 'valence' - dark to positive (0.0 to 1.0)

UserProfile stores:
- preferred genre, mood, energy, and valence

Scoring formula:
      Score = 0.35 · genre_match + 0.25 · mood_match
        + 0.20 · energy_proximity + 0.20 · valence_proximity

How songs are chosen:
All songs are scored, sorted highest to lowest to maintain order and the top matches are returned.

Algorithm Recipe:
      Score = 2.0 · genre_match
        + 1.5 · mood_match
        + 1.0 · energy_proximity
        + 1.0 · valence_proximity

Potential biases:
- Genre is weighted highest so good songs that match mood 
  but not genre may get missed.
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
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```
Loaded songs: 20

Top 5 Recommendations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1 Sunrise City — Neon Echo
    Score: 5.4 / 5.5
    ✔ genre match: pop (+2.0)
    ✔ mood match: happy (+1.5)
    ✔ energy proximity: 0.98 (+0.98)
    ✔ valence proximity: 0.96 (+0.96)
#2 Gym Hero — Max Pulse
    Score: 3.8 / 5.5
    ✔ genre match: pop (+2.0)
    ✔ mood mismatch: intense vs happy (0.0)
    ✔ energy proximity: 0.87 (+0.87)
    ✔ valence proximity: 0.97 (+0.97)
#3 Rooftop Lights — Indigo Parade
    Score: 3.5 / 5.5
    ✔ genre mismatch: indie pop vs pop (0.0)
    ✔ mood match: happy (+1.5)
    ✔ energy proximity: 0.96 (+0.96)
    ✔ valence proximity: 0.99 (+0.99)
#4 Golden Highway — Maple Ridge
   

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried
Loaded songs: 20

--- Profile 1: Conflicting (pop/sad/high energy) ---
User profile: genre=pop, mood=sad, energy=0.95, valence=0.05

🎵 Top 5 Recommendations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1 Gym Hero — Max Pulse
    Score: 3.3 / 5.5
    ✔ genre match: pop (+2.0)
    ✔ mood mismatch: intense vs sad (0.0)
    ✔ energy proximity: 0.98 (+0.98)
    ✔ valence proximity: 0.28 (+0.28)

#2 Sunrise City — Neon Echo
    Score: 3.1 / 5.5
    ✔ genre match: pop (+2.0)
    ✔ mood mismatch: happy vs sad (0.0)
    ✔ energy proximity: 0.87 (+0.87)
    ✔ valence proximity: 0.21 (+0.21)

#3 Midnight Skyline — Atlas Reed
    Score: 3.0 / 5.5
    ✔ genre mismatch: hip hop vs pop (0.0)
    ✔ mood match: sad (+1.5)
    ✔ energy proximity: 0.73 (+0.73)
    ✔ valence proximity: 0.73 (+0.73)

#4 Winter Glass — Orchid Quartet
    Score: 2.6 / 5.5
    ✔ genre mismatch: classical vs pop (0.0)
    ✔ mood match: sad (+1.5)
    ✔ energy proximity: 0.36 (+0.36)
    ✔ valence proximity: 0.77 (+0.77)

#5 Iron Harbor — Crimson Vale
    Score: 1.9 / 5.5
    ✔ genre mismatch: metal vs pop (0.0)
    ✔ mood mismatch: angry vs sad (0.0)
    ✔ energy proximity: 1.00 (+1.00)
    ✔ valence proximity: 0.85 (+0.85)


--- Profile 2: Missing Genre (salsa) ---
User profile: genre=salsa, mood=romantic, energy=0.6, valence=0.7

🎵 Top 5 Recommendations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1 Velvet Harbor — Marina Vale
    Score: 3.4 / 5.5
    ✔ genre mismatch: R&B vs salsa (0.0)
    ✔ mood match: romantic (+1.5)
    ✔ energy proximity: 0.99 (+0.99)
    ✔ valence proximity: 0.92 (+0.92)

#2 Golden Highway — Maple Ridge
    Score: 3.3 / 5.5
    ✔ genre mismatch: country vs salsa (0.0)
    ✔ mood match: romantic (+1.5)
    ✔ energy proximity: 0.89 (+0.89)
    ✔ valence proximity: 0.87 (+0.87)

#3 Sunlit Overpass — The Drift Society
    Score: 1.9 / 5.5
    ✔ genre mismatch: reggae vs salsa (0.0)
    ✔ mood mismatch: relaxed vs romantic (0.0)
    ✔ energy proximity: 0.89 (+0.89)
    ✔ valence proximity: 0.97 (+0.97)

#4 Coffee Shop Stories — Slow Stereo
    Score: 1.8 / 5.5
    ✔ genre mismatch: jazz vs salsa (0.0)
    ✔ mood mismatch: relaxed vs romantic (0.0)
    ✔ energy proximity: 0.77 (+0.77)
    ✔ valence proximity: 0.99 (+0.99)

#5 Rooftop Lights — Indigo Parade
    Score: 1.7 / 5.5
    ✔ genre mismatch: indie pop vs salsa (0.0)
    ✔ mood mismatch: happy vs romantic (0.0)
    ✔ energy proximity: 0.84 (+0.84)
    ✔ valence proximity: 0.89 (+0.89)


--- Profile 3: Indecisive (no genre or mood) ---
User profile: genre=, mood=, energy=0.5, valence=0.5

🎵 Top 5 Recommendations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1 Backroads at Dusk — June Hollow
    Score: 1.9 / 5.5
    ✔ genre mismatch: country vs  (0.0)
    ✔ mood mismatch: melancholic vs  (0.0)
    ✔ energy proximity: 0.96 (+0.96)
    ✔ valence proximity: 0.96 (+0.96)

#2 Midnight Coding — LoRoom
    Score: 1.9 / 5.5
    ✔ genre mismatch: lofi vs  (0.0)
    ✔ mood mismatch: chill vs  (0.0)
    ✔ energy proximity: 0.92 (+0.92)
    ✔ valence proximity: 0.94 (+0.94)

#3 After the Rain — Seren Sol
    Score: 1.8 / 5.5
    ✔ genre mismatch: R&B vs  (0.0)
    ✔ mood mismatch: melancholic vs  (0.0)
    ✔ energy proximity: 0.93 (+0.93)
    ✔ valence proximity: 0.91 (+0.91)

#4 Sunlit Overpass — The Drift Society
    Score: 1.8 / 5.5
    ✔ genre mismatch: reggae vs  (0.0)
    ✔ mood mismatch: relaxed vs  (0.0)
    ✔ energy proximity: 0.99 (+0.99)
    ✔ valence proximity: 0.83 (+0.83)

#5 Focus Flow — LoRoom
    Score: 1.8 / 5.5
    ✔ genre mismatch: lofi vs  (0.0)
    ✔ mood mismatch: focused vs  (0.0)
    ✔ energy proximity: 0.90 (+0.90)
    ✔ valence proximity: 0.91 (+0.91)

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



