B = 2.18E-18
h = 6.63E-34
c = 3E8
synlig_lys = [400E-9, 750E-9]

fra_skall = int(input('Hvilket skall går elektronet fra? '))
til_skall = int(input('Hvilket skall går elektronet til? '))

print()

if fra_skall > til_skall:
    print('Atomet mister energi fordi et elektron faller nærmere kjernen.')
elif til_skall > fra_skall:
    print('Atomet får energi fordi et elektron kommer lenger unna kjernen.')



energiforskjell = abs((-B / fra_skall**2) - (-B / til_skall**2))
print(f'Energiforskjellen mellom skallene: {round(energiforskjell*1E18, 3)} aJ')

foton_frekvens = energiforskjell / h
print(f'Frekvensen til fotonet: {round(foton_frekvens / 1E12, 3)} THz')

foton_bolgelengde = c / foton_frekvens
print(f'Bølgelengden til fotonet: {round(foton_bolgelengde * 1E9, 3)} nm')

if foton_bolgelengde > synlig_lys[0] and foton_bolgelengde < synlig_lys[1]:
    print("Fotonet er innenfor området for synlig lys.")
else:
    print("Fotonet er ikke innenfor området for synlig lys.")

print()