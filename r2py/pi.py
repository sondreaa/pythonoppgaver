
def p(n):
    return (-1)**n / (2*n+1)

s = 0
end = 1000000
for i in range(end):
    s += p(i)

print(4*s)

