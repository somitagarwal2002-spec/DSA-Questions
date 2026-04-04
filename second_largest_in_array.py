nums = [55, 32, 97, -55, 45, 32, 88, 21]

# Brute Solution (Worst Solution)
arr = nums
largest = arr[0]
for i in range(0, len(arr)):
    if arr[i] > largest:
        largest = arr[i]
    
# arr.remove(largest)
print(arr)

second_largest = arr[0]
for i in range(0, len(arr)):
    if arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print(second_largest)

# Time Complexity = O(N+N) = O(2N) ~ O(N)
# Space Complexity = O(1)




# Optimal Solution

largest = nums[0]
second_largest = largest

for i in range(0, len(nums)):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]

print(second_largest)

# Time Complexity = O(N)
# Space Complexity = O(1)
