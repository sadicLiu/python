filename = 'alien.txt'
try:
	with open(filename) as f:
		content = f.read()
		print(content)
except FileNotFoundError:
	print('No such file!')