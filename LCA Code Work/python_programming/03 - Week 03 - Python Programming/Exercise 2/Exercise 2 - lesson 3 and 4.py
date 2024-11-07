# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator

x = 10
y = 5
print('3 + x is:', 3 + x)

# TODO: Multiply y by 2 using the *= operator

print('2 * y is:', 2 * y)

# TODO: Divide x by y and store the result in a variable called 'result'

result = x / y

# TODO: Print the value of 'result'

print(result)

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

a = 10
b = 5
c = 8

# TODO: Create a condition that checks if a is greater than b

condition1 = a > b

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)

condition2 = b % 2 == 0

# TODO: Create a condition that checks if c is less than or equal to a

condition3 = c <= a

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

finalcondition = condition1 or (condition2 and condition3)

# TODO: Print the value of 'final_condition'

print("Final Condition:", finalcondition)

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'

score = float(input("Enter test score (0-100): "))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = "Invalid score"

# TODO: Print the grade for the given score

print("Your grade is:", grade)

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'

operation = input("Enter an operation (+, -, *, /): ")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2

# TODO: Handle the case of division by zero

    if (num1, num2) != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
     result = "Invalid operation"

# TODO: Print the result of the operation

print("Result:", result)