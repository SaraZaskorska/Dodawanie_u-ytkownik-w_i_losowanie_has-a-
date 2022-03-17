#tworzenie osob, generowanie hasla i dodawanie ich do pliku
import random

print("Podaj jak ma nazywac sie plik w ktorym beda zapisywane twoje dane osobowe nie zapomnij po nazwie dodac .txt")
plik=open(input(),mode="w+",encoding="utf-8")
print("podaj swoje imie")
plik.write("Twoje imie to: ")
plik.write(input())
plik.write("\n")

print("Podaj swoje nazwisko:")
plik.write("Twoje nazwisko to: ")
plik.write(input())
plik.write("\n")

print("Podaj date urodzenia")
plik.write("Twoja data urodzenia to: ")
plik.write(input())
plik.write("\n")

podawanie=int(input("Podaj jak dlugie ma byc twoje haslo "))
UPPERCASE=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LOWERCASE=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CYFRY=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECJALNE=['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']
DODOAWANIE= SPECJALNE + CYFRY + LOWERCASE + UPPERCASE
haslo="".join(random.sample(DODOAWANIE,podawanie))
print("Twoje haslo to")
print(haslo)
plik.write("Twoje haslo to: ")
plik.write(haslo)
plik.write("\n")
plik.close()