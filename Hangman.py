import random # for choosing random word 

from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()
     
def play(word):
     word_completion = "_" * len(word) # every letter is underscore in start == to lem of the word
     guessed = False # at begin guess is false
     guessed_letters = []
     guessed_words = []
     tries = 6 # acc to the hangman parts
     print("Let's Play Hangman!")
     print(display_hangman(tries))
     print(word_completion)
     print("\n")
     
     while not guessed and tries > 0:
         print("\n")
         print("\n Number of letter in word: ", len(word))
         guess = input("Please Guess the letter or word: ").upper()
         if len(guess) == 1 and guess.isalpha():
             #if letter already been guessed
             if guess in guessed_letters:
                 print("You have already guessed the letter: ", guess)
             elif guess not in word: # letter not in guessed
                 print(guess, "is not in the word")
                 tries -= 1
                 guessed_letters.append(guess)
             else:
                 print("Good Job!!!!! " , guess , "is in the word!")
                 guessed_letters.append(guess)
                 # convert string to the list (so that we can index into this)
                 # update var word completion to reveal all occurrences of the guess
                 list_word = list(word_completion)
                 # checks corresponding letter is equal to guessed letter
                 indices = [i for i, letter in enumerate(word) if letter == guess]
                 # to change each underscore to the guessed letters
                 for index in indices:
                     list_word[index] = guess
                 word_completion = "".join(list_word) # to change list back to string
                 # completion check
                 if "_" not in word_completion:
                     guessed = True            
         elif len(guess) == len(word) and guess.isalpha():
             if guess in guessed_words:
                 print("You have already guessed the word: ", guess)
             elif guess != word:
                 print(guess, "is not in the word.")
                 tries -= 1
                 guessed_words.append(guess)
             else:
                 guessed = True
                 word_completion = word
         else:
             print("Guess is not correct")   
         print(display_hangman(tries))
         print(word_completion)
         print("\n")

     if guessed:
         print("\n 😍😍 Congrats, you guessed the word correctly!!!!Yay ")
     else:
         print("\n 🥺🥺 Sorry, you ran out of guesses!  Better luck 👍🚀 ")
         print("\n Correct Word : " + word)
     
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Wanna Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

# run our script on the command line
if __name__ == "__main__":
    main()
 