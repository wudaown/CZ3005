from doctor import Doctor
import sys
from functools import partial
from PyQt4.QtGui import QWidget, QLabel, QPushButton, QApplication, QMainWindow, QHBoxLayout, QVBoxLayout
from PyQt4 import QtCore


class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.doctor = Doctor()
		self.w = StartWindow()
		self.showWindow()
	
	def showWindow(self):
		self.w.StartWindow(self)
		self.show()



class StartWindow(object):
	def StartWindow(self, MainWindow):
		self.doctor = MainWindow.doctor
		MainWindow.setGeometry(50, 50, 400, 450)
		MainWindow.setWindowTitle("Smmpathetic Doctor")
		self.x = self.doctor.read() 
		self.w = QWidget(MainWindow)
		self.l = QLabel(self.w)
		self.yes = QPushButton(self.w)
		self.no = QPushButton(self.w)
		self.l.setText("Do you exprience pain that is {0}?".format(self.x))
		self.yes.setText("Yes")
		self.no.setText("No")
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
		self.yes.clicked.connect(partial(self.yesClick))
		self.no.clicked.connect(partial(self.noClick))

	def yesClick(self):
		self.doctor.yesEvent(self.x)
		try:
			s, text = self.doctor.deterStep()
			self.x = self.doctor.read()
			self.l.setText(text + self.x)
		except TypeError:
			self.diag()
	
	def noClick(self):
		self.doctor.noEvent(self.x)
		try:
			s, text = self.doctor.deterStep()
			self.x = self.doctor.read()
			if self.x == None:
				self.doctor.setFalse(s)
			s, text = self.doctor.deterStep()
			self.x = self.doctor.read()
			self.l.setText(text + self.x)
		except TypeError:
			self.diag()
	
	def diag(self):
		if not self.doctor.lastCheck():
			s = self.doctor.result()
			if s == 'others':
				self.l.setText('The current knowledge base cannot determine your diseases')
			else:
				self.l.setText("You may have {0}".format(s))
		self.yes.clicked.disconnect()
		self.no.clicked.disconnect()
		self.yes.clicked.connect(QtCore.QCoreApplication.quit)
		self.no.clicked.connect(QtCore.QCoreApplication.quit)




def main():
	app = QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
