from Domanda import Domanda
from Giocatore import Giocatore
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

def gestione_classifica(nomefile):
    classifica = []
    with open(nomefile, "r", encoding = 'utf-8') as file:
        parti = [line.strip().split() for line in file if line.strip().split()]
        for p in parti:
            if len(p) >= 2:
                nick = p[0]
                punti = p[1]
                classifica.append((nick, punti))
    #print(f"DEBUG Classifica: {classifica}")  # <--- TEST 2
    return classifica


def main():
    lista_domande_gioco = crea_lista_domande("domande.txt")
    if not lista_domande_gioco:
        print("Non ci sono domande nel file. Impossibile giocare.")
        return

    # Creazione di variabili utili per gli if e iterazioni
    lvl_attuale = 0
    # cerco lvl_max per gestire poi gli if
    lvl_max = max(d.lvl_difficolta for d in lista_domande_gioco)
    punteggio = 0
    stato_del_gioco = True

    # -GESTIONE del gioco
    print("----- TRIVIA GAME -----")
    while stato_del_gioco:
        domande_per_livello = [d for d in lista_domande_gioco if d.lvl_difficolta == lvl_attuale]
        domanda_proposta = random.choice(domande_per_livello)
        print(f"Livello: {domanda_proposta.lvl_difficolta}) {domanda_proposta.testo}")
        opzioni = domanda_proposta.genera_opzioni_mescolate()
        for i,opz in enumerate(opzioni,1):
            print(f"{i}. {opz}")
        scelta = int(input("Scegliere una risposta da 1 a 4: "))
        opzione_inserita = opzioni[scelta-1]

        if opzione_inserita == domanda_proposta.corretta:
            print("La risposta è corretta!")
            if lvl_attuale == lvl_max:
                print(f"Bravo! Hai risposto corettamente a tutte le domande! Il gioco è concluso.")
                stato_del_gioco = False
            else:
                lvl_attuale += 1
                punteggio += 1
        else:
            print(f"Hai sbagliato! la risposta corretta era: {domanda_proposta.corretta}.")
            stato_del_gioco = False

    # -GESTIONE Giocatore e classifica
    print(f"Hai totalizzato un punteggio di: {punteggio}")
    nickaname = input("Inserire il tuo Nickname:")


#main()
gestione_classifica('punti.txt')