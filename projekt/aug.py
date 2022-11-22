aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]


#Lehet e augusztus havi hóméséklet
#A legnagyobb hóméséklet
#A legkisebb hóméséklet
#Hány alkalommal volt a hőmeséklet 31 fok felett?
#mekkora volt a hómérséklet augusztus 20.-án?
#mekkora volt az átlag hőmérséklet?
#mekkora volt a hőingadoszás?
#Fájl írás

augtxt = open("aug.txt","w")

if len(aug) == 12:
    print(f"ez az augusztusi hőmérséklet adatsora")
else:
    print(f"ez nem az augusztusi hőmérséklet adatsora")

legnagyobb = aug[0]
for i in range(0,len(aug)):
    if aug[i] > legnagyobb:
        legnagyobb = aug[i]
print(f"Legnagyobb: {legnagyobb}")

legkisebb = aug[0]
for i in range(0,len(aug)):
    if aug[i] < legkisebb:
        legkisebb = aug[i]
print(f"Legkisebb: {legkisebb}")

ossz = 0
for i in range(0,len(aug)):
    ossz +=1
print(ossz)
print(len(aug))

felett = 0
szam = 31
for i in range(0,len(aug)):
    if aug[i] > szam:
        felett += 1
print(felett)

hanyadikán = 20
for i in range(0,len(aug)):
    if i == hanyadikán+1:
        hanyadikán_eredmény = aug[i]

atlag = 0
for i in range(0,len(aug)):
    if i == hanyadikán+1:
        atlag += aug[i]
atlag = atlag/len(aug)
        

augtxt.write(f"Legnagyobb : {legnagyobb}\n")
augtxt.write(f"Legkisebb : {legkisebb}\n")
augtxt.write(f"Összesen : {ossz}\n")
augtxt.write(f"{szam} alatt : {felett}\n")
augtxt.write(f"átlag : {atlag}\n")
augtxt.write(f"{hanyadikán}. : {hanyadikán_eredmény}\n")
augtxt.write(f"hőingadozás: {legnagyobb-legkisebb}\n")

augtxt.close()