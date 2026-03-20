nums = [5, 7, 8, 4, 1, 6, 9, 2]

# Ek-Ek ko check krte jana hai sabse pehle 0 index wale ko minimum manna hai
# agar usse chota koi mil jaye to use minimum maan lena hai aur jb hum poori array iterate
# kr lete hai to hume apna pehla minimum number mil jayega

# Ascending Order
for i in range(0, len(nums)):
    min_num = nums[i]
    for j in range(i+1, len(nums)):
        if nums[j] < min_num:
            min_num = nums[j]
            nums[j] = nums[i]
            nums[i] = min_num

print(nums)

# Descending Order
for i in range(len(nums)-1, -1, -1):
    max_num = nums[i]
    for j in range(len(nums)-1,-1,-1):
        if nums[j] > max_num:
            max_num = nums[j]
            nums[j] = nums[i]
            nums[i] = max_num

print(nums)


# Time Complexity = O(N(N+1)/2) ~ O(N^2)
# Space Complexity = O(1)
