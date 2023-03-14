from pylab import *
g = 9.81

s = 0   #sett inn startposisjon
v = 0
t = 0
a = 0.1

dt = 0.001
t_slutt = 5

v_verdier = []
s_verdier = []
t_verdier = []


#hvor mange iterasjoner vil vi ha?

while t < t_slutt:
    a += a*t
    v += a*dt
    s += v*dt
    t += dt
    v_verdier.append(v)
    s_verdier.append(s)
    t_verdier.append(t)

print(t,s)


plot(t_verdier, s_verdier)
title('Posisjon som funksjon av tid')
xlabel('$t$ [s]')
ylabel('$s$ [m]')
grid()

#show()