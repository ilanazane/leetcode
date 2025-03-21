"""
Example 1:

Input: n = 3
Output: 3

Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

"""

n = 3
first = "A"
paste = ""
counter = 0
copy = first


if len(first) != n:
    print("too short")

    while len(paste) != n:
        # first copy operation
        copy = first
        paste += copy
        counter += 1

print(paste)
print(counter)
