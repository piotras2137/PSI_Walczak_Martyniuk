czymjestloremipsum = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMake'

imie = 'Piotr'
nazwisko = 'Martyniuk'

litera1 = imie[2]
litera2 = nazwisko[3]

print('w tekscie jest {} liter {} i {} liter {}'.format(czymjestloremipsum.count(
    litera1), litera1, czymjestloremipsum.count(litera2), litera2))
