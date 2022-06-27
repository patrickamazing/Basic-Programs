# This program will convert different weight units to other weight units.
def main():
    modeInput = input("What unit are you converting from?\n")
    modeInput = modeInput.lower()
    def mode():
        if modeInput == 'kilogram' or modeInput == 'kilograms' or modeInput == 'kilos' or modeInput == 'kilo' or modeInput == 'kg' or modeInput == 'kgs':
            modeOutput = input("What unit are you converting to?\n")
            modeOutput = modeOutput.lower()
            if modeOutput == 'ounce' or modeOutput == 'ounces' or modeOutput == 'oz':
                weightInput = int(input("Input Kilograms:\n"))
                weightOutput = weightInput * 35.274
                print(weightInput, "Kilograms =", round(weightOutput, 2), "Ounces.")
            elif modeOutput == 'pounds' or modeOutput == 'pound' or modeOutput == 'lb' or modeOutput == 'lbs':
                weightInput = int(input("Input Kilograms:\n"))
                weightOutput = weightInput * 2.205
                print(weightInput, "Kilograms =", round(weightOutput, 2), "Pounds.")
            else:
                print("Error: Unknown Unit")
                mode()
        elif modeInput == 'pound' or modeInput == 'pounds' or modeInput == 'lb' or modeInput == 'lbs':
            modeOutput = input("What unit are you converting to?\n")
            modeOutput = modeOutput.lower()
            if modeOutput == 'kilogram' or modeOutput == 'kilograms' or modeOutput == 'kilos' or modeOutput == 'kilo' or modeOutput == 'kg' or modeOutput == 'kgs':
                weightInput = int(input("Input Pounds:\n"))
                weightOutput = weightInput * 0.453592
                print(weightInput, "Pounds =", round(weightOutput, 2), "Kilograms.")
            elif modeOutput == 'ounce' or modeOutput == 'ounces' or modeOutput == 'oz':
                weightInput = int(input("Input Pounds:\n"))
                weightOutput = weightInput * 16
                print(weightInput, "Pounds =", round(weightOutput, 2), "Ounces.")
            else:
                print("Error: Unknown Unit")
                mode()
        elif modeInput == 'ounce' or modeInput == 'ounces' or modeInput == 'oz':
            modeOutput = input("What unit are you converting to?\n")
            modeOutput = modeOutput.lower()
            if modeOutput == 'kilogram' or modeOutput == 'kilograms' or modeOutput == 'kilos' or modeOutput == 'kilo' or modeOutput == 'kg' or modeOutput == 'kgs':
                weightInput = int(input("Input Ounces:\n"))
                weightOutput = weightInput * 0.0283495
                print(weightInput, "Ounces =", round(weightOutput, 2), "Kilograms.")
            elif modeOutput == 'pounds' or modeOutput == 'pound' or modeOutput == 'lb' or modeOutput == 'lbs':
                weightInput = int(input("Input Ounces:\n"))
                weightOutput = weightInput * 0.0625
                print(weightInput, "Ounces =", round(weightOutput, 2), "Pounds.")
        else:
            print("Error: Unknown mode")
            main()
        def restarting():
            restart = input("Would you like to restart?\n")
            restart = restart.lower()
            if restart == 'y' or restart == 'yes':
                main()
            elif restart == 'n' or restart == 'no':
                print("Have a nice day! :D")
            else:
                print("Error: Incorrect Input")
        restarting()
    mode()
main()