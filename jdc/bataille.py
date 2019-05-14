#  bataille.py
# -*- coding: utf-8 -*-
#  Powered By EndMove
#  Copyright 2019 Jérémi_NIHART_-_classe5tc

import os
from random import randrange
from typing import List, Tuple, Dict

Carte = Tuple[int, int]
Jeu = List[Carte]
Labels = Dict[int, str]
Repertoire = List[str]
Joueurs = Dict[str, Jeu]
Donne = Dict[str, Carte]
Stats = Dict[str, int]

COULEURS = {0: "coeur", 1: "carreau", 2: "trèfle", 3: "pique"}

VALEURS = {0: "joker", 2: "deux", 3: "trois",
           4: "quatre", 5: "cinq", 6: "six", 7: "sept",
           8: "huit", 9: "neuf", 10: "dix", 11: "valet",
           12: "dame", 13: "roi", 14: "as"}


# ENDCOL powered by endmove.eu
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0;39m'


def construireJdC(vals: Labels = VALEURS, cols: Labels = COULEURS,
                  joker: bool = False):
    jeu = []
    for i in range(0, len(cols)):
        for y in range(0, len(vals)+1):
            carte = (y, i)
            if i == 0 and y == 0 and joker:
                for z in range(0, 4):
                    jeu.append(carte)
            elif y > 0:
                jeu.append(carte)
    return jeu


def battreCartes(jeu: Jeu):
    jeu_battu = []
    for i in range(0, len(jeu)):
        carte = randrange(0, len(jeu))
        jeu_battu.append(jeu[carte])
        jeu.remove(jeu[carte])
    return jeu_battu


def nomCarte(carte: Carte, vals: Labels = VALEURS,
             cols: Labels = COULEURS):
    return vals[carte[0]].capitalize() + " de " + cols[carte[1]].capitalize()


def tirerCarte(jeu: Jeu):
    nbr = len(jeu)
    if nbr < 1:
        return None
    else:
        carte = jeu[randrange(0, nbr)]
        jeu.remove(carte)
        return carte


def distribuerCartes(jeu: Jeu, joueurs: Repertoire):
    dico = {}
    jeu = battreCartes(jeu)
    nbr_joueurs = len(joueurs)
    nbr_jeu = len(jeu)
    for z in range(0, nbr_joueurs):
        dico[joueurs[z]] = []
    while nbr_jeu > 0:
        for y in range(0, nbr_joueurs):
            if nbr_jeu > 0:
                carte = tirerCarte(jeu)
                dico[joueurs[y]].append(carte)
                nbr_jeu -= 1
    return dico
   

def donnerCartes(joueurs: Joueurs):
    dico = {}
    keys_joueurs = list(joueurs.keys())
    for i in keys_joueurs:
        if len(joueurs[i]) > 0:
            dico[i] = []
            carte = joueurs[i][randrange(0, len(joueurs[i]))]
            dico[i].append(carte)
    return dico


#~ def comparerCartes(cartes: Donne):


#~ def ajouterGains(pli: Joueurs, gains: Jeu):


#~ def bataille(joueurs: Joueurs, gains: Jeu, first: bool = True):


#~ def jeuBataille(nbj: int, noms_joueurs: Repertoire):


if __name__ == "__main__":
    #print(battreCartes(construireJdC(VALEURS, COULEURS, True)))
    #print(construireJdC(VALEURS, COULEURS, True))
    #print(nomCarte((11, 1)))
    #print(tirerCarte([]))
    player = ["Jérémi", "Melanie", "Virginie", "Michel", "bernard", "mdr", "sweet"]
    carte = construireJdC(VALEURS, COULEURS, True)
    # ~ print(distribuerCartes(carte, player))
    print(donnerCartes(distribuerCartes(carte, player)))
    print(donnerCartes({'Jérémi': [(9, 3), (11, 3), (0, 0), (5, 0), (1, 1), (8, 0), (7, 2), (0, 0), (12, 1)], 'Melanie': [(1, 3), (12, 2), (3, 1), (10, 1), (12, 0), (11, 1), (4, 0), (9, 1), (5, 2)], 'Virginie': [(10, 0), (14, 2), (11, 0), (2, 1), (2, 0), (13, 1), (14, 1), (4, 2), (6, 1)], 'Michel': [(14, 3), (6, 3), (8, 1), (10, 2), (1, 2), (9, 2), (13, 2), (10, 3), (14, 0)], 'bernard': [(12, 3), (8, 3), (11, 2), (3, 2), (2, 2), (4, 3), (9, 0), (3, 3)], 'mdr': [(4, 1)], 'sweet': []}))
