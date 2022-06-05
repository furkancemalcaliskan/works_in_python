
def faktoriyel(a):
    if a == 0:
        return 1
    else:
        return a * faktoriyel(a-1)

sayi = int(input("Bir sayi girin"))
if sayi<0:
    print("Negatif sayıların faktoriyeli olmaz")
else:
    print(faktoriyel(sayi))