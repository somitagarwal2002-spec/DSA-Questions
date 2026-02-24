# All Factors of a given number

num = int(input("Enter any positive number: "))

n = num
factors = []

for i in range(1, n):
    if n % i == 0:
        factors.append(i)
        
print(factors)
