from view.ui_PlayPage import Ui_PlayPage


class PlayPage(Ui_PlayPage):
    def __init__(self, parent=None):
        super(PlayPage, self).__init__(parent)
        self.setupUi()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = PlayPage()
    w.show()
    sys.exit(app.exec_())

