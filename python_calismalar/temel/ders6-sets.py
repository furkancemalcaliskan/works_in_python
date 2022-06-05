
#Setler

studentsSet = {"Engin","Derin","Salih"}
studentsSet2 = set("Engin","Derin","Salih")
print(studentsSet)

#sıralı göstermiyor

for student in studentsSet:
    print(student)

print("derin" in studentsSet) #boolean ifade döndürür.
#py. büyük-küçük harf duyarlı

print("Derin" in studentsSet)

if "Derin" in studentsSet:
    print("Listede var")


studentsSet.add("Ali")

print(studentsSet)

studentsSet.update(["Merve","Mert","Selin"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Selin") #remove bulamazsa hata verir
print(len(studentsSet))

studentsSet.discard("Selin") #discard bulamazsa hata vermez
print(len(studentsSet))

x = studentsSet.pop() #random eleman siler
x  = studentsSet.clear() #setin içini temizler
del studentsSet #seti siler

