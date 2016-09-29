"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
while True:
	user_input = raw_input(">")

	if user_input == "q":
		break
	else:
		list_input = user_input.split(" ")
		if len(list_input) == 3:
			argument_1, argument_2 = int(list_input[1]), int(list_input[2])
		elif len(list_input) == 2:
			argument_1, argument_2 = int(list_input[1]), 5

		maths = {
			"+": add(argument_1, argument_2), 
			"-": subtract(argument_1, argument_2), 
			"*": multiply(argument_1, argument_2), 
			"/": divide(argument_1, argument_2), 
			"square": square(argument_1), 
			"cube": cube(argument_1), 
			"pow": power(argument_1, argument_2), 
			"mod": mod(argument_1, argument_2)}


		if list_input[0] in maths:
			value = maths[list_input[0]]
			print value
		