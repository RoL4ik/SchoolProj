import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first app")
        self.setGeometry(300, 300, 300, 300)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.main_layout = QVBoxLayout()
        self.centralwidget.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
