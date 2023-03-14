import numpy as np

a = 0 #start
b= 20 #slutt

n = 10 #antall trapeser

dx = (b - a)/n

sum = 0

def f(x): #funksjonen som skal integreres
    return 5*np.sin(0.1*x)

for i in range(n - 1): #finner summen
    sum += f(i*dx)
    i += dx

sum = dx/2 * (f(a) + f(b) + 2 * sum) #det endelige integralet

print(round(sum, 2))
