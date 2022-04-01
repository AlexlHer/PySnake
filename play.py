import random
from color import _color
from dessins import _dessin_carre, _dessin_rond
from levels import _level_0, _level_1, _level_2, _level_3, _level_4, _level_5, _level_6
from menuEtGrille import _create_grille, _create_menu, _efface_grille
from vars import DEBUG


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
			if touche == "plus":
				self.bonbon += 1
				self.limite_miam -= 1
			if touche == "minus":
				self.bonbon -= 1
				self.limite_miam += 1
			if touche == "asterisk":
				temp = _verif_miam(self)
				_changement_de_bonbon(self, temp)
				DEBUG_bonbon = True
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
		global DEBUG_bonbon
		_avance_serpent(self)

		temp = _verif_miam(self)
		if DEBUG and DEBUG_bonbon:
			del self.tab_serpent_pos[len(self.tab_serpent_pos)-1]
			DEBUG_bonbon = False
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
					if self.bonbon % 100 == 0:
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
