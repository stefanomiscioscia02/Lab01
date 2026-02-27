from Domanda import Domanda

import random

def crea_lista_domande(nomefile):
    lista_domande = []
    with open(nomefile, "r", encoding = 'utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
        for i in range(0, len(lines), 6): # (start, stop, step) -> step perchè 6 righe per domanda
            testo = lines[i]
            lvl_difficolta = lines[i+1]
            corretta = lines[i+2]
            sbagliata = [lines[i+3], lines[i+4], lines[i+5]]

            dTemp = Domanda(testo, lvl_difficolta, corretta, sbagliata)
            lista_domande.append(dTemp)
    return lista_domande
