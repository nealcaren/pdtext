#!/usr/bin/env python
# coding: utf-8

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from string import punctuation

def word_count(text, include_numbers = True):

    '''Count number of words in a string.
    text = string to count.
    include_numbers = Boolean on whether to include numbers as words.
    '''

    if include_numbers == True:
        return sum([len(w.strip(punctuation))>0 for w in text.split()])
    else:
        return sum([w.strip(punctuation).isalpha() for w in text.split()])



def make_wf_df(text_column, summary=False, **kwargs):
    vectorizer = CountVectorizer(**kwargs, token_pattern=r"(?u)\b\w+\b")

    wf = vectorizer.fit_transform(text_column)

    index = text_column.index

    word_freq_df = pd.DataFrame(
        wf.toarray(), columns=vectorizer.get_feature_names(), index=index
    )
    if summary == False:
        return word_freq_df

    summary_df = word_freq_df.sum().sort_values(ascending=False)
    return summary_df


# In[ ]:
