# 챗봇에서 사용할 사전파일 생성

from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

# Load corpus data


def read_corpus_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data


corpus_data = read_corpus_data('./corpus.txt')

# create preprocess object
p = Preprocess()
dict = []  # strore preprocessed corpus data in dict array
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])

tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

f = open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()
