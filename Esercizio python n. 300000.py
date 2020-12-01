#Esercizio - stringhe
stringa=input("Digita quello che vuoi ")
Lettere = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
for lettera in Lettere:
    if stringa.count(lettera) > 0:
        print(lettera, " = ", stringa.count(lettera))
