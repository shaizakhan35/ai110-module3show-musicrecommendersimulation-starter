"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    # package-relative import when run as module: python -m src.main
    from .recommender import load_songs, recommend_songs
except Exception:
    # fallback for script execution: python src/main.py
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        (
            "Profile 1: Conflicting (pop/sad/high energy)",
            {
                "preferred_genre": "pop",
                "preferred_mood": "sad",
                "preferred_energy": 0.95,
                "preferred_valence": 0.05,
            },
        ),
        (
            "Profile 2: Missing Genre (salsa)",
            {
                "preferred_genre": "salsa",
                "preferred_mood": "romantic",
                "preferred_energy": 0.6,
                "preferred_valence": 0.7,
            },
        ),
        (
            "Profile 3: Indecisive (no genre or mood)",
            {
                "preferred_genre": "",
                "preferred_mood": "",
                "preferred_energy": 0.5,
                "preferred_valence": 0.5,
            },
        ),
    ]

    for label, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n--- {label} ---")
        print(f"User profile: genre={user_prefs['preferred_genre']}, mood={user_prefs['preferred_mood']}, energy={user_prefs['preferred_energy']}, valence={user_prefs['preferred_valence']}")
        print("\n🎵 Top 5 Recommendations")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for index, rec in enumerate(recommendations, start=1):
            song = rec["song"]
            score = rec["score"]
            reasons = rec["reasons"]

            print(f"#{index} {song['title']} — {song['artist']}")
            print(f"    Score: {score:.1f} / 5.5")
            for reason in reasons:
                print(f"    ✔ {reason}")
            print()


if __name__ == "__main__":
    main()
