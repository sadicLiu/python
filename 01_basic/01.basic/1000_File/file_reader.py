# 一次读取所有内容
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

print('\n')

# 逐行读取
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())

print('\n')

# 先将文件内容存储到列表中,之后再读取列表
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

pi = ''
for line in lines:
	pi += line.strip()
print(pi)
print(len(pi))