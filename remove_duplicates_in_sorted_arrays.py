# Unique items batane hai kitne hai 
nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
# output: nums = [1, 2, 3, 4, 7, 9, 10, 1, 1, 4, 9, 9]

# Brute Solution
freq_map = {}
for i in range(0, len(nums)):
    freq_map[nums[i]] = 0

j = 0
for k in freq_map:
    nums[j] = k
    j += 1

print(nums)
print(j)

# Time Complexity = O(2N) ~ O(N)
# Space Complexity = O(N)

# Optimal Solution

i = 0
j = 0

for k in range(0, len(nums)):
    if len(nums) == 1:
        break
    elif nums[i] == nums[j]:
        j += 1
    elif nums[i] != nums[j]:
        i += 1
        nums[i], nums[j] = nums[j], nums[i]
        j += 1

print(nums)
print("Unique values = ",i+1)

# Time Complexity = O(N)
# Space Complexity = O(1)
