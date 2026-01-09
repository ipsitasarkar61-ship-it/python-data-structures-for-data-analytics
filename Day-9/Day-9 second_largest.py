def find_second_largest(arr):
    # Edge case: array must have at least 2 elements
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None

    return second_largest


# Driver code
if __name__ == "__main__":
    arr = [10, 5, 20, 8, 15]
    result = find_second_largest(arr)

    if result is not None:
        print("Second largest element:", result)
    else:
        print("Second largest element does not exist.")