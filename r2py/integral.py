n = 5

def f(x):
    return 2*x + 1

a = 0
b = 5
areal = 0
bredde = (b - a)/n

for i in range(n):
    hoyde = f(0 + i*bredde)
    areal = areal + hoyde*bredde

    print(areal)