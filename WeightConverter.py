# This program will convert lb's to kg's or in reverse
lbFactor = 2.204623
roundingNumber = int(input("Input the number you will be rounding to: "))
def main():
    modeSelection = int(input("Please select your mode: \n1 = kg to lb.\n2 = lb to kg. "))
    if modeSelection != 1 and modeSelection != 2:
        print("Error: Incorrect mode.")
        main()
    else:
        inputWeight = int(input("Enter weight you will be converting: "))
        if modeSelection == 1:
          print(inputWeight,"kg's converted to lb's is:",round(inputWeight*lbFactor, roundingNumber))
        else:
            print(inputWeight,"lb's converted to kg's is:",round(inputWeight/lbFactor, roundingNumber))
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