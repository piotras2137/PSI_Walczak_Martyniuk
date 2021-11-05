# Kacper Walczak 155621
lista = [
    {"imie":"Kacper", "nazwisko":"Walczak", "studia":"informatyka"}, {"imie":"Kowalski", "nazwisko":"Janusz", "studia":"ekonomia"}, 
    {"imie":"Michał", "nazwisko":"Nowak", "studia":"prawo"}, {"imie":"Jeremiasz", "nazwisko":"Motyka", "studia":"geodezja"}, 
]

for i in lista:
    print(" {} {} studiuje {}".format( i["imie"], i["nazwisko"], i["studia"]))