def next_permutation(nums):
    n = len(nums)
    i = n - 2

    # Step 1: Find the first decreasing element from right
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: Find element just larger than nums[i]
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the elements after index i
    nums[i + 1:] = reversed(nums[i + 1:])


# Driver Code
arr = [1, 2, 3]
next_permutation(arr)
print(arr)