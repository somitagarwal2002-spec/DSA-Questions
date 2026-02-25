# Armstrong Number

num = int(input("Enter any positive number: "))

n = num
result = 0
length = len(str(n))

while(n > 0):
    digit = n % 10
    result = result + (digit**length)
    n = n // 10

print(result)

if result == num:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
