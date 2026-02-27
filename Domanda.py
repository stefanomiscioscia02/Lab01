import random
class Domanda:
    def __init__(self, testo:str, lvl_difficolta: int, corretta: str, sbagliata: str ):
       self.testo = testo # riga 1
       self.lvl_difficolta = lvl_difficolta # riga 2
       self.corretta = corretta # riga 3
       self.sbagliata = sbagliata # riga 4 in poi