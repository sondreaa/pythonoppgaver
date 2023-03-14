

a = 0
b= 24

n = 1000000

dx = (b - a)/n

summen = 0

def f(x):
    return 400*(0.95**x)

for i in range(n):
    summen += f(i*dx)
    i += dx

summen = dx/2 * (f(a) + f(b) + 2 * summen)

print(round(summen, 2))