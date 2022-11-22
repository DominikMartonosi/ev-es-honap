ev= [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650]

#ev=False
#if len(ev) == 12:
#    ev = True
#    print(f'ez egy év adatsora')
#else: 
#    print(f'ez nem egy év adatsora')
    


legnagyobb = ev[0]
for i in range(1,len(ev)):
    if ev[i] > legnagyobb:
        legnagyobb= ev[i]
print(f'Legnagyobb: {legnagyobb}')

legkisebb = ev[0]    
for i in range(1,len(ev)):
    if ev[i] < legkisebb:
        legkisebb= ev[i]
print(f'Legkisebb: {legkisebb}')


ossz = 0
for i in range(0,len(ev)):
    ossz +=1
print(ossz)
print(len(ev))

alatt = 0
szam = 2400
for i in range(0,len(ev)):
    if ev[i] < szam:
        alatt += 1
print(alatt)

evtxt = open("./11.22/ev.txt","w",1,"utf-8")
evtxt.write(f"Legnagyobb: {legnagyobb}\n")
evtxt.write(f"Legkisebb: {legkisebb}\n")
evtxt.write(f"Összesen: {ossz}\n")
evtxt.write(f"{szam} alatt: {alatt}")
evtxt.close()

