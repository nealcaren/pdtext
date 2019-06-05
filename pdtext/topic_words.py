from . import helpers


def topic_words(lda_model, vectorizer):
    '''
    Generate dataframe of words associated with a topic model.
    '''

    word_topic_scores = lda_model.components_.T
    vocabulary        = vectorizer.get_feature_names()


    topic_words_df = pd.DataFrame(word_topic_scores,
                                  index = vocabulary)

    topic_words_df = topic_words_df.apply(helpers.column_swap).reset_index(drop = True).rename_axis('rank')

    topic_words_df.index = topic_words_df.index + 1

    return topic_words_df
