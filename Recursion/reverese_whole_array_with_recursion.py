array = [1,2,3,4,5,6,7,8,9]

# Simplest Method
# Method 1:
print(array[::-1])

# Method 2:
print(array.reverse()) # This will give None output 
#                 Correct Way
array.reverse()
print(array)




# Using for loop without recursion

new_array = []
for i in range(len(array)-1, -1, -1):
    new_array.append(array[i])

print(new_array)




# Using Recursion

def reveresing(n):
    if n < 0:
        return
    return new_array.append(array[n]), reveresing(n-1)

new_array = []
length = len(array)
reveresing(length - 1)

print(new_array)




# Using Pointers
l = 0
r = len(array) - 1

def reverseArr(left, right):
    if left >= right:
        return
    array[left], array[right] = array[right], array[left]
    return reverseArr(left+1, right-1)

reverseArr(l, r)
print(array)

