import numpy as np
import pandas as pd


def class_words(classifier, vectorizer, nlargest=5):
    """Generate  a pandas dataframe of words and coefficients
    from with a classifier
    Keyword arguments:
    classifier  -- fitted scikit-learn  classifier
    vectorizer  -- fitted scikit-learn vectorizer used to construct classifier features.
    nlargest    -- number of tokes per class to return

    Note: probably breaks for binary outcomes.
    """

    word_df = pd.DataFrame(
        np.matrix.transpose(classifier.coef_), columns=classifier.classes_
    )

    word_df["token"] = vectorizer.get_feature_names()

    word_df_long = word_df.melt(
        id_vars="token", var_name="class", value_name="estimate"
    )

    word_df_long = word_df_long.set_index("token")

    return word_df_long.groupby("class")["estimate"].nlargest(nlargest).to_frame()
