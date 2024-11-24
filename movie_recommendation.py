import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample Movie Dataset
data = {
    'title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Avengers: Endgame',
        'Mad Max: Fury Road', 'Jurassic Park', 'The Terminator', 'Fight Club', 'The Shawshank Redemption',
        'Parasite', 'Black Panther', 'Gladiator', 'Dune', 'The Prestige',
        'The Batman', 'Tenet', 'Edge of Tomorrow', 'John Wick', 'Blade Runner 2049'
    ],
    'genres': [
        'Action Sci-Fi', 'Action Sci-Fi Thriller', 'Adventure Drama Sci-Fi', 'Action Crime Drama',
        'Action Adventure Sci-Fi', 'Action Sci-Fi', 'Adventure Sci-Fi', 'Action Sci-Fi',
        'Drama Thriller', 'Drama', 'Drama Thriller', 'Action Sci-Fi', 'Action Drama',
        'Sci-Fi Drama', 'Drama Thriller', 'Action Thriller', 'Sci-Fi Action',
        'Action Sci-Fi', 'Action Thriller', 'Sci-Fi Thriller'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# TF-IDF Vectorization of the Genres
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genres'])

# Compute Similarity Scores
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to Get Movie Recommendations
def recommend_movies(title, df, cosine_sim):
    # Ensure the title exists in the dataset
    if title not in df['title'].values:
        return f"No movie found with the title '{title}'. Please check your input."
   
    # Get the index of the movie
    idx = df[df['title'] == title].index[0]
   
    # Get pairwise similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
   
    # Sort scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
   
    # Get top 5 similar movies
    top_similar = sim_scores[1:6]  # Exclude the input movie itself
   
    # Fetch the titles of similar movies
    recommended_titles = [df['title'].iloc[i[0]] for i in top_similar]
   
    return recommended_titles

# User Input
user_movie = input("Enter a movie title: ").strip()

# Get Recommendations
recommendations = recommend_movies(user_movie, df, cosine_sim)

# Display Recommendations
if isinstance(recommendations, list):
    print(f"Movies similar to '{user_movie}':")
    for movie in recommendations:
        print(f"- {movie}")
else:
    print(recommendations)
