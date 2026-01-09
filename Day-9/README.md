# Find Second Largest Element in an Array

## 📌 Problem Statement
Given an array of integers, find the **second largest element** in the array.

The second largest element is the element that is **strictly smaller than the largest** and **greater than all other elements**.

---

## 🧠 Approach
- Initialize two variables:
  - `largest`
  - `second_largest`
- Traverse the array once.
- Update the values based on comparison.
- This approach works in **O(n)** time and **O(1)** extra space.

---

##  Example

**Input:**[10, 5, 20, 8, 15]
**Output:**15
---

##  Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Key Notes
- Works even if the array is unsorted.
- Handles negative numbers.
- If the second largest element does not exist, the program returns `None`.

---

##  Use Case (Data Analytics)
- Useful in ranking systems
- Finding top-2 values
- Feature selection & summary statistics

---

##  Author
Ipsita Sarkar