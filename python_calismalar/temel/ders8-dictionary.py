

sozluk = {

    "book" : "kitap",
    "table" : "masa"
}
sozluk2 = dict(kitap ="book", masa = "table")


sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
print(sozluk)

del(sozluk["book"]) #sozlukten kitapı siler
print(len(sozluk))