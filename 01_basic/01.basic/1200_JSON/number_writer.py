import json

numbers = [1, 3, 2, 4, 5, 6]
filename = 'numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)