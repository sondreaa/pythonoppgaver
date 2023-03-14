import requests
from bs4 import BeautifulSoup

def hentord():
    response=requests.get("https://www.korrekturavdelingen.no/ord-uttrykk-frekvensordliste-500-vanligste-norsk.htm")
    soup=BeautifulSoup(response.text , "html.parser")
    fil=open("ordliste.txt", "a")
    for item in soup.find_all("tr"):
        rad = item.find_all("td") # en liste med to elementer, der ord ligger på plass 2 (indeks 1)
        ord=rad[1].text
        fil.write(ord)
        fil.write("\n")
    fil.close()
