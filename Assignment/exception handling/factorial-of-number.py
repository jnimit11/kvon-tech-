# def factorial_calculator(number):
#     if number < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")


#     result = 1

#     for i in range(1, number + 1):
#         result *= i
#     return result
    

# try:
#     num = int(input("Enter a number: "))
#     print("factorial:", factorial_calculator(num))

# except ValueError as e:
#     print("Error:", e)


import math

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise ValueError("Negative numbers are not defined , please enter a positive number!")
    
    result = math.factorial(num)
    print(f"The factorial of {num} is {result}")

except ValueError as e:
    print("Error:", e)

