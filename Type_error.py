
from math import  sqrt

def sqrt_of_sum(first_number, second_number):
    """
    >>> first_number = 2
    >>> second_number = 2
    >>> sqrt_of_sum(first_number, second_number)
    2.0
    """
    return sqrt(first_number + second_number)

try:
    number_1 = int(input("Enter first number: \n"))
    number_2 = int(input("Enter second number: \n"))
except TypeError:
    print("TypeError occured try again")
except EOFError:
    print("OOPS! EOFError occurred")
except ValueError:
    print("OOPS! ValueError occurred please try again")
else:
    print(sqrt_of_sum(number_1, number_2))






