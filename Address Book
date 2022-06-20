# An address book

import pickle
import os

def main():
    mode = input("Which mode will you be using? \nSave, Load, Delete or Exit? ")
    if mode == 'Save':
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        address1 = input("Address 1: ")
        address2 = input("Address 2: ")
        city = input("City: ")
        state = input("State/Province: ")
        postCode = input("Post/Zip Code: ")
        phoneNumber = input("Phone Number: ")
        email = input("E-mail: ")
        birthday = input("Birthday: ")
        names = firstName, lastName, address1, address2, city, state, postCode, phoneNumber, email, birthday
        fileName = firstName + " " + lastName + ".txt"
        pickle.dump(names, open(fileName, "wb"))
        main()
    elif mode == 'Load':
        try: 
            loadFileInput = input("Enter the First Name and Last Name of the person you want to see: ")
            loadFileInput = loadFileInput + ".txt"
            loadFile = pickle.load(open(loadFileInput, "rb"))
            print(loadFile)
            main()
        except FileNotFoundError:
            print("File not found.")
            main()
    elif mode == 'Delete':
        try: 
            deleteFileInput = input("Enter the First Name and Last Name of the person you want to delete: ")
            deleteFile = deleteFileInput + ".txt"
            os.remove(deleteFile)
            print("Removed", deleteFile, "Successfully!")
            main()
        except FileNotFoundError:
            print("File not found.")
            main()
    elif mode == 'Exit':
        print("Have a good day! :D")
        quit()
    elif mode != 'Load' and mode != 'Save' and mode != 'Delete' and mode != 'Exit':
        print("Error : Incorrect Mode.")
        main()
main()