from pylab import *

mA = 14       #masse A
mB = 1.5      #masse B
vA0 = 2       #startfart A
vB0 = -1      #startfart B


sA0 = 2     #startstrekning A
sB0 = 10    #startstrekning B

vA = (mA*vA0 - mB*vA0 + 2*mB*vB0)/(mA + mB) #fart A etter kollisjon
vB = vA + vA0 - vB0                         #fart B etter kollisjon
#print(vA, vB)

t = 0 #starttid
dt = 0.001 #delta tid

pos_A = [] #alle posisjonsverdier A
pos_B = [] #alle posisjonsverdier B
tid = [] #alle tidsverdier

sA = sA0 #strekning A
sB = sB0 #strekning B

while sA <= sB:
    pos_A.append(sA) 
    pos_B.append(sB)
    tid.append(t)

    sA += vA0 * dt
    sB += vB0 * dt
    t += dt

t_kollisjon = t

while t <= t_kollisjon*2:
    pos_A.append(sA)
    pos_B.append(sB)
    tid.append(t)
    sA += vA * dt
    sB += vB * dt
    t += dt

#print(pos_A, tid)

plot(tid, pos_A)
plot(tid, pos_B)
show()