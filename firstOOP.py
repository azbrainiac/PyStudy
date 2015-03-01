class Drobe:
	
	def __init__(self, top, bottom):

		self.num = top
		self.den = bottom

	def show(self):
		print(self.num, "/", self.den)

	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	def __add__(self, otherfraction):
		
		newnum = self.num * otherfraction.den + self.den * otherfraction.num
		newden = self.den * otherfraction.den

		return Drobe(newnum, newden)

myfraction = Drobe(3, 5)

myfraction.show()

print(myfraction)

print(Drobe(3, 5) + Drobe(5, 3))