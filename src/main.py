from PyQt5.QtWidgets import QApplication
import sys

from pages import MainWindow


class MIREACenter:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
    
    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    app = MIREACenter()
    app.run()