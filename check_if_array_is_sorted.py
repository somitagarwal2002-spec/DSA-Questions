nums = [3, 5, 6, 8, 9, 10]
# nums = [1, 2, 5, 8, 3, 10, 14, 15]
count = 0

for i in range(0, len(nums)-2):
    if nums[i] < nums[i+1]:
        count = 0
    else:
        count += 1
        break

if count != 0:
    print("False")
else:
    print("True")

# Time Complexity = O(N)
# Space Complexity = O(1)
