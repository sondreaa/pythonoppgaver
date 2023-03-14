from math import sqrt
from pylab import *
import numpy as np
'''
p er bevart

MA * VA1 = Mv2
va1 = Mv2/MA


1/2 * v2**2 = g * h
v2 = sqrt(2gh)

bevegelsesmengde
1: pa1 = mava1 = p1
2: p2 = mv2

energi
2: e2 = ep2 + ek2 = ek2 = 1/2mv2^2
3: e3 = ep3 + ek3 = ep3 = mgh
'''
avstand_fra_blink = 1

#målinger
m_A = 0.462/1000
m_B = 47.66/1000
Mtotal = m_A + m_B

h = 0.12
g = 9.81

v2 = sqrt(2*g*h)
print("v2 = ",v2)

va1 = (Mtotal*v2)/m_A
print("va1 = ",va1)

def fart(h):
    return sqrt(Mtotal*(2*h*g))/m_A

høyder = np.arange(0,1,0.01)
farter = fart(høyder)

plot(høyder,farter)
grid()
xlabel('Høyde i meter')
ylabel('utgangshastighet i m/s')
title('utgangshastighet for luftgeværkule som funksjon av høyde')


show()