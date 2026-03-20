nums = [5, 7, 8, 4, 1, 6, 9, 2]

# ek-ek number ko uthate jao usse greater and smaller jiske mid mein wo best rahe waha
# use place krdo
# jo greater honge unhe selected number ke right mein adjust krte jao fir hume humari 
# sorted array mil jayegi

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

print(nums)
        
# Time Complexity = O(N(N+1)/2) ~ O(N^2)
# Space Complexity = O(1)

