'''
# Problem 2: Search in a Rotated Sorted Array

Given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

Search the target value. If found in the array return its index, otherwise return -1.

Assumption: there are no duplicates in the array and the algorithm's runtime
complexity must be in the order of O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

'''

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # check if None in Input
    if input_list is None:
       print("Error: Input list couldn't be None\n")
       return -1

    # check non-list input_list
    if not isinstance(input_list, list):
        print("Error: Input is not a list\n")
        return -1

    # check empty List
    if len(input_list)==0:
        print("Error: Input list is empty\n")
        return -1

    end = len(input_list) - 1
    pivot = find_pivot(input_list, 0, end)

    if pivot == -1 or pivot==end:
        return binary_search(input_list, 0, end, number)
    if input_list[pivot] == number:
        return pivot
    if input_list[pivot] > number >= input_list[end]:
        return binary_search(input_list, 0, pivot - 1, number)
    return binary_search(input_list, pivot + 1, end, number)

# locate the pivot point where the list rotate
def find_pivot(list, left, right):
    if left == right:
        return left

    mid = (left + right)//2

    left_value = list[left]
    mid_value = list[mid]

    # check if it's in order
    if mid_value > list[mid+1]:
        return mid
    if mid_value < list[mid-1]:
        return mid-1

    if left_value > mid_value:
        return find_pivot(list, left, mid)

    return find_pivot(list, mid+1, right)


# binary search
def binary_search(list, left, right, target):
    mid = (left + right)//2
    mid_value = list[mid]

    if mid_value == target:
        return mid
    elif left > right:
        return -1
    elif mid_value > target:
        return binary_search(list, left, mid - 1, target)
    return binary_search(list, mid + 1, right, target)


# functions for TEST
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# TEST
print('----------Test1----------')
# test array without rotated values
test_function([[1, 2, 3, 4], 2])   # Pass
print('\n')

print('----------Test2----------')
# test array with rotated values
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])   # Pass
print('\n')

print('----------Test3----------')
# test array with rotated values without input number
test_function([[6, 7, 8, 1, 2, 3, 4], 8])   # Pass
print('\n')

print('----------Test4----------')
# test None input_list
rotated_array_search(None, 1)   # Error: Input list couldn't be None
print('\n')

print('----------Test5----------')
# test empty input_list
rotated_array_search([], 1) # Error: Input list is empty
print('\n')

print('----------Test6----------')
# test non list input_list
rotated_array_search('6, 7, 8,', 1) # Error: Input is not a list
print('\n')
