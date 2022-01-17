from utils.Preprocess import Preprocess

sent = "내일은 하체운동 하는 날이니, 잘 먹어놔야지"

p =Preprocess(userdic='../utils/user_dict.tsv')

pos = p.pos(sent)

ret = p.get_keyword(pos, without_tag= False)
print(ret)

ret = p.get_keyword(pos,without_tag=True)
print(ret)
