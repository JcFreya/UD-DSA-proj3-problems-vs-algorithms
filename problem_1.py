'''
# Problem 1: Square Root of an Integer
Find the square root of the integer without using any Python library.
Find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196
whose floor value is 5.

The expected time complexity is O(log(n))
'''

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # check None input
    if number is None:
        print("Error: Input number couldn't be None\n")
        return None

    # check NaN invalid input
    if type(number) != int:
        print("Error: Input is not a valid number\n")
        return None

    # check invalid input
    if number < 0:
        print("Error: Input number must be greater than 0\n")
        return None

    left = 1
    right = number

    # start from the middle, and search the rest half for each iteration
    while left <= right:
        mid = (left + right)//2
        mid_square = mid ** 2

        # compare the square of middle value to input number
        if mid_square > number:
            right = mid - 1
        elif mid_square < number:
            left = mid + 1
        else:
            return mid

    # if no match, use floor
    return right


print('----------Test1----------')
print(sqrt(9)) # 3, Pass
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print('\n')

print('----------Test2----------')
print(sqrt(0)) # 0, Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print('\n')

print('----------Test3----------')
# test invalid negative input
print ("Pass" if  (None == sqrt(-27)) else "Fail")
# Error: Input number must be greater than 0, Pass
print('\n')

print('----------Test4----------')
# test None input
print ("Pass" if  (None == sqrt(None)) else "Fail")
# Error: Input number couldn't be None, Pass
print('\n')

print('----------Test5----------')
# check NaN input
print ("Pass" if  (None == sqrt('number')) else "Fail")
# Error: Input is not a valid number, Pass
print('\n')

print('----------Test6----------')
# test float number
print ("Pass" if  (None == sqrt(10.2)) else "Fail")
# Error: Input is not a valid number, Pass
print('\n')

print('----------Test7----------')
print(sqrt(27)) #5, Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print('\n')
