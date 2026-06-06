import random

liczba = random.randint(1, 10)


waga = int(input("Ile waży dupa twojej matki? "))

cyc = int(input("Ile ma cycków? "))

print("Jej bodycount to : " + str(liczba * waga / cyc))


