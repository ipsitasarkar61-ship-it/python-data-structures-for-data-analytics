# Find First Non-Repeating Character in a String (Python)

## 🧠 Problem Statement
Given a string, find the **first character that does not repeat** anywhere in the string.  
If no such character exists, return `None`.

---

## 📥 Input
A string `s`

---

## 📤 Output
The first non-repeating character in the string, or `None` if all characters repeat.

---

## 🧪 Example

### Example 1
Input:s = "analytics"
Output:a
### Example 2
Input:s="aabbcc"
Output:None

---

## 🛠️ Approach
1. Use a **dictionary (hash map)** to count the frequency of each character.
2. Traverse the string again to find the **first character with frequency = 1**.
3. This ensures **O(n)** time complexity.

---

## ⏱️ Complexity Analysis
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

## 🧩 Use Case (Data Analytics Perspective)
- Text preprocessing
- Feature extraction
- Data cleaning
- NLP pipelines

---
