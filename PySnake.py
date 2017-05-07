# -*- coding: utf-8 -*-
# ------------------------------
# PySnake v2.0
# Auteur : Alexandre l'Heritier
#-------------------------------
from tkinter import *
import random

DEBUG = False
version = "PySnake v2.0"

def _dessin_line(self, posdeb, posfin, horiverti, xy):
	tab = []
	pos = []
	if horiverti == "x":
		for i in range(posdeb, posfin+1):
			tab.append(_dessin_carre(self, i, xy))
			pos.append([i, xy])
	
	if horiverti == "y":
		for i in range(posdeb, posfin+1):
			tab.append(_dessin_carre(self, xy, i))
			pos.append([xy, i])
	
	return (tab, pos)

def _dessin_carre(self, posx, posy):
	self.testx0 = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * posx
	self.testy0 = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * posy
	self.testx1 = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * (posx + 1)
	self.testy1 = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * (posy + 1)

	return self.canvas.create_rectangle(self.testx0, self.testy0, self.testx1, self.testy1, fill = self.color)

def _dessin_rond(self, posx, posy):
	self.testx0 = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * posx
	self.testy0 = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * posy
	self.testx1 = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * (posx + 1)
	self.testy1 = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * (posy + 1)

	return self.canvas.create_oval(self.testx0, self.testy0, self.testx1, self.testy1, fill = self.color)

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
	self.tab_menu = []
	self.tab_menu.append(self.canvas.create_rectangle(self.cadrepx0, self.cadrepy0, self.cadrepx1, self.cadrepy1, outline=self.cadrepcouleur, width=5))

	self.tab_menu.append(self.canvas.create_rectangle(self.cadredx0, self.cadredy0, self.cadredx1, self.cadredy1, outline=self.cadredcouleur, width=1))

	self.nb_ligne = 24
	self.nb_colonne = 14

	for i in range(1, self.nb_ligne+1):
		x0temp = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * i
		y0temp = self.cadredy0
		x1temp = self.cadredx0 + ((self.cadredx1 - self.cadredx0) / (self.nb_ligne + 1)) * i
		y1temp = self.cadredy1
		self.tab_menu.append(self.canvas.create_line(x0temp, y0temp, x1temp, y1temp, fill = self.color))

	for i in range(1, self.nb_colonne+1):
		x0temp = self.cadredx0
		y0temp = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * i
		x1temp = self.cadredx1
		y1temp = self.cadredy0 + ((self.cadredy1 - self.cadredy0) / (self.nb_colonne + 1)) * i
		self.tab_menu.append(self.canvas.create_line(x0temp, y0temp, x1temp, y1temp, fill = self.color))

def _create_menu(self):
	self.color = "#ffffff"
	self.canvas.config(bg = "#000000")
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

	self.tab_menu += _dessin_line(self, 1, 7, "y", 4)[0]
	self.tab_menu += _dessin_line(self, 5, 7, "x", 1)[0]
	self.tab_menu += _dessin_line(self, 1, 4, "y", 7)[0]
	self.tab_menu += _dessin_line(self, 5, 7, "x", 4)[0]

	self.tab_menu += _dessin_line(self, 9, 12, "x", 5)[0]
	self.tab_menu += _dessin_line(self, 3, 7, "y", 12)[0]
	self.tab_menu += _dessin_line(self, 3, 5, "y", 9)[0]

	self.tab_menu += _dessin_line(self, 15, 18, "x", 1)[0]
	self.tab_menu += _dessin_line(self, 1, 4, "y", 15)[0]
	self.tab_menu += _dessin_line(self, 15, 18, "x", 4)[0]
	self.tab_menu += _dessin_line(self, 4, 7, "y", 18)[0]
	self.tab_menu += _dessin_line(self, 15, 18, "x", 7)[0]

	self.tab_menu += _dessin_line(self, 3, 7, "y", 20)[0]
	self.tab_menu.append(_dessin_carre(self, 21, 4))
	self.tab_menu.append(_dessin_carre(self, 22, 5))
	self.tab_menu += _dessin_line(self, 3, 7, "y", 23)[0]

	self.tab_menu += _dessin_line(self, 3, 7, "y", 25)[0]
	self.tab_menu += _dessin_line(self, 25, 28, "x", 3)[0]
	self.tab_menu += _dessin_line(self, 3, 7, "y", 28)[0]
	self.tab_menu += _dessin_line(self, 25, 28, "x", 5)[0]

	self.tab_menu += _dessin_line(self, 3, 7, "y", 30)[0]
	self.tab_menu.append(_dessin_carre(self, 31, 5))
	self.tab_menu.append(_dessin_carre(self, 32, 4))
	self.tab_menu.append(_dessin_carre(self, 32, 6))
	self.tab_menu.append(_dessin_carre(self, 33, 3))
	self.tab_menu.append(_dessin_carre(self, 33, 7))

	self.tab_menu += _dessin_line(self, 3, 7, "y", 35)[0]
	self.tab_menu += _dessin_line(self, 35, 37, "x", 5)[0]
	self.tab_menu += _dessin_line(self, 35, 38, "x", 7)[0]
	self.tab_menu += _dessin_line(self, 35, 38, "x", 3)[0]
	
	self.tab_menu += _dessin_line(self, 24, 40, "x", 14)[0]
	self.tab_menu += _dessin_line(self, 24, 40, "x", 10)[0]
	self.tab_menu += _dessin_line(self, 10, 14, "y", 24)[0]
	self.tab_menu += _dessin_line(self, 10, 14, "y", 40)[0]
	self.tab_menu.append(self.canvas.create_text(900, 378, text = "Mode survie - Plusieurs niveaux", fill = "#ffffff", font=("Purisa", 20)))

	self.tab_menu += _dessin_line(self, 24, 40, "x", 19)[0]
	self.tab_menu += _dessin_line(self, 24, 40, "x", 15)[0]
	self.tab_menu += _dessin_line(self, 15, 19, "y", 24)[0]
	self.tab_menu += _dessin_line(self, 15, 19, "y", 40)[0]
	self.tab_menu.append(self.canvas.create_text(900, 522, text = "Mode infinie - Niveau sans murs", fill = "#ffffff", font=("Purisa", 20)))

	def clique(event):
		if event.x < 1128 and event.x > 667 and event.y < 452 and event.y > 311:
			self.unbind("<Button-1>")
			_efface_menu(self)
			self.mode = True
			_play(self)
		
		if event.x < 1128 and event.x > 667 and event.y < 595 and event.y > 452:
			self.unbind("<Button-1>")
			_efface_menu(self)
			self.mode = False
			_play(self)
	
	self.bind("<Button-1>", clique)

def _efface_menu(self):
	for elems in self.tab_menu:
		self.canvas.delete(elems)

def _verif_miam(self):
	for i in range(0, len(self.miam_pos)):
		if self.miam_pos[i] == self.tab_serpent_pos[0]:
			return i
	return -1

def _changement_de_bonbon(self, temp):
	self.canvas.delete(self.miam[temp])
	self.miam_pos[temp][0] = random.randint(0, self.nb_ligne - 1)
	self.miam_pos[temp][1] = random.randint(0, self.nb_colonne - 1)

	while self.miam_pos[temp] in self.tab_serpent_pos or self.miam_pos[temp] in self.murs_pos:
		self.miam_pos[temp][0] = random.randint(0, self.nb_ligne - 1)
		self.miam_pos[temp][1] = random.randint(0, self.nb_colonne - 1)

	self.miam[temp] = _dessin_rond(self, self.miam_pos[temp][0], self.miam_pos[temp][1])

def _avance_serpent(self):
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

def _verif_perdu(self):
	temp = []
	for i in range(1, len(self.tab_serpent_pos)):
		temp.append(self.tab_serpent_pos[i])

	if self.tab_serpent_pos[0] in temp or self.tab_serpent_pos[0] in self.murs_pos:
		return True

	return False

def _efface_grille(self):
	for elems in self.tab_menu:
		self.canvas.delete(elems)
	for elems in self.tab_serpent:
		self.canvas.delete(elems)
	for elems in self.murs:
		self.canvas.delete(elems)
	for elems in self.miam:
		self.canvas.delete(elems)

def _level_0(self):
	_create_grille(self)
	self.tab_serpent_pos = [[4, 2], [3, 2], [2, 2]]
	self.tab_serpent = []
	self.tab_serpent.append(_dessin_carre(self, 4, 2))
	self.tab_serpent.append(_dessin_carre(self, 3, 2))
	self.tab_serpent.append(_dessin_carre(self, 2, 2))

	self.murs_pos = []
	self.murs = []

	self.miam_pos = [[5, 5], [20, 5]]
	self.miam = []
	self.miam.append(_dessin_rond(self, 5, 5))
	self.miam.append(_dessin_rond(self, 20, 5))

	self.entrer_level_suivant = [0, 12]
	self.limite_miam = 9999
	self.bonbon = 0

	self.time = 500
	self.time_dim = -1

def _level_1(self):
	self.color = "#ffffff"
	_create_grille(self)
	self.tab_serpent_pos = [[4, 2], [3, 2], [2, 2]]
	self.tab_serpent = []
	self.tab_serpent.append(_dessin_carre(self, 4, 2))
	self.tab_serpent.append(_dessin_carre(self, 3, 2))
	self.tab_serpent.append(_dessin_carre(self, 2, 2))

	self.murs_pos = [[9, 9], [9, 8], [9, 5], [9, 6], [9, 7], [10, 7], [11, 7], [12, 7], [13, 7], [14, 7], [15, 7], [15, 6], [15, 5], [15, 8], [15, 9]]
	self.murs = []
	self.murs.append(_dessin_carre(self, 9, 9))
	self.murs.append(_dessin_carre(self, 9, 8))
	self.murs.append(_dessin_carre(self, 9, 5))
	self.murs.append(_dessin_carre(self, 9, 6))
	self.murs.append(_dessin_carre(self, 9, 7))
	self.murs.append(_dessin_carre(self, 10, 7))
	self.murs.append(_dessin_carre(self, 11, 7))
	self.murs.append(_dessin_carre(self, 12, 7))
	self.murs.append(_dessin_carre(self, 13, 7))
	self.murs.append(_dessin_carre(self, 14, 7))
	self.murs.append(_dessin_carre(self, 15, 7))
	self.murs.append(_dessin_carre(self, 15, 8))
	self.murs.append(_dessin_carre(self, 15, 9))
	self.murs.append(_dessin_carre(self, 15, 6))
	self.murs.append(_dessin_carre(self, 15, 5))

	self.miam_pos = [[5, 5], [20, 5]]
	self.miam = []
	self.miam.append(_dessin_rond(self, 5, 5))
	self.miam.append(_dessin_rond(self, 20, 5))

	self.entrer_level_suivant = [0, 12]
	self.limite_miam = 20
	self.bonbon = 0

	self.time = 500
	self.time_dim = -15

def _level_2(self):
	self.color = "#ff0000"
	self.canvas.config(bg = "#840000")

	_create_grille(self)
	self.tab_serpent_pos = [[4, 2], [3, 2], [2, 2]]
	self.tab_serpent = []
	self.tab_serpent.append(_dessin_carre(self, 4, 2))
	self.tab_serpent.append(_dessin_carre(self, 3, 2))
	self.tab_serpent.append(_dessin_carre(self, 2, 2))

	self.murs_pos = [[9, 9], [9, 8], [9, 5], [9, 6], [9, 7], [10, 7], [11, 7], [12, 7], [13, 7], [14, 7], [15, 7], [15, 6], [15, 5], [15, 8], [15, 9]]
	self.murs = []
	self.murs.append(_dessin_carre(self, 9, 9))
	self.murs.append(_dessin_carre(self, 9, 8))
	self.murs.append(_dessin_carre(self, 9, 5))
	self.murs.append(_dessin_carre(self, 9, 6))
	self.murs.append(_dessin_carre(self, 9, 7))
	self.murs.append(_dessin_carre(self, 10, 7))
	self.murs.append(_dessin_carre(self, 11, 7))
	self.murs.append(_dessin_carre(self, 12, 7))
	self.murs.append(_dessin_carre(self, 13, 7))
	self.murs.append(_dessin_carre(self, 14, 7))
	self.murs.append(_dessin_carre(self, 15, 7))
	self.murs.append(_dessin_carre(self, 15, 8))
	self.murs.append(_dessin_carre(self, 15, 9))
	self.murs.append(_dessin_carre(self, 15, 6))
	self.murs.append(_dessin_carre(self, 15, 5))

	temp = _dessin_line(self, 0, 24, "x", 0)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 0, 24, "x", 14)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 0, 14, "y", 0)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 0, 14, "y", 24)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	self.miam_pos = [[5, 5], [20, 5]]
	self.miam = []
	self.miam.append(_dessin_rond(self, 5, 5))
	self.miam.append(_dessin_rond(self, 20, 5))

	self.entrer_level_suivant = [0, 12]
	self.limite_miam = 20
	self.bonbon = 0

	self.time = 500
	self.time_dim = -15

def _play(self):

	global DEBUG
	self.updown = 0
	self.leftright = 1
	self.appui_touche = True
	self.niveau = 1
	self.continu = True

	if self.mode:
		_level_1(self)
	else:
		_level_0(self)

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
	

	def boucle():
		
		_avance_serpent(self)

		temp = _verif_miam(self)
		if temp == -1:
			del self.tab_serpent_pos[len(self.tab_serpent_pos)-1]
		else:
			_changement_de_bonbon(self, temp)
			self.time += self.time_dim
			self.limite_miam -= 1
			self.bonbon += 1

		
		if _verif_perdu(self):
			self.continu = False
			self.unbind("<Key>")
			self.rect = []
			self.rect.append(self.canvas.create_rectangle(303, 200, 900, 503, fill = self.color))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /3, text = "Vous avez perdu", fill = "#000000", font=("Purisa", 20)))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /2, text = "Nb de bonbon : " + str(self.bonbon) + "    Niveau : " + str(self.niveau), fill = "#000000", font=("Purisa", 20)))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT *2/3, text = "Cliquer ici pour retourner au menu principal", fill = "#000000", font=("Purisa", 20)))

			def clique(event):
				if event.x < 900 and event.x > 303 and event.y < 503 and event.y > 200:
					self.unbind("<Button-1>")
					self.unbind("<Key>")
					for elems in self.rect:
						self.canvas.delete(elems)
					_efface_grille(self)
					_create_menu(self)

			self.bind("<Button-1>", clique)

		self.appui_touche = True

		if self.limite_miam == 0:
			_efface_grille(self)
			self.bonbon = 0
			if self.niveau == 1:
				self.niveau += 1
				_level_2(self)

		if self.continu:
			self.after(self.time, boucle)
	
	boucle()
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
