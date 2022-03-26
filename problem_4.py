'''
# Problem 4: Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
Any sorting function that Python provides is not allowed.

Note: O(n) does not necessarily mean single-traversal.
For e.g. if you traverse the array twice, that would still be an O(n) solution
but it will not count as single traversal.

reference: https://classroom.udacity.com/nanodegrees/nd256/parts/c5673d01-cc48-
4210-ab05-18d50a57b555/modules/7e089424-dc28-4587-88ec-6bf97b0e89f2/lessons/1d6
b1d42-3f6f-4151-96d1-a32ce3dd81f7/concepts/12324aa3-a38b-4959-9f81-5851a432b827
'''

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # check None inpout
    if input_list is None:
        print("Error: Input list couldn't be None")
        return None

    if len(input_list) == 0:
        print("Error: Input list couldn't be empty")
        return None

    if len(input_list)==1:
        return input_list

    # set the initial pointers for positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_idx = 0

    while front_idx <= next_pos_2:
        if input_list[front_idx] == 0:
            input_list[front_idx] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_idx += 1
        elif input_list[front_idx] == 2:
            input_list[front_idx] = input_list[next_pos_2]
            input_list[next_pos_2] == 2
            input_list[front_idx] -= 1
        else:
            front_idx += 1
    return input_list

# TEST
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

print('----------Test1----------')
# test normal array
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# Pass
print('\n')

print('----------Test2----------')
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# Pass
print('\n')

print('----------Test3----------')
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Pass
print('\n')

print('----------Test4----------')
# test array with one element
test_function([1])  # [1], Pass
print('\n')

print('----------Test5----------')
# test None input
sort_012(None)  # Error: Input list couldn't be None
print('\n')

print('----------Test6----------')
# test empty array
sort_012([])    # Error: Input list couldn't be empty
print('\n')
