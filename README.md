# similar_item_recommendation
Recommender Systems Project SS19

*** Project A: Similar item recommendations ***
The goal is to experiment with different strategies to generate recommendations of similar items. The movie domain can be used for this experiment. 

Generally, similar item recommendations can be found on many websites, including video streaming sites. It is, however, not always immediately clear when we should consider two movies to be similar.
It could be because they have the same actors, the same director, similar plot descriptions, the same genre, or just a similar movie cover. 

The first task in this project is to develop a number of (at least 5) functions in Python that, given a reference movie ID, return a ranked list of the top-5 most similar items. Each function has to implement a different strategy.

For the experiment, you can use the MovieLens 20M (or a smaller) dataset, which also contains some content information, see: 
https://grouplens.org/datasets/movielens/

In addition, a number of additional movie features can be found here:
https://drive.google.com/file/d/1je77e0Lq8naVUsjoOzk5RuI2H3ceHlSz/view )(500 MB)

This zip file contains a number of JSON-files, each file containing additional data for a given movie (but no ratings). The MovieLens dataset can be combined with this dataset based on the field “movielensID”.

Next, implement a user interface, where the reference movie can be searched by title. The user can then select one of the returned search results and the system then presents five lists, each one containing similar movie recommendations.
Each list is based on one of the implemented similarity functions.

The user interface can either be web-based (e.g., using the Django framework) or simply a console application.
In any case, it has to be designed in a way that it is reasonably easy to use in terms of searching, movie selection, and the analysis of the results.

The final task lies in the evaluation of the different strategies. Try out at least 20 movies from different genres and manually inspect the different result lists.
Write a short report that summarizes the observations.
Possible contents could be: Which recommendation method led to the best results? Which method led to surprises? Which method led to poor or unexpected results etc.
Submit your project code including light documentation and the report by the agreed deadline.
