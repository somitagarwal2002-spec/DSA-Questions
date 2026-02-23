# Palindrome Number

num = int(input("Enter any positive number: "))

n = num
result = 0

while n > 0:
    digit = n % 10
    result = (result * 10) + digit
    n = n // 10

# print(result)

if result == num:
    print("Palindrome")
else:
    print("Not a Palindrome")

