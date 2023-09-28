import random
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('design.ui')
        self.ui.show()
        self.ui.setWindowTitle('Number Guessing Game')
        self.ui.b_check.clicked.connect(self.check)
        self.number = random.randint(0, 100)

    def check(self):
        guess = int(self.ui.tb.text())
        if self.number < guess:
            msgBox = QMessageBox()
            msgBox.setText('متاسفم عدد مدنظر من کوچیک تره')
            msgBox.exec()
            self.ui.tb.setText('')
        elif self.number > guess :
            msgBox = QMessageBox()
            msgBox.setText('متاسفم عدد مدنظر من بزرگتره')
            msgBox.exec()
            self.ui.tb.setText('')
        else:
            msgBox = QMessageBox()
            msgBox.setText('بهت تبریک میگم تو برنده شدی')
            msgBox.exec()
            self.ui.tb.setText('')

app = QApplication([])
window = MainWindow()
app.exec()