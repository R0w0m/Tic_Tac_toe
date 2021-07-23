import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
#import keyboard
#import time
import random
 



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

		self.bot_first = False
		self.difficulty = None
		# Easy    = 1
		# Normal  = 2
		# Hard    = 3
		# Extreme = 4


		self.user_score = 0
		self.bot_score = 0
		self.A1 = "X"
		self.A2 = "O"
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

		# Добавление кнопок (поля)
		for i in range(9): 
			x = self.get_XY(i)[0]
			y = self.get_XY(i)[1]
			but = QtWidgets.QPushButton()
			but.clicked.connect(lambda event, i=i: self.user_move(i))
			self.centralwidget.layout().addWidget(but, x+1, y)
			but.setStyleSheet('Background: rgb(200,200,200); border:none')
			but.setFixedSize(100, 100)
			self.buttons.append(but)



	# Ход пользователя
	def user_move(self, num):
		x = self.get_XY(num)[0]
		y = self.get_XY(num)[1]
		if  self.field[x][y] == None:
			self.buttons[num].setText(self.A1)
			self.buttons[num].setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 50px; ')
			self.field[x][y] = 1
			self.user_score += 1
			self.update_score()
		if num == 8:
			print(self.bot_logic())
			self.check_winner()

	# Ход бота
	def bot_move(self):
		i = self.bot_logic()
		x = self.get_XY(i)[0]
		y = self.get_XY(i)[1]
		if self.field[x][y] == None:
			self.buttons[num].setText(self.A2)
			self.buttons[num].setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 50px; ')
			self.field[x][y] = 1
			self.user_score += 1

	# Логика бота
	def bot_logic(self):
		free_positions = []
		# Добавление в массив "свободных клеток"
		for j in range(9):
			XY = self.get_XY(j)
			if self.field[XY[0]][XY[1]] == None:
				free_positions.append([XY[0], XY[1]])

		if len(free_positions) != 0:
			return free_positions[random.randint(0,(len(free_positions)))]
		else:
			return 0


	# Проверка поля на наличие 3 в ряд:
	# Добавление к счету---
	# Перезапуск+++
	def check_winner(self):
		for i in range(3):
			if self.field[i][0] == self.field[i][1] == self.field[i][2] != None:
				self.winner_list.append([[i,0], [i,1], [i,2]])
			if self.field[0][i] == self.field[1][i] == self.field[2][i] != None:
				self.winner_list.append([[0,i], [1,i], [2,i]])
		if self.field[0][0] == self.field[1][1] == self.field[2][2] != None:
			self.winner_list.append([[0,0], [1,1], [2,2]])
		if self.field[2][0] == self.field[1][1] == self.field[0][2] != None:
			self.winner_list.append([[2,0], [1,1], [0,2]])
		if len(self.winner_list) > 0:
			self.buttons[4].setText("Restart")
			self.buttons[4].setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 50px; ')
			self.buttons[4].clicked.connect(self.relaunch_game())
		# Если кто-то выиграл, то на кнопке посередине вылазиет надпись Restart
			

	# Перезапуск игры, очистка поля
	def relaunch_game(self):
		for i in range(9):
			self.buttons[i].setStyleSheet('Background: rgb(200,200,200); border:none')
			self.buttons[i].setText("")
		self.field = [[None] * 3 for i in range(3)]
		self.winner_list.clear()
		self.update_score()





#   ____________         ____________
#   ____________Completed____________>>>






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