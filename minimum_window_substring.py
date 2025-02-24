# 76 
# NOT FINISHED 
import numpy as np 
from collections import Counter


s = "ADOBECODEBANC"
t = "ABC"

left = 0 
right = 0 


t_count = Counter(t)
window_count = {}
print(t_count)

formed = 0 

while right < len(s):
    current_char = s[right]
    print('current char',current_char)
    # capture all unique characters as we increase window size 
    window_count[current_char] = window_count.get(current_char,0)+1
    print('window count',window_count)

    if current_char in t_count and window_count[current_char] == t_count[current_char]:
        print('in here')
        print(current_char, t_count,window_count[current_char],t_count[current_char])
        formed += 1 
        print('formed',formed)

    right +=1



    

