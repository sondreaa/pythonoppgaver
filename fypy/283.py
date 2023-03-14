import math

s1 = 0
ds1 = -0.01
v1 = 0
a1 = -3.3

s2 = 0
ds2 = 0.001
v2 = 0
a2 = 3.3

avstand = 0
while avstand < 0.26:
    v1 = math.sqrt(2*a1*s1)
    s1 += ds1

    v2 = math.sqrt(2*a2*s2)
    s2 += ds2

    avstand = abs(s1) - abs(s2)

    print(avstand, v1, v2)