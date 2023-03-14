"""
Lag en enkel nøstet if-setning.
Altså en if-setning inni en if-setning.
Den skal først sjekke og en variabel er større enn et tall
og så sjekke om variabelen modulo 2 (%) blir akkurat 1. 
Dersom det er sant skal det printes «Oddetall!» 
Dersom det ikke er sant skal det printes «Partall!» 
"""

tall = 0
variabel = int(input("tall: "))

if variabel > tall:
    print("positivt")
    if variabel%2 != 0:
        print("oddetall")
    else:
        print("partall")
else:
    print("negativt")
    if variabel%2 != 0:
        print("oddetall")
    else:
        print("partall")
