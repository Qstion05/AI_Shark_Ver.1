import sys, random, time
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import uic
from threading import Timer


form_class = uic.loadUiType("gui.ui")[0]

class ChatWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_send.clicked.connect(self.send_message)
        self.image.setPixmap(QPixmap("BG.png").scaled(self.width(), self.height() - 50))
        opacity_effect = QGraphicsOpacityEffect(self.image)
        opacity_effect.setOpacity(0.35)
        self.image.setGraphicsEffect(opacity_effect)


        self.start_Chat()
    def start_Chat(self):
        self.add_chat('                                                               [나]님이 접속하셨습니다.                                                            ')   
        self.add_chat('                                                               [이상준]님이 접속하셨습니다.                                                            ')
        self.add_chat('\n')
        self.add_chat('[이상준] %s'%("어 반갑고 반갑고~"))

    def send_message(self):
        msg = self.input_message.toPlainText()
        self.add_chat('[나] %s'%(msg))
        self.input_message.setPlainText('')
        QTest.qWait(random.randint(300, 1001))
        self.Random_msg()

    def Random_msg(self):
        msg = ["자 한번 가보자~", "So deep mind... ", "나이스~", "ㅎㅋㅋㅋㅋㅋㅋㅋ", "과제가 비상이긴 해~", "굳", "옼케이~", "호오올리..."]
        idx = random.randint(0, 8)
        self.add_chat('[이상준] %s'%(msg[idx]))

    def add_chat(self, msg):
        self.chats.appendPlainText(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = ChatWindow()
    myWindow.setWindowTitle("AI 이상준 메신저")
    myWindow.show()
    app.exec_()
