#!/usr/bin/env python3

'''
A short guessing game that uses custom built exceptions as classes
to correct a users guesses until they find the specific number value.
Borrowed/adapted from https://www.programiz.com/python-programming/online-compiler/?ref=8329c0ac
'''

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

# you need to guess this number
number = 10

# user guesses a number until they gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!\n")
    except ValueTooLargeError:
        print("This value is too large, try again!\n")

print("Congratulations! You guessed it correctly.")
