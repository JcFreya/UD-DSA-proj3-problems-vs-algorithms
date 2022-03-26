'''
# Problem 6: Unsorted Integer Array
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

'''

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # check None inpout
    if ints is None:
        print("Error: Input list couldn't be None")
        return None

    if len(ints) == 0:
        print("Error: Input list couldn't be empty")
        return None

    if len(ints)==1:
        return (ints[0], ints[0])

    # set the initial location for min and max pointers
    min = ints[0]
    max = ints[0]

    for element in ints:
        if element < min:
            min = element # update the min
        elif element > max:
            max = element # update the max
    return (min, max)


# TEST
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print('----------Test1----------')
# test normal input
print(get_min_max(l))
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# (0, 9)
# Pass
print('\n')

print('----------Test2----------')
# test normal input
print(get_min_max([3,54,8,2,33,-21,445,7]))
print ("Pass" if ((-21, 445) == get_min_max([3,54,8,2,33,-21,445,7])) else "Fail")
# (-21, 445)
# Pass
print('\n')

print('----------Test3----------')
# test list with one element
print(get_min_max([0]))
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
# (0, 0)
# Pass
print('\n')

print('----------Test4----------')
# test None input
print(get_min_max(None))
# Error: Input list couldn't be None
# None
print('\n')

print('----------Test5----------')
# test empty input
print(get_min_max([]))
# Error: Input list couldn't be empty
# None
print('\n')
