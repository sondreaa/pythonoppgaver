
tekst = 'uten mat og drikke, duger helten ikke' 
vokaler = 'aeiouyæøå'
konsonanter = 'bcdfghjklmnpqrstvwxz'
v=[]
k=[]
for element in tekst:
    if element in vokaler:
        v.append(element)
    elif element in konsonanter:
        k.append(element)
print(v)
print(k)

