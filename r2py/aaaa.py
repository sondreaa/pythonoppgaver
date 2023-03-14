a = 1       #nedre grense i intervallet
b = 5       #øvre grense i intervallet
n = 100     #antall rektangler
noyaktighet = 0.1

def f(x):
    return x**2 - 2*x + 2

venstresum = 0
hoyresum = 0
delta_x = (b - a)/n     #rektangelbredden

for i in range(n):  #i fra og med 0 til og med n-1
    venstresum += f(a + i*delta_x) * delta_x
    hoyresum += f(a + (i+1)*delta_x) * delta_x

diff = abs(venstresum-hoyresum)


while diff > noyaktighet:
    venstresum = 0
    hoyresum = 0
    n += 1

    for i in range(n):
        venstresum += f(a + i*delta_x) * delta_x
        hoyresum += f(a + (i+1)*delta_x) * delta_x

    


    print(round(hoyresum, 1))
    print(round(venstresum, 1))