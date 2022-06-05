

sayi = int(input("Birinci sayiyi gir"))
sayi2 = int(input("İkinci sayiyi gir"))
sayi3 = int(input("Ücüncü sayiyi gir"))

if (sayi >= sayi2) and (sayi >= sayi3):
    enBuyuk = sayi
elif (sayi2 >= sayi) and (sayi2 >= sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3

print("En Büyük :",enBuyuk)


            
