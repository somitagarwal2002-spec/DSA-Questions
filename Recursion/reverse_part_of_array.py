array = [5,7,3,2,6,1,5,9]
l = 0
r = len(array) - 1

# Full Array

def reverseArr(left, right):
    if left >= right:
        return
    array[left], array[right] = array[right], array[left]
    return reverseArr(left+1, right-1)

reverseArr(l, r)
print(array)

# hume beech mein jo digits hai 3,2,6,1 hai bss use reverse krna hai baki same rhega
# from index 2 to 5 (included)

reverseArr(2,5)
print(array)


# Time Complexity = O(N/2) ~ O(N)
# Space Complexity = O(N/2) ~ O(N)
