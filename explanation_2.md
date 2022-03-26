# Problem 2: Search in a Rotated Sorted Array

## Reason
In order to make the algorithm's runtime complexity O(log n), here decide to use binary search with recursion.

In each iteration, compare the middle value to input. But the scenarios can be 1) the array was not rotated, then just need to do the basic binary search to get the result. 2) the array was rotated and the middle is greater than both left and right values. 3) the array was rotated and the middle is less than both left and right values. So for the rotated cases, we apply the binary search on either left or right half of arrays


## Efficiency

- Time complexity
  O(log(n)). Finding the pivot is similar to binary search which shrink the array by half in each iteration which takes O(log(n)). Given the pivot point, locate the possible side of array which takes O(1), and then search again on the picked side of array which still takes O(log(n))

- Space complexity
  O(log(n)). For each iteration, takes O(1), since there's log(n) iterations which get the final space complexity to O(log(n))
  
