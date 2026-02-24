# Printing Digits of a Number from ones place

try:
    num = int(input("Enter any number: "))
except:
    print("Enter integers only")
    num = int(input("Enter any number: "))

while(num > 0):
    last_digit = num % 10
    print(last_digit)
    num = num // 10
