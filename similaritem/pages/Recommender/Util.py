import numpy as np
def tfIdfVectorize(texts):
    # given a list of plots represented as strings, maps them into vectors in which each word is represented by its
    # tf-idf weight
    from sklearn.feature_extraction.text import TfidfVectorizer

    # definining the vectorizer with english stopwords
    vectorizer = TfidfVectorizer(stop_words='english')

    vectorized_plots = vectorizer.fit_transform(texts)

    return vectorized_plots

def countVectorize(strings):
    from sklearn.feature_extraction.text import CountVectorizer

    # definining the vectorizer with english stopwords
    vectorizer = CountVectorizer()

    vectorized_plots = vectorizer.fit_transform(strings)

    return vectorized_plots

def getCosineSimilarity(vect1,vect2):
    # given 2 vectorized plots returns the cosine similarity between them
    from sklearn.metrics.pairwise import linear_kernel
    # Generate cosine similarities
    cosineSimilarity = linear_kernel(vect1, vect2)
    return cosineSimilarity

def minMaxScaling(vals):
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 1))
    vals = scaler.fit_transform(vals)
    return vals

