import csv
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
    """Reads the CSV and returns a list of song dicts with numeric fields converted to int/float."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            for key in ("energy", "valence", "danceability", "acousticness"):
                row[key] = float(row[key])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song against the user prefs (max 5.0) and returns (score, list of reasons)."""
    score = 0.0
    reasons = []

    user_genre = user_prefs["genre"].lower()
    song_genre = song["genre"].lower()
    if song_genre == user_genre:
        score += 2.0
        reasons.append(f"genre match ({song['genre']}) +2.0")
    elif user_genre in song_genre or song_genre in user_genre:
        score += 1.0
        reasons.append(f"related genre ({song['genre']}) +1.0")

    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.0
        reasons.append(f"mood match ({song['mood']}) +1.0")

    energy_sim = 1.0 - abs(user_prefs["energy"] - song["energy"])
    score += 1.5 * energy_sim
    reasons.append(f"energy closeness +{1.5 * energy_sim:.2f}")

    acoustic_target = 1.0 if user_prefs.get("acoustic", False) else 0.0
    acoustic_sim = 1.0 - abs(acoustic_target - song["acousticness"])
    score += 0.5 * acoustic_sim
    reasons.append(f"acousticness fit +{0.5 * acoustic_sim:.2f}")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song, sorts high to low, and returns the top k as (song, score, explanation)."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, ", ".join(reasons)))
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
