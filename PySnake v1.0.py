# -*- coding: utf-8 -*-
# ------------------------------
# PySnake v1.0
# Auteur : Alexandre l'Heritier
#-------------------------------
from tkinter import *
import random

DEBUG = True
version = "PySnake v1.0"

def _dessin_line(self, posdeb, posfin, horiverti, xy):
	tab = []
	if horiverti == "x":
		for i in range(posdeb, posfin+1):
			tab.append(_dessin_carre(self, i, xy))
	
	if horiverti == "y":
		for i in range(posdeb, posfin+1):
			tab.append(_dessin_carre(self, xy, i))
	
	return tab

def _dessin_carre(self, posx, posy):
	self.testx0 = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * posx
	self.testy0 = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * posy
	self.testx1 = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * (posx + 1)
	self.testy1 = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * (posy + 1)

	return self.canvas.create_rectangle(self.testx0, self.testy0, self.testx1, self.testy1, fill = "#ffffff")

def _verif_pos(self, newposx, newposy):
	while newposx > self.nb_ligne:
		newposx -= self.nb_ligne + 1

	while newposy > self.nb_colonne:
		newposy -= self.nb_colonne + 1

	while newposx < 0:
		newposx += self.nb_ligne + 1

	while newposy < 0:
		newposy += self.nb_colonne + 1
	
	return (newposx, newposy)

def _create_grille(self):
	self.canvas.create_rectangle(self.cadrepx0, self.cadrepy0, self.cadrepx1, self.cadrepy1, outline=self.cadrepcouleur, width=5)

	self.canvas.create_rectangle(self.cadredx0, self.cadredy0, self.cadredx1, self.cadredy1, outline=self.cadredcouleur, width=1)

	self.nb_ligne = 24
	self.nb_colonne = 14

	for i in range(1, self.nb_ligne+1):
		x0temp = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * i
		y0temp = self.cadredy0
		x1temp = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * i
		y1temp = self.cadredy1
		self.canvas.create_line(x0temp, y0temp, x1temp, y1temp, fill = "#ffffff")

	for i in range(1, self.nb_colonne+1):
		x0temp = self.cadredx0
		y0temp = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * i
		x1temp = self.cadredx1
		y1temp = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * i
		self.canvas.create_line(x0temp, y0temp, x1temp, y1temp, fill = "#ffffff")

def _create_menu(self):
	self.cadrepx0 = 13
	self.cadrepy0 = 13
	self.cadrepx1 = self.WIDTH - 10
	self.cadrepy1 = self.HEIGHT - 10
	self.cadrepcouleur = "#ffffff"

	self.canvas.create_rectangle(self.cadrepx0, self.cadrepy0, self.cadrepx1, self.cadrepy1, outline=self.cadrepcouleur, width=5)
		
	self.cadredx0 = self.cadrepx0 + 10
	self.cadredy0 = self.cadrepy0 + 10
	self.cadredx1 = self.cadrepx1 - 10
	self.cadredy1 = self.cadrepy1 - 10
	self.cadredcouleur = "#ffffff"
		
	self.canvas.create_rectangle(self.cadredx0, self.cadredy0, self.cadredx1, self.cadredy1, outline=self.cadredcouleur, width=1)

	self.nb_ligne = 42
	self.nb_colonne = 22

	self.tab_menu = []

	self.tab_menu += _dessin_line(self, 1, 7, "y", 4)
	self.tab_menu += _dessin_line(self, 5, 7, "x", 1)
	self.tab_menu += _dessin_line(self, 1, 4, "y", 7)
	self.tab_menu += _dessin_line(self, 5, 7, "x", 4)

	self.tab_menu += _dessin_line(self, 9, 12, "x", 5)
	self.tab_menu += _dessin_line(self, 3, 7, "y", 12)
	self.tab_menu += _dessin_line(self, 3, 5, "y", 9)

	self.tab_menu += _dessin_line(self, 15, 18, "x", 1)
	self.tab_menu += _dessin_line(self, 1, 4, "y", 15)
	self.tab_menu += _dessin_line(self, 15, 18, "x", 4)
	self.tab_menu += _dessin_line(self, 4, 7, "y", 18)
	self.tab_menu += _dessin_line(self, 15, 18, "x", 7)

	self.tab_menu += _dessin_line(self, 3, 7, "y", 20)
	self.tab_menu.append(_dessin_carre(self, 21, 4))
	self.tab_menu.append(_dessin_carre(self, 22, 5))
	self.tab_menu += _dessin_line(self, 3, 7, "y", 23)

	self.tab_menu += _dessin_line(self, 3, 7, "y", 25)
	self.tab_menu += _dessin_line(self, 25, 28, "x", 3)
	self.tab_menu += _dessin_line(self, 3, 7, "y", 28)
	self.tab_menu += _dessin_line(self, 25, 28, "x", 5)

	self.tab_menu += _dessin_line(self, 3, 7, "y", 30)
	self.tab_menu.append(_dessin_carre(self, 31, 5))
	self.tab_menu.append(_dessin_carre(self, 32, 4))
	self.tab_menu.append(_dessin_carre(self, 32, 6))
	self.tab_menu.append(_dessin_carre(self, 33, 3))
	self.tab_menu.append(_dessin_carre(self, 33, 7))

	self.tab_menu += _dessin_line(self, 3, 7, "y", 35)
	self.tab_menu += _dessin_line(self, 35, 37, "x", 5)
	self.tab_menu += _dessin_line(self, 35, 38, "x", 7)
	self.tab_menu += _dessin_line(self, 35, 38, "x", 3)
	
	self.tab_menu += _dessin_line(self, 24, 40, "x", 18)
	self.tab_menu += _dessin_line(self, 24, 40, "x", 14)
	self.tab_menu += _dessin_line(self, 14, 18, "y", 24)
	self.tab_menu += _dessin_line(self, 14, 18, "y", 40)
	self.tab_menu.append(self.canvas.create_text(900, 490, text = "Cliquer ici", fill = "#ffffff", font=("Purisa", 20)))

	def clique(event):
		if event.x < 1128 and event.x > 667 and event.y < 562 and event.y > 428:
			self.unbind("<Button-1>")
			_efface_menu(self)
			_create_grille(self)
			_play(self)
	
	self.bind("<Button-1>", clique)

def _efface_menu(self):
	for elems in self.tab_menu:
		self.canvas.delete(elems)

def _verif_miam(self):
	return self.tab_serpent_pos[0] == self.miam_pos[0]

def _level_1(self):
	self.tab_serpent_pos = [[4, 2], [3, 2], [2, 2]]
	self.tab_serpent = []
	self.tab_serpent.append(_dessin_carre(self, 4, 2))
	self.tab_serpent.append(_dessin_carre(self, 3, 2))
	self.tab_serpent.append(_dessin_carre(self, 2, 2))

	self.murs_pos = [[7, 7]]
	self.murs = []
	self.murs.append(_dessin_carre(self, 7, 7))

	self.miam_pos = [[5, 5]]
	self.miam = []
	self.miam.append(_dessin_carre(self, 5, 5))

	self.entrer_level_suivant = [-1, -1]

def _play(self):

	global DEBUG
	self.updown = 0
	self.leftright = 1
	self.appui_touche = True

	_level_1(self)

	def clavier(event):
		touche = event.keysym

		if DEBUG:
			print(touche)

		if touche == "Up":
			if self.updown != 1 and self.leftright != 0 and self.appui_touche:
				self.updown = -1
				self.leftright = 0
				self.appui_touche = False
		
		if touche == "Down":
			if self.updown != -1 and self.leftright != 0 and self.appui_touche:
				self.updown = 1
				self.leftright = 0
				self.appui_touche = False
		
		if touche == "Left":
			if self.updown != 0 and self.leftright != 1 and self.appui_touche:
				self.updown = 0
				self.leftright = -1
				self.appui_touche = False
		
		if touche == "Right":
			if self.updown != 0 and self.leftright != -1 and self.appui_touche:
				self.updown = 0
				self.leftright = 1
				self.appui_touche = False
	

	def time():
		for elems in self.tab_serpent:
			self.canvas.delete(elems)

		self.tab_serpent = []
		temp = [[0, 0]]

		(temp[0][0], temp[0][1]) = _verif_pos(self, self.tab_serpent_pos[0][0] + self.leftright, self.tab_serpent_pos[0][1] + self.updown)

		self.tab_serpent.append(_dessin_carre(self, temp[0][0], temp[0][1]))

		for elems in self.tab_serpent_pos:
			self.tab_serpent.append(_dessin_carre(self, elems[0], elems[1]))
			temp.append([elems[0], elems[1]])

		self.tab_serpent_pos = temp

		if not _verif_miam(self):
			del self.tab_serpent_pos[len(self.tab_serpent_pos)-1]
		else:
			self.canvas.delete(self.miam[0])
			self.miam_pos[0][0] = random.randint(0, self.nb_ligne - 1)
			self.miam_pos[0][1] = random.randint(0, self.nb_colonne - 1)
			self.miam[0] = _dessin_carre(self, self.miam_pos[0][0], self.miam_pos[0][1])

		self.appui_touche = True

		self.after(500, time)
	
	time()
	self.bind("<Key>", clavier)

class Application(Tk):

	# Initialisations
	def __init__(self):

		Tk.__init__(self)

		global version
		
		# Self config
		self.tk_setPalette(background='#2d2d30', foreground='#ececec', activeBackground='#212123', activeForeground="#ffffff")

		self.title(version)
		
		self.WIDTH 	= 1200
		self.HEIGHT = 700

		self.canvas = Canvas(self, width = self.WIDTH, height = self.HEIGHT, bg = "#000000")

		_create_menu(self)
		
		self.canvas.pack()

def main():
	process = Application()
	process.mainloop()
	return 0

main()
