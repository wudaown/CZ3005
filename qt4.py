import sys
from functools import partial
from PyQt4.QtGui import QWidget, QLabel, QPushButton, QApplication, QMainWindow, QHBoxLayout, QVBoxLayout

from TalkBox import Kid

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.kid = Kid()
		self.w = selectBread()
		self.o = selectOther()
		self.d = finalMenu()
		self.c = catMenu()
		self.startCat()

	def startBread(self):
		self.w.setupWindow(self)
		self.w.yes.clicked.connect(partial(self.startOther))
		self.show()

	def startOther(self):
		self.o.setupWindow(self)
		self.o.done.clicked.connect(partial(self.startFinal))
		self.show()

	def startFinal(self):
		self.d.FinalMenu(self)
		self.show()

	def startCat(self):
		self.c.catMenu(self)
		self.c.normal.clicked.connect(partial(self.startBread))
		self.c.veggie.clicked.connect(partial(self.startBread))
		self.c.vegan.clicked.connect(partial(self.startBread))
		self.show()

class catMenu(object):
	def catMenu(self, MainWindow):
		self.kid = MainWindow.kid
		MainWindow.setGeometry(50, 50, 400, 450)
		# MainWindow.setFixedSize(400, 450)
		MainWindow.setWindowTitle("Category Menu")
		self.w = QWidget(MainWindow)
		self.l = QLabel("Select you meal type", self.w)
		self.normal = QPushButton("Normal", self.w)
		self.veggie = QPushButton("Vegetarian", self.w)
		self.vegan = QPushButton("Vegan", self.w)
		MainWindow.setCentralWidget(self.w)

		self.hbox = QHBoxLayout()
		self.hbox.addStretch()
		self.hbox.addWidget(self.l)
		self.hbox.addStretch()
		self.vbox = QVBoxLayout()
		self.vbox.addWidget(self.normal)
		self.vbox.addWidget(self.veggie)
		self.vbox.addWidget(self.vegan)
		self.vbox.addLayout(self.hbox)
		self.w.setLayout(self.vbox)

		self.veggie.clicked.connect(partial(self.kid.setVeggie))
		self.vegan.clicked.connect(partial(self.kid.setVegan))

class finalMenu(object):
	def FinalMenu(self, MainWindow):
		self.kid = MainWindow.kid
		self.order = self.kid.order()
		self.f = ''
		for i in self.order:
			self.f = self.f + i +'\n'
		MainWindow.setGeometry(50, 50, 400, 450)
		# MainWindow.setFixedSize(400, 450)
		MainWindow.setWindowTitle("Final Menu")
		self.w = QWidget(MainWindow)
		self.l = QLabel("Final Menu", self.w)
		self.finalLabel = QLabel(self.f, self.w)
		# self.finalLabel.move(50,50)
		self.l.move(170,0)
		self.finalLabel.move(170,100)
		MainWindow.setCentralWidget(self.w)

class selectOther(object):
	def setupWindow(self, MainWindow):
		self.kid = MainWindow.kid
		self.y = self.kid.Event()
		MainWindow.setGeometry(50, 50, 400, 450)
		# MainWindow.setFixedSize(400, 450)
		MainWindow.setWindowTitle("Select Other")
		self.w = QWidget(MainWindow)
		self.l = QLabel("Would you like to have {0}".format(self.y), self.w)
		self.yes = QPushButton('Yes', self.w)
		self.no = QPushButton("No", self.w)
		self.c = QPushButton("Continue to next category", self.w)
		self.done = QPushButton("Done ordering", self.w)
		# self.yes.move(50, 350)
		# self.no.move(150, 350)
		# self.c.move(150,300)
		# self.done.move(50,400 )
		MainWindow.setCentralWidget(self.w)

		self.hbox = QHBoxLayout()
		self.hbox.addStretch()
		self.hbox.addWidget(self.l)
		self.hbox.addStretch()

		self.vbox = QVBoxLayout()
		self.vbox.addWidget(self.yes)
		self.vbox.addWidget(self.no)
		self.vbox.addWidget(self.c)
		self.vbox.addWidget(self.done)
		self.vbox.addLayout(self.hbox)
		self.w.setLayout(self.vbox)

		self.yes.clicked.connect(partial(self.nextItemYes))
		self.no.clicked.connect(partial(self.nextItemNo))
		self.c.clicked.connect(partial(self.conItem))

	def conItem(self):
		text = "Would you like to have "
		self.kid.doneItem()
		x = self.kid.nextToOffer(self.y)
		self.l.setText(text + x)
		self.y = x
		# print(self.y)

	def nextItemYes(self):
		text = "Would you like to have "
		self.kid.yesEvent(self.y)
		x = self.kid.nextToOffer(self.y)
		if x == None:
			self.kid.retractall('reject(X)')
		x = self.kid.nextToOffer(self.y)
		self.l.setText(text + x)
		self.y = x
		# print(self.y)

	def nextItemNo(self):
		text = "How about "
		self.kid.noEvent(self.y)
		x = self.kid.nextToOffer(self.y)
		if x == None:
			self.kid.retractall('reject(X)')
		x = self.kid.nextToOffer(self.y)
		self.l.setText(text + x)
		self.y = x
		# print(self.y)


class selectBread(object):
	def setupWindow(self, MainWindow):
		self.kid = MainWindow.kid
		self.y = self.kid.askBread()
		MainWindow.setGeometry(50, 50, 400, 450)
		# MainWindow.setFixedSize(400, 450)
		MainWindow.setWindowTitle("Window")
		self.w = QWidget(MainWindow)
		self.l = QLabel(self.w)
		self.yes = QPushButton(self.w)
		self.no = QPushButton(self.w)
		self.l.setText("Would you like to have {0}: ".format(self.y))
		self.yes.setText("Yes")
		self.no.setText("No")
		# self.l.move(80,50)
		# self.yes.move(70,100)
		# self.no.move(150,100)
		MainWindow.setCentralWidget(self.w)

		self.hbox = QHBoxLayout()
		self.hbox.addStretch()
		self.hbox.addWidget(self.l)
		self.hbox.addStretch()

		self.vbox = QVBoxLayout()
		self.vbox.addWidget(self.yes)
		self.vbox.addWidget(self.no)
		self.vbox.addLayout(self.hbox)


		self.w.setLayout(self.vbox)

		self.yes.clicked.connect(partial(self.btnBread))
		self.no.clicked.connect(partial(self.btnBreadNo))

	def btnBread(self):
		text = "Would you like to have "
		x = self.kid.yesBread(self.y)
		if x == None:
			self.kid.retractall()
		self.l.setText(text + x)
		self.y = x
		# print(self.y)

	def btnBreadNo(self):
		text = "How about "
		self.kid.noBread(self.y)
		x = self.kid.nextBread(self.y)
		if x == None:
			self.kid.retractall('reject(X)')
		x = self.kid.nextBread(self.y)
		self.l.setText(text + x)
		self.y = x
		# print(self.y)



def main():
	app = QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
