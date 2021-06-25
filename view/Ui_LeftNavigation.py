from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *


class UiLeftNavigation(QScrollArea):
    itemHeight = 45
    style = '''
        QWidget#leftWidget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
        }
        QLabel{
            border:none;
            color:pink;
            font-size:18px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            background-color:rgba(0,0,0,0);
        }
        QListWidget{
            border:0px;
            color:gray;
            outline:0px;
            font-size:18px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            background-color:rgba(0,0,0,0);
        }
        QPushButton{
            outline:0px;
            border:none;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
    '''

    def setupUi(self):
        self.setWidgetResizable(True)
        self.setFixedWidth(300)
        self.setFixedHeight(800)

        # 设置左侧导航栏
        self.leftWidget = QtWidgets.QWidget()
        self.setWidget(self.leftWidget)

        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftWidget.setLayout(self.leftLayout)

        # 左侧导航栏设置
        # 设置LOGO
        self.lb_logo = QtWidgets.QLabel()
        self.lb_logo.setText("LOGO")
        self.lb_logo.setFixedHeight(50)
        self.leftLayout.addWidget(self.lb_logo)

        # 设置Qlabel标签
        self.lft_lb_recommand = QLabel('在线音乐')
        self.lft_lb_recommand.setStyleSheet('padding-left:5px;')
        self.lft_lb_recommand.setFixedHeight(self.itemHeight)

        self.lft_lw_recommand = QListWidget()
        self.leftLayout.addWidget(self.lft_lb_recommand)
        self.leftLayout.addWidget(self.lft_lw_recommand)

        item = QListWidgetItem("推荐")
        item.setSizeHint(QSize(100, 30))
        self.lft_lw_recommand.addItem(item)
        # self.lft_lw_recommand.insertItem(row, item)
        # self.lft_lw_recommand.setItemWidget(item, itemWeight)

        item = QListWidgetItem("音乐馆")
        self.lft_lw_recommand.addItem(item)

        item = QListWidgetItem("视频")
        self.lft_lw_recommand.addItem(item)

        item = QListWidgetItem("电台")
        self.lft_lw_recommand.addItem(item)

        self.lft_lb_recommand2 = QLabel('我的音乐')
        self.lft_lb_recommand2.setStyleSheet('padding-left:5px;')
        self.lft_lb_recommand2.setFixedHeight(self.itemHeight)

        self.lft_lw_recommand2 = QListWidget()
        self.leftLayout.addWidget(self.lft_lb_recommand2)
        self.leftLayout.addWidget(self.lft_lw_recommand2)

        item = QListWidgetItem("我喜欢")
        self.lft_lw_recommand2.addItem(item)

        item = QListWidgetItem("本地和下载")
        self.lft_lw_recommand2.addItem(item)

        item = QListWidgetItem("最近播放")
        self.lft_lw_recommand2.addItem(item)

        item = QListWidgetItem("试听列表")
        self.lft_lw_recommand2.addItem(item)

        self.lft_lb_recommand3 = QLabel('创建的歌单')
        self.lft_lb_recommand3.setStyleSheet('padding-left:5px;')
        self.lft_lb_recommand3.setFixedHeight(self.itemHeight)

        self.lft_lw_recommand3 = QListWidget()
        self.leftLayout.addWidget(self.lft_lb_recommand3)
        self.leftLayout.addWidget(self.lft_lw_recommand3)

        item = QListWidgetItem("我最爱听")
        self.lft_lw_recommand3.addItem(item)

        self.lft_lb_recommand4 = QLabel('收藏的歌单')
        self.lft_lb_recommand4.setStyleSheet('padding-left:5px;')
        self.lft_lb_recommand4.setFixedHeight(self.itemHeight)

        self.lft_lw_recommand4 = QListWidget()
        self.leftLayout.addWidget(self.lft_lb_recommand4)
        self.leftLayout.addWidget(self.lft_lw_recommand4)

        self.leftWidget.setStyleSheet(self.style)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QLabel, QListWidget, QListWidgetItem, QScrollArea, QWidget

    app = QApplication(sys.argv)
    w = UiLeftNavigation()
    w.setupUi()
    w.show()
    sys.exit(app.exec_())
