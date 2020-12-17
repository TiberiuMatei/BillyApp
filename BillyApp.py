import sys
import platform
import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

os.system('Pyrcc5 billy_app.qrc -o billy_app_qrc.py')

import billy_app_qrc

# GUI File
#from ui_main import Ui_MainWindow

# Import functions
#from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        

        # Move window
        def moveWindow(event):
            # Restore before move
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # If left click hold - move windoe
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Set title bar
        self.ui.title_bar.mouseMoveEvent = moveWindow

        # Set title name
        self.setWindowTitle("Billy")

        # Set window icon
        # self.setWindowIcon(QtGui.QIcon(":/test_runner/Resources/verifone_logo.png"))

        # Set UI Definitions
        UIFunctions.uiDefinitions(self)

        # Show Main Window
        self.show()

    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_menu.width()

        if width == 40:
            # Expand menu
            newWidth = 180
        else:
            # Restore left menu
            newWidth = 40

        # Animate left menu transition
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    # App events

    # Move app window - drag
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())