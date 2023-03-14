import time
import random
import requests
from bs4 import BeautifulSoup

def hentord():
    response=requests.get("https://www.korrekturavdelingen.no/ord-uttrykk-frekvensordliste-500-vanligste-norsk.htm")
    soup=BeautifulSoup(response.text , "html.parser")
    fil=open("ordliste.txt", "a")
    for item in soup.find_all("tr"):
        rad = item.find_all("td") # en liste med to elementer, der ord ligger på plass 2 (indeks 1)
        ord=rad[1].text
        if len(ord) >= 4:
            fil.write(ord)
            fil.write("\n")
    fil.close()

def speed_type_test() : 
    fil=open("ordliste.txt", "r")
    alt=fil.read()
    ord=list(map(str, alt.split()))
    skriv=random.choice(ord)

    start="start"
    print("skriv 'start' for å starte. alt annet vil avslutte programmet.")
    start=input()
    if start == "start":
        wpm=0
        feil=0
        rett=0
        starttid=time.time()
        play=True
        while play==True:
            if starttid + 60 < time.time():
                play=False
            else:
                skriv=random.choice(ord)
                print("ordet ditt:",skriv)
                deg=input("skriv her: ")
                if deg == skriv:
                    print("riktig!")
                    rett=rett+1
                else:
                    print("feil!")
                    feil=feil+1
        wpm=rett
        print("ord per minutt:",wpm)
        'print("riktige:",rett)' #når spillet bare varer 60 sek er denne litt unødvendig
        print("skrivefeil:",feil)
    else:
        print("hade bra!")

    fil.close()

speed_type_test()
#hentord()

