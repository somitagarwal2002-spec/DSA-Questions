# Fibonacci Sequence

# num = int(input("Enter how many fibonacci numbers you want to see: "))

# n = num 

# numbers = [1, 1]
# i = 2

# while(i < n):
#     numbers.append(numbers[i - 1] + numbers[i - 2])
#     i += 1

# # print(numbers[num - 1])

# print(numbers)





# Using Recursion

def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n-1) + fib(n-2)

num = int(input("Enter any positive number: "))
answer = fib(num)
print(answer)

# Time Complexity = O(2^N)
# Space Complexity = O(2^N)
