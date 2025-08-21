import pandas as pd
import random


def load_movies(file_path="genre_movies_selenium.xlsx"):
    """Load scraped movies dataset"""
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"⚠️ Error loading file: {e}")
        return pd.DataFrame()

def suggest_movie(df, genre):
    """Suggest a random movie for a given genre"""
    # Filter movies for that genre
    genre_movies = df[df["Genre"].str.contains(genre, case=False, na=False)]

    if genre_movies.empty:
        return f"❌ No movies found for genre '{genre}'. Try another!"
    
    # Pick a random row
    movie = genre_movies.sample(n=1).iloc[0]
    return f"🎬 Suggested Movie: {movie['Title']} ({movie['Year']}) ⭐ {movie['Rating']}"

def main():
    df = load_movies()
    if df.empty:
        return
    
    while True:
        user_genre = input("\n👉 Enter a genre (or type 'exit' to quit): ").strip()
        if user_genre.lower() == "exit":
            print("👋 Goodbye! Happy watching!")
            break

        suggestion = suggest_movie(df, user_genre)
        print(suggestion)

if __name__ == "__main__":
    main()
