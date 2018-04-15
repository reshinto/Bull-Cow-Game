def intro():
    intro_txt = "Welcome to Bulls and Cows word game."
    question = "Can you guess the {} letter isogram?".format(len(guess_word))
    print("#"*len(intro_txt))
    print(intro_txt)
    print("""
              }   {         ___
              (o o)        (o o)
       /-------\\ /          \\ /-------\\
      / | BULL |O            O| COW  | \\
     *  |-,--- |              |------|  *
        ^      ^              ^      ^ """)
    print(question)

def rules():
    choice = input("Do you want to read the Concept & Rules before playing the game (y/n)? ").lower()
    if choice == "y":
        print("""
Concept & Rules
This is a "Guess the isogram" game.
An isogram is a word with no repeating letters.
The user has a limited number of guesses.
After each guess the computer outputs..
    Bull = right letter in the right place.
    Cow = right letter in the wrong place.
You win by guessing the word within max tries.""")

def play_game():
    global current_try
    current_try = 1
    guess()

def guess():
    # Required to increase count
    global current_try, Bulls, Cows

    # Auto adjust number of max tries based on guess word length
    WordLenToMaxTries = {3:4, 4:7, 5:10, 6:16, 7:20}
    max_try = WordLenToMaxTries[len(guess_word)]

    while current_try <= max_try:
        Bulls, Cows = 0, 0
        guess_attempt = input("\nTry {} of {}. Enter your guess: ".format(current_try, max_try)).lower()
        if current_try <= max_try:
            # Ensure guesses are of the correct word length
            if len(guess_attempt) != len(guess_word):
                print("Please enter a {} letter word.".format(len(guess_word)))
                if current_try >0:
                    current_try -= 1
            # Ensure all guesses are alphabets
            elif guess_attempt.isalpha() == False:
                print("Please enter only alphabets")
                if current_try >0:
                    current_try -= 1
            # Ensure all letters are not repeated
            elif len(guess_attempt) != len(set(guess_attempt)):
                print("Please enter a word without repeating letters")
                if current_try >0:
                    current_try -= 1
            elif len(guess_attempt) == len(set(guess_attempt)):
                for i in range(len(guess_word)):
                    # Ensure only letters that are correct are given a score
                    if guess_attempt[i] in guess_word:
                        # Ensure correct positioned letter is given a bull, and wrong positioned letter a cow
                        if guess_attempt[i] == guess_word[i]:
                            Bulls += 1
                        else:
                            Cows += 1
                print("Bulls: {} | Cows: {}".format(Bulls, Cows))
                if Bulls == len(guess_word):
                    break
        current_try += 1
    summary(guess_word)

def play_again():
    prompt = input("\nDo you want to play again (y/n)? ")
    if prompt == "y":
        play_game()
    elif prompt == "n":
        print("See ya!")
    else:
        print("Invalid input!")
        play_again()

def summary(guess_word):
    global Bulls
    if Bulls == len(guess_word):
        print("Congrats!! - You win!")
        play_again()
    else:
        print("Too bad! you just got owned!")
        play_again()

if __name__ == "__main__":
    guess_word = "help" # Please set guess word from 3 to 7 characters long
    intro()
    rules()
    play_game()

