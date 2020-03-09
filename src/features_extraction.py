from root import *

import pickle
import numpy as np
import pandas as pd
from sklearn.feature_selection import chi2
from sklearn.feature_extraction.text import TfidfVectorizer


with open(Pickles + '/clean_corpus.pickle', 'rb') as data:
    clean_corpus = pickle.load(data)
df = clean_corpus.reset_index().rename(columns={'index': 'Channel'})

channel_code = {'SMS': 1, 'EMAILS': 2, 'CHATS': 3}

# Communication Channel mapping
df['Channel_code'] = df['Channel']
df = df.replace({'Channel_code': channel_code})
corpus = df.drop('Channel', axis=1).copy()

# Parameter selection We have chosen different values as a first approximation and these are the ones that yield the
# most meaningful features

ngram_range = (1, 2)
min_df = 1
max_df = 7
user_input = 200


def __feats__(ngram_range,min_df, max_df, user_input ):


    tfidf = TfidfVectorizer(encoding='utf-8',
                            ngram_range=ngram_range,
                            stop_words=None,
                            lowercase=False,
                            max_df=max_df,
                            min_df=min_df,
                            max_features=user_input,
                            norm='l2',
                            sublinear_tf=True)

    features = tfidf.fit_transform(corpus.Messages)
    labels = corpus.Channel_code

    for wrd, channel_id in sorted(channel_code.items()):
        features_chi2 = chi2(features, labels == channel_id)
        indices = np.argsort(features_chi2[0])
        feature_names = np.array(tfidf.get_feature_names())[indices]
        unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
        bigrams = [v for v in feature_names if len(v.split(' ')) == 2]

        _list = []
        for k, in bigrams:
            bigrams.append(_list)

        _l =[]
        for z in wrd:
            wrd.append(_l)




    return [print("# '{}' channel:".format(_l)),
        print("  . Most correlated bigrams:\n. {}".format('\n. '.join(_list[-6:])))]




__feats__(ngram_range,min_df, max_df, user_input)

























