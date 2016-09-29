def add(numbers):
    """Add variable amount of numbers

    Add content of list numbers to get an integer output"""

    return reduce(lambda x, y: x + y, numbers)

def subtract(numbers):
    """Find the difference between variable amount of numbers

    Subtract contents of list numbers to get an integer output"""

    return reduce(lambda x, y: x - y, numbers)

def multiply(numbers):
    """Find the product of variable amount of numbers
    Multiply contents of list numbers to get an integer output
    """
    return reduce(lambda x, y: x * y, numbers)

def divide(numbers):
    """Find the quotient of variable amount of numbers
    Divide initial list item by all following list contents to get a float
    """
    return reduce(lambda x, y: x / y, numbers)

def square(numbers):
    """ Square a number.
    Square num1 to get an integer output
    """
    return numbers[0] ** 2

def cube(numbers):
    """ Cube a number
    Cube num1 to get an integer output
    """
    return numbers[0] ** 3

def power(numbers):
    """Find the nth power of a number
    Raise num1 to the power of num2 to get an integer output
    """
    return reduce(lambda x, y: x ** y, numbers)

def mod(numbers):
    """Find the remainder after the division of two numbers
    Returns the remainder integer after dividing num1 by num2
    """
    return reduce(lambda x, y: x % y, numbers)
