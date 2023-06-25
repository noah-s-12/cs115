# CS 115 - HW 1

from functools import reduce

# mult function
def mult(x,y):
    '''This python function will accept two inputs and multiply them by each other.'''
    return x*y


# add function
def add(x,y):
    '''This python function will accept two inputs and returns the sum of these two numbers.'''
    return x+y


# factorial function
def factorial(x):
    '''This python function will accept one input and returns a function that shows the factorial of that number.'''
    return reduce(mult,range(1,x+1))


# mean function
def mean(x):
    '''This python function will accept a list of numbers and returns a function that shows the mean of the list.'''
    return reduce(add,x)/len(x)





