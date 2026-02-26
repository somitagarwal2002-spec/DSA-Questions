s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

# Method 1: Most Basic/Brute Solution

for i in range(0, len(q)):
    count = 0
    for j in range(0, len(s)):
        if s[j] == q[i]:
            count += 1
    print(f"{q[i]}: {count}")

# Time Complexity = O(N*M)
# Space Complexity = O(1)

# Method 2: By Using ASCII Code

hash_list = [0]*26

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

# print(hash_list)

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(f"{ch}: {hash_list[index]}")

# Time Complexity = O(N+M)
# Space Complexity = O(26+1+1) or O(1)


# Method 3: Using a Dictionary

dictionary = {}

for ch in s:
    if ch in dictionary:
        dictionary[ch] += 1
    else:
        dictionary[ch] = 1

# print(dictionary)

for ch in q:
    if ch in dictionary:
        print(f"{ch}: {dictionary[ch]}")

    else:
        print(f"{ch}: 0")
        