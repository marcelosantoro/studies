# Binary search

Binary search is an efficient search algorithm for sorted lists. The basic idea of binary search is to halve the search range on each iteration by comparing the target value with the value in the middle of the range and adjusting the search range accordingly.

## How it works

- The binary_search function follows this basic idea in a while loop:
  Initially, we set left to the first index of the list (0) and right to the last index of the list (len(list) - 1).
- As long as left is less than or equal to right, we keep looking. This ensures that the fetch range is not empty.
- We find the middle index of the search range, which is calculated by arithmetic mean of left and right. We use integer division with // to ensure the result is an integer.
- We compare the value at the middle index with the target value. If the value at the middle index equals the target value, we return the middle index, indicating that we found the target value in the list.
- If the value at the middle index is less than the target value, we know that the target value must be in the right half of the search range. So we adjust the fetch range to half right by setting left to half + 1.
- If the value at the middle index is greater than the target value, we know that the target value must be in the left half of the search range. So we adjust the fetch range to half left, setting right to half - 1.
- If we get to the end of the loop and we don't find the target value, we return None to indicate that the target value is not in the list.
