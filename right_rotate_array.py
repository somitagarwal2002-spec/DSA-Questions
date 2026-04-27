nums = [5, -2, 3, 9, 0, 6, 10, 7]

# Using my own Brain
# i = 0
# j = 1
# for j in range(0, len(nums)):
#     nums[i], nums[j] = nums[j], nums[i]
# print(nums)

# Time Complexity = O(N)
# Space Complexity = O(1)
    



# Using Slicing Method
# n = len(nums)
# nums[:] = [nums[-1]] + nums[0:n-1]
# print(nums)

# Time Complexity = O(N)
# Space Complexity = O(1)




# Using For loops another method
n = len(nums)
temp = nums[-1]
for i in range(n-2, -1, -1):
    nums[i+1] = nums[i]

nums[0] = temp
print(nums)
