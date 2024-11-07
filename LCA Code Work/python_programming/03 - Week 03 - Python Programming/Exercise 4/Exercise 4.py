import math
# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "banana", "grape", "strawberry", "mango", "guava"]

# TODO: Use a for loop to print each fruit in the list
list
for fruit in fruits:
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1

countup = 5
while countup <= 15:
    print(countup)
    countup += 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers

for i in range(1, 11):
    print(i ** 2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random

# TODO: Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# TODO: Use a for loop to select and print 3 random colors from the list
for _ in range(3):
    print(random.choice(colors))


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:

"""def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

"""
# TODO: Import the custom module and use its functions

import math_operations

# TODO: Use a while loop to create a simple calculator

def calculator():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", math_operations.add(num1, num2))
            elif choice == '2':
                print("Result:", math_operations.subtract(num1, num2))
            elif choice == '3':
                print("Result:", math_operations.multiply(num1, num2))
            elif choice == '4':
                print("Result:", math_operations.divide(num1, num2))
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid input. Please choose a valid option.")

calculator()