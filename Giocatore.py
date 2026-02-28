class Giocatore:
    def __init__(self, Nickname: str, punteggio: int):
        self.Nickname = Nickname
        self.punteggio = punteggio

    def __str__(self):
        return f"{self.nickname} {self.punteggio}"