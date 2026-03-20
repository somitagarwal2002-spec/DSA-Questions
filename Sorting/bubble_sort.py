nums = [5, 8, 1, 6, 9, 2, 4]

# Bubble sort works on Adjacent Swapes (aaju-baju swapes)

# Ascending Order
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            max_num = nums[i]
            nums[i] = nums[j]
            nums[j] = max_num

print(nums)

# Descending Order
for i in range(len(nums) - 1, -1, -1):
    for j in range(i -1, -1, -1):
        if nums[i] > nums[j]:
            max_num = nums[i]
            nums[i] = nums[j]
            nums[j] = max_num

print(nums)




# ************************** OR *********************************************

# Ascending Order
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)

# Descending Order
for i in range(len(nums) - 1, -1, -1):
    for j in range(i -1, -1, -1):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)

# Time Complexity = O(N(N+1)/2) ~ O(N^2)
# Space Complexity = O(1)
