from color import _color
from menuEtGrille import _create_grille

def _level_2p_0(self):
	_color(self, -1)
	self.nb_ligne = 144
	self.nb_colonne = 84
	_create_grille(self)
	self.tab_serpent1_pos = [[144, 84]]
	self.tab_serpent1 = []

	self.tab_serpent2_pos = [[0, 84]]
	self.tab_serpent2 = []

	self.murs_pos = []
	self.murs = []

	self.limite_miam = 9999
	self.bonbon1 = 0
	self.bonbon2 = 0

	self.time = 100
	self.time_dim = 0
	self.change_color = False
