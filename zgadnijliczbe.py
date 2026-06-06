import random

liczba = random.randint(1, 100)

while True:
    strzal = int(input("Zgadnij liczbę od 1 do 100: "))

    if strzal < liczba:
        print("Za mało!")
    elif strzal > liczba:
        print("Za dużo!")
    else:
        print("Zgadłeś!")
        break


