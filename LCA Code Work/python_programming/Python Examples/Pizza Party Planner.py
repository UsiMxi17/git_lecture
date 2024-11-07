# Exercise: Pizza Party Planner

# You're throwing a pizza party and need to calculate how many pizzas you'll need.
# Write a function that takes the number of people and how many slices each person eats,
# then calculates the total number of slices needed.

# Task: Ask the user how many guests they are inviting and how many slices each person wants.
# Then, tell them how many slices of pizza they need.

def pizza_party_planner():
    # Asking for the number of guests
    guests = int(input("How many guests are you inviting? "))
    
    # Asking for the number of slices each person wants
    slices_per_person = int(input("How many slices does each person want? "))
    
    # Calculate the total number of slices needed
    total_slices = guests * slices_per_person
    
    # Assuming a standard pizza has 8 slices
    slices_per_pizza = 8
    pizzas_needed = total_slices // slices_per_pizza
    
    # If there are leftover slices, we need an additional pizza
    if total_slices % slices_per_pizza != 0:
        pizzas_needed += 1
    
    print(f"You will need {pizzas_needed} pizzas for your party.")

# Call the function
pizza_party_planner()


# Use the correct type of loop to create games or activities that continue until the user chooses to stop.
# Ask the user to set their own secret password for someone else to guess.

def password_guessing_game():
    while True:
        # Ask the user to set a secret password
        secret_password = input("Set a secret password for someone to guess: ")
        
        # Start the guessing process
        print("The guessing takes fold! Ask someone to guess the password.")
        
        while True:
            guess = input("Enter your guess (or type 'exit' to stop): ")
            
            if guess == 'exit':
                print("Exiting the guessing game.")
                break
            elif guess == secret_password:
                print("Congratulations! You've guessed the password!")
                break
            else:
                print("Incorrect guess. Try again.")

        # Ask if the user wants to play again
        play_again = input("Do you want to set another password? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

# Start the game
password_guessing_game()
