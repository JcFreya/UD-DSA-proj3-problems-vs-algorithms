'''
# Problem 3: Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum.Return these two numbers.
You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1.
Any sorting function that Python provides is not allowed and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]
The expected answer would be [531, 42]. Another expected answer can be [542, 31].
In scenarios such as these when there are more than one possible answers, return any one.

reference:
https://classroom.udacity.com/nanodegrees/nd256/parts/c5673d01-cc48-4210-ab05-18d50a57b555/modules/7e089424
-dc28-4587-88ec-6bf97b0e89f2/lessons/1d6b1d42-3f6f-4151-96d1-a32ce3dd81f7/concepts/ab330d3d-e567-4b82-baeb-
6454fe283c4d

'''

def heapify(arr, n, i):

    # set the current index as largest
    largest_idx = i
    left = 2*i + 1
    right = 2*i + 2

    # compare with left child
    if left < n and arr[largest_idx] < arr[left]:
        largest_idx = left

    # compare with right child
    if right < n and arr[largest_idx] < arr[right]:
        largest_idx = right

    # when either of left and right is the largest
    if largest_idx != i:
        arr[i], arr[largest_idx] = arr[largest_idx], arr[i]

        heapify(arr, n, largest_idx)

def heapsort(arr):
    # convert array to heap and sort it, swap largest to the end
    n = len(arr)

    # build maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract the elments
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
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

    # sort the input list
    heapsort(input_list)

    # reverse the order
    reversed_list = []
    for i in range(len(input_list)-1, -1, -1):
        reversed_list.append(input_list[i])

    num1, num2 = '', ''

    for i in range(0, len(reversed_list), 2):
        num1 += str(reversed_list[i])

    for i in range(1, len(reversed_list), 2):
        num2 += str(reversed_list[i])

    return [int(num1), int(num2)]


# TEST
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


print('----------Test1----------')
# test sorted input
test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case) # Pass
print('\n')

print('----------Test2----------')
# test unsorted input
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case) # Pass
print('\n')

print('----------Test3----------')
# test none input
rearrange_digits(None)  # Error: Input list couldn't be None
print('\n')

print('----------Test4----------')
# test empty input
rearrange_digits([])    # Error: Input list couldn't be empty
print('\n')
