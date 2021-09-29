class Libri_Scolastici:
    def __init__(self, materia, numero_pagine, editore, prezzo):
        self.materia = materia
        self.numero_pagine = numero_pagine
        self.editore = editore
        self.prezzo = prezzo

    def scheda_libro(self):
        return f"\nSched\n Materia: {self.materia}\n Numero Pagine: {self.numero_pagine}\n Editore: {self.editore}\n Prezzo: {self.prezzo}"

Libro_uno= Libri_Scolastici("Latino", "305", "Zanichelli", "24.90")
Libro_due= Libri_Scolastici("Inglese", "186", "Tresei", "19.85")
Libro_tre= Libri_Scolastici("Matematica", "593", "Zanichelli", "33.90")
Libro_quattro= Libri_Scolastici("Inglese", "255", "Atlas", "21.99")

print(Libri_Scolastici.scheda_libro(Libro_uno))
print(Libri_Scolastici.scheda_libro(Libro_due))
print(Libri_Scolastici.scheda_libro(Libro_tre))
print(Libri_Scolastici.scheda_libro(Libro_quattro))
