# Move All Zeros to the End (Python)

##  Problem Statement
Given an array of integers, move all the zeros to the **end of the array** while maintaining the **relative order of the non-zero elements**.

This operation must be performed **in-place**, without creating a new array for the result.

---

##  Example

Input:[0, 1, 0, 3, 12]
Output:[1, 3, 12, 0, 0]

---

##  Approach (Two Pointer Technique)

- Maintain a pointer `non_zero_index` to track the position of the next non-zero element
- Traverse the array
- Whenever a non-zero element is found, place it at `non_zero_index`
- After traversal, fill the remaining positions with zeros

This ensures:
- Order of non-zero elements is preserved
- No extra space is used

---

##  Time & Space Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) (in-place)

---

##  Real-World Use Cases

- Data cleaning and preprocessing
- Handling missing or null values
- Feature engineering pipelines
- Interview problem for array manipulation

---

##  How to Run

```bash
python move_zeros_to_end.py