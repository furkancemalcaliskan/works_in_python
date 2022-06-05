#Asal Sayı Hesaplama

#2,3,5,7,11,13

sayı = int(input("Sayı giriniz : "))
asallMi = True
for x in range(2,sayı):
    if (sayı % x) == 0:
        asallMi = False
        break

if asallMi == True:
    print("ASAL")
else:
    print("ASAL DEĞİL") 