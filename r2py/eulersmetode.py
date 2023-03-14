from pylab import *

a = 0
b = 50
n = 10000
delta_t = (b-a)/n
N0 = 6500

def f(x): #ikke en del av metoden, brukes bare for å sammenligne med 'fasiten'
    return 10071*e**(-0.007*t) - 3571

def Nder(N):
    return -0.007*N - 25

N = zeros(n)

N[0] = N0

for i in range(n - 1):
    N[i+1] = N[i] + Nder(N[i]) * delta_t

t = linspace(a, b, n)

plot(t, N)
plot(t, f(i)) #ikke en del av metoden
xlabel("Tid (år)")
ylabel("Innbyggertall")

show()
