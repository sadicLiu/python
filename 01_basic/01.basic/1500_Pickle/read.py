import pickle

filename = 'person'

infile = open(filename, 'rb')
person_dict, dog_dict = pickle.load(infile)
infile.close()

print(person_dict)
print(dog_dict)
