arr = [55, 32, -97, 99, 3, 67]

largest = arr[0]
for i in range(0, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)

# Time Complexity = O(N)
# Space Complexity = O(1)
