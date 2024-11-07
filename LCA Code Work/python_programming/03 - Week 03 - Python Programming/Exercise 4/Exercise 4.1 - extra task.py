#------------------------------------------------------------------------------------
#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.

def check_attendance(students, absentees):
    return [student for student in students if student in absentees]

# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.

students_list = ["Alice", "Bob", "Charlie", "David"]
absentees_list = ["Bob", "David"]
absent_students = check_attendance(students_list, absentees_list)
print("Absent Students:", absent_students)

#------------------------------------------------------------------------------------
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.

def calculate_average_grade(grades):
    return sum(grades.values()) / len(grades)

# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.

grades_dict = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
average_grade = calculate_average_grade(grades_dict)
print("Average Grade:", average_grade)

#------------------------------------------------------------------------------------
# Task 3: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.

def operation_selector(operation):
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "multiply":
        return lambda x, y: x * y

# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.

add_function = operation_selector("add")
multiply_function = operation_selector("multiply")

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.

print("4 + 6 =", add_function(4, 6))
print("3 * 7 =", multiply_function(3, 7))

#------------------------------------------------------------------------------------
# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.

def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    return (distance / fuel_efficiency) * fuel_price

# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)
# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.

grocery_inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Tomatoes": 25,
    "Bread": 15,
    "Milk": 10
}

# TODO: Use a for loop to print each item and its quantity in stock.

for item, quantity in grocery_inventory.items():
    print(f"{item}={quantity}")

# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).

total_items = sum(grocery_inventory.values())
print("Total items in stock:", total_items)

#------------------------------------------------------------------------------------
# Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)

# TODO: Ask the user to input their PIN.
# TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
# TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".

correct_pin = "1234"
attempts = 0

# TODO: Use a while loop to implement the retry system.66

while attempts < 3:
    pin_input = input("Enter your PIN: ")
    if pin_input == correct_pin:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Incorrect PIN. Try again.")
if attempts == 3:
    print("Account Locked")

#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System

# TODO: Create a list with 10 random assignment scores (between 0 and 100).

# TODO: Use a for loop to calculate the total score.

# TODO: Calculate and print the average score for the class.
# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.

import random

# List of 10 student scores.
scores = [random.randint(0, 100) for _ in range(10)]

total_score = 0
for score in scores:
    total_score += score

# TODO: Calculate total and average scores.

average_score = total_score / len(scores)
print(f"Scores: {scores}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score:.2f}")

if average_score > 75:
    print("Congratulations! The class performed well!")

#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)

# TODO: Create a list with the names of 20 participants.
# TODO: Use the random module to select 5 random participants.
# TODO: Print the names of the selected team members.

import random

# List of participants.

participants = [f"Person{i}" for i in range(1, 21)]

# TODO: Randomly select 5 people from the participants list.

selected_team = random.sample(participants, 5)

#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)

# Step 1: Create a module named 'fitness_tracker.py' with the following functions:
"""
def walk_calories(distance_km):
    # Calories burned per km walking: 50
    return distance_km * 50

def run_calories(distance_km):
    # Calories burned per km running: 100
    return distance_km * 100

def cycle_calories(distance_km):
    # Calories burned per km cycling: 70
    return distance_km * 70
"""

# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.

import fitness_tracker

# TODO: Ask the user to input the distance they walked, ran, and cycled today.

distance_walked = int(input("Enter the distance walked (in km): "))
distance_ran = int(input("Enter the distance ran (in km): "))
distance_cycled = int(input("Enter the distance cycled (in km): "))

# TODO: Calculate and print the total calories burned for each activity.

calories_walked = fitness_tracker.walk_calories(distance_walked)
calories_ran = fitness_tracker.run_calories(distance_ran)
calories_cycled = fitness_tracker.cycle_calories(distance_cycled)

print(f"Calories burned walking: {calories_walked} kcal")
print(f"Calories burned running: {calories_ran} kcal")
print(f"Calories burned cycling: {calories_cycled} kcal")

# TODO: Sum and print the total calories burned for the day.

total_calories = calories_walked + calories_ran + calories_cycled
print(f"Total calories burned today: {total_calories} kcal")

#------------------------------------------------------------------------------------
# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)

# TODO: Ask the user to input the total loan amount.

loan_amount = float(input("Enter the total loan amount: "))

# TODO: Ask the user to input their monthly repayment amount.

monthly_payment = float(input("Enter your monthly payment amount: "))

# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.

monthly_payment = float(input("Enter your monthly payment amount: "))

# Use a while loop to simulate the repayment process.
while loan_amount > 0:
    # Deduct the monthly payment from the loan amount.
    loan_amount -= monthly_payment
    
    # Ensure the loan amount does not go negative.
    if loan_amount < 0:
        loan_amount = 0

# TODO: Print the remaining loan amount after each payment.

print(f"Remaining loan amount: ${loan_amount:.2f}")

# TODO: When the loan is fully paid off, print a congratulatory message.

print("Congratulations! Your loan has been fully paid off!")