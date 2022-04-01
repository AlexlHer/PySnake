from color import _color
from dessins import _dessin_carre, _dessin_line
from play import _play
from play2P import _play2p
from vars import version


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

	self.tab_menu += _dessin_line(self, 24, 40, "x", 20)[0]
	self.tab_menu += _dessin_line(self, 24, 40, "x", 16)[0]
	self.tab_menu += _dessin_line(self, 16, 20, "y", 24)[0]
	self.tab_menu += _dessin_line(self, 16, 20, "y", 40)[0]
	self.tab_menu.append(self.canvas.create_text(self.WIDTH /1.333, self.HEIGHT /1.27, text = "Mode infinie - Niveau sans murs", fill = "#ffffff", font=("Purisa", 14)))

	self.tab_menu += _dessin_line(self, 2, 18, "x", 14)[0]
	self.tab_menu += _dessin_line(self, 2, 18, "x", 10)[0]
	self.tab_menu += _dessin_line(self, 10, 14, "y", 2)[0]
	self.tab_menu += _dessin_line(self, 10, 14, "y", 18)[0]
	self.tab_menu.append(self.canvas.create_text(self.WIDTH /3.9, self.HEIGHT /1.85, text = "Mode 2 joueurs - VS", fill = "#ffffff", font=("Purisa", 14)))
	"""
	self.tab_menu += _dessin_line(self, 2, 18, "x", 20)[0]
	self.tab_menu += _dessin_line(self, 2, 18, "x", 16)[0]
	self.tab_menu += _dessin_line(self, 16, 20, "y", 2)[0]
	self.tab_menu += _dessin_line(self, 16, 20, "y", 18)[0]
	self.tab_menu.append(self.canvas.create_text(self.WIDTH /3.9, self.HEIGHT /1.27, text = "Mode 2 joueurs - Course", fill = "#ffffff", font=("Purisa", 14)))
	"""
	self.tab_menu.append(self.canvas.create_text(self.WIDTH/2, self.HEIGHT * 1.02, text = version, fill = self.cadrecouleur, font=("Purisa", 14)))

	def clique(event):
		if event.x < self.WIDTH /1.06 and event.x > self.WIDTH /1.8 and event.y < self.HEIGHT /1.55 and event.y > self.HEIGHT /2.25:
			self.unbind("<Button-1>")
			_efface_menu(self)
			self.mode = True
			_play(self)

		if event.x < self.WIDTH /1.06 and event.x > self.WIDTH /1.8 and event.y < self.HEIGHT /1.12 and event.y > self.HEIGHT /1.47:
			self.unbind("<Button-1>")
			_efface_menu(self)
			self.mode = False
			_play(self)

		if event.x < self.WIDTH /2.25 and event.x > self.WIDTH /16 and event.y < self.HEIGHT /1.55 and event.y > self.HEIGHT /2.25:
			self.unbind("<Button-1>")
			_efface_menu(self)
			self.mode = False
			_play2p(self)
		"""
		if event.x < self.WIDTH /2.25 and event.x > self.WIDTH /16 and event.y < self.HEIGHT /1.12 and event.y > self.HEIGHT /1.47:
			self.unbind("<Button-1>")
			_efface_menu(self)
			self.mode = True
			_play2p(self)
		"""

	self.bind("<Button-1>", clique)

def _efface_menu(self):
	for elems in self.tab_menu:
		self.canvas.delete(elems)

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

def _efface_grille_2p(self):
	for elems in self.tab_menu:
		self.canvas.delete(elems)
	for elems in self.tab_serpent1:
		self.canvas.delete(elems)
	for elems in self.tab_serpent2:
		self.canvas.delete(elems)
	for elems in self.murs:
		self.canvas.delete(elems)
	#for elems in self.miam:
	#	self.canvas.delete(elems)
	self.canvas.delete(self.information[0])
	self.canvas.delete(self.information[1])
