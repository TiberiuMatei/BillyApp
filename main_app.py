import sys
import platform
import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sqlite3
import pathlib
import datetime
import os

os.system('Pyrcc5 billy_app.qrc -o billy_app_qrc.py')

import billy_app_qrc

# GUI File
from ui_main import Ui_BillyAppMain

# GLOBALS

GLOBAL_STATE = 0

# Import functions

class MainWindow(QMainWindow):
    def __init__(self, usernameAuth, emailAuth):
        QMainWindow.__init__(self)
        self.ui = Ui_BillyAppMain()
        self.ui.setupUiMain(self)

        self.username = usernameAuth
        self.email = emailAuth
        self.ui.lblSetProfileEmail.setText(self.email)
        self.ui.txtUsername.setText(self.username)
        self.ui.btnUsername.setText(self.username)

        # Initializing existing profile page data from db
        # Getting the app path
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Setting the earnings data fields from db if it exists
        earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(self.username,))
        earnings = earnings_result.fetchone()[0]
        if (earnings != None):
            self.ui.txtEarnings.setText(earnings)
            self.ui.lblEarningsValue.setText(earnings)
        # Setting the Enel electricity supplier
        enel_result = db_connection.execute("SELECT electricity_enel FROM accounts WHERE username = ?",(self.username,))
        enel = earnings_result.fetchone()[0]
        if (enel == 1):
            self.ui.btnEnelSelection.setChecked(True)
        # Setting the Engie natural gas supplier
        engie_result = db_connection.execute("SELECT gas_engie FROM accounts WHERE username = ?",(self.username,))
        engie = engie_result.fetchone()[0]
        if (engie == 1):
            self.ui.btnEngieSelection.setChecked(True)
        # Setting the Internet provider
        rds_result = db_connection.execute("SELECT internet_rds FROM accounts WHERE username = ?",(self.username,))
        rds = rds_result.fetchone()[0]
        if (rds == 1):
            self.ui.btnRCSRDSSelection.setChecked(True)
        # Setting the Netflix subscription
        netflix_result = db_connection.execute("SELECT subscription_netflix FROM accounts WHERE username = ?",(self.username,))
        netflix = netflix_result.fetchone()[0]
        if (netflix == 1):
            self.ui.btnNetflixSelection.setChecked(True)
        # Setting the Spotify subscription
        spotify_result = db_connection.execute("SELECT subscription_spotify FROM accounts WHERE username = ?",(self.username,))
        spotify = spotify_result.fetchone()[0]
        if (spotify == 1):
            self.ui.btnSpotifySelection.setChecked(True)
        connection.commit()
        connection.close()

        # Create directories for bill storage
        now = datetime.datetime.now()
        pathlib.Path(str(pathlib.Path().absolute())+f'/Bills/{self.username}/Electricity/{now.year}').mkdir(parents=True, exist_ok=True)
        pathlib.Path(str(pathlib.Path().absolute())+f'/Bills/{self.username}/NaturalGas/{now.year}').mkdir(parents=True, exist_ok=True)
        pathlib.Path(str(pathlib.Path().absolute())+f'/Bills/{self.username}/InternetTV/{now.year}').mkdir(parents=True, exist_ok=True)

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
        self.ui.btnBillyMain.clicked.connect(self.mainBillyDashboard)
        self.ui.btnUsername.clicked.connect(self.usernameProfilePage)

        # Profile page buttons
        self.ui.btnSetProfileName.clicked.connect(self.setAccountInformation)
        self.ui.txtEarnings.returnPressed.connect(self.setAccountInformation)
        self.ui.btnEnelSelection.clicked.connect(self.setElectricitySupplierEnel)
        self.ui.btnEngieSelection.clicked.connect(self.setNaturalGasSupplierEngie)
        self.ui.btnRCSRDSSelection.clicked.connect(self.setInternetProviderRCSRDS)
        self.ui.btnNetflixSelection.clicked.connect(self.setSubscriptionNetflix)
        self.ui.btnSpotifySelection.clicked.connect(self.setSubscriptionSpotify)

        # Tree view context
        self.ui.treeElectricityDirectory.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeElectricityDirectory.customContextMenuRequested.connect(self.contextMenu)

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
        # Full Electricity page functionality
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageElectricity, self.ui.btnElectricity, [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions])
        username = self.username
        email = self.email
        # Checking the selected Electricity supplier
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Setting the earnings data fields from db if it exists
        enel_result = db_connection.execute("SELECT electricity_enel FROM accounts WHERE username = ?",(username,))
        enel = enel_result.fetchone()[0]
        cez_result = db_connection.execute("SELECT electricity_cez FROM accounts WHERE username = ?",(username,))
        cez = cez_result.fetchone()[0]
        eon_result = db_connection.execute("SELECT electricity_eon FROM accounts WHERE username = ?",(username,))
        eon = eon_result.fetchone()[0]
        digi_result = db_connection.execute("SELECT electricity_digi FROM accounts WHERE username = ?",(username,))
        digi = digi_result.fetchone()[0]
        connection.commit()
        connection.close()
        if enel == 1 or cez == 1 or eon == 1 or digi == 1:
            # Checking the selected Electricity supplier
            if enel == 1:
                self.ui.btnElectricitySupplierDisplay.setStyleSheet("background-image: url(:/images/Resources/enel_supplier.png);\
                                                                        background-color: #202528;\
                                                                        border-radius: 5px;\
                                                                        background-repeat: none;\
                                                                        background-position: center;")
                currpath = pathlib.Path().absolute()
                electricity_path = str(currpath)+f'\\Bills\\{self.username}\\Electricity'
                self.model = QtWidgets.QFileSystemModel()
                self.model.setRootPath(electricity_path)
                self.ui.treeElectricityDirectory.setModel(self.model)
                self.ui.treeElectricityDirectory.setRootIndex(self.model.index(electricity_path))
                self.ui.treeElectricityDirectory.setSortingEnabled(True)

        else:
            self.generateMessageBox(window_title='Electricity page', msg_text='Please select the desired Electricity supplier from the Account preferences!')

    # Tree view open menu
    def contextMenu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        delete = menu.addAction("Delete")
        menu.setStyleSheet("QMenu{height: 53px; width: 80px; background-color: #2a2e32;} QMenu::item {height: 25px; width: 80px; font-family: \"SF UI Display\"; font-size: 10pt; color: #f3f5f6;} QMenu::item:selected {height: 25px; width: 80px; background-color: #EE4540; color: #f3f5f6;}")
        open.triggered.connect(self.openFile)
        delete.triggered.connect(self.deleteFile)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def openFile(self):
        index = self.ui.treeElectricityDirectory.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def deleteFile(self):
        index = self.ui.treeElectricityDirectory.currentIndex()
        file_path = self.model.filePath(index)
        os.remove(file_path)

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

    def setElectricitySupplierEnel(self):
        self.ui.btnEnelSelection.setChecked(True)
        username = self.ui.txtUsername.text()
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Updating the earnings field for the logged in user in the db
        db_connection.execute("UPDATE accounts SET electricity_enel = 1,\
                                electricity_cez = 0,\
                                electricity_eon = 0,\
                                electricity_digi = 0\
                                WHERE username = '{}'".format(username))
        connection.commit()
        connection.close()

    def setNaturalGasSupplierEngie(self):
        self.ui.btnEngieSelection.setChecked(True)
        username = self.ui.txtUsername.text()
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Updating the earnings field for the logged in user in the db
        db_connection.execute("UPDATE accounts SET gas_engie = 1,\
                                gas_cez = 0,\
                                gas_eon = 0,\
                                gas_enel = 0\
                                WHERE username = '{}'".format(username))
        connection.commit()
        connection.close()

    def setInternetProviderRCSRDS(self):
        self.ui.btnRCSRDSSelection.setChecked(True)
        username = self.ui.txtUsername.text()
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Updating the earnings field for the logged in user in the db
        db_connection.execute("UPDATE accounts SET internet_rds = 1,\
                                internet_upc = 0,\
                                internet_telekom = 0,\
                                internet_gts = 0\
                                WHERE username = '{}'".format(username))
        connection.commit()
        connection.close()

    def setSubscriptionNetflix(self):
        self.ui.btnNetflixSelection.setChecked(True)
        username = self.ui.txtUsername.text()
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Updating the earnings field for the logged in user in the db
        db_connection.execute("UPDATE accounts SET subscription_netflix = 1 WHERE username = '{}'".format(username))
        connection.commit()
        connection.close()

    def setSubscriptionSpotify(self):
        self.ui.btnSpotifySelection.setChecked(True)
        username = self.ui.txtUsername.text()
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Updating the earnings field for the logged in user in the db
        db_connection.execute("UPDATE accounts SET subscription_spotify = 1 WHERE username = '{}'".format(username))
        connection.commit()
        connection.close()

    def mainBillyDashboard(self):
        # Animate left side menu upon pressing the main logo button and focus on Dashboard
        self.ui.frameMenuContent.setGeometry(250, 250, 0, 670)
        self.animation9 = QPropertyAnimation(self.ui.frameMenuContent, b"geometry")
        self.animation9.setDuration(700)
        self.animation9.setEndValue(QRect(0, 250, 200, 670))
        self.animation9.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation9.start()
        MainWindow.clickLeftMenuButton(self, self.ui.pageDashboard, self.ui.btnDashboard, [self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions])

    def usernameProfilePage(self):
        mainButtonsList = [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions]
        for button in mainButtonsList:
            button.setChecked(False)
        # self.ui.stackedWidget.setCurrentWidget(self.ui.pageProfile)
        MainWindow.profilePage(self)

    # Profile Page content and buttons
    def profilePage(self):
        mainButtonsList = [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions]
        for button in mainButtonsList:
            button.setChecked(False)
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
        # Animate subscriptions frame
        self.ui.subscriptionsPage.setGeometry(30, 710, 0, 140)
        self.animation8 = QPropertyAnimation(self.ui.subscriptionsPage, b"geometry")
        self.animation8.setDuration(800)
        self.animation8.setEndValue(QRect(30, 710, 530, 140))
        self.animation8.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation8.start()

    def setAccountInformation(self):
        if self.ui.txtEarnings.text() == '':
            self.generateMessageBox(window_title='Account information', msg_text='Please fill in the Earnings field!')
        else:
            # Getting the app path
            username = self.ui.txtUsername.text()
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            # Updating the earnings field for the logged in user in the db
            db_connection.execute("UPDATE accounts SET earnings = '{}' WHERE username = '{}'".format(self.ui.txtEarnings.text(), username))
            self.ui.lblEarningsValue.setText(self.ui.txtEarnings.text())
            connection.commit()
            connection.close()

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