import sys
from functools import partial
from PyQt5 import QtWidgets

from TalkBox import Kid


class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.kid = Kid()
		self.y = self.kid.initEvent()
		self.w = QtWidgets.QWidget()
		self.yes = QtWidgets.QPushButton(self.w)
		self.no = QtWidgets.QPushButton(self.w)
		self.l = QtWidgets.QLabel(self.w)
		self.yes.setText("Yes")
		self.no.setText("No")
		# self.l.setText("Would you like to have {0}: ".format(initEvent()))
		self.l.setText("Would you like to have {0}: ".format(self.y))

		self.hbox = QtWidgets.QHBoxLayout()
		self.hbox.addStretch()
		self.hbox.addWidget(self.l)
		self.hbox.addStretch()

		self.vbox = QtWidgets.QVBoxLayout()
		self.vbox.addWidget(self.yes)
		self.vbox.addWidget(self.no)
		# self.# vbox.addWidget(l)
		self.vbox.addLayout(self.hbox)


		self.w.setLayout(self.vbox)

		# w.setGeometry(100,100,300,200)
		# yes.move(50, 100)
		# no.move(150, 100)
		# l.move(75, 50)
		self.yes.clicked.connect(partial(self.btnClicked))
		self.no.clicked.connect(partial(self.btnClicked))
		self.w.show()

	def btnClicked(self):
		text = self.kid.readQues()
		self.kid.yesEvent(self.y)
		x = self.kid.nextToOffer(self.y)
		if x == None:
			x = "None"
		self.l.setText(text + x)
		self.y = x
		print(self.y)
		# return y



def main():
	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
