import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import keyboard
import time
from PyQt5 import QtWidgets
 

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import keyboard
import time


class Main(QWidget):

	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.show()


	def setupUi(self, MainWindow):
		MainWindow.resize(330, 367)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.centralwidget.setLayout(QtWidgets.QGridLayout())

		self.user_score = 0
		self.bot_score = 0
		self.A1 = "X"
		self.A2 = "O"
		self.bot_first = False
		self.winner_list = []
		self.field = [[None] * 3 for i in range(3)]
		self.buttons = []

		self.start()




	def start(self):
		self.label_bot = QtWidgets.QLabel("Bot")#first label
		self.label_bot.setStyleSheet('Background: rgb(255,150,150); border:none; font-size: 22px')
		self.centralwidget.layout().addWidget(self.label_bot, 0, 0)
		self.label_user = QtWidgets.QLabel("You")#second label
		self.label_user.setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 22px')
		self.centralwidget.layout().addWidget(self.label_user, 0, 2)
		self.label_ = QtWidgets.QLabel(f"{self.bot_score}:{self.user_score}")#third label
		self.label_.setStyleSheet('Background: rgb(255,255,255); border: 2px dashed grary; font-size: 22px')
		self.centralwidget.layout().addWidget(self.label_, 0, 1)


		for i in range(9):
			x = self.get_XY(i)[0]
			y = self.get_XY(i)[1]
			but = QtWidgets.QPushButton()
			but.clicked.connect(lambda event, i=i: self.user_move(i))
			self.centralwidget.layout().addWidget(but, x+1, y)
			but.setStyleSheet('Background: rgb(200,200,200); border:none')
			but.setFixedSize(100, 100)
			self.buttons.append(but)




	def user_move(self, num):#ход пользователя
		x = self.get_XY(num)[0]
		y = self.get_XY(num)[1]
		if  self.field[x][y] == None:
			self.buttons[num].setText(self.A1)
			self.buttons[num].setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 50px; ')
			self.field[x][y] = 1
			self.user_score += 1
			self.update_score()
		if x+y == 4 and self.field[x][y] != None:
			self.check_winner()


	def check_winner(self):
		for i in range(3):
			if self.field[i][0] == self.field[i][1] == self.field[i][2]:
				self.winner_list.append([self.field[i][0], self.field[i][1], self.field[i][2]])
			if self.field[0][i] == self.field[1][i] == self.field[2][i]:
				self.winner_list.append([self.field[0][i], self.field[1][i], self.field[2][i]])
		if self.field[0][0] == self.field[1][1] == self.field[2][2]:
			self.winner_list.append([self.field[i][0], self.field[i][1], self.field[i][2]])
		if self.field[2][0] == self.field[1][1] == self.field[0][2]:
			self.winner_list.append([self.field[i][0], self.field[i][1], self.field[i][2]])
	
		if len(self.winner_list) > 0:
			relaunch_game()



#____________         ____________
#____________Completed____________>>>


	def get_XY(self, i):
		x = i//3
		y = i-(i//3)*3
		return [x,y]


	def update_score(self):
		self.label_.setText(f"{self.bot_score}:{self.user_score}")
		self.label_.setStyleSheet('Background: rgb(255,255,255); border: 2px dashed grary; font-size: 22px')






				



if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Main()
	ex.show()
	sys.exit(app.exec_())
	 


'''

git commands

git init
git status
git commit -m "comentary"
git push -u origin main


'''
        
        
