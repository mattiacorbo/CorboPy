
#Primo esercizio
#Soluzione equazione (ax+b=0)
a=int(input("Valore di a: "))
b=int(input("Valore di b: "))
print (a,"x","+",b,"=",0)
x=-b/a
print("x=",x)


#Secondo esercizio
c=int(input("Valore di c: "))
#Restituisco il valore più grande fra i 3 valori dati
valore_maggiore=max(a,b,c)
print("il numero più grande è",valore_maggiore)


#Terzo esercizio
a,b=b,a
print("a=",a)
print("b=",b)
