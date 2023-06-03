
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from test0517 import Ui_answer_2
import sys
 

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_answer_2() #接物件
        self.ui.setupUi(self)  #執行setupui

        #self.ui.answer.clicked.connect(show)
        self.ui.comboBox.addItems(["English","中文"])
        self.ui.comboBox.activated.connect(self.trans)
    def trans(self):
        if self.ui.comboBox.currentIndex() == 2:
            self.ui.ADD.setText("加法")
            self.ui.SUBTRACTION.setText("減法")
            self.ui.MULTIPLICATION.setText("乘法")
            self.ui.answer.setText("答案")
        elif self.ui.comboBox.currentIndex() == 1:
           self.ui.ADD.setText("ADD")
           self.ui.SUBTRACTION.setText("SUBTRACTION")
           self.ui.MULTIPLICATION.setText("MULTIPLICATION")
           self.ui.answer.setText("show answer")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Main() # class 的名稱


    mywindow.show()
    app.exec_() #執行


