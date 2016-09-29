"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculate(operand, numbers):
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

	fn_to_call = maths[operand]
	print fn_to_call(numbers)


while True:
	user_input = raw_input(">")

	if user_input == "q":
		break
	else:
		list_input = user_input.split(" ")
		numbers = []
		for item in list_input[1:]:
			for char in item:
				if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
					numbers.append(int(item))
				else:
					print "Your entry doesn't look like a number! This is a calculator! Please try again."
					break
		calculate(list_input[0], numbers)
		
