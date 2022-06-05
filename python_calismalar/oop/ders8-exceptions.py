#Temel hata yönetimi

try:
    sayi = int(input("Sayı giriniz."))
except ValueError:
    print("Hata! Tip uyuşmazlığı.")
except ZeroDivisionError:
    print("Payda sıfır olamaz.")
except:
    print("Hata oluştu")
print("Bitti")

