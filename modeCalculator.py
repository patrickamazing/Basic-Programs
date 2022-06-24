# Calculator with modes
def main():
    print("Mode: \n Addition:1 \n Subtraction:2 \n Multiplication:3 \n Division:4")
    try: 
        mode = int(input("Enter your preffered mode: "))
    except ValueError:
        print("Error: Unrecognised mode")
        main()
    if mode != 1 and mode != 2 and mode != 3 and mode != 4:
        print("Error: Unrecognised mode")
        main()
    else:
        intA = int(input("First Integer: ")) 
        intB = int(input("Second Integer: "))

        if mode == 1:
            print(intA, "+", intB, "=", (intA+intB))
        elif mode == 2:
            print(intA, "-", intB, "=", (intA-intB))
        elif mode == 3:
            print(intA, "x", intB, "=", (intA*intB))
        elif mode == 4:
            print(intA, "/", intB, "=", (intA//intB), "(Jest to w przybliżeniu.)")
        else:
            print("Incorrect Mode.")

    def res():
        restart = input("Do you want to restart? (y/n) ")
        if restart == 'y':
            main()
        elif restart == 'n':
            print("Have a nice day! :D")
            quit()
        else:
            print("Error")
            res()
    res() 
main()