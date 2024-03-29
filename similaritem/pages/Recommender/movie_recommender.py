import json
import pandas as pd
# only for django else without the dot
from . import Util
from sklearn.preprocessing import MinMaxScaler
from django.urls import path
import numpy as np

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'Recommender/ml-1m/movies.dat')
file_path_big = os.path.join(BASE_DIR, 'Recommender/ml-20m/movies.csv')
file_path_genome = os.path.join(BASE_DIR, 'Recommender/ml-20m/genome-scores.csv')


class Recommender:
    # pfad = path()
    # print(pfad )

    extractedpath = os.path.join(BASE_DIR, 'Recommender/extracted_content_ml-latest/')

    # All Movies
    movies = pd.read_csv(file_path, header=None, encoding="ISO-8859-1", sep="::",
                         names=["MovieID", "Title", "Genres"], engine='python')

    # All movies of movielens 20M
    movies_big = pd.read_csv(file_path_big, skiprows=1, encoding="ISO-8859-1", sep=",",
                             names=["MovieID", "Title", "Genres"], engine='python')

    def __init__(self, username):

        self.username = username

    def same_actors(self, movie_id):

        # series to store movies with their similarity score
        similar_movies = pd.DataFrame(columns=['MovieID', 'Score', 'Popularity'])

        # check if json file exists for the given movie, if not return an empty list
        try:
            with open(self.extractedpath + str(movie_id) + '.json', encoding="utf8") as json_file:
                data = json.load(json_file)
                actors = data['movielens']['actors']
        except FileNotFoundError:
            return []

        # for all movies
        for key, row in self.movies.iterrows():
            # movieID of the current movie
            movie_id_2 = row['MovieID']
            # if the current movie is the same movie as the movie for which the similarity values are computed,
            # ignore this movie
            if movie_id == movie_id_2:
                continue

            # how many actors the movies have in common
            score = 0

            # check if json file exists for the given movie, if not skip this movie
            try:
                with open(self.extractedpath + str(movie_id_2) + '.json', encoding="utf8") as json_file:
                    data = json.load(json_file)
                    actors_2 = data['movielens']['actors']
                    popularity = data['movielens']['numRatings']
            except FileNotFoundError:
                continue

            # check if the 2 movies have actors in common, if so increase the score for each actor by 1
            for actor in actors:
                if actor in actors_2:
                    score += 1

            # add the movie, its score and its popularity to the dataframe
            similar_movies = similar_movies.append({
                'MovieID': movie_id_2,
                'Score': score,
                'Popularity': popularity
            }, ignore_index=True)

        # sort the dataframe, the movie with the highest score being on top
        # if there is a tie, rank the more popular movies higher
        similar_movies = similar_movies.sort_values(ascending=False, by=['Score', 'Popularity'])

        # return the 5 most similar movies
        list = []
        for key, row in similar_movies.head(5).iterrows():
            list.append(int(row['MovieID']))

        print("Same Actors")
        print(similar_movies.head(5))
        return list

    def same_directors(self, movie_id):

        # series to store movies with their similarity score
        similar_movies = pd.DataFrame(columns=['MovieID', 'Score', 'Popularity'])

        # check if json file exists for the given movie, if not return an empty list
        try:
            with open(self.extractedpath + str(movie_id) + '.json', encoding="utf8") as json_file:
                data = json.load(json_file)
                directors = data['movielens']['directors']
        except FileNotFoundError:
            return []

        # for all movies
        for key, row in self.movies.iterrows():
            # movieID of the current movie
            movie_id_2 = row['MovieID']
            # if the current movie is the same movie as the movie for which the similarity values are computed,
            # ignore this movie
            if movie_id == movie_id_2:
                continue

            # how many genres the movies have in common
            score = 0

            # check if json file exists for the given movie, if not skip this movie
            try:
                with open(self.extractedpath + str(movie_id_2) + '.json', encoding="utf8") as json_file:
                    data = json.load(json_file)
                    directors_2 = data['movielens']['directors']
                    popularity = data['movielens']['numRatings']
            except FileNotFoundError:
                continue

            # if there are not any directors specified for the movie, skip this iteration
            if len(directors) == 0:
                continue

            # check if the 2 movies have directors in common, if so increase the score for each director by 1
            for director in directors:
                if director in directors_2:
                    score += 1

            # normalize the score on the number of direcotrs of the  movie in comparison
            # score = score / len(directors_2)

            # add the movie, its score and its popularity to the dataframe
            similar_movies = similar_movies.append({
                'MovieID': movie_id_2,
                'Score': score,
                'Popularity': popularity
            }, ignore_index=True)

        # sort the dataframe, the movie with the highest score being on top
        # if there is a tie, rank the more popular movies higher
        similar_movies = similar_movies.sort_values(ascending=False, by=['Score', 'Popularity'])

        # return the 5 most similar movies
        list = []
        for key, row in similar_movies.head(5).iterrows():
            list.append(int(row['MovieID']))

        print(similar_movies.head(5))
        return list

    def same_genres(self, movie_id):
        # series to store movies with their similarity score
        similar_movies = pd.DataFrame(columns=['MovieID', 'Score', 'Popularity'])

        # check if json file exists for the given movie, if not return an empty list
        try:
            with open(self.extractedpath + str(movie_id) + '.json', encoding="utf8") as json_file:
                data = json.load(json_file)
                genres = data['movielens']['genres']
        except FileNotFoundError:
            return []

        # for all movies
        for key, row in self.movies.iterrows():
            # movieID of the current movie
            movie_id_2 = row['MovieID']
            # if the current movie is the same movie as the movie for which the similarity values are computed,
            # ignore this movie
            if movie_id == movie_id_2:
                continue

            # how many genres the movies have in common
            score = 0

            # check if json file exists for the given movie, if not skip this movie
            try:
                with open(self.extractedpath + str(movie_id_2) + '.json', encoding="utf8") as json_file:
                    data = json.load(json_file)
                    genres_2 = data['movielens']['genres']
                    popularity = data['movielens']['numRatings']
            except FileNotFoundError:
                continue

            # if there are not any genres specified for the movie, skip this iteration
            if len(genres_2) == 0:
                continue

            # check if the 2 movies have genres in common, if so increase the score for each genre by 1
            for genre in genres:
                if genre in genres_2:
                    score += 1

            # normalize the score on the number of genres of the  movie in comparison
            score = score / len(genres_2)

            # add the movie, its score and its popularity to the dataframe
            similar_movies = similar_movies.append({
                'MovieID': movie_id_2,
                'Score': score,
                'Popularity': popularity
            }, ignore_index=True)

        # sort the dataframe, the movie with the highest score being on top
        # if there is a tie, rank the more popular movies higher
        similar_movies = similar_movies.sort_values(ascending=False, by=['Score', 'Popularity'])

        # return the 5 most similar movies
        list = []
        for key, row in similar_movies.head(5).iterrows():
            list.append(int(row['MovieID']))

        # print(similar_movies.head(5))
        return list

    def similar_plot_description(self, movie_id):
        # check if json file exists for the given movie, if not return an empty list
        try:
            with open(self.extractedpath + str(movie_id) + '.json', encoding="utf8") as json_file:
                data = json.load(json_file)
                plot = data['movielens']['plotSummary']
                genres = data['movielens']['genres']
                movie_title = data['movielens']['originalTitle']
        except FileNotFoundError:
            return []

        # for all movies
        features = [(movie_id, plot, 1, 1, 0)]
        for key, row in self.movies.iterrows():
            # movieID of the current movie
            movie_id_2 = row['MovieID']

            # print("analyzing movie: " + str(movie_id_2))
            # if the current movie is the same movie as the movie for which the similarity values are computed,
            # ignore this movie
            if str(movie_id) == str(movie_id_2):
                continue

            # check if json file exists for the given movie, if not skip this movie
            try:
                with open(self.extractedpath + str(movie_id_2) + '.json', encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if "tmdb" not in data: continue
                    plot_2 = data['movielens']['plotSummary']
                    genres_2 = data['movielens']['genres']
                    avg_rate_2 = data['movielens']['avgRating']
                    movie_title = data['movielens']['originalTitle']
                    popularity_2 = data["tmdb"]["popularity"]
                    if not plot_2: continue
            except FileNotFoundError:
                continue

            # number of genres the 2 movies have in common
            common_genres = len([g for g in genres if g in genres_2])
            # normalization of the number of genres in common by the number of genres for the input movie
            genre_similarity = common_genres / len(genres_2)
            # normalized average rating for the movies
            normalized_rate = avg_rate_2 / 5.0

            # add the movie and the score to the series
            features.append((movie_id_2, plot_2, genre_similarity, normalized_rate, popularity_2))

        import numpy as np
        # mapping the movies plots to tfidf vectors
        vectorized_plots = Util.tfIdfVectorize(np.array(features)[:, 1])
        similarities = []

        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_popularities = scaler.fit_transform(np.array(features)[:, 4].reshape(-1, 1))

        for i, elem in enumerate(features):
            # calculating the plot similarity between current and input movie based on the cosine similarity between their
            # vectorized plots
            plot_similarity = Util.getCosineSimilarity(vectorized_plots[0], vectorized_plots[i])
            # measure of genre similarity between the 2 movies
            genre_similarity = features[i][2]
            # normalized avg rate of the movie
            rate = features[i][3]
            # scaled popularity
            scaled_popularity = scaled_popularities[i]
            # final predicted score for the current movie
            score = plot_similarity * genre_similarity * rate * scaled_popularity
            similarities.append((features[i][0], score))

        # sort the series, the movie with the highest score being on top
        similarities = sorted(similarities, key=lambda k: k[1], reverse=True)

        # return the 5 most similar movies
        list = []
        for elem in similarities[0:5]:
            list.append(elem[0])

        return list

    def similar_keywords(self, movie_id):
        # check if json file exists for the given movie, if not return an empty list
        try:
            with open(self.extractedpath + str(movie_id) + '.json', encoding="utf8") as json_file:
                data = json.load(json_file)
                # extracting tmdb keywords as a single string
                keywords = data['tmdb']['keywords']
                keywords = [k["name"] for k in keywords]
                keywords = ' '.join(keywords)
                genres = data['movielens']['genres']
                # movie_title = data['movielens']['originalTitle']
        except FileNotFoundError:
            return []

        # for all movies
        features = [(movie_id, keywords, 1, 1, 0)]
        for key, row in self.movies.iterrows():
            # movieID of the current movie
            movie_id_2 = row['MovieID']

            # print("analyzing movie: " + str(movie_id_2))
            # if the current movie is the same movie as the movie for which the similarity values are computed,
            # ignore this movie
            if str(movie_id) == str(movie_id_2):
                continue

            # check if json file exists for the given movie, if not skip this movie
            try:
                with open(self.extractedpath + str(movie_id_2) + '.json', encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if "tmdb" not in data: continue
                    # extracting keywords as a single string
                    keywords_2 = data['tmdb']['keywords']
                    keywords_2 = [k["name"] for k in keywords_2]
                    keywords_2 = ' '.join(keywords_2)
                    # extracting genres
                    genres_2 = data['movielens']['genres']
                    # extracting avg rate
                    avg_rate_2 = data['movielens']['avgRating']
                    # extracting movie title
                    movie_title = data['movielens']['originalTitle']
                    # extracting movie title
                    popularity_2 = data["tmdb"]["popularity"]
                    if not keywords_2: continue
            except FileNotFoundError:
                continue

            # number of genres the 2 movies have in common
            common_genres = len([g for g in genres if g in genres_2])
            # normalization of the number of genres in common by the number of genres for the input movie
            genre_similarity = common_genres / len(genres_2)
            # normalized average rating for the movies
            normalized_rate = avg_rate_2 / 5.0

            # add the movie and the score to the series
            features.append((movie_id_2, keywords_2, genre_similarity, normalized_rate, popularity_2))

        # mapping the movies plots to tfidf vectors
        vectorized_keywords = Util.countVectorize(np.array(features)[:, 1])

        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_popularities = scaler.fit_transform(np.array(features)[:, 4].reshape(-1, 1))

        similarities = []
        for i, elem in enumerate(features):
            # print("evaluating:  " + str(i))
            # calculating the plot similarity between current and input movie based on the cosine similarity between their
            # vectorized plots
            plot_similarity = Util.getCosineSimilarity(vectorized_keywords[0], vectorized_keywords[i])
            # measure of genre similarity between the 2 movies
            genre_similarity = features[i][2]
            # normalized avg rate of the movie
            rate = features[i][3]
            # scaled popularity
            scaled_popularity = scaled_popularities[i]
            # final predicted score for the current movie
            score = plot_similarity * genre_similarity * rate * scaled_popularity
            similarities.append((features[i][0], score))

        # sort the series, the movie with the highest score being on top
        similarities = sorted(similarities, key=lambda k: k[1], reverse=True)

        # return the 5 most similar movies
        list = []
        for elem in similarities[0:5]:
            list.append(elem[0])

        return list

    def similar_genome(self, movie_id):
        # check if json file exists for the given movie, if not return an empty list
        # check if json file exists for the given movie, if not return an empty list

        global genome

        print("genome list contruction done")

        try:
            with open(file_path_genome + str(movie_id) + '.json', encoding="utf8") as json_file:
                data = json.load(json_file)
                # extracting movie genres
                genres = data['imdb']['genres']
        except FileNotFoundError:
            return []

        # genome vector of the movie we want to get the recommendation for
        movie_genome_vector = genome[movie_id].reshape(1, -1)
        similarities = []
        for key, row in self.movies_big.iterrows():

            # movieID of the current movie
            movie_id_2 = row['MovieID']
            movie_title = row['Title']

            # print(movie_id_2)
            # print("analyzing movie: " + str(movie_id_2))
            # if the current movie is the same movie as the movie for which the similarity values are computed,
            # ignore this movie
            if str(movie_id) == str(movie_id_2) or movie_id_2 > 131171:
                continue

            # building genome vector for other movies
            movie_genome_vector_2 = genome[movie_id_2].reshape(1, -1)
            similarity = Util.getCosineSimilarity(movie_genome_vector, movie_genome_vector_2)[0][0]
            try:
                with open(self.extractedpath + str(movie_id_2) + '.json', encoding="utf8") as json_file:
                    data = json.load(json_file)
                    if "tmdb" not in data: continue
                    # extracting genres
                    genres_2 = data['imdb']['genres']
                    if not genres_2: continue

            except FileNotFoundError:
                continue

            # number of genres the 2 movies have in common
            common_genres = len([g for g in genres if g in genres_2])

            # normalization of the number of genres in common by the number of genres for the input movie
            genre_similarity = common_genres / len(genres_2)

            # add the movie and the score to the series
            similarities.append((movie_id, similarity * genre_similarity))

        # sort the series, the movie with the highest score being on top
        similarities = sorted(similarities, key=lambda k: k[1], reverse=True)

        # return the 5 most similar movies
        list = []
        for elem in similarities[0:5]:
            list.append(elem[0])

        return list



    # ****************************************************************************
    # methods used for django

    def echo(self, somestring):
        # print(somestring + " 3" )
        return somestring + " 3"

    # returns id
    def get_id(self, name):

        id = -1

        print(name)

        for key, row in self.movies_big.iterrows():

            title = row['Title']
            title = title[:-6].strip()
            title = title.strip('"')

            if title.lower() == name.lower():
                id = row['MovieID']

            else:
                continue

        return id

    def get_name(self, id):
        name = "No Name"
        for key, row in self.movies.iterrows():

            m_id = row['MovieID']

            # print(m_id == name)

            if id == m_id:
                # print(key)
                name = row['Title']

            else:
                continue

        return name


if __name__ == '__main__':
    recommender = Recommender("CARL")

    result = recommender.same_actors(1)
    result2 = recommender.same_directors(1)
    # result = same_genres(1)
    # result = similar_plot_description(1)
    print('+++++')
    print(result)
    print('**************')
    # print(result2)

    '''for key, row in movies.iterrows():
        try:
            with open('./extracted_content_ml-latest/' + str(row['MovieID']) + '.json', encoding="utf8") as json_file:
                data = json.load(json_file)
                director = data['movielens']['directors']
                print(director)
        except FileNotFoundError:
            continue'''
