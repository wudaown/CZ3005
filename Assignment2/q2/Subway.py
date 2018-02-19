from pyswip import *

class Subway(Prolog):
	def __init__(self):
		# super().__init__()
		self.mains = Functor('askMains', 1)
		self.cheeses = Functor('askCheeses', 1)
		self.vegs = Functor('askVegs', 1)
		self.sauces = Functor('askSauces', 1)
		self.cookies = Functor('askCookies', 1)
		self.addons = Functor('askAddons', 1)
		self.func = self.vegs
		self.selectMain = True
		self.selectCheeses = True
		self.selectVegs = True
		self.selectSauces = True
		self.selectCookies = True
		self.selectAddons = True
		self.prolog = Prolog()
		self.prolog.consult("Subway.pl")


	def setVeggie(self):
		self.selectMain = False
		self.selectCheeses = False

	def setVegan(self):
		self.selectMain = False
		self.selectCheeses = False
		self.selectCookies = False

	def askBread(self):
		n = list(self.prolog.query('askBread(X,Y)', maxresult=1))[0]['X']
		# print(n)
		return n

	def yesBread(self, y):
		self.prolog.asserta('order(' + y + ')')
		for i in list(self.prolog.query('askBread(X,' + y + ')')):
			if i['X'] != y:
				self.prolog.asserta('pass(' + i['X'] + ')')

		n = self.Event()
		return n

	def noBread(self, y):
		self.prolog.asserta('reject(' + y + ')')
		n = list(self.prolog.query('askBread(X,' + y + ')'))
		return n

	def nextBread(self, y):
		n = self.reject()
		for x in list(self.prolog.query('askBread(X,' + y + ')')):
			if x['X'] not in n:
				return x['X']

	def Event(self):
		self.deterFunc()
		# n = list(self.prolog.query('askMains(X)', maxresult=1))[0]['X']
		s = []
		a = []
		x = Variable()
		q = Query(self.func(x))
		while q.nextSolution():
			s.append(x.value)
		for i in s:
			a.append(i.value)

		# n =  q[0].value.value
		n = a[0]
		q.closeQuery()
		# print(n)
		return n



	def yesEvent(self, y):
		self.prolog.asserta('order(' + y + ')')


	def noEvent(self, y):
		self.prolog.asserta('reject(' + y + ')')

	def doneItem(self):
		if self.func is self.mains:
			self.selectMain = False
		elif self.func is self.cheeses:
			self.selectCheeses = False
		elif self.func is self.vegs:
			self.selectVegs = False
		elif self.func is self.sauces:
			self.selectSauces = False
		elif self.func is self.cookies:
			self.selectCookies = False
		elif self.func is self.addons:
			self.selectAddons = False

	def deterFunc(self):
		if self.selectMain:
			self.func = self.mains
		elif self.selectCheeses:
			self.func = self.cheeses
		elif self.selectVegs:
			self.func = self.vegs
		elif self.selectSauces:
			self.func = self.sauces
		elif self.selectCookies:
			self.func = self.cookies
		elif self.selectAddons:
			self.func = self.addons

	def nextToOffer(self, y):
		n = self.order() + self.reject()
		s = []
		a = []
		self.deterFunc()

		x = Variable()
		q = Query(self.func(x))
		while q.nextSolution():
			s.append(x.value)
		for i in s:
			a.append(i.value)

		q.closeQuery()
		for x in a:
			if x not in n:
				return x

	def order(self):
		n = list(self.prolog.query('order(X)'))
		o = []
		for i in n:
			o.append(i['X'])
		return o

	def reject(self):
		n = list(self.prolog.query('reject(X)'))
		o = []
		for i in n:
			o.append(i['X'])
		return o

