# Day 4: Find Maximum and Minimum in an Array
# DSA using Python for Data Analyst Role

def find_max_min(arr):
    if len(arr) == 0:
        return None, None

    maximum = arr[0]
    minimum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


data = [45, 12, 78, 34, 89, 23, 5, 67]

max_value, min_value = find_max_min(data)

print("Maximum Value:", max_value)
print("Minimum Value:", min_value)