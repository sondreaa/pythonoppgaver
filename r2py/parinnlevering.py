
#opppgave 1

def a(n): #definerer eksplisitt formel for lønn per dag
    return 2 ** (n - 1)

lønn = 0
for i in range(1, 21): #regner ut sum etter 20 dager
    lønn += a(i)

print("Oppgave 1: Etter 20 dager vil du tjene",lønn,"kr")


#oppgave 2

print("Oppgave 2a:")

def b(n): #definerer eksplisitt formel for rekka
    return 1 / (1+n)**2

for i in range(1, 20): #printer ut alle tallene i rekka
    print(b(i))

print("Oppgave 2b:")
s = 0
for i in range(1, 20): #regner ut summen av alle tallene i rekka
    s += b(i)
    print(s)


