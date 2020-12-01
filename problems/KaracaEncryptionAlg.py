#!/usr/bin/python3

# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# 
#    a => 0
#    e => 1
#    i => 2
#    o => 2
#    u => 3
# 
# Output: "1lpp0"
#
# https://edabit.com/challenge/JzBLDzrcGCzDjkk5n

def garble(s):
    """
    Replace the following chars in a string.
        a => 0
        e => 1
        i => 2
        o => 2
        u => 3
    """

    s = s[::-1]
    s = s.replace('a', '0')
    s = s.replace('e', '1')
    s = s.replace('i', '2')
    s = s.replace('o', '2')
    s = s.replace('u', '3')

    return s + 'aca'

def _print_help(name):
    s = """
        Usage: %s [OPTION] WORD

        Encrypts an input word. The word must be all lowercase.

        -h          print this message.
        """ % name
    print(s)
    exit(0)

if __name__ == '__main__':
    
    import sys
    
    word = ''
    
    for arg in sys.argv[1:]:
        if arg == '-h':
            _print_help(sys.argv[0])
        if arg.islower():
            word = arg
        else:
            _print_help(sys.argv[0])

    print(word)
    print(garble(word))
            
