########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/Elta305/Projet-Chasse
#########################

Projet Chasse  
Simulation d'un environnement avec des proies et des prédateurs.  

Contraintes:
- Le projet doit être écrit sur un seul fichier  
- Il ne faut pas utiliser de classes d'objets  
- Il faut utiliser la librairie tkinter pour l'interface graphique  

Mode d'emploi:

Cliquez sur "Jouer" pour lancer la simulation.  
Le nombre de proies, de prédateurs et d'itérations est indiqué en dessous est s'actualise en direct.  

Paramètres: Ouvre la fenêtre des paramètres. Ecrire dans la case de texte et cliquer sur les boutons en dessous (à l'exception du bouton "Mode Super Prédateurs"). Les paramètres sont actualisés en direct même si la simulation est en cours. Les proies et prédateurs déjà sur le terrain ne sont pas affectées par les changements effectués sauf si vous relancez une simulation.  
Mode Super Prédateurs: Active le mode Super Prédateurs qui permet aux prédateurs de détecter la proie la plus proche et d'aller vers elle. Cliquez à nouveau pour passer au mode Normal (flair à une portée de 10 maximum dans la configuration de base)  
Interrompre: Interrompt la simulation. Si l'on clique sur "Jouer" après avoir interrompu et sans cliquer sur "Reprendre", la simulation se fera itération par itération.  
Reprendre: Reprend la simulation  
Sauvegarder: Sauvegarde la configuration actuelle dans le fichier "saves.txt" (le fichier se crée automatiquement s'il n'existe pas).  
Charger: Charge une configuration sauvegardée au choix (la 1ère sauvegarde est à l'indice 1 et non 0). Ecrire le numéro de sauvegarde dans l'entrée au dessus du bouton.  


Evolution d'une simulation de 3 300 itérations:  
Orange: nombre de prédateurs  
Bleu: nombre de proies  
![graphique](https://media.discordapp.net/attachments/902559091703029765/971737377636745236/proiespred.png)  

Heatmap de la simulation:  
![heatmap](https://media.discordapp.net/attachments/902559091703029765/971737378119098428/proiespredheatmap.png)  

Note de l'analyse:
Dans la configuration de base, il est impossible pour les prédateurs de gagner. En effet, ne pouvant pas recouvrir entièrement le terrain, il y aura toujours de la place pour que les proies se multiplient alors que les prédateurs meurent de faim. Pour faire gagner les prédateurs, il faut mettre à 0 la variable Fpro qui permet aux proies d'avoir au moins Fpro individus vivants chaque itération.
