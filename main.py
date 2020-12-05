import random
from hangman_arts import stages, logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code, can be deleted once you operated this game
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

guessed_already = []

while not end_of_game:

    guess = input("Guess a letter: ").lower()
    if guess in guessed_already:
        print(f"{guess} has already been guessed. Please change another one.")
        continue
    else:
        guessed_already.append(guess)

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guessed letter {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
