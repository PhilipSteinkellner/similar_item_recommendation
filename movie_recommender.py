import json
import pandas as pd

# All Movies
movies = pd.read_csv('./ml-1m/movies.dat', header=None, encoding="ISO-8859-1", sep="::",
                     names=["MovieID", "Title", "Genres"], engine='python')


def same_actors(movie_id):

    # series to store movies with their similarity score
    similar_movies = pd.Series()

    # check if json file exists for the given movie, if not return an empty list
    try:
        with open('./extracted_content_ml-latest/' + str(movie_id) + '.json', encoding="utf8") as json_file:
            data = json.load(json_file)
            actors = data['movielens']['actors']
    except FileNotFoundError:
        return []

    # for all movies
    for key, row in movies.iterrows():
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
            with open('./extracted_content_ml-latest/' + str(movie_id_2) + '.json', encoding="utf8") as json_file:
                data = json.load(json_file)
                actors_2 = data['movielens']['actors']
        except FileNotFoundError:
            continue

        # check if the 2 movies have actors in common, if so increase the score for each actor by 1
        for actor in actors:
            if actor in actors_2:
                score += 1

        # add the movie and the score to the series
        similar_movies.loc[movie_id_2] = score

    # sort the series, the movie with the highest score being on top
    similar_movies = similar_movies.sort_values(ascending=False)

    # return the 5 most similar movies
    list = []
    for key, value in similar_movies.head(5).iteritems():
        list.append(key)

    print(similar_movies.head(5))
    return list


def same_director(movie_id):

    return []


def same_genres(movie_id):

    return []


def similar_plot_description(movie_id):

    return []


def similar_keywords(movie_id):

    return []


if __name__ == '__main__':

    result = same_actors(1)

    print(result)