import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from controller.LeftNavigation import LeftNavigation
from view.Ui_MainWindow import Ui_MainWindow


class MyWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.setupUi(self)
        self.initNaviUi()

    def initNaviUi(self):
        self.leftNavigation = LeftNavigation(self)

        # 加载导航栏和主框体到主窗口, 并设置比例
        self.centralLayout.addWidget(self.leftNavigation)
        self.centralLayout.setStretchFactor(self.leftNavigation, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWin()
    myWin.show()
    sys.exit(app.exec_())
