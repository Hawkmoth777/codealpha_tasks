import random
words = ["apple", "bat", "couch", "doll", "eat"]

while True:
    k = 0 
    chosen = words[random.randint(0,4)]
    guessed_letters = "" 
    
    print("      NEW GAME STARTED!      ")

    while k < 6:
        guess = input("\nTake a guess of a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter exactly ONE letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter! Try a different one.")
            continue
        
        guessed_letters = guessed_letters + guess 
        blank = "" 
        
        for letter in chosen:
            if letter in guessed_letters:
                blank = blank + letter + " "
            else:
                blank = blank + "_ "
                
        print("Word: " + blank)
        
        if guess in chosen:
            print("Good guess! Attempts used: " + str(k))
        else:
            k = k + 1
            print("No, that letter is not in the word.")
            print("Attempts used: " + str(k))
            
        if "_" not in blank:
            print("\nCongratulations! You guessed the word!")
            break 
            
    else:
        print("\nSorry, you've run out of guesses. The word was: " + chosen)
        
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break