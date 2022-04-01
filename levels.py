from color import _color
from dessins import _dessin_carre, _dessin_line, _dessin_rond
from menuEtGrille import _create_grille
from vars import DEBUG

def _level_0(self):
	self.nb_ligne = 24
	self.nb_colonne = 14
	_create_grille(self)
	self.tab_serpent_pos = [[4, 2], [3, 2], [2, 2]]
	self.tab_serpent = []

	self.murs_pos = []
	self.murs = []

	self.miam_pos = [[5, 7], [20, 7], [5, 10], [20, 10]]
	self.miam = []
	self.miam.append(_dessin_rond(self, 5, 7))
	self.miam.append(_dessin_rond(self, 20, 7))
	self.miam.append(_dessin_rond(self, 5, 10))
	self.miam.append(_dessin_rond(self, 20, 10))

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
	self.miam.append(_dessin_rond(self, 12, 11))

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

	self.miam_pos = [[9, 5], [27, 5], [9, 16], [27, 16]]
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
	self.miam.append(_dessin_rond(self, 9, 12))
	self.miam.append(_dessin_rond(self, 27, 12))

	self.entrer_level_suivant = [0, 12]
	self.limite_miam = 50
	if DEBUG: self.limite_miam = 1
	self.bonbon = 0

	self.time = 300
	self.time_dim = -2

	self.updown = -1
	self.leftright = 0
