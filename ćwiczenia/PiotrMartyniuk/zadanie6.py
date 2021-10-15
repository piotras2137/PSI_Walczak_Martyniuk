lista = [i for i in range(1, 11)]
print(lista)
lista2 = lista[5:]
lista = lista[:5]
print(lista)
print(lista2)
polaczone = [0] + lista + lista2
print(polaczone)
lista3 = polaczone
lista3.sort(reverse=True)
print(lista3)
