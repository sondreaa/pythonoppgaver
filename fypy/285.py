import math

g = 9.81

a = g

m = 1.3
k = 0.24

s = 0 
v = 0
a = 0.1

tyngde = m*g
luftmotstand = k * (v**2)

ds = 0.0001
s_slutt = 4.4


while s < s_slutt:
    v = math.sqrt(2*a*s)
    
    luftmotstand = k * (v**2)
    if luftmotstand < tyngde:
        a = (tyngde-luftmotstand)/m

    s += ds


    print(round(v, 3), round(s, 3))
