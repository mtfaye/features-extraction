from root import *

import re
import json
import string
import pandas as pd
from nltk.corpus import stopwords




def load(input_data):
    # load input raw data and convert to dataframe

    load_ = []
    with open(raw) as f:
        for line in f:
            load_.append(json.loads(line))
    df = pd.DataFrame.from_dict(load_, orient='columns').transpose()
    df.columns = ['Messages']
    return df


text_processed = load(raw)



def cleaning(text):
    # 3 rounds of cleaning- see notebooks for more details on my approach

    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)

    # Copied as much as possible some chinese and hindu characters from the dataset because they are not supported by
    # the tools
    text = re.sub('是东亚地区统一的一党主权国家门特别行政区照总面积计算現在裤脚許多人需要同意還沒有重庆鞋子全部打湿完了我會等待確認裤脚鞋子全部打湿完了こんにちはこれは日本語の例です', '',
                  text)
    return text


# Remove square brackets
rounds_of_cleaning = lambda x: cleaning(x)
clean_corpus = pd.DataFrame(text_processed.Messages.apply(rounds_of_cleaning))

# Remove top words for all languages supported by nltk
stop_words = list(stopwords.words())

for stop_word in stop_words:
    regex_stopword = r"\b" + stop_word + r"\b"
    clean_corpus['Messages'] = clean_corpus['Messages'].str.replace(regex_stopword, '')




