def textinfo(data_text):
    length = len(data_text)
    letters = []
    for i in range(length):
        letters.append(data_text[i])
    capital = data_text.upper()
    small = data_text.lower()
    informations = {'length': length, 'letters': letters,
                    'big_letters': capital, 'small_letters': small}
    return informations


print(textinfo("konstantynopolitanczykowianeczka"))
