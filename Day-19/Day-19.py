def is_sorted(arr):
    """
    Check if the given array is sorted in ascending order.
    Returns True if sorted, otherwise False.
    """

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 1, 4, 2]

print("Array 1 is sorted:", is_sorted(arr1))
print("Array 2 is sorted:", is_sorted(arr2))