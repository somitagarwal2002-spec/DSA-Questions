# Palindrome String

# Using For Loop
string = input("Enter any word: ").strip()

new_string = string
result = ""

for i in range(len(new_string) - 1, -1, -1):
    result = result + new_string[i]

if result == new_string:
    print("Palindrome String")
else:
    print("Not a Palindrome String")





# Using Recursion

def check(a, b, result):
    if b < a:
        return result
    result = result + string[b]
    return check(a, b-1, result)

first = 0
last = len(string) - 1
result = ""
og = check(first, last, result)

if og == string:
    print("Palindrome String")
else:
    print("Not a Palindrome String")




# Using 2 pointer
string = input("Enter any word: ").strip()

l = 0
r = len(string) - 1

def check(a, b):
    if a >= b:
        return "Palindrome String"
    elif string[a] == string[b]:
        return check(a+1, b-1)
    elif string[a] != string[b]:
        return "Not a Palindrome String"

result = check(l, r) 
print(result) 
