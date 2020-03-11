import pickle
import pandas as pd
from __PATH_FILES__ import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# load saved corpus - see path on __PATH_FILES__
with open(Pickles + '/clean_corpus.pickle', 'rb') as data:
    clean_corpus = pickle.load(data)
df = clean_corpus.reset_index().rename(columns={'index': 'Channel'})

channel_code = {'SMS': 1, 'EMAILS': 2, 'CHATS': 3}

# Channel mapping
df['Channel_code'] = df['Channel']
df = df.replace({'Channel_code': channel_code})
corpus = df.drop('Channel', axis=1).copy()


def extract_features():
    count_vec = CountVectorizer(stop_words=None,
                                analyzer='word',
                                ngram_range=(3, 3),
                                max_df=0.8,
                                min_df=0.3,
                                token_pattern=r"(?u)\b\w+\b",
                                max_features=None)

    dt_mat = count_vec.fit_transform(corpus.Messages)

    tfidf_transformer = TfidfTransformer()
    tfidf_mat = tfidf_transformer.fit_transform(dt_mat)

    # Convert sparse matrix to a dense representation and wrap it in a dataFrame
    trigrams = pd.DataFrame(dt_mat.todense(), index=corpus.index, columns=count_vec.get_feature_names())
    trigrams['channel_code'] = df.Channel_code

    trigrams_long = (pd.melt(trigrams.reset_index(), id_vars=['index','channel_code'],
                             value_name='count').query('count > 0').sort_values(['index', 'channel_code']))

    # Repeat for tfdif
    tfidf = pd.DataFrame(tfidf_mat.todense(), index=df.index, columns=count_vec.get_feature_names())
    tfidf['channel_code'] = df.Channel_code

    tfidf_long = pd.melt(tfidf.reset_index(), id_vars=['index', 'channel_code'], value_name='score').query('score > 0')

    # Merge trigrams and tfidf
    fulldf = (trigrams_long.merge(tfidf_long, on=['index', 'channel_code', 'variable']).set_index('index'))
    fulldf.score = fulldf.score.round(2)

    # Filter the 20 highest scores for each channel
    result = fulldf.groupby('channel_code').apply(lambda x: x.nlargest(15, 'count')).reset_index(drop=True)
    result = result.applymap(str)

    return result


# Save result
with open(outfiles + 'features' + '.pickles', 'wb') as output:
    pickle.dump(extract_features(), output)

print(extract_features())
