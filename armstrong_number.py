# Armstrong Number

num = int(input("Enter any positive number: "))

n = num
result = 0

while(n > 0):
    digit = n % 10
    result = result + (digit**3)
    n = n // 10

print(result)

if result == num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
