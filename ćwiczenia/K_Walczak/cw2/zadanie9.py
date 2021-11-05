from zadanie8 import *

txt = FileManager("plik.txt")
txt.update_file("Ala ma kota")
print(txt.read_file())
