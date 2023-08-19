import requests
szam=999
li=[]
while szam!=9999:
    print("keresem"+str(szam))
    r = requests.head("https://icast.connectmedia.hu/"+str(szam)+"/live.mp3")
    if(r.status_code==200):
        li.append(szam)
    szam+=1
print("Sikeresen végig futott a keresés. Összesen "+str(len(li))+"db rádió adást talált.")
print("Kírjam txtbe? (I/N)")
ker=input()
if(ker=="I" or ker=="i"):
    with open('mukodooldalak.txt', 'w') as f:
        for line in li:
            f.write(f"https://icast.connectmedia.hu/"+str(line)+"/live.mp3\n")
    f.close()


    