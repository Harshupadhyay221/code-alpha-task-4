import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "science", "algorithm"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word().lower()
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    
    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.add(guess)
                if set(word_to_guess) <= guessed_letters:
                    print(f"Congratulations! You guessed the word: {word_to_guess}")
                    break
            else:
                attempts += 1
                print(f"Wrong guess! Attempts remaining: {max_attempts - attempts}")

                if attempts == max_attempts:
                    print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")
                    break
            guessed_letters.add(guess)
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
