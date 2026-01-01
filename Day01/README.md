# Day 01 – Two Sum (Python DSA)

This is my first problem as part of the **100 Days of Code challenge**, focused on
Python DSA concepts required for **Data Analyst roles**.

## 📌 Problem
Given a list of integers and a target value, find the indices of two numbers such that their sum equals the target.

## 💡 Approach (Using HashMap)
- Created a HashMap (Python dictionary) to store each number and its index while traversing the list.
- For each element, calculated the complement needed to reach the target.
- Checked whether the complement already exists in the HashMap.
- If found, returned the indices of the current element and the stored complement.
- If not found, stored the current element and its index in the HashMap.

This approach avoids nested loops and improves efficiency.

## ⏱ Complexity
- **Time Complexity:** O(n) — single pass through the list
- **Space Complexity:** O(n) — extra space for the HashMap

## 🛠 Language
- Python

## 🎯 Goal
To strengthen problem-solving skills and build a solid foundation in Python DSA required for Data Analytics and Analyst roles.