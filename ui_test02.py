import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from_class = uic.loadUiType('ui/untitled.ui')[0] # ui 불러오기

class MyWindow(QMainWindow, from_class):
    def __init__(self): # 초기화자
        super().__init__()
        self.setupUi(self) # 만들어 놓은 test.ui 연결
        self.setWindowTitle('연습용프로그램') # 윈도우 제목 설정
        self.setWindowIcon(QIcon('img/test_icon.png')) # 윈도우 아이콘 설정
        self.statusBar().showMessage('Test Application ver 1.0') # 윈도우 상태표시줄 입력
        self.test_button.clicked.connect(self.btn_clicked) # 버튼 클릭시 연결될 함수 설정


    def btn_clicked(self):
       # print('버튼이 클릭되었습니다.')
        self.label.setText('안녕!반갑습니다!!!')


app = QApplication(sys.argv)
window = MyWindow()
window.show()

app.exec_()