def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

num = int(input("Enter any positive integer: "))
factorial = fact(num)
print(factorial)

# Time Complexity - O(N)
# Space Complexity - O(N)


# Simple Method Without Any Method

num = int(input("Enter any number: "))

n = num
result = 1

for i in range(n, 0, -1):
    result = result * i

print(result)

