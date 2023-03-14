import requests
from requests import api

url = 'https://api.kanye.rest/'

"""
api_response = requests.get(url) #passer på at URL fungerer
kanyequote = api_response.json() #oversetter json-koden
kanyequote = kanyequote['quote'] #uten parantes og hermetegn
"""

def getkanyequote() :
    api_response = requests.get(url)
    kanye_quote = api_response.json()
    return kanye_quote['quote']


user_input = ''
while user_input != 'q' :
    print('Tast n for ny kanye quote')
    print('Tast s for å se alle lagrede sitater')
    print('Tast q for å avlsutte')

    user_input = input('>')

    if user_input == 'n' :
        quote = getkanyequote()
        print(quote)
        
        print('Tast l desom du ønsker å lagre sitatet. Alt annet tar deg tilbake til menyen')
       
        user_input = input('>')

        if user_input == 'l' :
            fil = open('quotes.txt' , 'a')
            fil.write(quote)
            fil.write('\n')
            fil.close()
        
    if user_input == 's':
        with open('quotes.txt' , 'r') as fil :
         print(fil.read())
