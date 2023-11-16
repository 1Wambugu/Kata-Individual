def find_unsorted_subarray(arr):
    n = len(arr)

    # Check if the array is already sorted
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)) or all(arr[i] >= arr[i + 1] for i in range(n - 1)):
        return [0, 0]

    # Find the left bound of the unsorted subarray
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    # Find the right bound of the unsorted subarray
    right = n - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    # Find the minimum and maximum values within the unsorted subarray
    min_val = min(arr[left:right + 1])
    max_val = max(arr[left:right + 1])

    # Expand the left bound to include an element smaller than the minimum value
    while left > 0 and arr[left - 1] > min_val:
        left -= 1

    # Expand the right bound to include an elements larger than the maximum value
    while right < n - 1 and arr[right + 1] < max_val:
        right += 1

    return [left, right]

# Assuming this is the array
arr = [6, 7, 8, 5, 4, 3]
result = find_unsorted_subarray(arr)
print(result)
