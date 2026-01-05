def find_first_and_last_occurrence(arr, target):
    first_index = -1
    last_index = -1

    for index in range(len(arr)):
        if arr[index] == target:
            if first_index == -1:
                first_index = index
            last_index = index

    return first_index, last_index


# Sample dataset (can represent real-world numeric data)
data = [4, 2, 7, 2, 9, 2, 5]
target_value = 2

first, last = find_first_and_last_occurrence(data, target_value)

print(f"First occurrence of {target_value}: {first}")
print(f"Last occurrence of {target_value}: {last}")