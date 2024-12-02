import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100. Type 'exit' to quit.")

# Initialize score
score = 100

while True:
    user_input = input("Enter your guess: ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Thanks for playing! The number was:", random_number)
        break

    try:
        user_guess = int(user_input)
        if user_guess < random_number:
            print("Too low! Try again.")
            score -= 10
        elif user_guess > random_number:
            print("Too high! Try again.")
            score -= 10
        else:
            print(f"Correct! You guessed the number. Your score is {score}.")
            break
    except ValueError:
        print("Please enter a valid number!")
