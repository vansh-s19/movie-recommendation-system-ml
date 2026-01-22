import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""### DATA COLLECTION AND PRE-PROCESSING"""

#loading the data
movies_data = pd.read_csv('/Users/vanshsaxena/Documents/Machine Learning Models/Movie Recommendation System/data/movies.csv')


#selecting the relevant features for recommedation
selected_features = ['genres','keywords','tagline','director','cast']


#replacing the null values with null string
for features in selected_features:
  movies_data[features] = movies_data[features].fillna('')

#combining all the 5 selected features
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['director']+' '+movies_data['cast']

#converting the text data into feature vectors
vectorizer = TfidfVectorizer()
feature_vector = vectorizer.fit_transform(combined_features)

"""### Cosine Similarity Score"""

#Getting the similarity score using the Cosine Similarity
similarity = cosine_similarity(feature_vector)

# getting the movie name from user
movie_name = input(' Enter ypur favourite movie name : ')

#creating a list with all the movie names given in the dataset
list_of_all_titles = movies_data['title'].tolist()

#finding the close match for the movie name given by the user
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]

#find the index of the movie with title
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

#getting the list of similar movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))

#sorting the movies based on the similarity score
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

#Print the names of the similar movies based on the index
print('Movies Suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if  (i<21):
    print(i, '.', title_from_index)
    i+=1
