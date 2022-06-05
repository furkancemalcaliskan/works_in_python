class DortIslem:
    def topla(x,y):
        return x + y
    def cikar(x,y):
        return x - y
    def carp(x,y):
        return x * y
    def bol(x,y):
        return x / y

print("1: Toplama İşlemi")
print("2: Çıkarma İşlemi")
print("3: Çarpma İşlemi")
print("4: Bölme İşlemi")
operasyon = int(input("Operasyon?"))
if operasyon <=4 and operasyon >= 1:
    a = int(input("ilk sayı?"))
    b = int(input("ikinci sayı?"))
    if operasyon == 1:
        print("Sonuc: " + DortIslem.topla(a,b))
    elif operasyon == 2:
        print("Sonuc: " + DortIslem.cikar(a,b))
    elif operasyon == 3:
        print("Sonuc: " + DortIslem.carp(a,b))
    elif operasyon == 4:
        print("Sonuc: " + DortIslem.bol(a,b))
else:
    print("Geçersiz İşlem")


