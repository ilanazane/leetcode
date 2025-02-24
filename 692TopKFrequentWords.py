"""
692. Top K Frequent words 
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
"""


def topKFrequentWords(words, k):

    # create dictionary
    word_dict = {}

    # init dictionary so all keys have count value of 0
    for i in range(len(words)):
        word_dict[words[i]] = 0

    for i in range(len(words)):
        # if word is already in dict then increment value
        if words[i] in word_dict:
            word_dict[words[i]] += 1
        # otherwise count the value (i.e. it exists)
        else:
            word_dict[words[i]] = 1
    # sort keys
    sorted_keys = sorted(word_dict, key=word_dict.get, reverse=True)
    # get top k keys
    return sorted_keys[:k]


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4

output = topKFrequentWords(words, k)
print(output)
