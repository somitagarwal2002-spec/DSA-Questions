# Count of Digits

from math import *
try:
    num = int(input("Enter any number: "))
except:
    print("Enter positive numbers only")
    num = int(input("Enter any number: "))

n = num
count = 0

while(n > 0):
    n = n // 10
    count += 1

print(count)

# Short Method and More efficient

print(int(log10(num)+1))
