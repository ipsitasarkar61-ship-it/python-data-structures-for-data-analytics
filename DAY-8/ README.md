# Day 8 – DSA Problem

## Problem: Reverse an Array

### Problem Statement
Given an array of integers, write a Python function to **reverse the array**.

**Example:**Input: [1, 2, 3, 4, 5] Output: [5, 4, 3, 2, 1]
### Approach
- Use Python slicing: `arr[::-1]`
- Or loop from end to start and append elements to a new array

**Time Complexity:** O(n)  
**Space Complexity:** O(n) for new array (or O(1) if reversed in-place)

### Python Code
```python
def reverse_array(arr):
    return arr[::-1]

# Sample Test
arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)
print("Reversed Array:", reverse_array(arr))