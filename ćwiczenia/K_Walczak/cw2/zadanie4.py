# Kacper Walczak 155621

def temperatura(wartosc, typ):
    wynik = 0
    if typ == "Fahrenheit" or typ == "fahrenheit":
        wynik = (wartosc*1.8)+32
    elif typ == "Rankine" or typ == "rankine":
        wynik = (wartosc + 273.15) * 1.8
    elif typ == "Kelvin" or typ == "kelvin":
        wynik = wartosc + 273.15 * 1.8
    else:
        return "Niepoprawna wartosc"
    return wynik


print(temperatura(-10, "Fahrenheit"))
print(temperatura(15, "rankine"))
print(temperatura(13, "kelvin"))
print(temperatura(20, "farenhajt"))
