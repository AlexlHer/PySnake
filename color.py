def _color(self, num_couleur):
	if num_couleur == -1:
		self.color = "#000000"
		self.background = "#000000"
		self.cadrecouleur = "#ffffff"
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
