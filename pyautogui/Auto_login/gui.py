import sys
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton
import pyautogui as auto
import time
import subprocess
import pyperclip
import datetime

class Madoka(QWidget):
    def __init__(self):
        super().__init__()
        botan = QPushButton('botで送る',self)
        botan.clicked.connect(self.bot)
        self.setGeometry(100,100,200,150)
        botan.setGeometry(30,30,100,70)

    def bot(self):
        print(auto.position())
        subprocess.run('open -a Slack', shell=True)
        time.sleep(4)
        auto.click(35,161)
        auto.moveTo(117,584)
        auto.scroll(100)
        time.sleep(0.5)
        auto.click(117,584)
        auto.click(396,1004)
        auto.click(485,844)
        time.sleep(1)
        auto.click(901,455)
        pyperclip.copy("セキタクマ")
        auto.keyDown("command")
        auto.press("v")
        auto.keyUp("command")
        auto.click(877,539)
        auto.press("down")
        auto.press("enter")
        auto.click(957,633)
        now = datetime.datetime.now()
        # print(now)
        h = now.hour
        # print(h)
        m = now.minute
        # print(m)
        push = 0
        if h - 9 == 0 and m >= 25 or h - 9 == 1 and m <= 24:
            push = 1
        elif h - 9 == 1 and m >= 25 or h - 9 == 2 and m <= 24:
            push = 2
        elif h - 9 == 2 and m >= 25 or h - 9 == 3 and m <= 20:
            push = 3
        elif h - 9 == 3 and m >= 21 or h - 9 == 4 and m <= 24:
            pyperclip.copy("今はお昼休みだよ？")
            auto.keyDown("command")
            auto.press("v")
            auto.keyUp("command")
            time.sleep(0.5)
            auto.keyDown("command")
            auto.press("a")
            auto.keyUp("command")
            auto.press("delete")
            pyperclip.copy("出し忘れとかならどうぞ")
            auto.keyDown("command")
            auto.press("v")
            auto.keyUp("command")
            time.sleep(0.5)
            auto.keyDown("command")
            auto.press("a")
            auto.keyUp("command")
            auto.press("delete")
        elif h - 9 == 4 and m >= 25 or h - 9 == 5 and m <= 24:
            push = 4
        elif h - 9 == 5 and m >= 25 or h - 9 == 6 and m <= 24:
            push = 5
        else:
            pyperclip.copy("今は学校の時間じゃないよ？")
            auto.keyDown("command")
            auto.press("v")
            auto.keyUp("command")
            time.sleep(0.5)
            auto.keyDown("command")
            auto.press("a")
            auto.keyUp("command")
            auto.press("delete")
            pyperclip.copy("出し忘れとかならどうぞ")
            auto.keyDown("command")
            auto.press("v")
            auto.keyUp("command")
            time.sleep(0.5)
            auto.keyDown("command")
            auto.press("a")
            auto.keyUp("command")
            auto.press("delete")
        # print(push)
        for i in range(push):
            auto.press("down")
        auto.press("enter")
        auto.moveTo(1048,702)


qAp = QApplication(sys.argv)
mado = Madoka()
mado.show()
qAp.exec()