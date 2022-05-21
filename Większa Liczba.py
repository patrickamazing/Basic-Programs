# This program will give you the biggest number out of the ones inputted.
def main():
    firstInt = int(input("Input the first number: " ))
    secondInt = int(input("Input the second number: " ))
    if firstInt > secondInt:
        print("The bigger number is:" + firstInt + ",  the first number you inputted.")
    elif firstInt < secondInt:
        print("The bigger number is: " + secondInt + ", the second number you inputted.")
    def restarting():
        restart = input("Do you want to run this program again? (y/n) ")
        if restart != 'y' and restart != 'n':
            print("Error.")
            restarting()
        elif restart == 'y':
            main()
        elif restart == 'n':
            print("Have a good day! :)")
            input("Press enter to exit. ")
    restarting()    
main()
quit()