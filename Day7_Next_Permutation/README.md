# 📌 Day 7 – DSA Journey

## 🔁 Problem: Next Permutation

### 🧠 Problem Statement
Given an array of integers, rearrange it into the **next lexicographically greater permutation**.
If such arrangement is not possible, rearrange it as the **lowest possible order** (sorted in ascending order).

### 🏢 Interview Relevance
This problem is frequently asked in interviews at:
- Uber
- Goldman Sachs
- Adobe

### 🧠 Approach (In-Place Algorithm)
1. Traverse from the right to find the **first decreasing element**.
2. Find the element just larger than it on the right side.
3. Swap both elements.
4. Reverse the remaining array after the swapped index.

### ⏱ Time Complexity
- O(n)

### 🧮 Space Complexity
- O(1) (In-place modification)

### 📌 Key Learnings
- Understanding lexicographical order
- In-place array manipulation
- Strong problem-solving logic
- Popular interview question

### 💻 Language Used
- Python

---

🚀 *Day 7 completed with a high-quality interview problem.*