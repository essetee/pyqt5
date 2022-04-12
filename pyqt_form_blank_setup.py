import sys
import form # name of your created form without the .py extension
from PyQt5.QtCore import QStandardPaths, QDir
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget


class Window(QMainWindow, form.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.center(self) # method to center the form
        myConfigPath = self.setConfigDir()  # will return the correct path for every OS
        print("All data will be stored at: ", myConfigPath) # to see the used path
        myError = "example error message usefully with database errors"
        self.errorMsg(self, myError) # show error msg example
        self.btnClose.clicked.connect(self.close)
        self.btnClearText.clicked.connect(self.btnClear)
        self.btnClickMe.clicked.connect(self.btnClick)

    def btnClear(self):
        self.lineEditNaam.setText("")
        self.label.setText("")

    def btnClick(self):
        txt = "Welcome " + self.lineEditNaam.text()
        self.label.setText(txt)

    @staticmethod
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @staticmethod
    def errorMsg(self, errormsg):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText(errormsg)
        msg.exec()

    @staticmethod
    def setConfigDir():
        saveDir = QStandardPaths.locate(QStandardPaths.GenericDataLocation, str(), QStandardPaths.LocateDirectory)
        myDir = QDir()
        if not myDir.exists(saveDir):
            myDir.mkpath(saveDir)
        return saveDir


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
