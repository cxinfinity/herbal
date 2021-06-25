from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class Ui_PlayPage(QWidget):

    MAX_WIDTN = 1300  # 最大化窗口时，每个tab页面里面的内容最大宽度

    def setupUi(self):
        self.setObjectName("play_page")
        # self.resize(1079, 743)  # 初始化不要设置size，免得放入QScrollArea中出现滚动条，不设置size，放入水平布局后自然会设置成合适的大小

        self.horizontalLayout = QHBoxLayout(self)
        self.tabW_findMusic = QTabWidget(self)

        self.tab_personal_recom = QWidget()
        self.tab1_vly_layout = QVBoxLayout(self.tab_personal_recom)

        self.scrollArea_pers_recom = QScrollArea(self.tab_personal_recom)
        self.scrollArea_pers_recom.setWidgetResizable(True)

        self.area_pers_recom = QWidget()
        self.hly_pers_recom = QHBoxLayout(self.area_pers_recom)  # 这个是个性推荐总布局，里面只放一个大控件（其他类写的控件：RecommandUi）
        self.per_label = QLabel('测试线 - 1')
        self.per_label2 = QLabel('测试线 - 2')
        self.per_label3 = QLabel('测试线 - 3')
        self.hly_pers_recom.addWidget(self.per_label)
        self.hly_pers_recom.addWidget(self.per_label2)
        self.hly_pers_recom.addWidget(self.per_label3)

        self.scrollArea_pers_recom.setWidget(self.area_pers_recom)
        self.tab1_vly_layout.addWidget(self.scrollArea_pers_recom)
        self.tabW_findMusic.addTab(self.tab_personal_recom, "")

        self.tab_song_sheet = QWidget()
        self.tabW_findMusic.addTab(self.tab_song_sheet, "")
        self.tab_anchor_station = QWidget()
        self.tabW_findMusic.addTab(self.tab_anchor_station, "")
        self.tab_rank = QWidget()
        self.tabW_findMusic.addTab(self.tab_rank, "")
        self.tab_singer = QWidget()
        self.tabW_findMusic.addTab(self.tab_singer, "")
        self.tab_lastest_music = QWidget()
        self.tabW_findMusic.addTab(self.tab_lastest_music, "")

        self.horizontalLayout.addWidget(self.tabW_findMusic)

        self.tabW_findMusic.setCurrentIndex(0)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget

    app = QApplication(sys.argv)
    w = Ui_PlayPage()
    w.setupUi()
    w.show()
    sys.exit(app.exec_())
