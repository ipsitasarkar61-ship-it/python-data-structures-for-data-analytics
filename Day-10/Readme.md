# Split Array into Equal Sum Parts (Python)

## 📌 Problem Statement
Given an array of integers, determine whether it can be split into **two contiguous parts** such that the **sum of both parts is equal**.

---

## 🧠 Approach
1. Calculate the **total sum** of the array.
2. If the total sum is **odd**, it is impossible to split into two equal parts.
3. Traverse the array while maintaining a **prefix sum**.
4. If at any index:
   
   prefix_sum == total_sum - prefix_sum

   then the array can be split at that index.

---

## ⏱️ Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## 🧪 Example

### Input:
```python
arr = [1, 2, 3, 3]

Output:-True

Explanation:
Left part: [1, 2, 3] → sum = 6
Right part: [3] → sum = 6