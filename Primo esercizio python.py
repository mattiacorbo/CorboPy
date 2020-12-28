stringa1 = "Per quanti giorni hai intenzione di noleggiare uno scooter 50 cc?"
stringa2 = "Il prezzo è di €"
R1 = 45.00
R2 = 80.00
R3 = 120.00
R4 = 160.00

print(stringa1)
a = int(input("Inserisci il numero di giorni: "))
p_g_dopo4 = R4 + (a-4)*40
if a == 1 :
    print(stringa2, R1)
if a == 2 :
    print(stringa2, R2)
if a == 3 :
    print(stringa2, R3)
if a == 4 :
    print(stringa2, R4)
if a > 4 :
    print(stringa2, p_g_dopo4)
