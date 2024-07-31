# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    new_array = []
    for number in source_array:
        if number % 2 != 0:
            new_array.append(number)
    
    new_array.sort()

    odd_index = 0
    result_array = source_array[:]

    for i in range(len(result_array)):
        if result_array[i] % 2 != 0:
            result_array[i] = new_array[odd_index]
            odd_index += 1
    return result_array

print(sort_array([5, 3, 2, 8, 1, 4]))
