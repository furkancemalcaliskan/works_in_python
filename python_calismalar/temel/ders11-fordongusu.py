

sehirler = ["Ankara","İstanbul","İzmir"]
#print(sehirler[0])
#print(sehirler[1])
#print(sehirler[2])

for sehir in sehirler:
    print(sehir[0:1]) #0'dan 1'e kadar, 1 dahil değil


for sehir in sehirler:
    if sehir == "Ankara":

        print(sehir + " için kod = " + sehir[0:3])
        
for sehir in sehirler:
    if sehir == "Ankara":
        break
    print(sehir + " için kod = " + sehir[0:3])
    print("*******")

for sehir in sehirler:
    if sehir == "Ankara":
        continue
    print(sehir + " için kod = " + sehir[0:3])
    print("*******")