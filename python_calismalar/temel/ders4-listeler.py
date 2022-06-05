

#ogrenci1 = "Engin"
#ogrenci2 = "Salih"
#ogrenci3 = "Derin"

#print(ogrenci1)
#print(ogrenci2)
#print(ogrenci3)

ogrenciler = ["Furkan", "Cemal", "Çalışkan"]

print(ogrenciler[1])
ogrenciler[0] = "hebele"
ogrenciler.append("dejkoveci")
ogrenciler.remove("Cemal")
print(ogrenciler)

#list constructor

sehirler = list(("Ankara","İstabul"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar

#print(sehirler.clear())
print("Ankara sayısı" + str(sehirler.count("Ankara")))
print("Ankara indexi= " + str(sehirler.index("Ankara")))
sehirler.pop(1)
sehirler.insert(0,"İstanbul")
sehirler.reverse()
print(sehirler)

sehirler2 = sehirler #bellekte aynı yere gidiyor
sehirler2[0] = "İzmir"
print(sehirler2)
print(sehirler) #sehirler2 ve sehirler eşit çıkıyor
sehirler3 = sehirler.copy()

sehirler.extend(sehirler3)
print(sehirler)

sehirler.sort()
sehirler.reverse()
print(sehirler)
