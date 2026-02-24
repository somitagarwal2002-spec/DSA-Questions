# Palindrome String

string = input("Enter any word: ").strip()

new_string = string
result = ""

for i in range(len(new_string) - 1, -1, -1):
    result = result + new_string[i]

# print(result)

if result == new_string:
    print("Palindrome String")
else:
    print("Not a Palindrome String")
