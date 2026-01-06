# Day 6 – DSA Practice (Binary Search)

## 📌 Problem Statement
Implement the Binary Search algorithm to efficiently find a target element in a sorted array.

Binary Search works by repeatedly dividing the search space in half, making it much faster than linear search for sorted data.

---

## 🧠 Approach
1. Start with two pointers: `low` and `high`.
2. Find the middle index.
3. Compare the middle element with the target:
   - If equal → target found.
   - If target is smaller → search the left half.
   - If target is larger → search the right half.
4. Repeat until the element is found or the search space becomes empty.

---

## ⏱ Time & Space Complexity
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

---

## 💡 Why This Matters
Binary Search builds strong logical thinking and optimization skills, which are essential for:
- Efficient data processing
- Writing optimized analytics workflows
- Handling large datasets

---

## 🧪 Example
**Input:**  
Array = [2, 4, 6, 8, 10, 12]  
Target = 8  

**Output:**  
Index = 3

---

## 🚀 Learning Outcome
- Improved understanding of divide-and-conquer strategy
- Strengthened problem-solving fundamentals
- Enhanced analytical thinking for real-world applications

---

### 🔗 Language Used
- Python