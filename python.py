import random

# Define the rules
rules = {
    "Snake": "Water",  # Snake drinks water
    "Water": "Gun",    # Water destroys gun
    "Gun": "Snake"     # Gun kills snake
}

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif rules[user_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ["Snake", "Water", "Gun"]
    print("Welcome to the Snake-Water-Gun Game!")
    print("Your choices are: Snake, Water, Gun")

    while True:
        user_choice = input("Enter your choice: ").capitalize()
        if user_choice not in choices:
            print("Invalid choice. Please choose 'Snake', 'Water', or 'Gun'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()
