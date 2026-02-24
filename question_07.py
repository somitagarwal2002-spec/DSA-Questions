# Fibonacci Sequence

num = int(input("Enter how many fibonacci numbers you want to see: "))

n = num 

numbers = [1, 1]
i = 2

while(i < n):
    numbers.append(numbers[i - 1] + numbers[i - 2])
    i += 1

# print(numbers[num - 1])

print(numbers)

