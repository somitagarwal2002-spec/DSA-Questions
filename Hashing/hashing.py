""" 
    Hashing :
    Prestoring values into some datastructure like list/dictionary/set and then fetching it
"""

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# Method 1: Most Basic Method

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1
    print(f"{num}: {count}")

# Time Complexity = O(N*M)
# Space Complexity = O(1)


# Method 2: Optimal Solution

hash_list = [0]*11

for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(f"{num}: 0")
    else:
        print(f"{num}: {hash_list[num]}")

# Time Complexity = O(N+M)
# Space Complexity = O(11) or we can say O(1)


# Method 3: Using Dictionary

dictionary = {}

for i in range(0, len(n)):
    if n[i] in dictionary:
        dictionary[n[i]] += 1

    else:
        dictionary[n[i]] = 1

# print(dictionary)

for i in range(0, len(m)):
    if m[i] in dictionary:
        print(f"{m[i]}: {dictionary[m[i]]}")
    else:
         print(f"{m[i]}: 0")

# Time Complexity = O(N+M)
# Space Complexity = O(N)

