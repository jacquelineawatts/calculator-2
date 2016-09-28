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
			argument_1 = int(list_input[1])

		if list_input[0] == "+":
			result = add(argument_1, argument_2)
			print result

		elif list_input[0] == "-":
			result = subtract(argument_1, argument_2)
			print result

		elif list_input[0] == "*":
			result = multiply(argument_1, argument_2)
			print result

		elif list_input[0] == "/":
			result = divide(argument_1, argument_2)
			print result

		elif list_input[0] == "square":
			result = square(argument_1)
			print result

		elif list_input[0] == "cube":
			result = cube(argument_1)
			print result

		elif list_input[0] == "pow":
			result = power(argument_1, argument_2)
			print result

		elif list_input[0] == "mod":
			result = mod(argument_1, argument_2)
			print result