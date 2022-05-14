# This program will convert lb's to kg's
lb = 2.204623
rounding = int(input("Please enter the number you will want to be rounding to (max=6): "))
def main():
    modes = int(input("Please select your mode: \n1 = kg to lb.\n2 = lb to kg. "))
    if modes != 1 and modes != 2:
        print("Error: Incorrect mode.")
        main()
    else:
        input1 = int(input("Enter weight you will be converting: "))
        if modes == 1:
          print(input1,"kg's converted to lb's is:",round(input1*lb, rounding))
        else:
            print(input1,"lb's converted to kg's is:",round(input1/lb, rounding))
    def restarting():
        restart = input("Do you want to convert again? (y/n) ")
        if restart != 'y' and restart != 'n':
            print("Error.")
            restarting()
        elif restart == 'y':
            main()
        elif restart == 'n':
            input("Have a good day!\nPress enter to exit.")
            quit()
    restarting()
main()