import pandas as pd



def topic_words(lda_model, vectorizer, ntokens = 10):
    '''Generate  a pandas dataframe of words associated with a scikit-learn topic model.
    Keyword arguments:
    lda_model  -- fitted lda model
    vectorizer -- fitted scikit-learn vectorizer used to construct word frequencies used in the topic model.
    '''


    def column_swap(column):
        column = column.sort_values(ascending = False)
        return column.index



    word_topic_scores = lda_model.components_.T
    vocabulary        = vectorizer.get_feature_names()

    # Column names based on number of topics
    number_of_topics = lda_model.get_params()['n_components']
    column_names = ['Topic %s' % i for i in range(1, number_of_topics + 1)]

    #data frame of words and scores by topic
    topic_words_df = pd.DataFrame(word_topic_scores,
                                  index = vocabulary,
                                  columns = column_names)

    # Resort so each column is sorted by word_topic_score
    topic_words_df = topic_words_df.apply(column_swap).reset_index(drop = True).rename_axis('rank')

    # start at 1, not zero for rank
    topic_words_df.index = topic_words_df.index + 1

    topic_words_df = topic_words_df.head(ntokens).T

    return topic_words_df
