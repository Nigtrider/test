import random

zahl = random.randint(1, 10)
rate = int(input("Rate eine Zahl zwischen 1 und 10: "))

if rate == zahl:
    print("Richtig geraten!")
else:
    print("Leider falsch. Die Zahl war:", zahl)