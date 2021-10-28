# Kacper Walczak 155621
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista[5:10]
lista = lista[0:5]
print(lista2)
print(lista)

polaczoneListy = lista + lista2
print(polaczoneListy)
polaczoneListy.insert(0, 0)
print(polaczoneListy)
kopia = polaczoneListy
print(kopia)
kopia.reverse()
print(kopia)
