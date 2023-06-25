# CS115 - HW 3

from cs115 import*


scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]


# Problem 1
def letterScore(letter,scoreList):
    '''This python function return the Scrabble score associated with the
       single lowercase letter input from 'letter'.'''
    L = scoreList[0]
    if letter == '':
        return 0
    else:
        L = scoreList[0]
        if letter == L[0]:
            return L[1]
        else:
            return letterScore(letter, scoreList[1:])

# Problem 2
def wordScore(S,scoreList):
    '''This python function returns the scrabble score associated with the
       lowercase word(s) with no spaces inputted from 'S'.'''
    if S == '':
        return 0
    else:
        return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

