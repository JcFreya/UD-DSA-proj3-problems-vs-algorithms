# Problem 1: Square Root of an Integer

## Reason
To find the square root of the integer, use binary search to get the target. With the search range from 1 to input number, in each iteration, we only compare the square value of middle number to the input number. Then do the same process for the rest half of data based on the result of comparison. Therefore, we reduce half of the search range in each iteration.

## Efficiency

- Time complexity
  O(log(n)), here split the data to half and only compare the square of middle value to the input number, which is the same as binary search.

- Space complexity
  O(1), regardless of what operation is used, it takes the constant amount of memory to store the variable.
