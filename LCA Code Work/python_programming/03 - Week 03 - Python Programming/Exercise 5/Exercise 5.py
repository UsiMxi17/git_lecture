# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits

fruits = ["apple", "banana", "grape", "strawberry", "mango", "guava"]

# TODO: Add a fruit to the end of the list

fruits.append("kiwi")

# TODO: Insert a fruit at the beginning of the list

fruits.insert(0, "pear")  # Inserts 1 at index 0

# TODO: Remove a fruit from the list

fruits.remove("grape")

# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5

numbers = [1, 2, 3, 4, 5]

# TODO: Create a new list with each number squared

squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# TODO: Find the sum and average of the original numbers

total_sum = sum(numbers)
average = total_sum / len(numbers)

# TODO: Print the results

print("Sum: ", total_sum)
print("Average:", average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals

countries_and_capitals = {
    "Canada": "Ottawa",
    "France": "Paris",
    "United States": "Washington, D.C.",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "United Kingdom": "London",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "South Africa": "Pretoria"
}


# TODO: Add a new country-capital pair

countries_and_capitals["Argentina"] =  "Buenos Aires"


# TODO: Update the capital of an existing country

countries_and_capitals["South Africa"] = "Cape Town"

# TODO: Remove a country-capital pair

del countries_and_capitals["Germany"]

# TODO: Print the modified dictionary

print(countries_and_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors

fruit_colors = {
    "pear": "green",
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "strawberry": "red",
    "mango": "yellow",
    "guava": "yellow",
    "kiwi": "brown"
}

# TODO: Print all the fruits (keys)

print("Fruits:", list(fruit_colors.keys()))

# TODO: Print all the colors (values)

print("Fruits:", list(fruit_colors.values()))

# TODO: Print each fruit and its color

print("Fruits and their colors:")

for fruit, color in fruit_colors.items():

    print(f"{fruit}={color}" )

# TODO: Check if a fruit is in the dictionary and print its color

print(fruit_colors["strawberry"])