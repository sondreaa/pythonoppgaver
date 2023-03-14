import math

op = input("hvilken operasjon? (+, -, *, /, ^, ln) ")

if op != "ln":
    tall1 = int(input("tall1: "))
    tall2 = int(input("tall2: "))
else:
    tall = int(input("tall: "))
if op == "/" or op == "ln":
    komma = int(input("hvor mange desimaler: "))

def pluss():
    print(tall1,"+",tall2,"=",tall1 + tall2)

def minus():
    print(tall1,"-",tall2,"=",tall1 - tall2)
    print(tall2,"-",tall1,"=",tall2 - tall1)

def gange():
    print(tall1,"*",tall2,"=",tall1 * tall2)

def dele():
    print(tall1,"/",tall2,"=",round((tall1 / tall2), komma))
    print(tall2,"/",tall1,"=",round((tall2 / tall1), komma))

def eksponent():
    print(tall1,"^",tall2,"=",tall1 ** tall2)
    print(tall2,"^",tall1,"=",tall2 ** tall1)

def viten():
    a = str(round((math.log(tall)), komma))
    print(a)
    print("vitenskapelig notasjon: e^"+a)

if op == "+":
    pluss()
if op == "-":
    minus()
if op == "*":
    gange()
if op == "/":
    dele()
if op == "^":
    eksponent()
if op == "ln":
    viten()