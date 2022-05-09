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

# Paramètres de base

HAUTEUR = 810
LARGEUR = 810
N = 30
PROIES = []
PREDATEURS = []

# Paramètres proies

APRO = 7
FPRO = 3

# Paramètres prédateurs

APRE = 25
EREPRO = 17
EPRE = 14
MIAM = 5
FLAIR = 10

# Paramèters divers

MODE_PRE = 1
TEMPS_ATTENTE = 60
INTERRUPTION = False
ITERATIONS = 0

# Pour faire de l'analyse de données
# prolen = [5]
# predlen = [2]
# proies = []
# pred = []


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

def creer_proies(repro=0, x=15, y=15):
    """ int, int, int
        Crée une proie
    """
    a = 0
    if len(PROIES) >= 1:
        a = PROIES[-1][0] + 1
    PROIES.append([a, APRO, repro, [x, y]])

def creer_predateurs(cible=[], x=15, y=15):
    """ list, int, int
        Crée un prédateur
    """
    a = 0
    if len(PREDATEURS) >= 1:
        a = PREDATEURS[-1][0] + 1
    PREDATEURS.append([a, APRE, EPRE, cible, [x, y]])

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
    """ Lance la simulation """
    global PROIES, PREDATEURS, ITERATIONS
    deplacement_proies()
    deplacement_predateurs()
    manger()
    age(PROIES)
    age(PREDATEURS)
    creer_n_proies(FPRO)
    ITERATIONS += 1
    # Pour faire de l'analyse de donnée
    # predlen.append(len(PREDATEURS))
    # prolen.append(len(PROIES))
    # for i in range(len(PROIES)):
    #     proies.append(PROIES[i])
    # for j in range(len(PREDATEURS)):
    #     pred.append(PREDATEURS[j])
    init_affichage()
    if label["text"][0] == "L":
        return rejouer()
    elif len(PREDATEURS) == 0:
        label["text"] = "Les proies ont gagné !" + "\nNombre d'itérations: " + str(ITERATIONS)
        bouton_init["text"] = "Rejouer"
        # Pour faire de l'analyse de donnée
        # sauvegardes = open("data.txt", "a")
        # sauvegardes.write(str(prolen) + "\n")
        # sauvegardes.write(str(predlen) + "\n")
        # sauvegardes.write(str(proies) + "\n")
        # sauvegardes.write(str(pred) + "\n")
        # sauvegardes.close()
        return
    elif len(PROIES) == 0:
        label["text"] = "Les prédateurs ont gagné !" + "\nNombre d'itérations: " + str(ITERATIONS)
        bouton_init["text"] = "Rejouer"
        # Pour faire de l'analyse de donnée
        # sauvegardes = open("data.txt", "a")
        # sauvegardes.write(str(prolen) + "\n")
        # sauvegardes.write(str(predlen) + "\n")
        # sauvegardes.write(str(proies) + "\n")
        # sauvegardes.write(str(pred) + "\n")
        # sauvegardes.close()
        return
    label["text"] = "Nombre de proies: " + str(len(PROIES)) + "\nNombre de prédateurs: " + str(len(PREDATEURS)) + "\nNombre d'itérations: " + str(ITERATIONS)
    if INTERRUPTION == False:
        root.after(TEMPS_ATTENTE, simulation)

def rejouer():
    """ Réinitialise les conditions initiales et relance la simulation """
    global PROIES, PREDATEURS, ITERATIONS
    PROIES, PREDATEURS = [], []
    ITERATIONS = 0
    creer_n_proies()
    creer_n_predateurs()
    init_affichage()
    label["text"] = "Nombre de proies: " + str(len(PROIES)) + "\nNombre de prédateurs: " + str(len(PREDATEURS)) + "\nNombre d'itérations: " + str(ITERATIONS)
    simulation()

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
    """ int, int -> bool
        Renvoie False si la case aux coordonnées x, y est occupée
        False non
    """
    if x < 0 or x > 29 or y < 0 or y > 29:
        return False
    for i in range(len(PROIES)):
        if x == PROIES[i][-1][0] and y == PROIES[i][-1][1]:
            return False
    for j in range(len(PREDATEURS)):
        if x == PREDATEURS[j][-1][0] and y == PREDATEURS[j][-1][1]:
            return False
    return True

def age(pr):
    """ Diminue de 1 l'âge de la proie ou du prédateur """
    i = 0
    while i < len(pr):
        if pr[i][1] == 0:
            pr.remove(pr[i])
        else:
            pr[i][1] -= 1
            i += 1

# Proies

def deplacement_proies():
    """ Gère la reproduction et le déplacement des proies """
    for i in range(len(PROIES)):
        reproduction(PROIES[i])
        # Vérification des cases libres
        new_coords = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        nb = verif_mouv(PROIES[i])
        # Déplacement
        if len(nb) != 0:
            dir = rd.choice(nb)
            PROIES[i][-1][0], PROIES[i][-1][1] = PROIES[i][-1][0]+new_coords[dir][0], PROIES[i][-1][1]+new_coords[dir][1]

def reprod_case(num, proie, new_coords):
    """ int, list
        Crée une proie à côté de la proie qui se reproduit
    """
    creer_proies(x=proie[-1][0]+new_coords[num][0], y=proie[-1][1]+new_coords[num][1])

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

# Prédateurs

def deplacement_predateurs():
    """ Gère la reproduction et le déplacement des prédateurs """
    for i in range(len(PREDATEURS)):
        repro_pred(PREDATEURS[i])
        cible = flair(predateur = PREDATEURS[i])
        if cible == []:
            new_coords = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
            nb = verif_mouv(PREDATEURS[i])
            if len(nb) == 0:
                return
            dir = rd.choice(nb)
            PREDATEURS[i][-1][0], PREDATEURS[i][-1][1] = PREDATEURS[i][-1][0]+new_coords[dir][0], PREDATEURS[i][-1][1]+new_coords[dir][1]
        else:
            mouvement_predateur(PREDATEURS[i])

def flair(predateur, distance=1000, cible = []):
    """ list, int, list -> list
        Renvoie les coordonnées de la proie la plus proche du prédateur
    """
    for j in range(len(PROIES)):
        distancetmp = sqrt((predateur[-1][0] - PROIES[j][-1][0])**2 + (predateur[-1][1] - PROIES[j][-1][1])**2)
        if distancetmp <= distance:
            distance = distancetmp
            if MODE_PRE == 0:
                cible = PROIES[j][-1]
            else:
                if distance <= FLAIR:
                    cible = PROIES[j][-1]
        predateur[-2] = cible
    return cible

def mouvement_predateur(pr):
    """ list
        Déplace le prédateur avec l'algorithme de flair
    """
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
                PREDATEURS[i][-3] += MIAM
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
        predateur[-3] = EPRE
        creer_n_predateurs(1)

# Divers

def superpredateurs(bouton_pre):
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
    entree = entree_chargement.get()
    if not entree.isnumeric():
        return
    ligne = int(entree)
    sauvegardes = open(fichier, "r")
    save = sauvegardes.readlines()
    if ligne >= len(save)+1 or ligne <= 0:
        label["text"] = "Sauvegarde inexistante !"
        return
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

def params_entree(entree, id, label):
    global APRO, FPRO, APRE, EREPRO, EPRE, MIAM, TEMPS_ATTENTE
    if not entree.isnumeric():
        return
    if id == 0:
        APRO = int(entree)
        label['text'] = "Apro = " + str(APRO)
    elif id == 1:
        FPRO = int(entree)
        label['text'] = "Fpro = " + str(FPRO)
    elif id == 2:
        APRE = int(entree)
        label['text'] = "Apre = " + str(APRE)
    elif id == 3:
        if EPRE > int(entree):
            label['text'] = "Erepro ne peut pas être plus petit que Epro !"
            return
        EREPRO = int(entree)
        label['text'] = "Erepro = " + str(EREPRO)
    elif id == 4:
        EPRE = int(entree)
        label['text'] = "Epre = " + str(EPRE)
    elif id == 5:
        MIAM = int(entree)
        label['text'] = "Miam = " + str(MIAM)
    elif id == 6:
        FLAIR = int(entree)
        label['text'] = "Flair = " + str(FLAIR)
    elif id == 7:
        TEMPS_ATTENTE = int(entree)
        label['text'] = "Temps d'attente = " + str(TEMPS_ATTENTE) + "ms"

def menu_params():
    menu = tk.Toplevel()
    entry = tk.Entry(menu, text="Entrée", textvariable=tk.StringVar())
    entry.grid(column=0, row=0)
    label_apro = tk.Label(menu, text="Apro = " + str(APRO))
    label_apro.grid(column=1, row=1)
    bouton_apro = tk.Button(menu, text="Apro", command=lambda: params_entree(entry.get(), 0, label_apro))
    bouton_apro.grid(column=0, row=1)
    label_fpro = tk.Label(menu, text="Fpro = " + str(FPRO))
    label_fpro.grid(column=1, row=2)
    bouton_fpro = tk.Button(menu, text="Fpro", command=lambda: params_entree(entry.get(), 1, label_fpro))
    bouton_fpro.grid(column=0, row=2)
    label_apre = tk.Label(menu, text="Apre = " + str(APRE))
    label_apre.grid(column=1, row=3)
    bouton_apre = tk.Button(menu, text="Apre", command=lambda: params_entree(entry.get(), 2, label_apre))
    bouton_apre.grid(column=0, row=3)
    label_erepro = tk.Label(menu, text="Erepro = " + str(EREPRO))
    label_erepro.grid(column=1, row=4)
    bouton_erepro = tk.Button(menu, text="Erepro", command=lambda: params_entree(entry.get(), 3, label_erepro))
    bouton_erepro.grid(column=0, row=4)
    label_epre = tk.Label(menu, text="Epre = " + str(EPRE))
    label_epre.grid(column=1, row=5)
    bouton_epre = tk.Button(menu, text="Epre", command=lambda: params_entree(entry.get(), 4, label_epre))
    bouton_epre.grid(column=0, row=5)
    label_miam = tk.Label(menu, text="Miam = " + str(MIAM))
    label_miam.grid(column=1, row=6)
    bouton_miam = tk.Button(menu, text="Miam", command=lambda: params_entree(entry.get(), 5, label_miam))
    bouton_miam.grid(column=0, row=6)
    label_flair = tk.Label(menu, text="Flair = " + str(FLAIR))
    label_flair.grid(column=1, row=7)
    bouton_flair = tk.Button(menu, text="Flair", command=lambda: params_entree(entry.get(), 6, label_flair))
    bouton_flair.grid(column=0, row=7)
    label_tempsattente = tk.Label(menu, text="Temps d'attente = " + str(TEMPS_ATTENTE) + "ms")
    label_tempsattente.grid(column=1, row=8)
    bouton_tempsattente = tk.Button(menu, text="Temps d'attente", command=lambda: params_entree(entry.get(), 7, label_tempsattente))
    bouton_tempsattente.grid(column=0, row=8)
    bouton_pre = tk.Button(menu, text="Mode Super Prédateurs", bg="red3", command=lambda: superpredateurs(bouton_pre))
    bouton_pre.grid(column=0, row=9)


#########################

# Partie principale

root = tk.Tk()
root.title("Chasse")

canvas = tk.Canvas(root, height=HAUTEUR, width=LARGEUR, bg="white")
canvas.grid(column=1, row=0, rowspan=10)

creer_n_proies()
creer_n_predateurs()
init_affichage()

# Création des widgets

bouton_init = tk.Button(text="Jouer", command=simulation)
bouton_init.grid(column=0, row=1)

label = tk.Label(text="Nombre de proies: " + str(len(PROIES)) + "\nNombre de prédateurs: " + str(len(PREDATEURS)) + "\nNombre d'itérations: " + str(ITERATIONS))
label.grid(column=0, row=2)

bouton_param = tk.Button(text="Paramètres", command=menu_params)
bouton_param.grid(column=0, row=4)

bouton_int = tk.Button(text="Interrompre", command=interruption)
bouton_int.grid(column=0, row=5)
bouton_rep = tk.Button(text="Reprendre", command=reprendre)
bouton_rep.grid(column=0, row=6)

bouton_save = tk.Button(text="Sauvegarder", command=sauvegarder)
bouton_save.grid(column=0, row=7)
entree_chargement = tk.Entry(text="Entrée", textvariable=tk.StringVar())
entree_chargement.grid(column=0, row=8)
bouton_char = tk.Button(text="Charger", command=charger)
bouton_char.grid(column=0, row=9)


root.mainloop()
