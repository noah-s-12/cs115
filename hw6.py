'''
Created on  13 April 2023
CS115 - HW 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
# You may write helpers if you see fit. Remember: do not
# import anything, and do not use loops.

# HELPER FUNCTION
def isOdd(n):
    return n % 2 == 1

# HELPER FUNCTION
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '1':
        return 2 * binaryToNum(s[:-1]) + 1
    else:
        return 2 * binaryToNum(s[:-1]) + int(s[-1])


# HELPER FUNCTION
def numToBinary(n, size = COMPRESSED_BLOCK_SIZE):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return '0' * size
    elif isOdd(n) == True:
        return numToBinary(int(n // 2), size - 1) + "1"
    else:
        return numToBinary(n//2, size - 1) + "0"


def compress(S):
    '''compresses a 64-bit binary image (represented as 1's
    and 0's) using a run-length encoding'''
    def compressAlt(S, accumulator, current):
        if S == '':
            if accumulator != 0:
                binaryNumber = numToBinary(accumulator)
                return binaryNumber
            else:
                return ""
        if accumulator == MAX_RUN_LENGTH or current != S[0]:
            binaryNumber = numToBinary(accumulator)
            if current == "1":
                current = "0"
            else:
                current = "1"
            return binaryNumber + compressAlt(S, 0, current)
        return compressAlt(S[1:], accumulator + 1, current)
    return compressAlt(S, 0, "0")
            

def uncompress(C):
    '''uncompresses a run-length encoding to its original
    64-bit binary image'''
    def uncompressAlt(C, current):
        """x"""
        if C == "":
            return ""
        number = (binaryToNum(C[0:COMPRESSED_BLOCK_SIZE]))
        if current == "0":
            return (current * number) + uncompressAlt(C[COMPRESSED_BLOCK_SIZE:], "1")
        else:
            return (current * number) + uncompressAlt(C[COMPRESSED_BLOCK_SIZE:], "0")
    return uncompressAlt(C, "0")

