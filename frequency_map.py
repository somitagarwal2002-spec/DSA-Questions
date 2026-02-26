# Method 1:

num = [1,2,3,4,5,6,7,8,9,7,5,3,2,5,7,4,3,2,2,3]

dictionary = {} #or dictionary = dict()
# print(type(dictionary))

for i in range(0, len(num)):
    # print(i)
    if num[i] in dictionary:
        dictionary[num[i]] += 1
    else:
        dictionary[num[i]] = 1

print(dictionary)

# Method 2: Optimal Solution 

dictionary = {}

for i in range(0, len(num)):
    dictionary[num[i]] = dictionary.get(num[i], 0) + 1

print(dictionary)

