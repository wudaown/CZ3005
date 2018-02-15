import sys
from PyQt4 import QtGui, QtCore
from TalkBox import *

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setWindowTitle("CZ3005 Assignment 2")
		extractAction = QtGui.QAction("", self)
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip("Leave the app")
		extractAction.triggered.connect(self.Quit)
		self.statusBar()
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("File")
		fileMenu.addAction(extractAction)

		self.view()

	def view(self):
		btn = QtGui.QPushButton("Quit", self)
		# btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.clicked.connect(self.Quit)
		self.show()

	def Quit(self):
		print("Quit !")
		sys.exit()



app = QtGui.QApplication(sys.argv)
GUI = Window()

sys.exit(app.exec_())
