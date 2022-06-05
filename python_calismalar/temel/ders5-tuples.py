
tupleListe = (2,4,6,"Ankara",(2,3,4),[])
liste = [2,4,6,"Ankara",[3,4,5],()]

liste[0] = "6"
#tupleListe[0] = 6 #tuple listeler readonly, yani değiştirelemez.

print(tupleListe[1:2]) #1den 2ye kadar, 2 dahil değil.
print(liste[1:2])

print(tupleListe[-2]) #sağdan 2. sıra, sağda 1'den başlıyor
print(liste[-2])

print(type(tupleListe))
print(type(liste))

print(tupleListe)
print(liste)

print(len(tupleListe))
print(len(liste))

tupleDeger = ()