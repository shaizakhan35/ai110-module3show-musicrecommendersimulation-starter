import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and return a list of song dictionaries."""
    path = Path(csv_path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parents[1] / path

    with path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        songs = []
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": str(row["title"]),
                    "artist": str(row["artist"]),
                    "genre": str(row["genre"]),
                    "mood": str(row["mood"]),
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return (score, reasons)."""
    preferred_genre = user_prefs.get("preferred_genre", user_prefs.get("genre"))
    preferred_mood = user_prefs.get("preferred_mood", user_prefs.get("mood"))
    preferred_energy = user_prefs.get("preferred_energy", user_prefs.get("energy"))
    preferred_valence = user_prefs.get("preferred_valence", user_prefs.get("valence"))

    reasons: List[str] = []
    score = 0.0

    if song.get("genre") == preferred_genre:
        score += 1.0
        reasons.append(f"genre match: {song.get('genre')} (+1.0)")
    else:
        reasons.append(
            f"genre mismatch: {song.get('genre')} vs {preferred_genre} (0.0)"
        )

    if song.get("mood") == preferred_mood:
        score += 1.5
        reasons.append(f"mood match: {song.get('mood')} (+1.5)")
    else:
        reasons.append(
            f"mood mismatch: {song.get('mood')} vs {preferred_mood} (0.0)"
        )

    if preferred_energy is not None and song.get("energy") is not None:
        energy_proximity = 1 - abs(float(preferred_energy) - float(song["energy"]))
        score += (energy_proximity * 2.0)
        reasons.append(f"energy proximity: {energy_proximity:.2f} (+{(energy_proximity * 2.0):.2f})")

    if preferred_valence is not None and song.get("valence") is not None:
        valence_proximity = 1 - abs(float(preferred_valence) - float(song["valence"]))
        score += valence_proximity
        reasons.append(f"valence proximity: {valence_proximity:.2f} (+{valence_proximity:.2f})")

    return round(score, 3), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Dict]:
    """Return the top-k recommended songs as dicts with score and reasons."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append(
            {
                "song": {
                    "title": song["title"],
                    "artist": song["artist"],
                    "genre": song["genre"],
                    "mood": song["mood"],
                    "energy": song["energy"],
                    "valence": song["valence"],
                },
                "score": score,
                "reasons": reasons,
            }
        )

    scored_songs.sort(key=lambda item: item["score"], reverse=True)
    return scored_songs[:k]
