# Problem 3: Rearrange Array Elements

## Reason
In order to make the expected time complexity is O(nlog(n)), here utilize the heapsort that treats an array like a binary tree and moves the largest values to the end of the heap until the full array is sorted. Therefore, we can heapsort the array and pop the elements one by one to the two numbers, which will make sure the largest digit starts the number.

## Efficiency

- Time complexity
  O(log(n)), the time complexity is the same as Heapsort which divide the array in half every time when the pivot move down to the middle.

- Space complexity
  O(log(n)), Heapsort is an in-place sorting which takes constant space complexity O(1). However, in order to generate the two numbers for output, we need to traverse the sorted array again which takes the final space complexity O(n)
