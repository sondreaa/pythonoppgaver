a = 0
b = 24

n = 24

dx = (b - a)/n

summen = 0

def f(x):
    return(400 * 0.95**x)

for i in range(n):
    summen += f(a + (i - 1/2)*dx)*dx
    i += dx

print(round(summen,2))
