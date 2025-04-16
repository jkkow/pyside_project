import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from gui.ui_example import Ui_MainWindow # change module name to your ui python script

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(MyWindow, self).__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
