from pylab import *

def f(t):
    return 46.47 / (1 + 2.29 * (e**(-0.08*t)))

delta_x = 0.0001

def fder(a):
  return (f(a + delta_x) - f(a)) / delta_x

x_verdier = []
y_verdier = []


i=0
while i < 60:
    x_verdier.append(i)
    y_verdier.append(fder(i))

    i += 0.1

i=0
while i < 60:
    if fder(i-0.1)>fder(i):
        toppunkt = i
        print("x =",round(toppunkt, 2))
        print("y =",round(fder(toppunkt), 2))
        break
    i += 0.1

plot(x_verdier, y_verdier)
plot(toppunkt, fder(toppunkt), ".")
ylabel("Endring i Norges CO2-utslipp i millioner tonn")
xlabel("År etter 1959")

show()
