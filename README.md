# Function Definition

# To def find_unsorted_subarray(arr)

This defines a function that takes an array arr as its input.

# To Determine the Length of the Array:

n = len(arr)
this calculates the length of the input array and stores it in the variable n.

# To Check if the Array is Already Sorted:

if all(arr[i] <= arr[i + 1] for i in range(n - 1)) or all(arr[i] >= arr[i + 1] for i in range(n - 1)):
    return [0, 0]

This checks whether the array is already sorted in ascending or descending order. If it is, the function returns [0, 0] because no subarray needs to be sorted.

# To Find the Left Bound of the Unsorted Subarray:

left = 0
while left < n - 1 and arr[left] <= arr[left + 1]:
    left += 1
    This function iterates from the left side of the array until it finds an element that is not in ascending order with its next element. The index where this occurs is the left bound of the unsorted subarray.

# To Find the Right Bound of the Unsorted Subarray:

right = n - 1
while right > 0 and arr[right] >= arr[right - 1]:
    right -= 1
     the function iterates from the right side of the array until it finds an element that is not in descending order with its previous element. The index where this occurs is the right bound of the unsorted subarray.

# To Find the Minimum and Maximum Values Within the Unsorted Subarray:

 min_val = min(arr[left:right + 1])
 max_val = max(arr[left:right + 1])

  These lines find the minimum and maximum values within the unsorted subarray.

# We need to Expand the Left Bound:

 while left > 0 and arr[left - 1] > min_val:
    left -= 1
  This loop expands the left bound to include any elements smaller than the minimum value.

# We need to Expand the Right Bound:

 while right < n - 1 and arr[right + 1] < max_val:
    right += 1
 Similarly, this loop expands the right bound to include any elements larger than the maximum value.

# Return the Result:

 return [left, right]
 The function returns the indices [left, right], which represent the smallest unsorted subarray in the input array.