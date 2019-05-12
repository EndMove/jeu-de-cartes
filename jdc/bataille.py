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


#~ def donnnerCartes(joueurs: Joueurs):


#~ def comparerCartes(cartes: Donne):


#~ def ajouterGains(pli: Joueurs, gains: Jeu):


#~ def bataille(joueurs: Joueurs, gains: Jeu, first: bool = True):


#~ def jeuBataille(nbj: int, noms_joueurs: Repertoire):


if __name__ == "__main__":
    #print(battreCartes(construireJdC(VALEURS, COULEURS, True)))
    #print(construireJdC(VALEURS, COULEURS, True))
    #print(nomCarte((11, 1)))
    #print(tirerCarte([]))
