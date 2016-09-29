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
		numbers = []
		for item in list_input[1:]:
			numbers.append(int(item))

		maths = {
			"+": add,
			"-": subtract,
			"*": multiply,
			"/": divide,
			"square": square,
			"cube": cube,
			"pow": power,
			"mod": mod
			}

		fn_to_call = maths[list_input[0]]

		print fn_to_call(numbers)
		