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
