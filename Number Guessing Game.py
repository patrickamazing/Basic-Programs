print("A number guessing game from 0-10.")
NOGuesses = int(0)
def main():
    import random
    random_number = random.randint(0,10)
    # print(random_number)
    def game():
        NOGuesses +=1
        guess_number = int(input("Guess a number:\n"))
        if guess_number == random_number:
            print("Good job, you got it!")
        elif guess_number > random_number:
            print("Incorrect! your number is greater than the correct one.")
            game()
        elif guess_number < random_number:
            print("Incorrect! your number is lesser than the correct one.")
            game()
    game()
    
    print("You guessed ",NOGuesses," times.")
    restart = (input("Do you want to try again?\n"))
    if restart == 'y' or restart == 'yes':
        main()
    else:
        print("Szkoda :(, to do zobaczenia!")
main()
input("Press enter to quit.")
quit()
