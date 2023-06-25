# CS115 - HW 2

from functools import reduce
from cs115 import *

# Problem 1
def addOne(L):
    '''This Python function accepts a list of integers and outputs '1+ each integer'.'''
    if L == []:
        return []
    else:
        x = [y + 1 for y in L]
        return x

# Problem 2
def explode(s):
    '''This Python function accepts a string and transforms it into a list seperated by each character'''
    return list(s)

# For Problem 3
def even(n):
    '''This Python function accepts an integer and outputs even/odd'''
    if n%2 == 0:
        return True
    else:
        return False

# For Problem 3
def odd(n):
    '''This Python function accepts an integer and outputs even/odd'''
    if n%2 == 0:
        return False
    else:
        return True

# Problem 3   
def myFilter(func, L):
    '''This Python function calls on the even/odd functions and accepts two inputs then outputs a list dependent on func''' 
    if L == []:
        return []
    elif func(L[0]) == True:
        return [L[0]] + myFilter(func, L[1:])
    else:
        return myFilter(func, L[1:])

# For Problem 4
def Positive(x):
    '''This Python function accepts an integer and outputs positive/negative'''
    if x > 0:
        return True
    else:
        return False

# Problem 4
def SumPos(L):
    '''This Python function accepts a list and sums the positive values'''
    if L == []:
        return 0
    elif L[0] > 0:
        return L[0] + SumPos(L[1:])
    else:
        return SumPos(L[1:])
