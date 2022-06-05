# r Read(oku), a append(ekle), w write(yerine yazar), x create(oluştur)

f = open("musteriler.txt")
#print(f.read())

for l in f:
    print(f.readline())

f.close()

# fileToAppend = open("ogrenciler.txt","a")
# fileToAppend.write("\n")
# fileToAppend.write("Engin")
# fileToAppend.close()

fileToAppend = open("ogrenciler.txt","a")
fileToAppend.write("\n")
fileToAppend.write("Engin")
fileToAppend.close()

import os

os.remove("ogrenciler.txt") #dosyayı siler
if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
else:
    print("Dosya yok!")

#os.rmdir("klasör adı") klasör siler
