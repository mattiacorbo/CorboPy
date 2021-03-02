import json
Library={
    "Libro1":'{"Titolo":"Il bambino con il  pigiama a righe", "Autore":"John Boyne", "Genere":"Romanzo, Letteratura per ragazzi, Favola, Romanzo Storico, Letteratura postmoderna"}',
    "Libro2":'{"Titolo":"Una storia semplice", "Autore":"Leonardo Sciascia", "Genere":"Narrativa, Mystery"}',
    "Libro3":'{"Titolo":"La coscienza di Zeno", "Autore":"Italo Svevo", "Genere":"Romanzo, Narrativa"}',
    "Libro4":'{"Titolo":"Storia di una gabbianella e del gatto che le insegnò a volare", "Autore":"Luis Sepúlveda", "Genere":"Narrativa"}',
    "Libro5":'{"Titolo":"Hunger Games: La ragazza di fuoco", "Autore":"Suzanne Collins", "Genere":"Thriller, Letteratura per giovani adulti, Fantascienza, Avventura, Letteratura per adulti, Narrativa distopica, Fantascienza apocalittica e post apocalittica"}',
    "Libro6":'{"Titolo":"Il sentiero dei nidi di ragno", "Autore":"Italo Calvino", "Genere":"Narrativa"}',
    "Libro7":'{"Titolo":"Il giorno dello sciacallo", "Autore":"Frederick Forsyth", "Genere":"Thriller, Spionaggio, Fiction storica, Romanzo storico"}',
    "Libro8":'{"Titolo":"Tutta colpa del denaro", "Autore":" Il vostro caro Dexter", "Genere":"Biografia"}',
    "Libro9":'{"Titolo":"Iliade", "Autore":"Omero", "Genere":"Poema epico, Poesia, Epico"}',
    "Libro10":'{"Titolo":"Odissea", "Autore":"Omero", "Genere":"Poema epico, Epico"}',
    }

Libri=json.dumps(Library)
print(Libri)
