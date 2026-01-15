---

##  `move_zeros_to_end.py`

```python
def move_zeros_to_end(arr):
    """
    Moves all zeros in the array to the end
    while maintaining the order of non-zero elements.

    Parameters:
    arr (list): List of integers

    Returns:
    None (modifies the list in-place)
    """

    non_zero_index = 0

    # Move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1

    # Fill remaining positions with zero
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0


# Example usage
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeros_to_end(nums)
    print("Array after moving zeros:", nums)