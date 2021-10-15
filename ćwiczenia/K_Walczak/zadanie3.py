
class Data(object):
    def __repr__(self):
        return 'ząb'


czlowiek = {'first': 'Kacper', 'last': 'Walczak'}

print('{0!r} {0!a}'.format(Data()))
print('{:>15}'.format('test'))
print('{:^48}'.format('konstantynopolitańczykowianeczka'))
print('{p[first]} {p[last]}'.format(p=czlowiek))
print('{:=17d}'.format((- 23)))
