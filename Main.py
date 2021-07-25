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

		self.bot_first = False # True/False
		self.difficulty = None
		# Easy    = 1
		# Normal  = 2
		# Hard    = 3
		# Extreme = 4


		self.user_score = 0
		self.bot_score = 0
		self.A1 = "X"
		self.A2 = "O"
		self.game_not_stop = True
		self.winner_list = []
		self.field = [[None] * 3 for i in range(3)]
		self.buttons = []

		self.start()


	def chose_difficulty(self):
		self.start_but = QtWidgets.QPushButton()
		self.start_but.clicked.connect(lambda : self.start())
		self.start_but.setStyleSheet('Background: rgb(200,200,200); border:none')
		self.start_but.setGeometry(100, 100)

	def start(self):
		self.label_bot = QtWidgets.QLabel("Bot")
		self.label_bot.setStyleSheet('Background: rgb(255,150,150); border:none; font-size: 22px')
		self.centralwidget.layout().addWidget(self.label_bot, 0, 0)
		self.label_user = QtWidgets.QLabel("You")
		self.label_user.setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 22px')
		self.centralwidget.layout().addWidget(self.label_user, 0, 2)
		self.label_ = QtWidgets.QLabel(f"{self.bot_score}:{self.user_score}")
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
		if self.game_not_stop:
			x = self.get_XY(num)[0]
			y = self.get_XY(num)[1]
			if  self.field[x][y] == None:
				self.buttons[num].setText(self.A1)
				self.buttons[num].setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 50px; ')
				self.field[x][y] = 1
				self.check_winner()
				self.bot_move()
				self.check_winner()
		elif num == 4:
			self.relaunch_game()

	# Ход бота
	def bot_move(self):
		if self.game_not_stop and (not self.field_is_full()):
			i = self.bot_logic()
			x = i[0]
			y = i[1]
			num = self.get_num(x,y)
			if self.field[x][y] == None:
				self.buttons[num].setText(self.A2)
				self.buttons[num].setStyleSheet('Background: rgb(255,150,150); border:none; font-size: 50px; ')
				self.field[x][y] = 0

	# Логика бота(пока просто рандомные позиции)
	def bot_logic(self):
		free_positions = []
		for j in range(9):
			XY = self.get_XY(j)
			if self.field[XY[0]][XY[1]] == None:
				free_positions.append([XY[0], XY[1]])

		if len(free_positions) != 0:
			return random.choice(free_positions)
		else:
			return [0,0]


	# Проверка поля на наличие 3 в ряд:
	# Добавление к счету+-+
	# Перезапуск+++
	def check_winner(self):
		# Проверка по вертикали и горизонтали >>>
		for i in range(3):
			if self.field[i][0] == self.field[i][1] == self.field[i][2] != None:
				self.winner_list.append([[i,0], [i,1], [i,2]])
			if self.field[0][i] == self.field[1][i] == self.field[2][i] != None:
				self.winner_list.append([[0,i], [1,i], [2,i]])
		# По диагоналям >>>
		if self.field[0][0] == self.field[1][1] == self.field[2][2] != None:
			self.winner_list.append([[0,0], [1,1], [2,2]])
		if self.field[2][0] == self.field[1][1] == self.field[0][2] != None:
			self.winner_list.append([[2,0], [1,1], [0,2]])


		# Если нашлось "3 в ряд" и пустые клетки >>>
		if len(self.winner_list) > 0 or self.field_is_full():
			self.game_not_stop = False
			x = None # 0 - победил бот, 1 - победил юзер
			if self.field[self.winner_list[0][0][0]][self.winner_list[0][0][1]] == 1:
				self.user_score += 1
				x = 1
			else:
				self.bot_score += 1
				x = 0
			# Рамки >>>
			cantral_butt_w = "border: none;"
			for row in self.winner_list:
				for cage in row:
					self.buttons[self.get_num(cage[0],cage[1])].setStyleSheet(f'Background: rgb({150+(105*(1-x))},150,{150+(105*x)}); border: 5px solid rgb(110,255,110); font-size: 50px')
					if cage[0] == cage[1] == 1:
						cantral_butt_w = "border:5px solid rgb(110,255,110);"
			self.game_not_stop = False
			# Restart button >>>
			self.buttons[4].setText("Restart")
			self.buttons[4].setStyleSheet(f'Background: rgb({150+(105*(1-x))},150,{150+(105*x)}); {cantral_butt_w} font-size: 20px; ')
			#self.buttons[4].clicked.connect(lambda event: self.relaunch_game())
			

	# Перезапуск игры, очистка поля
	def relaunch_game(self):
		for i in range(9):
			self.buttons[i].setStyleSheet('Background: rgb(200,200,200); border:none')
			self.buttons[i].setText("")
		#self.buttons[4].clicked.connect(lambda event: self.user_move(4))
		self.field = [[None] * 3 for i in range(3)]
		self.winner_list.clear()
		self.update_score()
		self.game_not_stop = True



	def field_is_full(self):
		print(self.field)
		return None in [cage for cage in self.field]

	def get_num(self,x,y):
		return x*3+y

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
git add file.py
git commit -m "comentary"
git push -u origin main


'''