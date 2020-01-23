import pickle

person_dict = {'Zhangsan': 20, 'Lisi': 22, 'Wangwu': 33}
dog_dict = {'dahei': 1, 'xiaohei': 2}

filename = 'person'
outfile = open(filename, 'wb')

pickle.dump((person_dict, dog_dict), outfile)
outfile.close()
