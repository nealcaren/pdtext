#!/usr/bin/env python
# coding: utf-8

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re


def word_count(text, tokenizer="(\w[\w']*\w|\w)"):

    # Split words, counting contractions as one word
    rgx = re.compile(tokenizer)

    try:
        # it it is a string
        return len(rgx.findall(text))
    except:
        # If it is a pandas column
        return text.apply(rgx.findall).str.len()


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
