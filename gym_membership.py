try:
    months = int(input("Enter the number of months you want to join gym membership for \n"))
except:
    print("Invalid input")
    months = int(input("Enter the number of months you want to join gym membership for \n"))
    
price = 0
    
if months <= 0:
    print("Enter months greater than zero")
else:
    while months > 0:
        if months >= 12:
            price += 15000
            months -= 12
        elif months >= 9:
            price += 12000
            months -= 11
        elif months >= 6:
            price += 9000
            months -= 8
        elif months >= 3:
            price += 5000
            months -= 5
        else:
            price += 3000
            break
            
print(price)
