print("Ta gra polega na tym, aby zgadnąć liczbe która jest pomiędzy 0 a 50.")
def main():
    import random
    random_number = random.randint(0,50)
    # print(random_number)
    def game():
        guess_number = int(input("Proszę wpisz liczbe: "))
        if guess_number == random_number:
            print("Dobrze! Zgadłeś liczbe!")
        elif guess_number > random_number:
            print("Liczba wpisana jest zbyt duża, spróbuj jeszcze raz!")
            game()
        elif guess_number < random_number:
            print("Liczba wpisana jest zbyt mała, spróbuj jeszcze raz!")
            game()
    game()
    
    restart = (input("Czy chcesz jeszcze raz spróbować? (y/n) "))
    if restart == 'y':
        main()
    else:
        print("Szkoda :(, to do zobaczenia!")
        quit()
main()