# Intersection of Two Arrays (Python)

## Problem Statement
Given two arrays (or lists) of integers, find their **intersection**.  
The intersection contains the elements that are **common to both arrays**.

Each element in the result should be **unique**, and the order of elements does not matter.

---

## Example

Input:arr1 = [1, 2, 2, 1] arr2 = [2, 2]
Output:[2]

---

##  Approach

- Convert both arrays into **sets**
- Use set intersection operation to find common elements
- Convert the result back into a list

This approach ensures:
- No duplicate values
- Optimal time complexity

---

##  Time & Space Complexity

- **Time Complexity:** O(n + m)  
  where `n` and `m` are the sizes of the two arrays

- **Space Complexity:** O(n + m)  
  due to the use of sets

---

## Use Cases

- Data cleaning and preprocessing
- Identifying common users, products, or records
- Feature comparison in analytics pipelines
- Interview problem for Python & DSA fundamentals

---

##  Technologies Used

- Python 3
- Built-in data structures (`set`, `list`)

---

##  How to Run

```bash
python intersection_of_arrays.py