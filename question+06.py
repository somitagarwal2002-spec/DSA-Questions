# Factorial of a Number

num = int(input("Enter any number: "))

n = num
result = 1

for i in range(n, 0, -1):
    result = result * i

print(result)
