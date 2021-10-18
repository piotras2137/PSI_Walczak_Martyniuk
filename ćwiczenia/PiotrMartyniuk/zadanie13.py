lista = [
    {"imie":"piotrek", "nazwisko":"martyniuk", "studia":"informatyka"}, 
    {"imie":"olek", "nazwisko":"gruby", "studia":"prawo"}, 
    {"imie":"kacper", "nazwisko":"walczak", "studia":"informatyka"}, 
    {"imie":"maksio", "nazwisko":"michalik", "studia":"teraz w sumie to juz nie studiuje"}, 
]

for i in lista:
    print(" {} {} studiuje {}".format( i["imie"], i["nazwisko"], i["studia"]))