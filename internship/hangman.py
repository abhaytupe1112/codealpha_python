+import random

def hangman():
    # Step 1: Predefined list of words
    words = ["python", "apple", "dream", "mango", "cloud"]

    # Step 2: Randomly select a word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)  # Initially all blanks
    guessed_letters = []  # To store guessed letters
    attempts = 6  # Limit of wrong guesses

    print("Welcome to Hangman Game!")
    print("You have 6 chances to guess the word.")
    print("Word: ", " ".join(guessed_word))

    # Step 3: Game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Step 4: Check guess
        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        print("Word: ", " ".join(guessed_word))

    # Step 5: Result
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n❌ Game Over! The word was:", word)

# Run the game
hangman()