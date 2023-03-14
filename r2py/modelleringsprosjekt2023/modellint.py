from pylab import *

def f(x):
    return 46.47 / (1 + 2.29 * (e**(-0.08*x)))

x_verdier = []
f_integral = []

def sum_f(n):
    Sum = 0
    for i in range(n):
        Sum += f(i)
    return(Sum)

for i in range(61):
    f_integral.append(sum_f(i))
    x_verdier.append(i)

print("sum etter 60 år:",round(f_integral[60], 1))



plot(x_verdier, f_integral)
ylabel("Summen av Norges CO2-utslipp i millioner tonn")
xlabel("År etter 1959")

show()

