from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class Ui_RightCharts(QWidget):

    MAX_WIDTN = 1300  # 最大化窗口时，每个tab页面里面的内容最大宽度

    def setupUi(self):
        self.setObjectName("right_charts")
        # self.resize(1079, 743)  # 初始化不要设置size，免得放入QScrollArea中出现滚动条，不设置size，放入水平布局后自然会设置成合适的大小

        self.hLayout = QHBoxLayout(self)
        self.tabW_rightCharts = QTabWidget(self)

        self.tab_rc_recom = QWidget()
        self.tab1_rc_layout = QVBoxLayout(self.tab_rc_recom)

        self.scrollArea_rc_recom = QScrollArea(self.tab_rc_recom)
        self.scrollArea_rc_recom.setWidgetResizable(True)

        self.area_rc_recom = QWidget()
        self.hly_rc_recom = QHBoxLayout(self.area_rc_recom)  # 这个是个性推荐总布局，里面只放一个大控件（其他类写的控件：RecommandUi）
        self.per_label4 = QLabel('测试线 - 4')
        self.per_label5 = QLabel('测试线 - 5')
        self.hly_rc_recom.addWidget(self.per_label4)
        self.hly_rc_recom.addWidget(self.per_label5)

        self.scrollArea_rc_recom.setWidget(self.area_rc_recom)
        self.tab1_rc_layout.addWidget(self.scrollArea_rc_recom)
        self.tabW_rightCharts.addTab(self.tab_rc_recom, "")

        self.tab_code_sheet = QWidget()
        self.tabW_rightCharts.addTab(self.tab_code_sheet, "")
        self.tab_stock_station = QWidget()
        self.tabW_rightCharts.addTab(self.tab_stock_station, "")

        self.hLayout.addWidget(self.tabW_rightCharts)

        self.tabW_rightCharts.setCurrentIndex(0)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget

    app = QApplication(sys.argv)
    w = Ui_RightCharts()
    w.setupUi()
    w.show()
    sys.exit(app.exec_())
