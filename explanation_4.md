# Problem 4: Dutch National Flag Problem

## Reason
The idea here is to put 0 and 2 into the correct position so that the 1s will be in order automatically, which can also insure the single traversal. Use 1 as the pivot and swap the value based on pivot. For value 2, swap with the last 2, and for 0, swap with the last 0 and if it's 1, do nothing and move 1 pointer a step forward.

## Efficiency

- Time complexity
  O(n), the sorting complete in single traversal which takes O(n)

- Space complexity
  O(n), only has in place comparison and swap which takes O(n) space complexity)
