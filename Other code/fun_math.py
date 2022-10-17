"""This module has three functions:

cal_factorial receives a positive integer and returns its factorial.
list_multiples takes a non-negative integer and a positive length,
and returns a list of multiples.
find_max takes a list of integers and returns the maximum number.

Author: Ting Hu
Date: 2020-10-06
"""

def cal_factorial(x):
    """This function receives a positive integer
    and returns its factorial.
    """
    factorial = x
    
    for i in range(1,x):
        factorial = factorial*(x-i)

    return factorial


def list_multiples(number, length):
    """This function takes a non-negative integer and a positive length,
    and returns a list of multiples.
    """
    new_list = [number]
    
    for i in range(1,length):
        new_list.append(number*(i+1))

    return new_list


def find_max(a_list):
    """This function takes a list of integers
    and returns the maximum number.
    """
    current_max = a_list[0]
    
    for number in a_list[1:]:
        if number > current_max:
            current_max = number

    return current_max


# Testing functions in this module
if __name__ == "__main__":
    # Test cal_factorial
    x = 5
    print("The factorial of",x,"is",cal_factorial(x))

    x = 100
    print("The factorial of",x,"is",cal_factorial(x))

    x = 34
    print("The factorial of",x,"is",cal_factorial(x))

    x = 1
    print("The factorial of",x,"is",cal_factorial(x))

    x = 20
    print("The factorial of",x,"is",cal_factorial(x))

    # Test list_multiples
    number = 5
    length = 3
    print("The list of multiples is",list_multiples(number, length))

    number = 0
    length = 1
    print("The list of multiples is",list_multiples(number, length))

    number = 10
    length = 10
    print("The list of multiples is",list_multiples(number, length))

    number = 8
    length = 1
    print("The list of multiples is",list_multiples(number, length))

    number = 4
    length = 30
    print("The list of multiples is",list_multiples(number, length))

    # Test find_max
    a_list = [2,5,6,8]
    print("The max number of the list is", find_max(a_list))

    a_list = [2,5,-6,-8]
    print("The max number of the list is", find_max(a_list))

    a_list = [-2,5,0,8]
    print("The max number of the list is", find_max(a_list))

    a_list = [2,2,2,2]
    print("The max number of the list is", find_max(a_list))

    a_list = [-5,5,5,-5]
    print("The max number of the list is", find_max(a_list))










    
