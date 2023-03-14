import random

x=0
while x<1 :
    deg = input("Skriv 'stein', 'saks' eller 'papir': ")
    liste = ["stein", "saks", "papir",]
    maskin = random.choice(liste)
    print("---")
    print("Maskin:",maskin)
    print("Deg:",deg)
    print("---")
    if maskin=="stein" and deg=="saks" :
     print("Du tapte!")
    elif maskin=="papir" and deg=="stein" :
     print("Du tapte!")
    elif maskin=="saks" and deg=="papir" :
     print("Du tapte!")
    elif deg=="stein" and maskin=="saks" :
     print("Du vant!")
    elif deg=="papir" and maskin=="stein" :
     print("Du vant!")
    elif deg=="saks" and maskin=="papir" :
     print("Du vant!")
    elif maskin==deg :
     print("uavgjort!")
    else :
     print("Det er ikke sånn man spiller!")
    print("---")
