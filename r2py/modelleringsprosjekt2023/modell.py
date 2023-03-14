from pylab import *
from scipy.optimize import curve_fit

all_data = loadtxt("co2_Norge.txt", delimiter = ",", usecols = (0,1))

år_all = all_data[:, 0]-1959
co2_all = all_data[:, 1]

def f(t, B, a, k):
    return B / (1 + a * (e**(-k*t)))

antakelser = [45, 100, 0]
[B, a, k] = curve_fit(f, år_all, co2_all, p0=antakelser)[0]
print("B = ", round(B, 2))
print("a = ", round(a, 2))
print("k = ", round(k, 2))


plot(år_all, co2_all, ".")
ylabel("Norges CO2-utslipp i millioner tonn")
xlabel("År etter 1959")
t = linspace(0, 2017-1959, 1000)
plot(t, f(t, B, a, k), "r")
show()