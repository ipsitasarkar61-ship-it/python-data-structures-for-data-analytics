---

##  `intersection_of_arrays.py`

```python
def intersection_of_arrays(arr1, arr2):
    """
    Returns the intersection of two arrays.
    The result contains unique elements common to both arrays.

    Parameters:
    arr1 (list): First list of integers
    arr2 (list): Second list of integers

    Returns:
    list: A list containing common unique elements
    """

    set1 = set(arr1)
    set2 = set(arr2)

    intersection = set1.intersection(set2)

    return list(intersection)


# Example usage
if __name__ == "__main__":
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]

    result = intersection_of_arrays(arr1, arr2)
    print("Intersection of the two arrays:", result)