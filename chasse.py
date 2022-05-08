########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/Elta305/Projet-Chasse
########################

# Import des librairies

import tkinter as tk
import random as rd
from math import sqrt
import ast


########################

# Variables globales

HAUTEUR = 810
LARGEUR = 810
N = 30
PROIES = []
PREDATEURS = []
FPRO = 3
MIAM = 5
EREPRO = 17

MODE_PRE = 1
INTERRUPTION = False
ITERATIONS = 0

####################

# Fonctions

# Affichage

def init_affichage():
    """ Affiche la simulation dans un canvas tkinter """
    hauteur_case = HAUTEUR // N
    largeur_case = LARGEUR // N

    canvas.delete('all')
    for i in range(len(PROIES)):
        x = PROIES[i][-1][0]
        y = PROIES[i][-1][1]
        canvas.create_rectangle((x*largeur_case), (y*hauteur_case), (x*largeur_case+largeur_case), (y*hauteur_case+hauteur_case), fill="black")
    for j in range(len(PREDATEURS)):
        x = PREDATEURS[j][-1][0]
        y = PREDATEURS[j][-1][1]
        canvas.create_rectangle((x*largeur_case), (y*hauteur_case), (x*largeur_case+largeur_case), (y*hauteur_case+hauteur_case), fill="red")

# Création des proies et des prédateurs

def creer_proies(Apro=7, repro=0, x=15, y=15):
    """ int, int, int, int
        Crée une proie
    """
    a = 0
    if len(PROIES) >= 1:
        a = PROIES[-1][0] + 1
    PROIES.append([a, Apro, repro, [x, y]])

def creer_predateurs(Apre=25, Epre=14, cible=[], x=15, y=15):
    """ int, int, list, int, int
        Crée un prédateur
    """
    a = 0
    if len(PREDATEURS) >= 1:
        a = PREDATEURS[-1][0] + 1
    PREDATEURS.append([a, Apre, Epre, cible, [x, y]])

def creer_n_proies(Npro=5):
    """ int
        Crée n proies
    """
    for i in range(Npro):
        x = rd.randint(0, 29)
        y = rd.randint(0, 29)
        while verif_cases(x, y) is False:
            x = rd.randint(0, 29)
            y = rd.randint(0, 29)
        creer_proies(x = x, y = y)

def creer_n_predateurs(Npro=2):
    """ int
        Crée n prédateurs
    """
    for i in range(Npro):
        x = rd.randint(0, 29)
        y = rd.randint(0, 29)
        while verif_cases(x, y) is False:
            x = rd.randint(0, 29)
            y = rd.randint(0, 29)
        creer_predateurs(x = x, y = y)
# Mouvements généraux

def simulation():
    deplacement_proies()
    deplacement_predateurs()
    init_affichage()
    manger()
    #age()
    #creer_n_proies(1)
    if len(PREDATEURS) == 0:
        return print("Les proies ont gagné !")
    elif len(PROIES) == 0:
        return print("Les prédateurs ont gagné !")
    elif INTERRUPTION == False:
        root.after(150, simulation)

def verif_mouv(pr):
    """ list -> list
        Renvoie une liste contenant toutes les valeurs qui représentent des cases libres
    """
    nb = [0, 1, 2, 3, 4, 5, 6, 7]
    for j in range(8):
        if j == 0:
            x, y = pr[-1][0]-1, pr[-1][1]-1
        if j == 1:
            x, y = pr[-1][0], pr[-1][1]-1
        if j == 2:
            x, y = pr[-1][0]+1, pr[-1][1]-1
        if j == 3:
            x, y = pr[-1][0]-1, pr[-1][1]
        if j == 4:
            x, y = pr[-1][0]+1, pr[-1][1]
        if j == 5:
            x, y = pr[-1][0]-1, pr[-1][1]+1
        if j == 6:
            x, y = pr[-1][0], pr[-1][1]+1
        if j == 7:
            x, y = pr[-1][0]+1, pr[-1][1]+1
        if verif_cases(x, y) is False:
            nb.remove(j)
    return nb

def verif_cases(x, y):
    if x <= 0 or x >= 29 or y <= 0 or y >= 29:
        return False
    for i in range(len(PROIES)):
        if x == PROIES[i][-1][0] and y == PROIES[i][-1][1]:
            return False
    for j in range(len(PREDATEURS)):
        if x == PREDATEURS[j][-1][0] and y == PREDATEURS[j][-1][1]:
            return False
    return True

# Proies

def deplacement_proies():
    for i in range(len(PROIES)):
        # Vérification des cases libres
        new_coords = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        nb = mouvements(PROIES[i])
        # Déplacement
        if len(nb) != 0:
            dir = rd.choice(nb)
            PROIES[i][-1][0], PROIES[i][-1][1] = PROIES[i][-1][0]+new_coords[dir][0], PROIES[i][-1][1]+new_coords[dir][1]

def age():
    i = 0
    while i < len(PROIES):
        if PROIES[i][-2] == 0:
            PROIES.remove(PROIES[i])
        else:
            PROIES[i][-2] -= 1
            i += 1

def reproduction(proie):
    """ list
        Reproduit les proies entre elles
    """
    nb = [0, 1, 2, 3, 4, 5, 6, 7]
    nb2 = verif_mouv(proie)
    new_coords = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    k = 0
    while k < len(nb):
        if nb[k] not in nb2:
            nb.remove(nb[k])
            k -= 1
        k += 1
    for j in range(len(PROIES)):
        if proie[0] != PROIES[j][0] and proie[-2] != 1 and PROIES[j][-2] != 1 and nb != []:
            if ((proie[-1][0] == PROIES[j][-1][0]-1 and proie[-1][1] == PROIES[j][-1][1]-1)
            or (proie[-1][0] == PROIES[j][-1][0] and proie[-1][1] == PROIES[j][-1][1]-1) 
            or (proie[-1][0] == PROIES[j][-1][0]+1 and proie[-1][1] == PROIES[j][-1][1]-1)
            or (proie[-1][0] == PROIES[j][-1][0]-1 and proie[-1][1] == PROIES[j][-1][1]) 
            or (proie[-1][0] == PROIES[j][-1][0]+1 and proie[-1][1] == PROIES[j][-1][1])
            or (proie[-1][0] == PROIES[j][-1][0]-1 and proie[-1][1] == PROIES[j][-1][1]+1) 
            or (proie[-1][0] == PROIES[j][-1][0] and proie[-1][1] == PROIES[j][-1][1]+1)
            or (proie[-1][0] == PROIES[j][-1][0]+1 and proie[-1][1] == PROIES[j][-1][1]+1)):
                a = rd.choice(nb)
                reprod_case(a, proie, new_coords)
                proie[-2], PROIES[j][-2] = 1, 1

def verif_cases(x, y):
    if x <= 0 or x >= 29 or y <= 0 or y >= 29:
        return False
    for i in range(len(PROIES)):
        if x == PROIES[i][-1][0] and y == PROIES[i][-1][1]:
            return False
    return True

# Prédateurs

def deplacement_predateurs():
    for i in range(len(PREDATEURS)):
        distance = 1000
        cible = []
        for j in range(len(PROIES)):
            distancetmp = sqrt((PREDATEURS[i][-1][0] - PROIES[j][-1][0])**2 + (PREDATEURS[i][-1][1] - PROIES[j][-1][1])**2)
            if distancetmp <= distance:
                distance = distancetmp
                if MODE_PRE == 0:
                    cible = PROIES[j][-1]
                else:
                    if distance <= 12:
                        cible = PROIES[j][-1]
            PREDATEURS[i][-2] = cible
        if cible == []:
            new_coords = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
            nb = mouvements(PREDATEURS[i])
            if len(nb) == 0:
                return
            dir = rd.choice(nb)
            PREDATEURS[i][-1][0], PREDATEURS[i][-1][1] = PREDATEURS[i][-1][0]+new_coords[dir][0], PREDATEURS[i][-1][1]+new_coords[dir][1]
        else:
            mouvement_predateur(PREDATEURS[i])

def mouvement_predateur(pr):
    if pr[-1][0] > pr[-2][0] and pr[-1][1] > pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]-1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]+1

    elif pr[-1][0] < pr[-2][0] and pr[-1][1] == pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]

    elif pr[-1][0] > pr[-2][0] and pr[-1][1] < pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]+1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]-1

    elif pr[-1][0] == pr[-2][0] and pr[-1][1] > pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0], pr[-1][1]-1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0], pr[-1][1]+1

    elif pr[-1][0] == pr[-2][0] and pr[-1][1] < pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0], pr[-1][1]+1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0], pr[-1][1]-1

    elif pr[-1][0] < pr[-2][0] and pr[-1][1] > pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]-1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]+1

    elif pr[-1][0] > pr[-2][0] and pr[-1][1] == pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]

    elif pr[-1][0] < pr[-2][0] and pr[-1][1] < pr[-2][1]:
        pr[-1][0], pr[-1][1] = pr[-1][0]+1, pr[-1][1]+1
        for i in range(len(PREDATEURS)):
            if PREDATEURS[i][0] != pr[0] and PREDATEURS[i][-1] == pr[-1]:
                pr[-1][0], pr[-1][1] = pr[-1][0]-1, pr[-1][1]-1

def manger():
    """ Gère la satiété des prédateurs et supprime les proies de la liste PROIES si elles sont sur la même case que les prédateurs """
    for i in range(len(PREDATEURS)):
        PREDATEURS[i][-3] -= 1
        for j in range(len(PROIES)):
            if PREDATEURS[i][-1] == PROIES[j][-1]:
                PREDATEURS[i][-3] += 5
                PROIES.remove(PROIES[j])
                break
        if PREDATEURS[i][-3] == 0:
            PREDATEURS.remove(PREDATEURS[i])
            break

def repro_pred(predateur):
    """ list
        Crée un prédateur
    """
    if predateur[-3] >= EREPRO:
        # predateur[-3] = 14 car Epro = 14
        predateur[-3] = 14
        creer_n_predateurs(1)

# Divers

def superpredateurs():
    """ Change le mode des prédateurs """
    global MODE_PRE
    if MODE_PRE == 0:
        bouton_pre['text'] = "Mode Super Predateurs"
        bouton_pre['bg'] = "red3"
        MODE_PRE = 1
    else:
        bouton_pre['text'] = "Mode Normal"
        bouton_pre['bg'] = "SystemButtonFace"
        MODE_PRE = 0

def sauvegarder(fichier="saves.txt"):
    """ file
        Sauvegarde la configuration à la fin du fichier saves.txt
    """
    sauvegardes = open(fichier, "a")
    sauvegardes.write(str([PROIES, PREDATEURS]) + "\n")
    sauvegardes.close()

def charger(fichier="saves.txt"):
    """ file
        Charge la sauvegarde associée au numéro donnée
    """
    global PROIES, PREDATEURS
    ligne = int(input("Entrez le numéro de la sauvegarde : "))
    sauvegardes = open(fichier, "r")
    save = sauvegardes.readlines()
    if ligne >= len(save)+1 or ligne <= 0:
        return print("Sauvegarde inexistante !")
    save = save[ligne-1]
    save = ast.literal_eval(save)
    PROIES, PREDATEURS = save[0], save[1]
    label["text"] = "Sauvegarde " + str(ligne) + " chargée !"
    bouton_init["text"] = "Jouer"
    init_affichage()
    sauvegardes.close()

def interruption():
    """ Interrompt la stabilisation """
    global INTERRUPTION
    INTERRUPTION = True

def reprendre():
    """ -> func
        Reprend la stabilisation
    """
    global INTERRUPTION
    INTERRUPTION = False
    return simulation()


#########################

# Partie principale

root = tk.Tk()
root.title("Chasse")

canvas = tk.Canvas(root, height=HAUTEUR, width=LARGEUR, bg="white")
canvas.grid(column=1, row=0, rowspan=9)

creer_n_proies()
creer_n_predateurs()
init_affichage()

# Création des widgets

bouton_init = tk.Button(text="Jouer", command=simulation)
bouton_init.grid(column=0, row=1)

label = tk.Label(text="Nombre de proies: " + str(len(PROIES)) + "\nNombre de prédateurs: " + str(len(PREDATEURS)) + "\nNombre d'itérations: " + str(ITERATIONS))
label.grid(column=0, row=2)

bouton_pre = tk.Button(text="Mode Super Prédateurs", bg="red3", command=superpredateurs)
bouton_pre.grid(column=0, row=4)

bouton_int = tk.Button(text="Interrompre", command=interruption)
bouton_int.grid(column=0, row=5)
bouton_rep = tk.Button(text="Reprendre", command=reprendre)
bouton_rep.grid(column=0, row=6)

bouton_save = tk.Button(text="Sauvegarder", command=sauvegarder)
bouton_save.grid(column=0, row=7)
bouton_char = tk.Button(text="Charger", command=charger)
bouton_char.grid(column=0, row=8)


root.mainloop()




#########################

# Partie principale

root = tk.Tk()
root.title("Génération de terrain")

canvas = tk.Canvas(root, height=HAUTEUR, width=LARGEUR)
canvas.grid(column=1, row=0, rowspan=9)

# Création des widgets

bouton_init = tk.Button(text="Play", command=simulation)
bouton_init.grid(column=0, row=1)

bouton_pre = tk.Button(text="Mode Super Prédateurs", bg="red3", command=superpredateurs)
bouton_pre.grid(column=0, row=3)

bouton_int = tk.Button(text="Interrompre", command=interruption)
bouton_int.grid(column=0, row=5)
bouton_rep = tk.Button(text="Reprendre", command=reprendre)
bouton_rep.grid(column=0, row=6)

bouton_save = tk.Button(text="Sauvegarder", command=sauvegarder)
bouton_save.grid(column=0, row=7)
bouton_char = tk.Button(text="Charger", command=charger)
bouton_char.grid(column=0, row=8)


init_affichage()
root.mainloop()
