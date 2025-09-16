from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def get_turns_by_difficulty():
    """Ask for difficulty and return number of turns."""
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")


def compare_guess(user_guess, answer):
    """Return comparison result: 'high', 'low', or 'correct'."""
    if user_guess > answer:
        return "high"
    elif user_guess < answer:
        return "low"
    return "correct"


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    # print(f"Pssst, the correct answer is {answer}")  # For debugging

    turns = get_turns_by_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Validate numeric input
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        result = compare_guess(guess, answer)

        if result == "correct":
            print(f"🎉 You got it! The answer was {answer}.")
            return
        elif result == "high":
            print("Too high.")
        else:
            print("Too low.")

        turns -= 1

    print(f"😢 You've run out of guesses. The number was {answer}.")


game()
