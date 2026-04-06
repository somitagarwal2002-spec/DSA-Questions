nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
# output: nums = [1, 2, 3, 4, 7, 9, 10, 1, 1, 4, 9, 9]

for i in range(0, len(nums)-2):
    if nums[i] == nums[i+1]:
        print(nums)


