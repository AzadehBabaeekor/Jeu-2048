# 2048 — Implémentation en Python
Projet réalisé en Python reproduisant le jeu classique 2048 sur une grille 4 × 4 en ligne de commande.
## Aperçu technique
  Représentation du plateau : grille 4 × 4 modélisée sous forme de liste de listes de chaînes de caractères (Plateau = list[list[Case]]).
  Déplacements et fusions (pousser) : glissement et fusion des tuiles identiques dans les quatre directions (g : gauche, d : droite, h : haut, b : bas).
  Apparition aléatoire : génération d'une nouvelle tuile (2 avec 90 % de probabilité, 4 avec 10 % de probabilité) sur une case vide.
  Contrôle de la partie : validation des saisies, gestion des coups sans effet sur plateau plein et détection de l'absence de mouvement possible (jeu_possible).
## Exécution
Prérequis : Python 3.
'''bash
python3 2048.py
