#Given an array of integers, arr, find out 2 indices m, n(0<=m<=arr.length-1, 0<=n<=arr.length-1, m<=n), so that as long as all elements in the subarray(from index m to n, indices m and n inclusive) are sorted properly, with this sorted subarray relacing original subarray, the whole array is sorted (no matter ascendingly or descendingly).
#The subarray should include the least number of elements, means (n-m) must be of the smallest value, and n should also be the smallest one.
#The function accept an array of integers, arr, reutrn the subarray's start and end index in array format, [m,n] as a result.
#For example, in an array [1,2,3,6,4,4], the SMALLEST(with the least numbers of integers) subarray to be found is [6,4,4], if we sort it to [4,4,6], then replace the original subarray, the whole array now turns to be[1,2,3,4,4,6], which is sorted completely. This subarray begins from index 3, and ends in index 5, so the result is [3,5].
#If all elements in the array are the same, return array [0,0]. If all elements in the array are already sorted, no matter ascendingly or descendingly, return [0,0] as well.

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
