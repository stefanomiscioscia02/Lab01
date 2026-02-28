import random
class Domanda:
    def __init__(self, testo:str, lvl_difficolta: int, corretta: str, sbagliata: str ):
       self.testo = testo # riga 1
       self.lvl_difficolta = int(lvl_difficolta) # riga 2
       self.corretta = corretta # riga 3
       self.sbagliata = sbagliata # riga 4 in poi

    def genera_opzioni_mescolate(self):
        # Restituisce una lista di risposte (corretta + sbagliate) mescolate
        risposte = [self.corretta] + self.sbagliata
        random.shuffle(risposte)
        return risposte