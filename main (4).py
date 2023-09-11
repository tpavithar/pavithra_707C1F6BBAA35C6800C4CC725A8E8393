def factorial(n):
    result = 1
    if n < 0:
        return "Factorial is undefined for negative numbers"
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            result *= i
        return result

# Input from the user
try:
    num = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")

