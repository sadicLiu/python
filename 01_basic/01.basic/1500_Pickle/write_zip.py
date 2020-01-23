import bz2
import pickle

person_dict = {'Zhangsan': 20, 'Lisi': 22, 'Wangwu': 33}
dog_dict = {'dahei': 1, 'xiaohei': 2}

filename = 'person'
sfile = bz2.BZ2File('smallerfile', 'w')

pickle.dump((person_dict, dog_dict), sfile)
