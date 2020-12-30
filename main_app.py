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

# GLOBALS

GLOBAL_STATE = 0

# Import functions
#from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_BillyAppMain()
        self.ui.setupUiMain(self)

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
        self.ui.btnSetProfileName.clicked.connect(self.setAccountInformation)
        self.ui.txtUsername.returnPressed.connect(self.setAccountInformation)
        self.ui.txtEarnings.returnPressed.connect(self.setAccountInformation)

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
        self.ui.profileName.setGeometry(30, 80, 0, 130)
        self.animation1 = QPropertyAnimation(self.ui.profileName, b"geometry")
        self.animation1.setDuration(800)
        self.animation1.setEndValue(QRect(30, 80, 731, 130))
        self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation1.start()
        # Animate electricity supplier frame
        self.ui.electricitySupplier.setGeometry(30, 230, 0, 140)
        self.animation2 = QPropertyAnimation(self.ui.electricitySupplier, b"geometry")
        self.animation2.setDuration(800)
        self.animation2.setEndValue(QRect(30, 230, 1050, 140))
        self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation2.start()
        # Animate natural gas supplier frame
        self.ui.naturalGasSupplier.setGeometry(30, 390, 0, 140)
        self.animation3 = QPropertyAnimation(self.ui.naturalGasSupplier, b"geometry")
        self.animation3.setDuration(800)
        self.animation3.setEndValue(QRect(30, 390, 1050, 140))
        self.animation3.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation3.start()
        # Animate internet provider frame
        self.ui.internetProvider.setGeometry(30, 550, 0, 140)
        self.animation4 = QPropertyAnimation(self.ui.internetProvider, b"geometry")
        self.animation4.setDuration(800)
        self.animation4.setEndValue(QRect(30, 550, 1050, 140))
        self.animation4.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation4.start()
        # Animate earnings frame
        self.ui.earnings.setGeometry(780, 80, 0, 130)
        self.animation5 = QPropertyAnimation(self.ui.earnings, b"geometry")
        self.animation5.setDuration(800)
        self.animation5.setEndValue(QRect(780, 80, 300, 130))
        self.animation5.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation5.start()

    def setAccountInformation(self):
        if self.ui.txtUsername.text() == '':
            self.generateMessageBox(window_title='Account information', msg_text='Please fill in the Username field!')
        else:
            self.ui.lblSetProfileName.setText(self.ui.txtUsername.text())
        if self.ui.txtEarnings.text() == '':
            self.generateMessageBox(window_title='Account information', msg_text='Please fill in the Earnings field!')
        else:
            self.ui.lblEarningsValue.setText(self.ui.txtEarnings.text())

    # Move app window - drag
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

class UIFunctions(MainWindow):   

    #  MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.mainCentralWidget.setContentsMargins(0, 0, 0, 0)
            self.ui.mainCentralWidget.setStyleSheet("background-color: rgb(45, 20, 44);")
            self.ui.btnMaximizeRestore.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.mainCentralWidget.setContentsMargins(0, 0, 0, 0)
            self.ui.mainCentralWidget.setStyleSheet("background-color: rgb(45, 20, 44);")
            self.ui.btnMaximizeRestore.setToolTip("Maximize")

    #  UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #####################
        # APP TOOLTIP SECTION
        #####################

        # MAXIMIZE TOOLTIP
        self.ui.btnMaximizeRestore.setToolTip("Maximize")

        # BILLING FLAG
        self.ui.lblBillingFlag.setToolTip("RO")

        # Engie supplier
        self.ui.btnEngieSelection.setToolTip("ENGIE Romania S.A.")

        # Enel supplier
        self.ui.btnEnelSelection.setToolTip("Enel Energie Muntenia SA")

        # RCSRDS supplier
        self.ui.btnRCSRDSSelection.setToolTip("RCS & RDS S.A.")

        # Profile button
        self.ui.btnProfile.setToolTip("Account preferences")

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.mainCentralWidget.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btnMaximizeRestore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btnMinimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btnMinimize.setToolTip("Minimize")

        # CLOSE
        self.ui.btnClose.clicked.connect(lambda: self.close())
        self.ui.btnClose.setToolTip("Close")

    # RETURN STATUS IF WINDOWS IS MAXIMIZED OR RESTORED
    def returnStatus():
        return GLOBAL_STATE


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window2 = MainWindow()
    sys.exit(app.exec_())