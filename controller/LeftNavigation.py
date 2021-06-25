from view.Ui_LeftNavigation import UiLeftNavigation


class LeftNavigation(UiLeftNavigation):
    def __init__(self, parent=None):
        super(LeftNavigation, self).__init__(parent)
        self.setupUi()

        self.lft_lw_recommand.currentRowChanged.connect(self.display)

    def display(self, i):
        # 设置当前可见的选项卡的索引
        # self.body_stackedWidget.setCurrentIndex(i)
        print(i)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = LeftNavigation()
    w.show()
    sys.exit(app.exec_())
