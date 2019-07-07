from django.shortcuts import render
from .Recommender import movie_recommender
import os
import json


# Create your views here.
def result_view(request, *args, **kwargs):
    rec = movie_recommender.Recommender("carl")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    extractedpath = os.path.join(BASE_DIR, 'pages/Recommender/extracted_content_ml-latest/')

    if request.method == 'POST':
        form = request.POST
        #print(form)
        name = form['search field']
        movie_id = rec.get_id(name)
        #print(movie_id)

    else:
        movie_id = 1

    output = rec.same_actors(movie_id)
    output2 = rec.same_directors(movie_id)
    output3 = rec.same_genres(movie_id)
    output4 = rec.similar_plot_description(movie_id)
    output5 = rec.similar_keywords(movie_id)
    output6 = rec.similar_genome(movie_id)


    #structure looks like this [0] = movie 1 and then first item added is the poster and the secin is the name

    # data_all = [[],[],[],[],[]]
    # indexes = []
    #
    # for index, item in enumerate(output, start=0):
    # #for id in output:
    #
    #     with open(extractedpath + str(item) + '.json', encoding="utf8") as json_file:
    #         data = json.load(json_file)
    #         poster = data['movielens']['posterPath']
    #         name = data['movielens']['title']
    #
    #     data_all[index].append(poster)
    #     data_all[index].append(name)
    #     indexes.append(index)
    #     print (index)

    sameactor = create_movie_data(output)
    samedirector = create_movie_data(output2)
    samegenre = create_movie_data(output3)
    similarplot = create_movie_data(output4)
    similarkeywords = create_movie_data(output5)
    similargenome = create_movie_data(output6)

    my_context = {
        #"output": output,
        #"poster": data_all[0],
        #"names": data_all[1],
        "sameactor": sameactor,
        "samedirector": samedirector,
        "samegenre": samegenre,
        "similarplot": similarplot,
        "similarkeywords": similarkeywords,
        "similargenome": similargenome,
        "name": name
        #"indexes": indexes

    }

    return render(request, "result.html", my_context)


def initial_view(request, *args, **kwargs):
    my_context = {
    }
    return render(request, "home.html", my_context)


def movie_view(request, *args, **kwargs):
    my_context = {
    }
    return render(request, "moviehunter/index.html", my_context)


def create_movie_data(output):

    rec = movie_recommender.Recommender("carl")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    extractedpath = os.path.join(BASE_DIR, 'pages/Recommender/extracted_content_ml-latest/')

    data_all = [[], [], [], [], []]
    indexes = []

    for index, item in enumerate(output, start=0):
        # for id in output:

        with open(extractedpath + str(item) + '.json', encoding="utf8") as json_file:
            data = json.load(json_file)
            poster = data['movielens']['posterPath']
            name = data['movielens']['title']

        data_all[index].append(poster)
        data_all[index].append(name)
        indexes.append(index)
        #print(index)

    return data_all