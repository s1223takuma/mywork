import sys
from PyQt6.QtWidgets import QApplication,QWidget

class Madoka(QWidget):
    def __init__(self):
        super().__init__()

    def resizeEvent(self,e):
        s0 = e.oldSize() # 元の大きさ
        s1 = e.size() # 今の大きさ
        print('(%d,%d) > (%d,%d)'%(s0.width(),s0.height(),s1.width(),s1.height()))

qAp = QApplication(sys.argv)
mado = Madoka()
mado.show()
qAp.exec()