

with open('words_alpha.txt') as f_obj:
    lista = f_obj.read().split()

print(len(lista))
a,b,c,d,e,f = input("wpisz 6 liter: ").split()
g = input("wpisz literę ze środka: ")

dlglisty = len(lista)
for i in range(0, dlglisty):
      #print(f"│{lista[i]}│")
      if a and b and c and d and e and f not in lista[i]:
          print(lista[i])


