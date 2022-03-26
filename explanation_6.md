# Problem 6: Unsorted Integer Array

## Reason
Use two pointers to track the min and max, traverse the array and for each element check if it's the min or max of the list, update the existing min and max based on comparison. In this way, we can get the min and max at the same time in a single traversal.

## Efficiency

- Time complexity
  O(n), since we only traverse the array in a single time, for each comparison takes O(1) time, so the total time complexity will be O(n)

- Space complexity
  O(1), the whole process only use min and max pointers which takes constant space
