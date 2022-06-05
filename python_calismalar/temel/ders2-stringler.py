#-*- coding: utf-8 -*-
# substring
mesaj = "Merhaba Dünya!"

print(mesaj[2])
print(mesaj[2:5])
print(mesaj[:5])
print(mesaj[12:13])

yeniMesaj = mesaj[2:5]

print(yeniMesaj)

#len fonksiyonu

print(len(mesaj))

yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]

print(yeniMesaj2)

#lower upper

print(mesaj.upper())
print(mesaj.lower())

#replace

print(mesaj.replace("ü","u"))

#split

bilgi = "  furkan 21 karabük  ".strip
print(bilgi.split(" "))