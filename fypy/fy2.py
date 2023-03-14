from pylab import *

s = 0   #sett inn startposisjon
v = 0
t = 0
a = 5

dt = 0.1

v_verdier = []
s_verdier = []
t_verdier = []


#hvor mange iterasjoner vil vi ha?

while t <= 50:
    v += a*dt
    s += v*dt
    t += dt
    v_verdier.append(v)
    s_verdier.append(s)
    t_verdier.append(t)
while t <= 120:
    a += 18/70 * dt
    v += a*dt
    s += v*dt
    t += dt
    v_verdier.append(v)
    s_verdier.append(s)
    t_verdier.append(t)

plot(t_verdier, s_verdier)
title('Posisjon som funksjon av tid')
xlabel('$t$ [s]')
ylabel('$s$ [m]')
grid()

show()