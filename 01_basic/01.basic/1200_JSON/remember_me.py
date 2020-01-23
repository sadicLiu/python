import json

filename = 'username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What's your name?")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username)