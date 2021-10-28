# Kacper Walczak 155621
txt = "Kamil Ślimak"


def reverse(text):
    wynik = ""
    for i in range(len(text)-1, -1, -1):
        wynik += text[i]
    return wynik


print(reverse(txt))
