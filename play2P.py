from dessins import _dessin_carre
from levels2P import _level_2p_0
from menuEtGrille import _create_menu, _efface_grille_2p
from play import _verif_pos
from vars import DEBUG


def _play2p(self):

	self.updown1 = 0
	self.leftright1 = -1
	self.updown2 = 0
	self.leftright2 = 1
	self.appui_touche1 = True
	self.appui_touche2 = True
	self.niveau = 1
	self.continu = True
	self.quit = False
	self.tab_menu = []

	if self.mode:
		_level_2p_0(self)
	else:
		_level_2p_0(self)

	self.information = []
	self.information.append(self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, fill = self.cadrecouleur, font=("Purisa", 14)))
	self.information.append(self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.06, text = "Appuyer sur Echap pour retourner au menu principal", fill = self.cadrecouleur, font=("Purisa", 14)))

	def clavier(event):
		touche = event.keysym

		if DEBUG:
			print(touche)

		if touche == "Up":
			if self.updown1 != 1 and self.leftright1 != 0 and self.appui_touche1:
				self.updown1 = -1
				self.leftright1 = 0
				self.appui_touche1 = False

		if touche == "Down":
			if self.updown1 != -1 and self.leftright1 != 0 and self.appui_touche1:
				self.updown1 = 1
				self.leftright1 = 0
				self.appui_touche1 = False

		if touche == "Left":
			if self.updown1 != 0 and self.leftright1 != 1 and self.appui_touche1:
				self.updown1 = 0
				self.leftright1 = -1
				self.appui_touche1 = False

		if touche == "Right":
			if self.updown1 != 0 and self.leftright1 != -1 and self.appui_touche1:
				self.updown1 = 0
				self.leftright1 = 1
				self.appui_touche1 = False

		if touche == "z":
			if self.updown2 != 1 and self.leftright2 != 0 and self.appui_touche2:
				self.updown2 = -1
				self.leftright2 = 0
				self.appui_touche2 = False

		if touche == "s":
			if self.updown2 != -1 and self.leftright2 != 0 and self.appui_touche2:
				self.updown2 = 1
				self.leftright2 = 0
				self.appui_touche2 = False

		if touche == "q":
			if self.updown2 != 0 and self.leftright2 != 1 and self.appui_touche2:
				self.updown2 = 0
				self.leftright2 = -1
				self.appui_touche2 = False

		if touche == "d":
			if self.updown2 != 0 and self.leftright2 != -1 and self.appui_touche2:
				self.updown2 = 0
				self.leftright2 = 1
				self.appui_touche2 = False

		if touche == "Escape":
			self.quit = True

	def boucle():

		_avance_serpent_2p(self)

		if _verif_perdu_2p(self, 1):
			self.continu = False
			self.unbind("<Key>")
			self.rect = []
			self.rect.append(self.canvas.create_rectangle(self.WIDTH /3.96, self.HEIGHT /3.5, self.WIDTH /1.3333, self.HEIGHT /1.39, fill = self.background))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /3, text = "Joueur 1 : Vous avez perdu", fill = self.color, font=("Purisa", 14)))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /2, text = "Joueur 2 : Vous avez gagné", fill = self.color, font=("Purisa", 14)))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT *2/3, text = "Cliquer ici pour retourner au menu principal", fill = self.cadrecouleur, font=("Purisa", 14)))

			def clique(event):
				if event.x < self.WIDTH /1.333 and event.x > self.WIDTH /3.96 and event.y < self.HEIGHT /1.39 and event.y > self.HEIGHT /3.5:
					self.unbind("<Button-1>")
					self.unbind("<Key>")
					for elems in self.rect:
						self.canvas.delete(elems)
					_efface_grille_2p(self)
					_create_menu(self)

			self.bind("<Button-1>", clique)

		if _verif_perdu_2p(self, 2):
			self.continu = False
			self.unbind("<Key>")
			self.rect = []
			self.rect.append(self.canvas.create_rectangle(self.WIDTH /3.96, self.HEIGHT /3.5, self.WIDTH /1.3333, self.HEIGHT /1.39, fill = self.background))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /3, text = "Joueur 2 : Vous avez perdu", fill = self.color, font=("Purisa", 14)))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT /2, text = "Joueur 1 : Vous avez gagné", fill = self.color, font=("Purisa", 14)))
			self.rect.append(self.canvas.create_text(self.WIDTH /2, self.HEIGHT *2/3, text = "Cliquer ici pour retourner au menu principal", fill = self.cadrecouleur, font=("Purisa", 14)))

			def clique(event):
				if event.x < self.WIDTH /1.333 and event.x > self.WIDTH /3.96 and event.y < self.HEIGHT /1.39 and event.y > self.HEIGHT /3.5:
					self.unbind("<Button-1>")
					self.unbind("<Key>")
					for elems in self.rect:
						self.canvas.delete(elems)
					_efface_grille_2p(self)
					_create_menu(self)

			self.bind("<Button-1>", clique)

		self.appui_touche1 = True
		self.appui_touche2 = True

		if self.mode:
			self.canvas.itemconfig(self.information[0], text = "Niveau " + str(self.niveau) + "			Bonbons mangés : " + str(self.bonbon1) + "		Bonbon restant : " + str(self.limite_miam), fill = self.cadrecouleur)
			self.canvas.itemconfig(self.information[1], fill = self.cadrecouleur)
		else:
			self.canvas.itemconfig(self.information[0], text = "Bonbons mangés : " + str(self.bonbon1), fill = self.cadrecouleur)
			self.canvas.itemconfig(self.information[1], fill = self.cadrecouleur)

		if self.quit:
			self.continu = False
			self.unbind("<Key>")
			_efface_grille_2p(self)
			_create_menu(self)

		if self.continu:
			self.after(self.time, boucle)

	boucle()
	self.bind("<Key>", clavier)

def _avance_serpent_2p(self):
	for elems in self.tab_serpent1:
		self.canvas.delete(elems)

	self.tab_serpent1 = []
	temp = [[0, 0]]

	(temp[0][0], temp[0][1]) = _verif_pos(self, self.tab_serpent1_pos[0][0] + self.leftright1, self.tab_serpent1_pos[0][1] + self.updown1)

	self.color = "#ff0000"
	self.tab_serpent1.append(_dessin_carre(self, temp[0][0], temp[0][1]))

	for elems in self.tab_serpent1_pos:
		self.tab_serpent1.append(_dessin_carre(self, elems[0], elems[1]))
		temp.append([elems[0], elems[1]])

	self.tab_serpent1_pos = temp


	for elems in self.tab_serpent2:
		self.canvas.delete(elems)

	self.tab_serpent2 = []
	temp = [[0, 0]]

	(temp[0][0], temp[0][1]) = _verif_pos(self, self.tab_serpent2_pos[0][0] + self.leftright2, self.tab_serpent2_pos[0][1] + self.updown2)

	self.color = "#5050ff"
	self.tab_serpent2.append(_dessin_carre(self, temp[0][0], temp[0][1]))

	for elems in self.tab_serpent2_pos:
		self.tab_serpent2.append(_dessin_carre(self, elems[0], elems[1]))
		temp.append([elems[0], elems[1]])

	self.tab_serpent2_pos = temp

def _verif_perdu_2p(self, a):
	temp = []
	if a == 1:
		for i in range(1, len(self.tab_serpent1_pos)):
			temp.append(self.tab_serpent1_pos[i])

		if self.tab_serpent1_pos[0] in temp or self.tab_serpent1_pos[0] in self.murs_pos or self.tab_serpent1_pos[0] in self.tab_serpent2_pos:
			return True
	else:
		for i in range(1, len(self.tab_serpent2_pos)):
			temp.append(self.tab_serpent2_pos[i])

		if self.tab_serpent2_pos[0] in temp or self.tab_serpent2_pos[0] in self.murs_pos or self.tab_serpent2_pos[0] in self.tab_serpent1_pos:
			return True

	return False
