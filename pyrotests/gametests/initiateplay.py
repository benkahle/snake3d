import os

os.system('clear')
x = input('Welcome to Super Mega Snake. Please press 1 for single player, 2 for double player, and 3 for networked play.')

if x == 1:
	os.system('python vpythontests.py')
elif x == 2:
	os.system('python battlesnake.py')
elif x == 3:
	os.system('python snakeclient.py')