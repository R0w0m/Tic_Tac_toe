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
		self.plits([1,3])

		self.show()


	def setupUi(self, MainWindow):
		MainWindow.resize(300, 350)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(0, 438, 321, 4))
		self.line.setLineWidth(2)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.line_2 = QtWidgets.QFrame(self.centralwidget)
		self.line_2.setGeometry(QtCore.QRect(150, 0, 20, 681))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.line_3 = QtWidgets.QFrame(self.centralwidget)
		self.line_3.setGeometry(QtCore.QRect(230, 0, 20, 681))
		self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.line_4 = QtWidgets.QFrame(self.centralwidget)
		self.line_4.setGeometry(QtCore.QRect(70, 0, 20, 681))
		self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.line_5 = QtWidgets.QFrame(self.centralwidget)
		self.line_5.setGeometry(QtCore.QRect(0, 559, 321, 2))
		self.line_5.setLineWidth(2)
		self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.line_2.raise_()
		self.line_3.raise_()
		self.line_4.raise_()
		self.line_5.raise_()
		self.line.raise_()

		def press_start():
			self.start_bt.deleteLater()

		self.start_bt = QtWidgets.QPushButton(self.centralwidget)
		self.start_bt.setGeometry(QtCore.QRect(100, 0, 81, 0))#131
		self.start_bt.setText("Start")
		#self.start_bt.setStyleSheet("background-color:black;\n""border:none;")
		self.start_bt.raise_()
		self.start_bt.clicked.connect(press_start)

		self.buts=[]
		self.sbuts=[]

		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.tmr)
		self.timer.start(3)


	def tmr(self):
		for x in self.buts:
			x[2]+=1
			if x[2] <= 131:
				x[0].setGeometry(x[1], 0, 81, x[2])
			else:
				x[0].setGeometry(x[1], x[2], 81, 131)

		for x in self.sbuts:
			x[2]+=1
			if x[2] <= 131:
				x[0].setGeometry(x[1], 0, 81, x[2])
			else:
				x[0].setGeometry(x[1], x[2], 81, 131)


	def plits(self, a):
		for x in a:
			if type(x) is int:
				self.add_but(x)
			else:
				self.add_but(x[0])
				self.add_second_but(x[1])
				

	def add_but(self, bt_num):
		if bt_num == 1:
			y = -1
		if bt_num == 2:
			y = 79
		if bt_num == 3:
			y = 159
		if bt_num == 4:
			y = 239

		def clicked_():
			bt.deleteLater()
			del self.buts[0]

		bt = QtWidgets.QPushButton(self.centralwidget)
		bt.setGeometry(QtCore.QRect(y, 0, 81, 0))#131
		bt.setStyleSheet("background-color:black;\n""border:none;")
		bt.raise_()
		self.buts.append([bt, y, 0])

		bt.clicked.connect(clicked_)


	def add_second_but(self, bt_num):
		if bt_num == 1:
			y = -1
		if bt_num == 2:
			y = 79
		if bt_num == 3:
			y = 159
		if bt_num == 4:
			y = 239

		def clicked_():
			bt.deleteLater()
			del self.sbuts[0]

		bt = QtWidgets.QPushButton(self.centralwidget)
		bt.setGeometry(QtCore.QRect(y, 0, 81, 0))#131
		bt.setStyleSheet("background-color:black;\n""border:none;")
		bt.raise_()
		self.sbuts.append([bt, y, 0])

		bt.clicked.connect(clicked_)

if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Main()
	ex.show()
	sys.exit(app.exec_())
	 


'''
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Записки')
        self.setWindowIcon(QIcon('web.png'))     


        # Вот ниже находится label, который нужно центрировать.
        lbl1 = QLabel('Привет! Что нового?', self)
        lbl1.setAlignment(Qt.AlignCenter)                      #  (Qt.AlignVCenter)
#        #lbl1.move(0, 0) #если раскоментировать, чуда не произойдёт

        btn = QPushButton('Button', self) # Бонусный вопрос: Как центрировать кнопку? :з
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(self.test)
#        btn.resize(btn.sizeHint())
#        btn.move(3, 15)
        
        layout = QVBoxLayout(self)                         # +++
        layout.addWidget(lbl1)                             # +++
        layout.addWidget(btn)                              # +++    
   
#        self.show()

    def test(self):
        print('test удался')'''
        
        



'''
app = QtWidgets.QApplication([])
 
#user_score = 0
#bot_score = 0
#A1 = "X"
#A2 = "O"
#bot_first = False
#winner_list = []
#field = [[None] * 3 for i in range(3)]
#buttons = []
#
#window = QtWidgets.QWidget()#window
#window.resize(300, 350)
#window.setLayout(QtWidgets.QGridLayout())






def user_move(num):#ход пользователя
	global user_score
	x = get_XY(num)[0]
	y = get_XY(num)[1]
	if field[x][y] == None:
		buttons[num].setText(A1)
		buttons[num].setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 50px; ')
		field[x][y] = 1
		user_score += 1
		update_score()
	if x+y == 4 and field[x][y] != None:
		check_winner()
	
def bot_move():#ход бота
	x = get_XY(i)[0]
	y = get_XY(i)[1]
	if field[x][y] == None:
		field[x][y] = 0



def check_winner():
	for i in range(3):
		if field[i][0] == field[i][1] == field[i][2]:
			winner_list.append([field[i][0], field[i][1], field[i][2]])
		if field[0][i] == field[1][i] == field[2][i]:
			winner_list.append([field[0][i], field[1][i], field[2][i]])
	if field[0][0] == field[1][1] == field[2][2]:
		winner_list.append([field[i][0], field[i][1], field[i][2]])
	if field[2][0] == field[1][1] == field[0][2]:
		winner_list.append([field[i][0], field[i][1], field[i][2]])

	if len(winner_list) > 0:
		relaunch_game()










def relaunch_game():
	global field
	for i in range(9):
		buttons[i].setStyleSheet('Background: rgb(200,200,200); border:none')
		buttons[i].setText("")
	field = [[None] * 3 for i in range(3)]
	winner_list.clear()
	update_score()



def update_score():
	label_.setText(f"{bot_score}:{user_score}")
	label_.setStyleSheet('Background: rgb(255,255,255); border: 2px dashed grary; font-size: 22px')

#____________         ____________
#____________Completed____________>>>


def get_XY(i):
	x = i//3
	y = i-(i//3)*3
	return [x,y]


def start():
	label_bot = QtWidgets.QLabel("Bot")#first label
	label_bot.setStyleSheet('Background: rgb(255,150,150); border:none; font-size: 22px')
	window.layout().addWidget(label_bot, 0, 0)
	label_user = QtWidgets.QLabel("You")#second label
	label_user.setStyleSheet('Background: rgb(150,150,255); border:none; font-size: 22px')
	window.layout().addWidget(label_user, 0, 2)
	label_ = QtWidgets.QLabel(f"{bot_score}:{user_score}")#third label
	label_.setStyleSheet('Background: rgb(255,255,255); border: 2px dashed grary; font-size: 22px')
	window.layout().addWidget(label_, 0, 1)
	
	for i in range(9):
		x = get_XY(i)[0]
		y = get_XY(i)[1]
		but = QtWidgets.QPushButton()
		but.clicked.connect(lambda event, i=i: user_move(i))
		window.layout().addWidget(but, x+1, y)
		but.setStyleSheet('Background: rgb(200,200,200); border:none')
		but.setFixedSize(100, 100)
		buttons.append(but)
 
start()

window.show()
 
app.exec_()

'''