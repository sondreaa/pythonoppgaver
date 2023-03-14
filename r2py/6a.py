
def a(n):
    return 1/(n*(n+1))

s=0

for i in range(1, 6):
    s += a(i)
    print(round(s, 5))
