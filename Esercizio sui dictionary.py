Voti_Alunni={
    "Mario":{"matematica":6,"italiano":6,"scienze":7,"inglese":4},
    "Giovanni":{"matematica":4,"italiano":6,"scienze":5,"inglese":7},
    "Paola":{"matematica":9,"italiano":6,"scienze":8,"inglese":8}
    }
alunno=input("Alunno di cui vuoi visulizzare la media voti (tra Mario, Giovanni e Paola):")
a=Voti_Alunni[alunno].values()
somma=sum(a)
Media_Voti=somma/4
print("La media dei voti di",alunno,"è",Media_Voti)
