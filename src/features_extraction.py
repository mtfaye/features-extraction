from root import *

import pickle
import numpy as np
from sklearn.feature_selection import chi2
from sklearn.feature_extraction.text import TfidfVectorizer

with open(Pickles + '/clean_corpus.pickle', 'rb') as data:
    clean_corpus = pickle.load(data)
df = clean_corpus.reset_index().rename(columns={'index': 'Channel'})

channel_code = {'SMS': 1, 'EMAILS': 2, 'CHATS': 3}

# Communication Channel mapping
df['Channel_code'] = df['Channel']
df = df.replace({'Channel_code': channel_code})
df = df.drop('Channel', axis=1).copy()

# Parameter selection We have chosen different values as a first approximation and these are the ones that yield the
# most meaningful features
ngram_range = (1, 2)
min_df = 1
max_df = 7
max_features = 200


def extract_features(ngram_range, min_df, max_df, max_features):
    tfidf = TfidfVectorizer(encoding='utf-8',
                            ngram_range=ngram_range,
                            stop_words=None,
                            lowercase=False,
                            max_df=max_df,
                            min_df=min_df,
                            max_features=max_features,
                            norm='l2',
                            sublinear_tf=True)

    features = tfidf.fit_transform(df.Messages).toarray()
    labels = df.Channel_code

    for wrd, channel_id in sorted(channel_code.items()):
        features_chi2 = chi2(features, labels == channel_id)
        indices = np.argsort(features_chi2[0])
        feature_names = np.array(tfidf.get_feature_names())[indices]
        unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
        bigrams = [v for v in feature_names if len(v.split(' ')) == 2]




       # return [
       #     print("# '{}' channel:".format(wrd)),
       #     print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-6:]))),
       #    print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-6:]))),
         #   print("")

        #]

extract_features(ngram_range, min_df, max_df, max_features)
