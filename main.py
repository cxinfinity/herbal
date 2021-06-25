import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from controller.LeftNavigation import LeftNavigation
from controller.PlayPage import PlayPage
from controller.RightCharts import RightCharts
from view.ui_MainWindow import Ui_MainWindow


class MyWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.setupUi(self)
        self.initNaviUi()
        self.initBodyUi()

    def initNaviUi(self):
        self.leftNavigation = LeftNavigation(self)

        # 加载导航栏和主框体到主窗口, 并设置比例
        self.centralLayout.addWidget(self.leftNavigation)
        self.centralLayout.setStretchFactor(self.leftNavigation, 1)

        self.leftNavigation.lft_lw_recommand.currentRowChanged.connect(self.display)


    def initBodyUi(self):
        self.findMusic = PlayPage()
        self.hly_findMusic.addWidget(self.findMusic)

        self.findCharts = RightCharts()
        self.hly_page2.addWidget(self.findCharts)


    def display(self, i):
        # 设置当前可见的选项卡的索引
        self.body_stackedWidget.setCurrentIndex(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWin()
    myWin.show()
    sys.exit(app.exec_())
