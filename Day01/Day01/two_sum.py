# Day 01 - Two Sum (Python DSA)
# Optimized solution using HashMap (Dictionary)

def two_sum(nums, target):
    visited = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in visited:
            return [visited[complement], index]

        visited[value] = index

    return []

# Example
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))