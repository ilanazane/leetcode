# Length of Longest Substring without repeating characters

"""
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
# s = ""


def lengthOfLongestSubstring(s: str) -> int:
    unique = []

    if len(s) == 0:
        return 0

    for i in range(len(s)):
        start = i
        end = len(s)

        while start != end:
            interval = s[start:end]

            end -= 1
            # check if unique
            if len(interval) == len(set(interval)):
                unique.append(interval)

    sorted_str = sorted(unique, key=len, reverse=True)
    return len(sorted_str[0])


print("output:", lengthOfLongestSubstring(s))


# create optimized approach

# char_set = ()
# left = 0
# max_length = 0

# for right in range(len(s)):
#     print(s[right])
