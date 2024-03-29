import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from qtconsole.qt import QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 240))
        self.setWindowTitle("ZTS")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('URL:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('GO', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)

    def openUrl(self):
        url = QtCore.QUrl('https://www.google.com')
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')

    def clickMethod(self):
        print('Your name: ' + self.line.text())
        self.openUrl()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
