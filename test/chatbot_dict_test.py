import pickle
from utils.Preprocess import Preprocess

f = open("../train_tools/dict/chatbot_dict.bin", "rb")
word_index = pickle.load(f)
f.close()

sent = "내일 오전 10시에 스쿼트 하고 싶어 ㅋㅋ"

p = Preprocess(userdic='../utils/user_dict.tsv')

pos = p.pos(sent)

keyword = p.get_keyword(pos, without_tag=True)
for word in keyword:
    try:
        print(word, word_index[word])
    except KeyError: #해당 단어가 없는 경우 OOV 처리
        print(word, word_index['OOV'])