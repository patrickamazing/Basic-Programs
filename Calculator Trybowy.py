# Ten program jest kalkulatorem z trybami.
print("Tryb: \n Dodawanie:1 \n Odejmowanie:2 \n Mnożenie:3 \n Dzielenie:4")
mode = int(input("Prosze wprowadź typ: ")) # Tutaj użytkownik wpisuje tryb.

a = int(input("Prosze wprowadź pierwszą liczbe: ")) 
b = int(input("Prosze wprowadź drugą liczbe: "))

if mode == 1: # Jeśli tryb = 1, to:
    print(a, "+", b, "=", (a+b))
elif mode == 2: # Jeśli tryb = 2, to:
    print(a, "-", b, "=", (a-b))
elif mode == 3: # Jeśli tryb = 3, to:
    print(a, "x", b, "=", (a*b))
elif mode == 4: # Jeśli tryb = 4, to:
    print(a, "/", b, "=", (a//b), "(Jest to w przybliżeniu.)")
else: # Jeśli żaden z powyżej, to:
    print("Wystąpił błąd.")
quit()