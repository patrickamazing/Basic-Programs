# This program will show you the numbers inputted from biggest to smallest

def main():
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    c = int(input("Third Number: "))
    if a >= b and a >= c:
        print("1 :", a)
        if b >= c:
            print("2 :", b)
            print("3 :", c)
        elif b <= c:
            print("2 :", c)
            print("3 :", b)
    elif a >= b and a <= c:
        print("1 :", c)
        print("2 :", a)
        print("3 :", b)
    elif a <= b and a <= c:
        if b <= c:
            print("1 :", c)
            print("2 :", b)
        else:
            print("1 :", b)
            print("2 :", c)
        print("3 :", a)
    elif a <= b and a >= c:
        print("1 :", b)
        print("2 :", a)
        print("3 :", c)
    
    restart = input("Do you want to start again? (y/n) ")
    if restart == 'y':
        main()
    elif restart == 'n':
        print("Have a nice day! :D")
main()
