"""
    Recursion:
    When a function calls itself is known as recursion

    

    Infinite Recursion:
    Wo recursion jo rukega nhi use hum Infinite Recursion kehte hai
    e.g. def greet():
            print("Hello")
            greet()
         greet()
    iska koi end hi nhi hoga last mein ek error show kr dega stack overflow error
    Python mein by default 996 times (personally mere system pe) r
    ecursion call hota hai agr uske baad mein bhi baar baar
    call ho rha hai function iska matlab ye infinte recursion call ho rha hai


    Recursion Tree:
    har recursion ke sawal ko krne ke liye hume pehle Recursion Tree bana ke dekhna
    chahiye

    Time Complexity = O(N+1) ~ O(N)
    Space Complexity = O(N+1) ~ O(N)
"""

# Print Your Name 4 Times using Recursion

# Method 1:
def call():
    global count
    if count == 4:
        return
    print("Somit")
    count += 1
    call()

count = 0
call()

# Method 2:
def call(count):
    if count == 4:
        return
    print("Somit")
    call(count+1)
    # Ye ek "HEAD RECURION" kaha jayega kyuki isme pehle hum kaam kr rhe hai fir aakhri
        # mein function ko call kr rhe hai isi ka opposite hota hai
        # "TAIL RECURSION" jisme pehle hum function recurively call krte hai uske baad
        # hum apna kaam krte hai

call(0)

# Solving Same questionn by using TAIL RECURSION

def call():
    global count
    if count == 4:
        return  
    count += 1
    call()
    print("Somit")

count = 0
call()