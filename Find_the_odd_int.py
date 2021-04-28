# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

#EXAMPLE:
# [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5] return 5
# [1,1,2,-2,5,2,4,4,-1,-2,5] returns -1



def find_it(seq):
    my_dict = {}
    for num in seq:
        if num not in my_dict:
            my_dict[num] = 0
        my_dict[num] += 1
    for key in my_dict.keys():
        if my_dict[key] % 2 != 0:
            return key