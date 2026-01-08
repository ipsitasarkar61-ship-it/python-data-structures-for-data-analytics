# reverse_array.py
def reverse_array(arr):
    """
    Function to reverse an array
    :param arr: List of elements
    :return: Reversed list
    """
    return arr[::-1]  # simple slicing method

# Sample Test
arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)
print("Reversed Array:", reverse_array(arr))