import random

def get_computer_choice():
    return random.choice(["snake", "water", "gun"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    
    elif (
        (user == "snake" and computer == "water") or 
        (user == "water" and computer == "gun") or 
        (user == "gun" and computer == "snake")
    ):
        return "You Win!"
    
    else:
        return "Computer Wins!"

def play_game():
    print("Welcome to Snake, Water, Gun Game")
    choices = ["snake", "water", "gun"]

    user_choice = input("Enter your choice (snake/water/gun): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please enter snake, water, or gun.")
        return
    
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()