# This program will convert different weights.
lbFactor = 2.204623
ozFactor = 35.27396195
def main():
    modeSelection = int(input("Please select your mode: \n1 = kg to lb.\n2 = lb to kg.\n3 = kg to oz.\n4 = oz to kg. "))
    if modeSelection != 1 and modeSelection != 2 and modeSelection != 3 and modeSelection != 4:
        print("Error: Incorrect mode.")
        main()
    else:
        inputWeight = int(input("Enter weight you will be converting: "))
        if modeSelection == 1:
          print(inputWeight,"kg's converted to lb's is:",round(inputWeight*lbFactor, 3))
        elif modeSelection == 2:
            print(inputWeight,"lb's converted to kg's is:",round(inputWeight/lbFactor, 3))
        elif modeSelection == 3:
            print(inputWeight,"kg's converted to oz's is:",round(inputWeight*ozFactor, 3))
        elif modeSelection == 4:
            print(inputWeight,"oz's converted to kg's is:",round(inputWeight/ozFactor, 3))
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
main()
restarting()