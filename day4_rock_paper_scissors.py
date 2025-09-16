import random

print('Welcome to game: "Rock, Paper, Scissors!"')

while True:
    user_choice = input("Your choice: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer's choice:", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You won!")
        else:
            print("You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose.")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose.")
        else:
            print("You win")

    again = input("Do you want to play again? Yes or No? ").lower()
    if again == "no":
        break
