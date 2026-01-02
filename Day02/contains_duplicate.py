"""
Day 02 - Contains Duplicate
Python DSA for Data Analyst
"""

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Example
nums = [1, 2, 3, 1]
print(contains_duplicate(nums))