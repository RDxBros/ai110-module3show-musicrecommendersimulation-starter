"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

USER_PROFILES = [
    {"name": "High-Energy Pop", "genre": "pop", "mood": "happy", "energy": 0.85, "acoustic": False},
    {"name": "Chill Lofi", "genre": "lofi", "mood": "chill", "energy": 0.4, "acoustic": True},
    {"name": "Deep Intense Rock", "genre": "rock", "mood": "intense", "energy": 0.9, "acoustic": False},
]


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for prefs in USER_PROFILES:
        recommendations = recommend_songs(prefs, songs, k=5)

        print(f"\nTop {len(recommendations)} for {prefs['name']}")
        print(f"(genre={prefs['genre']}, mood={prefs['mood']}, energy={prefs['energy']})")
        print("=" * 40)
        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n{i}. {song['title']} - {song['artist']}")
            print(f"   Genre: {song['genre']} | Mood: {song['mood']}")
            print(f"   Score: {score:.2f} / 5.00")
            print(f"   Why: {explanation}")


if __name__ == "__main__":
    main()
