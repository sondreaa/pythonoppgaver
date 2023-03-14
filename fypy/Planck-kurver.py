import math
from pylab import *
h=6.63E-34
k=1.38E-23
c=3E8
a=0.0029

def ulam(l,T):
    return 2*math.pi*h*c**2/l**5  * 1/(math.e**(h*c/l/k/T)-1)

#Her kan du sett inn temperaturene til objektene, adskilt av komma. Noe annet trenger du ikke røre.
T=[5090,6500,3000]


antall_T=len(T)

lambdas=linspace(1E-9,2000E-9, 500)
antall_lam=len(lambdas)
lambdas_con=lambdas*1E9
uval=np.zeros((antall_T, antall_lam))

for t in range(antall_T):
    for lamb in range(antall_lam):
        uval[t,lamb]=ulam(lambdas[lamb], T[t])

farger=np.array([[0,'purple'],
                [450,'blue'],
                [495,'green'],
                [570,'yellow'],
                [590,'orange'],
                [620,'red']])

fig=plt.figure(figsize=(8,4.5))
opa = 0.3
axvspan(620,750, alpha=opa, facecolor='red')
axvspan(590,620, alpha=opa, facecolor='orange')
axvspan(570,590, alpha=opa, facecolor='yellow')
axvspan(495, 570, alpha=opa, facecolor='green')
axvspan(450,495, alpha=opa, facecolor='blue')    
axvspan(380,450, alpha=opa, facecolor='purple')
for i in range(antall_T):
    l_topp=int(floor(a/T[i]*10**9))
    for i2 in range(6):
        if l_topp>int(farger[i2][0]):
            farge=farger[i2][1]
    tilplot=uval[i]/10**12
    if antall_T==1:
        plt.fill_between(lambdas_con, tilplot,color=farge, alpha=0.5,label='U')
    plot(lambdas_con, tilplot, color=farge,label=f'$T$ = {T[i]} K, $\u03BB_t$ = {l_topp} nm ')
    tekst=f'$T$ = {T[i]} K, $\u03BB_t$ = {l_topp} nm '
    legend()
xlim(0,2000)
ylabel('$u$ / (kW/m\u00B2nm')
xlabel('$\u03BB$ / nm')
grid()
# filnavn= 'Planck-kurve'+tekst+'.png'
# plt.savefig(filnavn,dpi=800)
show()