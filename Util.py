
def vectorizePlots(plots):
    # given a list of plots represented as strings, maps them into vectors in which each word is represented by its
    # tf-idf weight
    from sklearn.feature_extraction.text import TfidfVectorizer

    # definining the vectorizer with english stopwords
    vectorizer = TfidfVectorizer(stop_words='english')

    vectorized_plots = vectorizer.fit_transform(plots)

    return vectorized_plots

def getPlotSimilarity(plot1,plot2):
    # given 2 vectorized plots returns the cosine similarity between them
    from sklearn.metrics.pairwise import linear_kernel
    # Generate cosine similarities
    cosineSimilarity = linear_kernel(plot1,plot2)
    return cosineSimilarity

#def getMostSimilarPlots(plots):

