
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import keyboard
import time
from PyQt5 import QtWidgets




app = QtWidgets.QApplication([])
 
user_score = 0
bot_score = 0
A1 = "X"
A2 = "O"
bot_first = False
winner_list = []
field = [[None] * 3 for i in range(3)]
buttons = []

window = QtWidgets.QWidget()#window
window.resize(300, 350)
window.setLayout(QtWidgets.QGridLayout())






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
 


window.show()
 
app.exec_()