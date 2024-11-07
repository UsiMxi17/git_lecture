#------------------------------------------------------------------------------------
# Task 1: Arithmetic and Assignment Operators (Advanced)

# Initialize a variable z with any value.
z = 20

# Subtract 5 from z using the -= operator.
z -= 5

# Assume x is already defined, for example:
x = 10

# Add the value of x to z using the += operator.
z += x

# Divide z by 3 using the /= operator and store the result back in z.
z /= 3

# Print the final value of z.
print("Final value of z:", z)

#------------------------------------------------------------------------------------
# Task 2: Nested Comparison and Logical Operators

# Initialize three variables p, q, and r with different values.
p = 15
q = 10
r = 20

# Create a condition that checks if p is greater than q OR r is greater than q.
condition1 = (p > q) or (r > q)

# Also, check if p is less than or equal to r AND q is an even number.
condition2 = (p <= r) and (q % 2 == 0)

# Combine these conditions using logical operators to create a 'complex_condition'.
complex_condition = condition1 and condition2

# Print the value of 'complex_condition'.
print("Complex condition is:", complex_condition)

#------------------------------------------------------------------------------------
# Task 3: Complex Conditional Statements

# Ask the user to input their age and store it in a variable 'age'.
age = int(input("Enter your age: "))

# If the age is 18 or above, print "Eligible to vote."
if age >= 18:
    print("Eligible to vote.")
# If the age is between 13 and 17 (inclusive), print "Teenager."
elif 13 <= age <= 17:
    print("Teenager.")
# If the age is below 13, check if it is an even or odd number.
else:
    if age % 2 == 0:
        print("Even-aged.")
    else:
        print("Odd-aged.")

#------------------------------------------------------------------------------------
# Task 4: Comparing Three Numbers

# Ask the user to input three numbers: a, b, and c.
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))

# Compare the three numbers and print which one is the largest.
if a > b and a > c:
    print("Largest number is a:", a)
elif b > a and b > c:
    print("Largest number is b:", b)
elif c > a and c > b:
    print("Largest number is c:", c)
else:
    # Check if all three numbers are equal.
    if a == b == c:
        print("All numbers are equal.")
    else:
        # If two numbers are equal and larger than the third.
        if a == b:
            print("a and b are equal and larger than c.")
        elif a == c:
            print("a and c are equal and larger than b.")
        elif b == c:
            print("b and c are equal and larger than a.")

#------------------------------------------------------------------------------------
# Task 5: Advanced Arithmetic and Logical Operations

# Ask the user to input two numbers: x and y.
x = float(input("Enter first number (x): "))
y = float(input("Enter second number (y): "))

# If both x and y are positive, print their sum.
if x > 0 and y > 0:
    print("Sum:", x + y)
# If both x and y are negative, print their product.
elif x < 0 and y < 0:
    print("Product:", x * y)
# If one of them is positive and the other is negative, print their absolute difference.
elif (x > 0 and y < 0) or (x < 0 and y > 0):
    print("Absolute difference:", abs(x - y))
# If both are zero, print "Both are zero."
elif x == 0 and y == 0:
    print("Both are zero.")