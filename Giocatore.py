class Giocatore:
    def __init__(self, nickname: str, punteggio: int):
        self.nickname = nickname
        self.punteggio = int(punteggio)

    def __str__(self):
        return f"{self.nickname} {self.punteggio}"