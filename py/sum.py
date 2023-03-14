
tall = [4, 5, 2, 3, 8, 6, 5, 6, 9, 2, 1]

def list_sum(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + list_sum(liste[1:])

print(sum(tall))
