
import random
import day007_hangman_art
import day007_hangman_words



chosen_word = random.choice(day007_hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(day007_hangman_art.logo)


#Create blanks
display = []
for _ in range(word_length):
    display += "_"
guesses = []

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    

    
    
    if guess in guesses:
      print (f"You've already guessed {guess}. Try again")
    else:
      
    #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
                guesses.append(guess)
            
    #Check if user is wrong.
        if guess not in chosen_word:
        
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            guesses.append(guess)
            if lives == 0:
                end_of_game = True
                print(f"You lose. Word was {chosen_word}.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(day007_hangman_art.stages[lives])