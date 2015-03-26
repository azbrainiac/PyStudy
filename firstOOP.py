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
		common = gcd(newnum, newden)

		return Drobe(newnum//common, newden//common)

	def __eq__(self, otherfraction):
		newselfnum = self.num * otherfraction.den
		newothernum = otherfraction.num * self.den
		return newselfnum == newothernum


def gcd(m, n):
	while m % n != 0:
		oldm = m
		oldn = n
		m = oldn
		n = oldm % oldn
	return n

myfraction = Drobe(3, 5)

myfraction.show()

print(myfraction)

print(Drobe(3, 5) + Drobe(5, 3))
print(gcd(35, 14))
print(Drobe(3, 5) + Drobe(6, 10))
print(Drobe(3, 5) == Drobe(5, 3))
print(Drobe(3, 5) == Drobe(3, 5))