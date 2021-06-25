from view.ui_RightCharts import Ui_RightCharts


class RightCharts(Ui_RightCharts):
    def __init__(self, parent=None):
        super(RightCharts, self).__init__(parent)
        self.setupUi()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = RightCharts()
    w.show()
    sys.exit(app.exec_())

