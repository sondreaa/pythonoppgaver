"""
Roman Values:
1 = I, 5 = V, 10 = X
L = 50, C = 100, D = 500, M = 1000

4 = IV, 9 = IX
40 = XL, 90 = XC
400 = CD, 900 = CM
"""

def num_to_roman(number):
    roman = '' #streng med romertall
    while number > 0: #løkke som legger til flere bokstaver avhengig av hvor høyt tallet er
        if number >= 1000:
            roman += 'M'
            number -= 1000
        elif number >= 900:
            roman += 'CM'
            number -= 900
        elif number >= 500:
            roman += 'D'
            number -= 500
        elif number >= 400:
            roman += 'CD'
            number -= 400
        elif number >= 100:
            roman += 'C'
            number -= 100
        elif number >= 90:
            roman += 'XC'
            number -= 90
        elif number >= 50:
            roman += 'L'
            number -= 50
        elif number >= 40:
            roman += 'XL'
            number -= 40
        elif number >= 10:
            roman += 'X'
            number -= 10
        elif number >= 9:
            roman += 'IX'
            number -= 9
        elif number >= 5:
            roman += 'V'
            number -= 5
        elif number >= 4:
            roman += 'IV'
            number -= 4
        elif number >= 1:
            roman += 'I'
            number -= 1
        #print(roman)
        #print(f'Remaining: {number}')
    print(f'Roman Number: {roman}') #printer ut den ferdige strengen

def roman_to_num(roman):
    leng = len(roman) #sjekker hvor langt romertallet er
    ind = 0 #indeks: starter på 0, altså første plass i strengen
    num = 0
    while leng > ind: #løkke som fortsetter til siste plassen i strengen er nådd og omdannet

        if roman[ind] == 'M': #legger til 1000 hvis neste tall er M
            num += 1000
        
        elif roman[ind] == 'D': #legger til 500 hvis neste tall er D
            num += 500
        
        elif roman[ind] == 'C': #her må man passe på at tallet C ikke er en del av et tall med to bokstaver, som 900 (CM) eller 400(CD)
            if ind+1 == leng: #hvis det ikke er noen flere tall igjen, kan det jo ikke være en del av et lengre tall, da legger den bare til 100
                num += 100
            elif roman[ind+1] == 'M':
                num += 900
                ind += 1 #hopper over neste ledd så den ikke teller M to ganger
            elif roman[ind+1] == 'D':
                num += 400
                ind += 1
            else:
                num += 100
        
        elif roman[ind] == 'L':
            num += 50
        
        elif roman[ind] == 'X': #samme logikk som med C, bare med 10, 90 og 40
            if ind+1 == leng:
                num += 10
            elif roman[ind+1] == 'C':
                num += 90
                ind += 1                

            elif roman[ind+1] == 'L':
                num += 40
                ind += 1
            else:
                num += 10
        
        elif roman[ind] == 'V':
            num += 5
        
        elif roman[ind] == 'I': #samme logikk som med X, bare med 1, 9 og 4
            if ind+1 == leng:
                num += 1
            elif roman[ind+1] == 'X':
                num += 9
                ind += 1
            elif roman[ind+1] == 'V':
                num += 4
                ind += 1
            else:
                num += 1
        
        else: #hvis brukeres legger inn bokstaver som ikke er romertall
            num = 'error'
            

        ind += 1 #hopper til neste plass i strengen
    
    if num == 'error':
        print(num)
    else:
        print(f'Arabic Number: {num}')

def write_number():
    num = input('Convert Number: ') #ber om et tall fra brukeren
    
    return num

def convert():
    a = write_number() #ber om et tall fra brukeren
    r = False
    for i in range(10): #sjekker om inputet er et romertall eller arabisk tall
        if str(i) in a:
            r = True
            break
    if r: #hvis r er True, er det et arabisk tall som skal konverteres. da gjøres brukerens input om til en integer
        num_to_roman(int(a))
    else:
        roman_to_num(a) #hvis r er False, er det et romertall som skal konverteres. da fortsetter man med en streng.

print('\n Type in an Arabic or Roman number: \n')
convert()
