#!/usr/bin/python3

# The Atbash cipher is an encryption method in which each letter of a word is
# replaced with its "mirror" letter in the alphabet:
# 
#    A <=> Z; B <=> Y; C <=> X; etc.
# 
# Create a function that takes a string and applies the Atbash cipher to it.
# 
# Examples
# atbash("apple") ➞ "zkkov"
# 
# atbash("Hello world!") ➞ "Svool dliow!"
# 
# atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
# Notes
# Capitalisation should be retained.
# Non-alphabetic characters should not be altered.
#
# https://edabit.com/challenge/MGALfBAXhXqqdFyqo

import string

# Generate dictionaries for 'mirroring'
lower = string.ascii_lowercase
upper = string.ascii_uppercase

MAX = len(lower) - 1

def _inverse(i):
    return MAX - i

def encrypt(s):
    cypher = ''
    for char in s:
        if char in lower:
            pos = _inverse(lower.find(char))
            cypher += lower[pos]
        elif char in upper:
            pos = _inverse(upper.find(char))
            cypher += upper[pos]
        else:
            cypher += char
    return cypher
 

def _print_help():
    s = """
        Usage: AtbashCipher.py [OPTIONS] "STRING"

        -h | --help         Print this message.

        String              Series of words or characters to be
                            encrypted.

        Encrypts words or phrases where each letter is replaced
        with a mirror. Capitalization is retained and non-alphabetic
        characters are not altered.
        """
       
    print(s)
    exit(0)


if __name__ == '__main__':

    import sys
    import time

    cypher = ''
    
    if len(sys.argv) < 2:
        _print_help()

    for arg in sys.argv[1:]:
        if arg == '-h' or arg == '--help':
            _print_help()
        if cypher == '':
            cypher = arg
        else:
            cypher = cypher + ' ' + arg
            pass

    print(cypher)
    print(encrypt(cypher))
