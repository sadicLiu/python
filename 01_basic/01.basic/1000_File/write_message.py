filename = 'message.txt'

# 'w': 以写入模式打开这个文件
# 打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）
# 如果你省略了模式实参，Python将以默认的只读模式打开文件
with open(filename, 'w') as f:
	# message = 'I love programming!'
	# message = 10
	f.write('I love programming!\n')
	f.write('I love deep learning!\n')

with open(filename, 'a') as f:
	f.write('I also love bodybuilding\n')


