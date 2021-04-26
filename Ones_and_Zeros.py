# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
# However, the arrays can have varying lengths, not just limited to 4.

def binary_array_to_number(arr):
    number = 0
    for i in range(len(arr)):
        number += (2**(len(arr)-i-1))*arr[i]
    return number