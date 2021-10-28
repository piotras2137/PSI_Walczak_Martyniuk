# Kacper Walczak 155621
def zadanie1(a_list, b_list):
    return [i for i in a_list if i % 2 == 0] + [j for j in b_list if j % 2 != 0]


lista1 = [1, 1, 2, 3, 4, 12, 35, 25, 38, 26]
lista2 = [3, 5, 7, 1, 2, 3, 4, 5, 8, 12, 34, 11]
print(zadanie1(lista1, lista2))
