
l = []

def minmax(list):
    a = -10000000
    b = 100000000
    for i in range(len(list)):
        if list[i] > a:
            a = list[i]
    print("min: ",a)

    for i in range(len(list)):
        if list[i] < b:
            b = list[i]
    print("max: ",b)

#minmax(l)
a = 0
