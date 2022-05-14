print("Your computer challenges you to a Rock Paper Scissors battle!")
def main():
    import random
    computer_play = random.randint(0,2)
    player_play = input("What do you choose? (r/p/s) \nRock?\nPaper?\nor Scissors? ")
    def game():
        if computer_play == 0:
            print("Good job! You win!")
            if player_play == 'r':
                print("The computer chose Scissors.")
            elif player_play == 'p':
                print("The computer chose Rock.")
            elif player_play == 's':
                print("The computer chose Paper.")
        elif computer_play == 1:
            print("It was a draw!")
            if player_play == 'r':
                print("The computer chose Rock aswell!")
            elif player_play == 'p':
                print("The computer chose Paper aswell!")
            elif player_play == 's':
                print("The computer chose Scissors aswell!")
        elif computer_play == 2:
            print("The computer won.")
            if player_play == 'r':
                print("The computer chose Paper.")
            elif player_play == 'p':
                print("The computer chose Scissors.")
            elif player_play == 's':
                print("The computer chose Rock.")
    game()

    restart = input("Would you like to try again? (y/n) ")
    if restart == 'y':
        main()
    elif restart == 'n':
        print("Okay, goodbye!")
input("Press enter to exit.")
main()
quit()