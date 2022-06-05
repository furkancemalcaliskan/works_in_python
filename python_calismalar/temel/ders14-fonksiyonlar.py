

#sehir = "Ankara"

#print(sehir.upper())


#print(sehir.endswith("a"))

def selamVer(isim = "ziyaretçi"): #default parametre
    print("Merhaba " + isim)


selamVer("Furkan")
selamVer()

def selamVer2(isim = "ziyaretçi",soyIsim = " arkadaş"): #default parametre
    print("Merhaba " + isim + " " + soyIsim)

selamVer2("Furkan","Çalışkan")
