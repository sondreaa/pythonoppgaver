import random

kolonner = int(input("kolonner: "))
rader = int(input("rader: "))

l = [ #når du bruker en posisjon, skriv l[rad][kolonne]
    
]

for i in range(rader): #legger til en antall "rader" i rutenettet
    l.append([])

for i in range(kolonner): #fyller inn tall i hver rad og kolonne
    for i in range(rader):
        l[i].append(random.choice(range(11)))

for i in range(rader): #printer ut rutenettet i et ryddig-ish format
    print(l[i])

score = l[0][0]
x = 0
y = 0
pos = l[y][x]

def running(): #funksjon som sjekker om algoritmen har truffet det motsatte hjørnet enda
    if (x == kolonner-1) and (y == rader-1):
        return False
    else:
        return True

while running() == True: #gjentar løkka til motsatte hjørnet er truffet
    if x == kolonner-1: #sjekker om algortimen har truffet veggen til høyre enda
        y += 1
    elif y == rader-1: #sjekker om algoritmen har truffet bånn enda
        x += 1
    elif l[y][x+1] >= l[y+1][x]: #sjekker hvor den helst vil gå hen
        x += 1
    else:
        y += 1
    
    pos = l[y][x] #oppdaterer posisjon og score til neste iterasjon
    score += l[y][x]

print(pos, score)
