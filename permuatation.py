import itertools
from itertools import combinations

def longestWord(letters):
    perms = []
    perm =[]
    count = len(letters)
    for i in range(0, count):
        perms += itertools.combinations(letters, count)
        perm = ["".join(line) for line in perms]
        count -=1
    return perm

print(longestWord("education"))

# def longestWord(letters):
#     perms = []
#     perm =[]
#     count = len(letters)
#     for i in range(0, count):
#         perms += itertools.permutations(letters, count)
#         perm = ["".join(line) for line in perms]
#         count -=1
#     return perm


# jsut as useless as my CountdownAlgo.py()repeating for loop for this algorithm
#http://stackoverflow.com/questions/28136435/python-munging-data-with-join-typeerror-sequence-item-0-expected-string

# instead of permuatations which will feed me every permutation in every iteration
# i can used combinations which will feed me the eight possible arragements which
# i can then feed into the word map to query it.

# nCr  =  	n!
#       -----------
#      	r!(n - r)!


# 9C9 = 1           1
# 9C8 = 9           10
# 9C7 = 36          46
# 9C6 = 84          130
# 9C5 = 126         256
# 9C4 = 126         382
# 9C3 = 84          466
# 9C2 = 36          502
# 9C1 = 9           511
