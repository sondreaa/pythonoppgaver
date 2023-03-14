import turtle as t

t.hideturtle()
t.speed(10000)
t.penup()
t.goto(-350,100)
t.pendown()

#Koch Curve
def draw(n, l):
    if n == 0:
        t.forward(l)
    else:
        draw(n - 1, l)
        t.left(60)
        draw(n - 1, l)
        t.right(120)
        draw(n - 1, l)
        t.left(60)
        draw(n - 1, l)

def length(n):
    if n >= 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 6
    elif n == 3:
        return 20
    elif n == 2:
        return 50
    elif n == 1:
        return 150
    elif n == 0:
        return 400

n = 4
l = length(n)


for i in range(3): #makes a triangle of koch curves
    draw(n, l)
    t.right(120)

# draw(n,l)

t.done()