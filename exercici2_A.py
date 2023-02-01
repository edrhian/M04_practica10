aDiccionari = {'un': 1, 'dos': 2, 'tres': 3, 'quatre': 4, 'cinc': 5, 'sis': 6}

#Mostra per pantalla la longitut del diccionari
print("Longitut del diccionari: " + str(len(aDiccionari)))

#Mostra per pantallla tots els valors del diccionari (no les keys)
print(aDiccionari.values())

#Extreu l'últim item del diccionari, mostra aquest per pantalla i mostra altre vegada el diccionari sense l'últim item
print("Item extret: " + str(aDiccionari.popitem()))
print("Diccionari sense l'últim item: " + str(aDiccionari))
