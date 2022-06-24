# This program will show you the numbers inputted from biggest to smallest

def main():
    intA = int(input("First Number: "))
    intB = int(input("Second Number: "))
    intC = int(input("Third Number: "))
    if intA >= intB and intA >= intC:
        print("1 :", intA)
        if intB >= intC:
            print("2 :", intB)
            print("3 :", intC)
        elif intB <= intC:
            print("2 :", intC)
            print("3 :", intB)
    elif intA >= intB and intA <= intC:
        print("1 :", intC)
        print("2 :", intA)
        print("3 :", intB)
    elif intA <= intB and intA <= intC:
        if intB <= intC:
            print("1 :", intC)
            print("2 :", intB)
        else:
            print("1 :", intB)
            print("2 :", intC)
        print("3 :", intA)
    elif intA <= intB and intA >= intC:
        print("1 :", intB)
        print("2 :", intA)
        print("3 :", intC)
    
    restart = input("Do you want to start again? (y/n) ")
    if restart == 'y':
        main()
    elif restart == 'n':
        print("Have a nice day! :D")
main()