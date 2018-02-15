from pyswip import *
from random import randrange

class Kid(Prolog):
	def __init__(self):
		super().__init__()
		self.prolog = Prolog()
		self.prolog.consult("TalkBox.pl")
		self.filePath = 'question.txt'


	def initEvent(self):
		n = list(self.prolog.query('ask(X,Y)', maxresult=1))[0]['X']
		print(n)
		return n

	def readQues(self):
		file = open(self.filePath,'r')
		quesList = []
		for i in file:
			quesList.append(list(i.split(",")))

		for i in quesList:
			x = randrange(1, len(i))
			question = (i[x])

		file.close()
		return question

	def yesEvent(self, y):
		self.prolog.asserta('order(' + y + ')')
		n = list(self.prolog.query('ask(X,' + y + ')'))
		return n


	def noEvent(self, y):
		self.prolog.asserta('reject(' + y + ')')
		n = list(self.prolog.query('ask(X,' + y + ')'))
		return n

	def nextToOffer(self, y):
		n = self.order()
		for x in list(self.prolog.query('ask(X,' + y + ')')):
			if x['X'] not in n:
				return x['X']
				# print(x['X'])
				# return True

	def order(self):
		n = list(self.prolog.query('order(X)'))
		o = []
		for i in n:
			o.append(i['X'])
		return o

