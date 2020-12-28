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
from ui_main import Ui_BillyAppMain

# Import functions
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_BillyAppMain()
        self.ui.setupUi(self)

        # Animate left side menu upon app loading
        self.ui.frameMenuContent.setGeometry(240, 240, 0, 540)
        self.animation = QPropertyAnimation(self.ui.frameMenuContent, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setEndValue(QRect(0, 240, 200, 540))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation.start() 

        # Move window
        def moveWindow(event):
            # Restore before move
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # If left click hold - move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Set title bars and move window
        self.ui.frameTitle.mouseMoveEvent = moveWindow
        self.ui.frameTitleSmall.mouseMoveEvent = moveWindow

        # Set the default opened page
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageDashboard)

        # Set title name
        self.setWindowTitle("Billy")

        # Set window icon
        self.setWindowIcon(QtGui.QIcon(":/images/Resources/billy_logo.png"))

        # Set UI Definitions
        UIFunctions.uiDefinitions(self)

        # Set the stacked widget switch and button check logic        
        self.ui.btnDashboard.clicked.connect(self.dashboardButton)
        self.ui.btnCalendar.clicked.connect(self.calendarButton)
        self.ui.btnElectricity.clicked.connect(self.electricityButton)
        self.ui.btnNaturalGas.clicked.connect(self.naturalGasButton)
        self.ui.btnInternetTV.clicked.connect(self.internetTVButton)
        self.ui.btnSubscriptions.clicked.connect(self.subscriptionsButton)
        self.ui.btnProfile.clicked.connect(self.profilePage)

        # Profile page buttons
        self.ui.btnSetProfileName.clicked.connect(self.setProfileName)

        # Show Main Window
        self.show()

    ############
    # APP EVENTS

    # Generate message boxes
    def generateMessageBox(self, window_title, msg_text):        
        QMessageBox.about(self, window_title, msg_text)

    # Method to unselect all buttons once one is pressed
    def uncheckOtherButtons(clickedButton, otherButtonsList):
        if clickedButton.isChecked():
            # Uncheck all buttons except the one that is clicked
            for button in otherButtonsList:
                button.setChecked(False)

    # Method to select widget page, button check state and call of the method that will uncheck other buttons
    def clickLeftMenuButton(self, widgetPage, currentButton, remainingButtonsList):
        self.ui.stackedWidget.setCurrentWidget(widgetPage)
        currentButton.setChecked(True)
        MainWindow.uncheckOtherButtons(currentButton, remainingButtonsList)

    # Click on the Dashboard button
    def dashboardButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageDashboard, self.ui.btnDashboard, [self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions])

    # Click on the Calendar button
    def calendarButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageCalendar, self.ui.btnCalendar, [self.ui.btnDashboard, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions])

    # Click on the Electricity button
    def electricityButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageElectricity, self.ui.btnElectricity, [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions])

    # Click on the NaturalGas button
    def naturalGasButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageNaturalGas, self.ui.btnNaturalGas, [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnInternetTV, self.ui.btnSubscriptions])

    # Click on the InternetTV button
    def internetTVButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageInternetTV, self.ui.btnInternetTV, [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnSubscriptions])

    # Click on the Subscriptions button
    def subscriptionsButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageSubscriptions, self.ui.btnSubscriptions, [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV])

    # Profile Page content and buttons
    def profilePage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageProfile)
        # Animate profile frame
        self.ui.profileName.setGeometry(30, 80, 0, 121)
        self.animation = QPropertyAnimation(self.ui.profileName, b"geometry")
        self.animation.setDuration(800)
        self.animation.setEndValue(QRect(30, 80, 401, 121))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation.start()

    def setProfileName(self):
        if self.ui.txtUsername.text() == '':
            self.generateMessageBox(window_title='Username information', msg_text='Please fill in the Username field!')
        else:
            self.ui.lblSetProfileName.setText(self.ui.txtUsername.text())

    # Move app window - drag
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())