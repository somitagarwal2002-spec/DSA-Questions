def merging_two_sorted_arrays(left, right):
    result = []
    n,m = len(left),len(right)
    i,j = 0,  0
    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    return result

def dividing_array(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = dividing_array(left_arr)
    right = dividing_array(right_arr)
    return merging_two_sorted_arrays(left, right)

nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]
final = dividing_array(nums)
print(final)

# Time Complexity = O(NlogN)
# Space Complexity = O(N)
