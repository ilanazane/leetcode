# 394. Decode String 

# not submmmitted, used chat, need to revist 

import numpy as np 

input = "3[a]2[bc]"
# output =  "aaabcbc"

# input = "3[a2[c]]"
# output = "accaccacc"

# input = "2[abc]3[cd]ef"
# output = "abcabccdcdcdef"

stack = []                 # Stack to hold numbers and strings
currentString = ""         # Current decoded string
currentNumber = 0          # Multiplier for the current substring

for char in input:
    if char.isdigit():     # If it's a number, build the multiplier
        currentNumber = currentNumber * 10 + int(char)
    elif char == '[':      # Start of a new encoded substring
        # Push current state onto the stack
        stack.append(currentString)
        stack.append(currentNumber)

        print(stack,currentString)
        # Reset for the new substring
        currentString = ""
        currentNumber = 0
    elif char == ']':      # End of an encoded substring
        # Pop the multiplier and previous string state
        print('close')
        multiplier = stack.pop()
        previousString = stack.pop()
        print('previous',previousString)
        # Decode and append to the previous string
        currentString = previousString + currentString * multiplier
    else:                  # Regular characters
        currentString += char

print(currentString)

