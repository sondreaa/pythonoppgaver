
a_1 = 300
k = 4/5
n = 1
sn = 0

while sn <= 1000:
    #sn = a_1 * (((k)**n - 1)/(k-1))
    sn += a_1 * 3**(n-1)
    n+=1

print(sn)
print(n)