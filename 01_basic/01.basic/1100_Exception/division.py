print("Give me two numbers, and I will divide them.\n")
print("Input 'q' to quit.")

while True:
	num1 = input('\nEnter the first number: ')
	if num1 == 'q':
		break
	num1 = int(num1)

	num2 = input('Enter the second number: ')
	if num2 == 'q':
		break
	num2 = int(num2)

	try:
		result = num1 / num2
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(result)