########################
# MITD-03
# Frédéric Li Combeau
# Lisa Vauvert
# Victor Combemorel
# Manel Mokrab
# https://github.com/uvsq-info/l1-python
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

Mode Super Prédateurs: Active le mode Super Prédateurs qui permet aux prédateurs de détecter la proie la plus proche et d'aller vers elle. Cliquez à nouveau pour passer au mode Normal (flair à une portée de 10 maximum)  
Interrompre: Interrompt la simulation. Si l'on clique sur "Jouer" après avoir interrompu et sans cliquer sur "Reprendre", la simulation se fera itération par itération.  
Reprendre: Reprend la simulation  
Sauvegarder: Sauvegarde la configuration actuelle  
Charger: Charge une configuration sauvegardée au choix (la 1ère sauvegarde est à l'indice 1 et non 0)  


Evolution d'une simulation de 3 300 itérations:  
Orange: prédateurs  
Bleu: proies  
![graphique](https://media.discordapp.net/attachments/902559091703029765/971737377636745236/proiespred.png)  

Heatmap de la simulation:  
![heatmap](https://media.discordapp.net/attachments/902559091703029765/971737378119098428/proiespredheatmap.png)
