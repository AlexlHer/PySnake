# -*- coding: utf-8 -*-
# ------------------------------
# PySnake v4.0
# Auteur : Alexandre l'Heritier
#-------------------------------
from tkinter import *
import random
import time

DEBUG = True
version = "PySnake v4.0"

def _color(self, num_couleur):
	if num_couleur == 0:
		self.color = "#ffffff"
		self.background = "#000000"
		self.cadrecouleur = "#ffffff"
	elif num_couleur == 1:
		self.color = "#ff0000"
		self.background = "#840000"
		self.cadrecouleur = "#ff0000"
	elif num_couleur == 2:
		self.color = "#5386fc"
		self.background = "#003b9b"
		self.cadrecouleur = "#5386fc"
	elif num_couleur == 3:
		self.color = "#00ff6f"
		self.background = "#007c36"
		self.cadrecouleur = "#00ff6f"
	elif num_couleur == 4:
		self.color = "#000000"
		self.background = "#ffffff"
		self.cadrecouleur = "#000000"
	elif num_couleur == 5:
		self.color = "#ff0000"
		self.background = "#000000"
		self.cadrecouleur = "#ff0000"
	elif num_couleur == 6:
		self.color = "#0000ff"
		self.background = "#000000"
		self.cadrecouleur = "#0000ff"
	self.canvas.config(bg = self.background)

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
	self.tab_menu.append(self.canvas.create_rectangle(self.cadrepx0, self.cadrepy0, self.cadrepx1, self.cadrepy1, outline=self.cadrecouleur, width=5))

	self.tab_menu.append(self.canvas.create_rectangle(self.cadredx0, self.cadredy0, self.cadredx1, self.cadredy1, outline=self.cadrecouleur, width=1))

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
	_color(self, 0)
	self.cadrepx0 = 13
	self.cadrepy0 = 13
	self.cadrepx1 = self.WIDTH - 10
	self.cadrepy1 = self.HEIGHT - 10
	self.cadrepcouleur = "#ffffff"

	self.canvas.create_rectangle(self.cadrepx0, self.cadrepy0, self.cadrepx1, self.cadrepy1, outline=self.cadrecouleur, width=5)
		
	self.cadredx0 = self.cadrepx0 + 10
	self.cadredy0 = self.cadrepy0 + 10
	self.cadredx1 = self.cadrepx1 - 10
	self.cadredy1 = self.cadrepy1 - 10
	self.cadredcouleur = "#ffffff"
		
	self.canvas.create_rectangle(self.cadredx0, self.cadredy0, self.cadredx1, self.cadredy1, outline=self.cadrecouleur, width=1)

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
	self.tab_menu.append(self.canvas.create_text(self.WIDTH /1.333, self.HEIGHT /1.85, text = "Mode survie - Plusieurs niveaux", fill = "#ffffff", font=("Purisa", 14)))

	self.tab_menu += _dessin_line(self, 24, 40, "x", 19)[0]
	self.tab_menu += _dessin_line(self, 24, 40, "x", 15)[0]
	self.tab_menu += _dessin_line(self, 15, 19, "y", 24)[0]
	self.tab_menu += _dessin_line(self, 15, 19, "y", 40)[0]
	self.tab_menu.append(self.canvas.create_text(self.WIDTH /1.333, self.HEIGHT /1.333, text = "Mode infinie - Niveau sans murs", fill = "#ffffff", font=("Purisa", 14)))
	self.tab_menu.append(self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, text = version, fill = self.cadrepcouleur, font=("Purisa", 14)))

	def clique(event):
		if event.x < self.WIDTH /1.06 and event.x > self.WIDTH /1.8 and event.y < self.HEIGHT /1.55 and event.y > self.HEIGHT /2.25:
			self.unbind("<Button-1>")
			_efface_menu(self)
			self.mode = True
			_play(self)
		
		if event.x < self.WIDTH /1.06 and event.x > self.WIDTH /1.8 and event.y < self.HEIGHT /1.18 and event.y > self.HEIGHT /1.55:
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
	self.canvas.delete(self.information[0])
	self.canvas.delete(self.information[1])

def _level_0(self):
	self.nb_ligne = 24
	self.nb_colonne = 14
	_create_grille(self)
	self.tab_serpent_pos = [[4, 2], [3, 2], [2, 2]]
	self.tab_serpent = []

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
	self.time_dim = 0
	self.change_color = False

def _level_1(self):
	self.nb_ligne = 24
	self.nb_colonne = 14

	_color(self, 0)

	_create_grille(self)

	self.tab_serpent_pos = [[4, 2], [3, 2], [2, 2]]
	self.tab_serpent = []

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
	if DEBUG: self.limite_miam = 1
	self.bonbon = 0

	self.time = 500
	self.time_dim = -15

def _level_2(self):
	_color(self, 1)

	_create_grille(self)

	self.tab_serpent_pos = [[4, 2], [3, 2], [2, 2]]
	self.tab_serpent = []

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
	if DEBUG: self.limite_miam = 1
	self.bonbon = 0

	self.time = 500
	self.time_dim = -15

	self.updown = 0
	self.leftright = 1

def _level_3(self):
	_color(self, 2)

	_create_grille(self)

	self.tab_serpent_pos = [[17, 2], [18, 2], [19, 2]]
	self.tab_serpent = []

	self.murs_pos = []
	self.murs = []

	temp = _dessin_line(self, 0, 24, "x", 7)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	self.miam_pos = [[12, 3], [12, 11]]
	self.miam = []
	self.miam.append(_dessin_rond(self, 12, 3))
	self.miam.append(_dessin_rond(self, 12, 9))

	self.entrer_level_suivant = [0, 12]
	self.limite_miam = 20
	if DEBUG: self.limite_miam = 1
	self.bonbon = 0

	self.time = 500
	self.time_dim = -15

	self.updown = 0
	self.leftright = -1

def _level_4(self):
	self.nb_ligne = 36
	self.nb_colonne = 21

	_color(self, 3)

	_create_grille(self)

	self.tab_serpent_pos = [[16, 2], [17, 2], [18, 2], [19, 2], [20, 2]]
	self.tab_serpent = []

	self.murs_pos = []
	self.murs = []

	temp = _dessin_line(self, 0, 36, "x", 10)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 0, 21, "y", 18)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	self.miam_pos = [[9, 5], [27, 5], [9, 14], [27, 14]]
	self.miam = []
	self.miam.append(_dessin_rond(self, 9, 5))
	self.miam.append(_dessin_rond(self, 27, 5))
	self.miam.append(_dessin_rond(self, 9, 16))
	self.miam.append(_dessin_rond(self, 27, 16))

	self.entrer_level_suivant = [0, 12]
	self.limite_miam = 50
	if DEBUG: self.limite_miam = 1
	self.bonbon = 0

	self.time = 300
	self.time_dim = -2

	self.updown = 0
	self.leftright = -1

def _level_5(self):
	self.nb_ligne = 36
	self.nb_colonne = 21

	_color(self, 4)

	_create_grille(self)

	self.tab_serpent_pos = [[34, 8], [34, 9], [34, 10], [34, 11], [34, 12]]
	self.tab_serpent = []

	self.murs_pos = []
	self.murs = []

	temp = _dessin_line(self, 3, 33, "x", 10)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 0, 15, "x", 0)
	self.murs += temp[0]
	self.murs_pos += temp[1]
	
	temp = _dessin_line(self, 21, 36, "x", 0)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 0, 15, "x", 21)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 21, 36, "x", 21)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 3, 18, "y", 18)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 0, 7, "y", 0)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 13, 21, "y", 0)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 0, 7, "y", 36)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 13, 21, "y", 36)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	self.miam_pos = [[9, 5], [27, 5], [9, 14], [27, 14]]
	self.miam = []
	self.miam.append(_dessin_rond(self, 9, 5))
	self.miam.append(_dessin_rond(self, 27, 5))
	self.miam.append(_dessin_rond(self, 9, 16))
	self.miam.append(_dessin_rond(self, 27, 16))

	self.entrer_level_suivant = [0, 12]
	self.limite_miam = 50
	if DEBUG: self.limite_miam = 1
	self.bonbon = 0

	self.time = 300
	self.time_dim = -2

	self.updown = -1
	self.leftright = 0

def _level_6(self):
	self.nb_ligne = 36
	self.nb_colonne = 21

	_color(self, 5)

	_create_grille(self)

	self.tab_serpent_pos = [[18, 5], [18, 6], [18, 7], [18, 8], [18, 9]]
	self.tab_serpent = []

	self.murs_pos = []
	self.murs = []

	temp = _dessin_line(self, 2, 16, "x", 5)
	self.murs += temp[0]
	self.murs_pos += temp[1]
	temp = _dessin_line(self, 2, 16, "x", 4)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 2, 16, "x", 10)
	self.murs += temp[0]
	self.murs_pos += temp[1]
	temp = _dessin_line(self, 2, 16, "x", 11)
	self.murs += temp[0]
	self.murs_pos += temp[1]
	
	temp = _dessin_line(self, 2, 16, "x", 16)
	self.murs += temp[0]
	self.murs_pos += temp[1]
	temp = _dessin_line(self, 2, 16, "x", 17)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 20, 34, "x", 5)
	self.murs += temp[0]
	self.murs_pos += temp[1]
	temp = _dessin_line(self, 20, 34, "x", 4)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 20, 34, "x", 10)
	self.murs += temp[0]
	self.murs_pos += temp[1]
	temp = _dessin_line(self, 20, 34, "x", 11)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	temp = _dessin_line(self, 20, 34, "x", 16)
	self.murs += temp[0]
	self.murs_pos += temp[1]
	temp = _dessin_line(self, 20, 34, "x", 17)
	self.murs += temp[0]
	self.murs_pos += temp[1]

	self.miam_pos = [[9, 7], [27, 7], [9, 12], [27, 12]]
	self.miam = []
	self.miam.append(_dessin_rond(self, 9, 7))
	self.miam.append(_dessin_rond(self, 27, 7))
	self.miam.append(_dessin_rond(self, 9, 14))
	self.miam.append(_dessin_rond(self, 27, 14))

	self.entrer_level_suivant = [0, 12]
	self.limite_miam = 50
	if DEBUG: self.limite_miam = 1
	self.bonbon = 0

	self.time = 300
	self.time_dim = -2

	self.updown = -1
	self.leftright = 0

def _play(self):

	self.updown = 0
	self.leftright = 1
	self.appui_touche = True
	self.niveau = 1
	self.continu = True
	self.quit = False
	self.tab_menu = []

	if self.mode:
		_level_1(self)
	else:
		_level_0(self)

	self.information = []
	self.information.append(self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, fill = self.cadrecouleur, font=("Purisa", 14)))
	self.information.append(self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.06, text = "Appuyer sur Echap pour retourner au menu principal", fill = self.cadrecouleur, font=("Purisa", 14)))

	def clavier(event):
		touche = event.keysym

		if DEBUG:
			print(touche)

		if touche == "Up" or touche == "z":
			if self.updown != 1 and self.leftright != 0 and self.appui_touche:
				self.updown = -1
				self.leftright = 0
				self.appui_touche = False
		
		if touche == "Down" or touche == "s":
			if self.updown != -1 and self.leftright != 0 and self.appui_touche:
				self.updown = 1
				self.leftright = 0
				self.appui_touche = False
		
		if touche == "Left" or touche == "q":
			if self.updown != 0 and self.leftright != 1 and self.appui_touche:
				self.updown = 0
				self.leftright = -1
				self.appui_touche = False
		
		if touche == "Right" or touche == "d":
			if self.updown != 0 and self.leftright != -1 and self.appui_touche:
				self.updown = 0
				self.leftright = 1
				self.appui_touche = False

		if touche == "Escape":
			self.quit = True
	
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
			self.rect.append(self.canvas.create_rectangle(self.WIDTH /3.96, self.HEIGHT /3.5, self.WIDTH /1.3333, self.HEIGHT /1.39, fill = self.background))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /3, text = "Vous avez perdu", fill = self.color, font=("Purisa", 14)))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /2, text = "Nb de bonbon : " + str(self.bonbon) + "    Niveau : " + str(self.niveau), fill = self.cadrecouleur, font=("Purisa", 14)))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT *2/3, text = "Cliquer ici pour retourner au menu principal", fill = self.cadrecouleur, font=("Purisa", 14)))

			def clique(event):
				if event.x < self.WIDTH /1.333 and event.x > self.WIDTH /3.96 and event.y < self.HEIGHT /1.39 and event.y > self.HEIGHT /3.5:
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
				self.information[0] = self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, fill = self.cadrecouleur, font=("Purisa", 14))
				_level_2(self)

			elif self.niveau == 2:
				self.niveau += 1
				self.information[0] = self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, fill = self.cadrecouleur, font=("Purisa", 14))
				_level_3(self)

			elif self.niveau == 3:
				self.niveau += 1
				self.information[0] = self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, fill = self.cadrecouleur, font=("Purisa", 14))
				_level_4(self)

			elif self.niveau == 4:
				self.niveau += 1
				self.information[0] = self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, fill = self.cadrecouleur, font=("Purisa", 14))
				_level_5(self)

			elif self.niveau == 5:
				self.niveau += 1
				self.information[0] = self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, fill = self.cadrecouleur, font=("Purisa", 14))
				_level_6(self)

			else:
				self.continu = False
				self.unbind("<Key>")
				self.rect = []
				self.rect.append(self.canvas.create_rectangle(self.WIDTH /3.96, self.HEIGHT /3.5, self.WIDTH /1.3333, self.HEIGHT /1.39, fill = self.background))
				self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /3, text = "Vous avez gagné !", fill = self.color, font=("Purisa", 14)))
				self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /2, text = "Niveau : " + str(self.niveau), fill = self.cadrecouleur, font=("Purisa", 14)))
				self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT *2/3, text = "Cliquer ici pour retourner au menu principal", fill = self.cadrecouleur, font=("Purisa", 14)))
				def clique(event):
					if event.x < self.WIDTH /1.333 and event.x > self.WIDTH /3.96 and event.y < self.HEIGHT /1.39 and event.y > self.HEIGHT /3.5:
						self.unbind("<Button-1>")
						self.unbind("<Key>")
						for elems in self.rect:
							self.canvas.delete(elems)
						_efface_grille(self)
						_create_menu(self)

				self.bind("<Button-1>", clique)

		if self.mode:
			self.canvas.itemconfig(self.information[0], text = "Niveau " + str(self.niveau) + "			Bonbons mangés : " + str(self.bonbon) + "		Bonbon restant : " + str(self.limite_miam), fill = self.cadrecouleur)
			self.canvas.itemconfig(self.information[1], fill = self.cadrecouleur)
		else:
			self.canvas.itemconfig(self.information[0], text = "Bonbons mangés : " + str(self.bonbon), fill = self.cadrecouleur)
			self.canvas.itemconfig(self.information[1], fill = self.cadrecouleur)
			if self.bonbon % 5 == 0:
				if self.change_color:
					_efface_grille(self)
					_color(self, random.randint(0, 6))
					self.change_color = False
					if self.bonbon % 20 == 0:
						if self.nb_colonne < 63:
							self.nb_colonne += 7
							self.nb_ligne += 12
						self.time -= 100
						if self.time < 50:
							self.time = 50
					_create_grille(self)
					self.miam = []
					for elems in self.miam_pos:
						self.miam.append(_dessin_rond(self, elems[0], elems[1]))
					self.information = []
					self.information.append(self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, fill = self.cadrecouleur, font=("Purisa", 14)))
					self.information.append(self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.06, text = "Appuyer sur Echap pour retourner au menu principal", fill = self.cadrecouleur, font=("Purisa", 14)))
			else:
				self.change_color = True
		if self.quit:
			self.continu = False
			self.unbind("<Key>")
			_efface_grille(self)
			_create_menu(self)

		if self.continu:
			self.after(self.time, boucle)
	
	boucle()
	self.bind("<Key>", clavier)


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

		_create_menu(self)
		
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

Changelog :
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
