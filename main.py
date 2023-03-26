import random

# lista słów do odgadnięcia
words = ["kot", "pies", "słońce", "kwiat", "dom", "drzewo", "księżyc"]

# wybierz losowe słowo z listy
word = random.choice(words)

# stwórz listę z kresem pod każdą literą wybranego słowa
display = ["_" for letter in word]

# stwórz listę z literami, które gracz już wybrał
used_letters = []

# ustaw licznik błędów na 0
mistakes = 0

# pętla gry
while True:
    # wyświetl kreski reprezentujące słowo
    print(" ".join(display))

    # wyświetl litery, które gracz już wybrał
    print("Wybrane litery: " + " ".join(used_letters))

    # pobierz literę od gracza
    letter = input("Podaj literę: ")

    # sprawdź, czy litera jest już wykorzystana
    if letter in used_letters:
        print("Ta litera już została wybrana. Spróbuj ponownie.")
        continue

    # dodaj literę do listy użytych liter
    used_letters.append(letter)

    # sprawdź, czy litera występuje w wybranym słowie
    if letter in word:
        # zamień kresek na literę w odpowiednich miejscach
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
    else:
        # zwiększ licznik błędów
        mistakes += 1
        print("Nie ma takiej litery. Błędów: " + str(mistakes))

    # sprawdź, czy gracz wygrał
    if "_" not in display:
        print("Gratulacje, wygrałeś!")
        break

    # sprawdź, czy gracz przegrał
    if mistakes == 6:
        print("Przegrałeś. Szukane słowo to: " + word)
        break
