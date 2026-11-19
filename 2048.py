from typing import List
import random
Case = str
# les elements de Case sont soit " " soit les puissance naturelles de 2 ('2', '4', '8', ...)
Plateau = List[List[Case]]
# les elements de Plateau sont des matrices 4*4
def plateau_2048()->Plateau:
    """Prend rien en entree et envoie un plateau de jeu initial pour jeu 2048. Au depart on aura un 2 et un 4 dans notre espace"""
    res:PlateauT= [[' '  for i in range (4)] for j in range (4)]
    i:int= random.randrange(0,4)
    j:int= random.randrange(0,4)
    i1:int= random.randrange(0,4)
    j1:int= random.randrange(0,4)
    while i1==i and j1==j:
        i1= random.randrange(0,4)
        j1= random.randrange(0,4)
    res[i][j]='2'
    res[i1][j1]=str(random.choice([2,4]))
    return res
#P1:Plateau= [['4', ' ', ' ', ' '], [' ', ' ', '2', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

def dessine_plateau2048(p:Plateau)->str:
    """renvoie une chaine de caractere correspondant a un affichage du plateau de jeu 2048 avec les bords."""
    i:int=0
    j:int
    s:str=''
    sep:str='+-----+-----+-----+-----+\n'
    while i<4:
        s=s+sep
        for j in range(4): 
            s=s+ f'| {p[i][j]:^4}'
        s=s +'|\n'
        i=i+1
    s=s+ sep
    return s
#print(dessine_plateau2048(P1))

def vide (p:Plateau, i:int, j:int)-> bool:
    """Precondition: 4>i>=0 and 4>j>=0
    verifie si la case de coordonnees (i, j) du plateau est vide."""
    return p[i][j]== ' '

def plein2048(p:Plateau)->bool:
    """Verifie si notre plateau est plein"""
    i:int
    j:int
    for i in range(4):
        for j in range(4):
            if vide(p, i, j):
                return False
    return True
#assert not plein2048(P1)

def jeu_possible(p: Plateau) -> bool:
    "Vérifie si c'est possible de continuer de jouer notre jeu en glissant le plateu ou non (GAME OVER!)"
    if not plein2048(p):
        return True
    for j in range(4):
        for i in range(4):
            if (j+1<4 and p[i][j]==p[i][j+1]) or (i+1<4 and p[i][j]==p[i+1][j]):
                return True
    return False

def pousser(p:Plateau, dir:str) ->Plateau:
    "Pousse et fusionne les cases du plateau dans la direction dir et renvoie le plateau mis à jour."
    if dir=='g':
        for i in range(4):
            ligne=[]
            for j in range(4):
                if not vide(p, i, j):
                    ligne.append(p[i][j])
            j=0
            while j<len(ligne)-1:
                if ligne[j]==ligne[j+1]:
                    ligne[j]= str(2*int(ligne[j]))
                    ligne.pop(j+1)
                j=j+1
            while(len(ligne)<4):
                ligne.append(' ')
            for j in range(4):
                p[i][j]=ligne[j]
    elif dir == 'd':
        for i in range (4):
            ligne=[]
            for j in range(3, -1, -1):
                if not vide(p,i,j):
                    ligne.append(p[i][j])
            j=0
            while j<len(ligne) - 1:
                if ligne[j]==ligne[j+1]:
                    ligne[j]= str(2*int(ligne[j]))
                    ligne.pop(j+1)
                j=j+1
            while len(ligne)<4 :
                ligne.append(' ')
            for k in range(4):
                p[i][3-k]= ligne[k]
    elif dir == 'h':
        for j in range(4):
            ligne = []
            for i in range(4):
                if not vide(p, i, j):
                    ligne.append(p[i][j])
            k = 0
            while k < len(ligne) - 1:
                if ligne[k] == ligne[k + 1]:
                    ligne[k] = str(2 * int(ligne[k]))
                    ligne.pop(k + 1)
                k = k + 1
            while len(ligne) < 4:
                ligne.append(' ')
            for i in range(4):
                p[i][j] = ligne[i]

    elif dir == 'b':
        for j in range(4):
            ligne = []
            for i in range(3, -1, -1):
                if not vide(p, i, j):
                    ligne.append(p[i][j])
            k = 0
            while k < len(ligne) - 1:
                if ligne[k] == ligne[k + 1]:
                    ligne[k] = str(2 * int(ligne[k]))
                    ligne.pop(k + 1)
                k = k + 1
            while len(ligne) < 4:
                ligne.append(' ')
            for idx in range(4):
                p[3 - idx][j] = ligne[idx]
    return p
                
def Jouer() -> None:
    "Correspond bien au jeu classique 2048. Vous pouvez choisir la direction de pousser les nombres (h pour haut, b pour bas, g pour gauche et d pour droite) et le code pousse les cases dans la direction souhaitée et fait apparaître de façon aléatoire un '2' ou un '4' dans un des cas de notre plateau."
    p: Plateau= plateau_2048()
    while jeu_possible(p):
        print(dessine_plateau2048(p))
        direction:str=(input("Choisissez la direction ('h' pour haut, 'b' pour bas, 'g' pour gauche et 'd' pour droite): "))
        while (direction!='g' and direction!='d' and direction!='b' and direction!='h'):
            direction:str=(input("Choisissez impérativement entre 'h' ou 'b' ou 'd' ou 'g':"))
        p= pousser(p, direction)
        if not jeu_possible(p):
            print(dessine_plateau2048(p))
            print("Vous avez perdu! Il ne reste plus de place dans le plateau.")
            return
        while (plein2048(p) and jeu_possible(p)):
            direction:str=input("Coup ilégal! Choisissez une autre direction: ")
            while (direction!='g' and direction!='d' and direction!='b' and direction!='h'):
                direction:str=(input("Choisissez impérativement entre 'h' ou 'b' ou 'd' ou 'g':"))
            pousser(p,direction)
        if not plein2048(p):
            i: int=random.randrange(0,4)
            j: int=random.randrange(0,4)
            while (not vide(p,i,j)):
                i: int=random.randrange(0,4)
                j: int=random.randrange(0,4)
            k:int
            if (random.random() < 0.9):
                k=2
            else:
                k=4
            p[i][j]= str(k)
        if not jeu_possible(p):
            print(dessine_plateau2048(p))
            print("Vous avez perdu! Il ne reste plus de place dans le plateu.")
            return
Jouer()
        


    
