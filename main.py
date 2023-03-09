import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in range(word_length):
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ")[0].lower()

    if guess in display:
        print(f'You already played letter "{guess}". Please try another one.')
        continue

    if guess not in chosen_word:
        lives -= 1
        print(f'The letter "{guess}" is not in the word. You lost a life.')
        print(f'Remaining lives: {lives}')
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"You loose... The word was: {chosen_word}")

    for i in range(word_length):
        if chosen_word[i] == guess:
            print(f'The letter "{guess}" is in the word! Good guess!')
            display[i] = guess

    print("".join(display))

    if "_" not in display:
        end_of_game = True
        print("You Win!")


