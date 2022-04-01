# -*- coding: utf-8 -*-
# ------------------------------
# PySnake v6.0
# Auteur : Alexandre l'Heritier
#-------------------------------
from tkinter import *
import menuEtGrille

class Application(Tk):

	# Initialisations
	def __init__(self):

		Tk.__init__(self)

		global version

		self.tk_setPalette(background='#2d2d30', foreground='#ececec', activeBackground='#212123', activeForeground="#ffffff")

		self.title(version)

		self.WIDTH 	= 1200
		self.HEIGHT = 700

		self.canvas = Canvas(self, width = self.WIDTH, height = self.HEIGHT+60, bg = "#000000")

		menuEtGrille._create_menu(self)

		self.canvas.pack()

def main():
	process = Application()
	process.mainloop()
	return 0

main()

"""
A faire :
- 2 joueurs
- Plus de levels
- Corriger le clignotement du serpent lors du changement de couleur.
- Menu pause.


Changelog :
v6.0 :
Code plus lisible.

v5.0 :
Mode 2 joueurs VS

v4.0 :
Gestion de la couleur du mode infinie amélioré : remplacement de la grille au lieu de la superposition.
Ajout de 4 nouveaux niveau.
Ajout du changement de la taille de la grille et de la vitesse dans le mode infinie.
Changement des couleurs un peu modifié.

v3.0 :
Ajout de la touche échap.
Gestion de la modification de couleur dans le mode infinie.
Création de l'écran win
Ajout du support de zqsd.
Tout les affichages sont maintenant calculé avec Width et Height.

v2.0 :
Création du mode survie ou aventure avec 2 niveaux.
Création du game over.
Le level 2 possede une autre couleur.
Bonbon rond

v1.0 :
Première version (pas de beta)
Création de la grille de déplacement.
Création du serpent avec déplacement a l'aide des touches directionnelles.
Création du bonbon permettant au serpent de grandir.
Création du mur mais aucun effet.
Création d'un menu principal.
Reste à faire :
- Game over en mordant la queux ou en touchant un mur.
- Un mode aventure.
- Des couleurs !
"""
