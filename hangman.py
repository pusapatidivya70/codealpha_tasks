import random

# User name
name = input("Enter your name: ")
print("Welcome", name, "to Hangman Game!")

# Word list
words = ["apple", "tiger", "chair", "robot", "python", "laptop", "college"]
word = random.choice(words)

guessed = []
attempts = 6

print("\nGuess the word!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Guessed letters:", guessed)

    if "_" not in display:
        print("\n You Win,", name, "!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print(" Already guessed!")
    elif guess in word:
        print(" Correct!")
        guessed.append(guess)
    else:
        attempts -= 1
        print(" Wrong! Chances left:", attempts)

if attempts == 0:
    print("\n You Lost,", name, "! The word was:", word)
