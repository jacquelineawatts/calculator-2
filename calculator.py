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

		maths = {
			"+": (add, 2),
			"-": (subtract, 2),
			"*": (multiply, 2),
			"/": (divide, 2),
			"square": (square, 1),
			"cube": (cube, 1),
			"pow": (power, 2),
			"mod": (mod, 2)
			}

		fn_to_call, num_args = maths[list_input[0]]


		if num_args == 1:
			print fn_to_call(int(list_input[1]))
		elif num_args == 2:
			print fn_to_call(int(list_input[1]), int(list_input[2]))
		
# "reduce" "*""  <--- Increase number of arguments