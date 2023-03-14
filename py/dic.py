from random import randint

# temp = {'oslo':7, 'bergen':5, 'trondheim':2, 'kristiansand':10}

# for key in temp:
#     print(key, temp[key])

# a = input('legg til by: ')
# b = int(input('legg til temp: '))

# temp[a] = b

# print(a, temp[a])



# person = {'name': 'Alex', 'age': 17, 'drivers license': False, 'height': 175, 'sex': 'non-binary'} 

# print(person['age'], person['height'])

# a = input('hva ønsker du å vite om? ')
# print(person[a])


# aksjekurs = {
# 'EQNR': [233.90, 'equinor', 3700000], 
# 'DNB': [210.50, 'dnb bank asa', 382664], 
# 'NHY': [71.04, 'norsk hydro', 3300000], 
# 'PMG': [18.52, 'play magnus', 26063]
# } 

# print(aksjekurs['PMG'][1],aksjekurs['PMG'][0])

# def navn(key):
#     a = aksjekurs[key][1].capitalize()
#     return a

# for key in aksjekurs:
#     print(navn(key))


# konti = {}

# def legg_til_konti(navn, saldo):
#     konti[navn] = saldo
#     print(konti)

# def oppdater_saldo(nokkel, verdi):
#     if nokkel in konti:
#         konti[nokkel] = verdi
#         print(konti)
#     else:
#         print('404')

# def banktjeneste():
#     start = 'a'
#     while start == 'a' or start == 'o':
#         start = input('hva vil du gjøre? (a/o): ')
        
#         if start == 'a':
#             a = input('navn: ')
#             b = int(input('saldo: '))
#             legg_til_konti(a, b)
#         elif start == 'o':
#             a = input('nokkel: ')
#             b = int(input('ny saldo: '))
#             oppdater_saldo(a, b)

#         print(konti)
    
#     print('avslutter')

# banktjeneste()

# def lis():
#     l = []
#     for i in range(5):
#         l.append(randint(0, 10))
#     return l

# print(lis())


# dic = {'tall': 12, 'streng':'hei', 'liste':[1, 2, 3, 'hei']}

# a = dic['tall']

# b = dic['liste'][2]

# dic['nynøkkel'] = 'sondre'

# dic['tall'] = 10
