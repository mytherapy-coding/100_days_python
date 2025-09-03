import random
'''
words = ["cat", "dog", "book", "car", "apple"]
word = random.choice(words)

guessed = ""
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    # Show the word with underscores and spaces
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

    # Check win
    if display.replace(" ", "") == word:
        print("You win! The word was:", word)
        break

    guess = input("Guess a letter: ")

    if guess in word:
        guessed += guess
        print("Good guess!")
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if tries == 0:
    print("Game over! The word was:", word)
'''

word_list = ["artwark", "baboon", "camel"]

word = random.choice(word_list)

placeholder = ''

for i in range(len(word)):
    placeholder += "-"
print(placeholder)

guess = input("Guess a letter: ").lower()

display = ''

for letter in word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)


