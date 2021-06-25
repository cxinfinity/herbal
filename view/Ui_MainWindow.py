import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QListWidget, QListWidgetItem, QLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1280, 870)

        # 默认的状态栏
        self.status = self.statusBar()
        self.status.showMessage("hello 你好 ^_^")

        # 标题栏
        self.setWindowTitle("Herbal 修养 茶")
        # self.resize(1280, 870)
        self.itemHeight = 45

        # 主窗口
        self.centralwidget = QtWidgets.QWidget()
        self.centralLayout = QtWidgets.QHBoxLayout()
        self.centralwidget.setLayout(self.centralLayout)

        # 设置边框间隙
        self.centralLayout.setSpacing(0)

        # 设置右侧主框体
        self.mainWidget = QtWidgets.QWidget()
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        # 加载导航栏和主框体到主窗口, 并设置比例
        self.centralLayout.addWidget(self.mainWidget)
        self.centralLayout.setStretchFactor(self.mainWidget, 5)

        # 加载主窗口
        self.setCentralWidget(self.centralwidget)

        # 右侧主框体设置
        # 1. 头条栏目, 包括搜索框和杂七杂八
        # 2. 分选栏目框, 也就是内容页
        # 3. 底部播放控制栏, 也包括一些时间显示什么的
        self.headWidget = QtWidgets.QWidget()
        self.headLayout = QtWidgets.QHBoxLayout()
        self.headWidget.setLayout(self.headLayout)

        self.searchLab = QLineEdit()
        self.searchLab.setPlaceholderText('请输入需要查询的数据')
        self.headLayout.addWidget(self.searchLab)

        self.btn_minwin = QtWidgets.QPushButton()
        self.btn_minwin.setText("min")
        self.headLayout.addWidget(self.btn_minwin)

        self.btn_maxwin = QtWidgets.QPushButton()
        self.btn_maxwin.setText("max")
        self.headLayout.addWidget(self.btn_maxwin)

        self.btn_closewin = QtWidgets.QPushButton()
        self.btn_closewin.setText("cls")
        self.headLayout.addWidget(self.btn_closewin)

        self.searchLab.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        # 2.
        self.contentWidget = QtWidgets.QWidget()
        self.contentLayout = QtWidgets.QVBoxLayout()
        self.contentWidget.setLayout(self.contentLayout)

        self.body_stackedWidget = QtWidgets.QStackedWidget()
        self.contentLayout.addWidget(self.body_stackedWidget)

        self.page_findMusic = QtWidgets.QWidget()
        self.body_stackedWidget.addWidget(self.page_findMusic)
        self.hly_findMusic = QtWidgets.QHBoxLayout(self.page_findMusic)
        self.hly_findMusic.setContentsMargins(0, 0, 0, 0)
        # self.stack_tstbtn = QtWidgets.QPushButton(self.page_findMusic)
        # self.stack_tstbtn.setText("stack1")

        self.page_2 = QtWidgets.QWidget()
        self.body_stackedWidget.addWidget(self.page_2)
        self.hly_page2 = QtWidgets.QHBoxLayout(self.page_2)
        self.hly_page2.setContentsMargins(0, 0, 0, 0)
        # self.stack_tstbtn2 = QtWidgets.QPushButton(self.page_2)
        # self.stack_tstbtn2.setText("stack2")

        # self.body_stackedWidget.setCurrentIndex(2)

        # 3.
        self.bottomWidget = QtWidgets.QWidget()
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomWidget.setLayout(self.bottomLayout)

        self.btn_preSong = QtWidgets.QPushButton()
        self.btn_preSong.setText("pre")
        self.bottomLayout.addWidget(self.btn_preSong)

        self.btn_play = QtWidgets.QPushButton()
        self.btn_play.setText("play")
        self.bottomLayout.addWidget(self.btn_play)

        self.btn_nextSong = QtWidgets.QPushButton()
        self.btn_nextSong.setText("next")
        self.bottomLayout.addWidget(self.btn_nextSong)

        self.right_process_bar = QtWidgets.QProgressBar()
        self.bottomLayout.addWidget(self.right_process_bar)

        # 整合主页面视图
        self.mainLayout.addWidget(self.headWidget)
        self.mainLayout.addWidget(self.contentWidget)
        self.mainLayout.addWidget(self.bottomWidget)

        self.mainLayout.setStretchFactor(self.headWidget, 1)
        self.mainLayout.setStretchFactor(self.contentWidget, 12)
        self.mainLayout.setStretchFactor(self.bottomWidget, 1)

        self.setWindowOpacity(0.95) # 设置窗口透明度
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
