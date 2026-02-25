# All Factors of a given number

num = int(input("Enter any positive number: "))

n = num
factors = []

for i in range(1, n+1):
    if n % i == 0:
        factors.append(i)
        
print(factors)


# More Effective Solution

num = int(input("Enter any positive number: "))

n = num
factors = []

for i in range(1, (n//2)+1):
    if n % i == 0:
        factors.append(i)
        
factors.append(n)
print(factors)

# Most Optimal Solution

from math import sqrt

num = int(input("Enter any positive number: "))

n = num
factors = []

for i in range(1, int(sqrt(n))+1):
    if n % i == 0:
        factors.append(i)
        if (n // i) != i:
            factors.append(num//i)

factors.sort()
print(factors)
