#Funcio sense parametres, demana el teu any de naixement i retorna la teva edat segons aquesta
def calcEdat():
    anyNaixement = input("Introdueix l'any que vas néixer: ")
    Edat = 2023 - int(anyNaixement)
    return Edat

