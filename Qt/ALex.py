from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from test0517 import Ui_answer_2
import sys

def load():
    x1 = int(ui.lineEdit_1.text())
    x2 = int(ui.lineEdit_2.text())
    x3 = int(ui.lineEdit_3.text())
    x4 = int(ui.lineEdit_4.text())
    x5 = int(ui.lineEdit_5.text())
    x6 = int(ui.lineEdit_6.text())
    x7 = int(ui.lineEdit_7.text())
    x8 = int(ui.lineEdit_8.text())
    x9 = int(ui.lineEdit_9.text())
    y1 = int(ui.lineEdit_11.text())
    y2 = int(ui.lineEdit_12.text())
    y3 = int(ui.lineEdit_13.text())
    y4 = int(ui.lineEdit_14.text())
    y5 = int(ui.lineEdit_15.text())
    y6 = int(ui.lineEdit_16.text())
    y7 = int(ui.lineEdit_17.text())
    y8 = int(ui.lineEdit_18.text())
    y9 = int(ui.lineEdit_19.text())
    global matrix_1 
    matrix_1 = [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]]
    global matrix_2 
    matrix_2 = [[y1,y2,y3],[y4,y5,y6],[y7,y8,y9]]


def initialize():
    global matrix_3
    for i in range(3):
        for j in range(3):
            matrix_3[i][j] = 0
            
def show():
    load()
    initialize()
    per = re_val()
    if ui.reverse.isChecked():
        change()
    if ui.ADD.isChecked():
        add(per)
    elif ui.SUBTRACTION.isChecked():
        subtraction(per)
    elif ui.MULTIPLICATION.isChecked():
        multiplication(per)
    elif ui.DET.isChecked():
        matdet_1 = determinant(matrix_1)
        matdet_2 = determinant(matrix_2)

        ui.label.setText("matrix_1 : "+str(matdet_1)+"\n"+"matrix_2 : "+str(matdet_2))
    else:
        error()

def change():
    global matrix_1
    global matrix_2
    temp = matrix_1
    matrix_1 = matrix_2
    matrix_2 = temp

        
def error():
    if not ui.ADD.isChecked() and not ui.SUBTRACTION.isChecked() and not ui.MULTIPLICATION.isChecked():
        message = QMessageBox()
        message.setWindowTitle("!!!")
        message.setInformativeText(("請選擇運算式"))
        message.exec_()

def add(per):
    x = "["

    for i in range(3):
        for j in range(3):
            matrix_3[i][j] = (int(matrix_1[i][j])+int(matrix_2[i][j]))*per
            if j == 2 and i == 2 :
                x = x+str(matrix_3[i][j])+"]"
            elif j== 2 :
                x = x+str(matrix_3[i][j])+"]"+"\n"+"["
            else:x = x+str(matrix_3[i][j])+","
    ui.label.setText(x)

def subtraction(per): 
    x = "["

    for i in range(3):
        for j in range(3):
            matrix_3[i][j] = (int(matrix_1[i][j])-int(matrix_2[i][j]))*per
            if j == 2 and i == 2 :
                x = x+str(matrix_3[i][j])+"]"
            elif j== 2 :
                x = x+str(matrix_3[i][j])+"]"+"\n"+"["
            else:x = x+str(matrix_3[i][j])+","
    ui.label.setText(x)

def multiplication(per):
    x = "["
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matrix_3[i][j] += (int(matrix_1[i][k])*int(matrix_2[k][j]))*per
            if j == 2 and i == 2 :
                x = x+str(matrix_3[i][j])+"]"
            elif j== 2 :
                x = x+str(matrix_3[i][j])+"]"+"\n"+"["
            else:x = x+str(matrix_3[i][j])+","

    ui.label.setText(x)
def determinant(matrix):
    n = len(matrix)
    det = 1  # 初始化行列式的值

    # 进行LU分解
    for j in range(n-1):
        pivot = 0
        pivot_row = j

        # 选取主元
        for i in range(j, n):
            if abs(int(matrix[i][j])) > pivot:
                pivot = abs(int(matrix[i][j]))
                pivot_row = i

        if pivot == 0:
            return 0  # 行列式为0

        if pivot_row != j:
            matrix[j], matrix[pivot_row] = matrix[pivot_row], matrix[j]
            det *= -1

        det *= int(matrix[j][j])

        # 消元
        for i in range(j+1, n):
            factor = (matrix[i][j]) / (matrix[j][j])
            for k in range(j+1, n):
                matrix[i][k] = (matrix[i][k])-factor * (matrix[j][k])

    det *= (matrix[n-1][n-1])
    return det
    
def trans():
    if ui.comboBox.currentIndex() == 2:
        ui.ADD.setText("加法")
        ui.SUBTRACTION.setText("減法")
        ui.MULTIPLICATION.setText("乘法")
        ui.answer.setText("答案")
    elif ui.comboBox.currentIndex() == 1:
        ui.ADD.setText("ADD")
        ui.SUBTRACTION.setText("SUBTRACTION")
        ui.MULTIPLICATION.setText("MULTIPLICATION")
        ui.answer.setText("show answer")

def slichose():
    y = ui.horizontalSlider.value()
    ui.progressBar.setValue(y)
    show()
def re_val():
    y = ui.horizontalSlider.value()
    return y/100

app = QApplication(sys.argv)
widge = QWidget()

t = QTranslator()
t.load("chinese.qm")
app.installTranslator(t)

ui = Ui_answer_2()
ui.setupUi(widge)

matrix_1 = [[0]*3 for _ in range(3)]
matrix_2 = [[0]*3 for _ in range(3)]
matrix_3 = [[0]*3 for _ in range(3)]

group1 = QButtonGroup(widge)
group1.addButton(ui.ADD)
group1.addButton(ui.SUBTRACTION)
group1.addButton(ui.MULTIPLICATION)
group1.addButton(ui.DET)
ui.progressBar.setMaximum(100)
ui.progressBar.setMinimum(0)
ui.progressBar.setValue(0)
ui.horizontalSlider.setMaximum(100)
ui.horizontalSlider.setMinimum(0)


ui.answer.clicked.connect(show)
ui.comboBox.addItems(["English","中文"])
ui.comboBox.activated.connect(trans)
ui.horizontalSlider.valueChanged.connect(slichose)

widge.show()
app.exec_()