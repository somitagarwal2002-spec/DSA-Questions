# Count of Digits

try:
    num = int(input("Enter any number: "))
except:
    print("Enter positive numbers only")
    num = int(input("Enter any number: "))

count = 0

while(num > 0):
    num = num // 10
    count += 1

print(count)
