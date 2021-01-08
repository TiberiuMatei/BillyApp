import sys
import platform
import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtCharts import *
import sqlite3
import pathlib
import datetime
import os
import shutil
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io
import re

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

        self.lay = QtWidgets.QVBoxLayout(self.ui.widget)
        self.ui.widget.setContentsMargins(0, 0, 0, 0)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.chartview = QtCharts.QChartView()
        # chartview.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.chartview)

        # Initializing existing profile page data from db
        # Getting the app path
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        # Creating the enel electricity table
        connection.execute("CREATE TABLE IF NOT EXISTS enel_bills([id_counter] integer PRIMARY KEY,\
            [username] text,\
            [email] text,\
            [bill_year] text,\
            [id_bill] text,\
            [address] text,\
            [client] text,\
            [client_code] text,\
            [pay_code] text,\
            [total_pay] text,\
            [issue_date] text,\
            [due_date] date)")
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
        self.ui.treeElectricityDirectory.customContextMenuRequested.connect(self.contextMenuElectricity)

        # Electricity page buttons
        self.ui.btnAddElectricityBill.clicked.connect(self.addElectricityBill)

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

    def readBillContent(self, billPath):
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        with open(pathlib.Path(billPath), 'rb') as fh:

            for page in PDFPage.get_pages(fh,
                                          caching=True,
                                          check_extractable=True):
                page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()

        # close open handles
        converter.close()
        fake_file_handle.close()
        return text

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
                db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
                connection = sqlite3.connect(f'{db_path}')
                try:
                    db_connection = connection.cursor()
                    db_connection.execute("SELECT id_bill, address, issue_date, due_date, total_pay FROM enel_bills ORDER BY due_date desc LIMIT 1")
                    latest_bill_info = db_connection.fetchall()
                    self.ui.lblElectricityLastBillID.setText(latest_bill_info[0][0])
                    self.ui.lblElectricityLastBillAddress.setText(latest_bill_info[0][1])
                    self.ui.lblElectricityLastBillIssueDate.setText(latest_bill_info[0][2])
                    self.ui.lblElectricityLastBillDueDate.setText(latest_bill_info[0][3])
                    self.ui.lblElectricityLastBillTotalPay.setText(latest_bill_info[0][4])
                    connection.commit()
                    connection.close()
                    # add here the charts
                except:
                    self.generateMessageBox(window_title='Electricity page', msg_text='Please add electricity bills in order to view data!')
                self.model = QtWidgets.QFileSystemModel()
                self.model.setRootPath(electricity_path)
                self.ui.treeElectricityDirectory.setModel(self.model)
                self.ui.treeElectricityDirectory.setRootIndex(self.model.index(electricity_path))
                self.ui.treeElectricityDirectory.setSortingEnabled(True)

        else:
            self.generateMessageBox(window_title='Electricity page', msg_text='Please select the desired Electricity supplier from the Account preferences!')

    # Tree view open menu
    def contextMenuElectricity(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        delete = menu.addAction("Delete")
        get_info = menu.addAction("Get info")
        menu.setStyleSheet("QMenu{height: 81px; width: 80px; background-color: #2a2e32;} QMenu::item {height: 25px; width: 80px; font-family: \"SF UI Display\"; font-size: 10pt; color: #f3f5f6;} QMenu::item:selected {height: 25px; width: 80px; background-color: #EE4540; color: #f3f5f6;}")
        open.triggered.connect(self.openFileElectricity)
        delete.triggered.connect(self.deleteFileElectricity)
        get_info.triggered.connect(self.getInfoElectricity)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def openFileElectricity(self):
        index = self.ui.treeElectricityDirectory.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def deleteFileElectricity(self):
        index = self.ui.treeElectricityDirectory.currentIndex()
        path = self.model.filePath(index)
        try:
            self.bill_content = self.readBillContent(path)
            self.enel_id_bill_to_delete = re.findall(r"ID factură:\s*([^\n\r]*)", self.bill_content)[0]
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("DELETE FROM enel_bills WHERE id_bill = ?",(self.enel_id_bill_to_delete,))
            connection.commit()
            connection.close()
            os.remove(path)
        except:
            directory_to_delete = os.path.basename(os.path.normpath(path))
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("DELETE FROM enel_bills WHERE bill_year = ?",(directory_to_delete,))
            connection.commit()
            connection.close()
            shutil.rmtree(path)

    def getInfoElectricity(self):
        index = self.ui.treeElectricityDirectory.currentIndex()
        path = self.model.filePath(index)
        try:
            self.bill_content = self.readBillContent(path)
            self.enel_id_bill = re.findall(r"ID factură:\s*([^\n\r]*)", self.bill_content)[0]
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            db_connection.execute("SELECT id_bill, address, issue_date, due_date, total_pay FROM enel_bills WHERE id_bill = ?",(self.enel_id_bill,))
            bill_info = db_connection.fetchall()
            earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(self.username,))
            earnings = earnings_result.fetchone()[0]
            self.ui.lblElectricityLastBillID.setText(bill_info[0][0])
            self.ui.lblElectricityLastBillAddress.setText(bill_info[0][1])
            self.ui.lblElectricityLastBillIssueDate.setText(bill_info[0][2])
            self.ui.lblElectricityLastBillDueDate.setText(bill_info[0][3])
            self.ui.lblElectricityLastBillTotalPay.setText(bill_info[0][4])
            total_pay = bill_info[0][4]

            #####################
            # Try adding the chart
            #####################

            # Calculate percentage
            bill_value_strip = total_pay.strip()
            bill_value_string = bill_value_strip.replace(',','.')
            total_pay_float = float(bill_value_string)

            earnings_strip = earnings.strip()
            earnings_float = float(earnings_strip)

            bill_percentage = round((total_pay_float/earnings_float)*100, 2)
            remaining_earnings_percentage = round(100 - bill_percentage, 2)


            series = QtCharts.QPieSeries()
            series.setHoleSize(0.35)
            slice1 = QtCharts.QPieSlice()
            slice1 = series.append(f"Bill {bill_percentage}%", bill_percentage+25)
            slice1.setBrush(QColor('#EE4540'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#EE4540'))
            slice1.setLabelVisible()
            slice2 = QtCharts.QPieSlice()
            slice2 = series.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice2.setBrush(QColor('#6c6e71'))
            slice2.setLabelColor(QColor('#EE4540'))
            slice2.setLabelVisible()
            
            
            # Create Chart and set General Chart setting
            chart = QtCharts.QChart()
            # chart.legend().hide()
            chart.addSeries(series)
            chart.legend().setAlignment(QtCore.Qt.AlignBottom)
            chart.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chart.legend().setColor(QtGui.QColor('#EE4540'))
     
            chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chart.setBackgroundBrush(QBrush(QColor("transparent")))
   
            self.chartview.setChart(chart)
            self.chartview.setRenderHint(QPainter.Antialiasing)
            # self.ui.widget.setParent(None)

            connection.commit()
            connection.close()

        except:
            self.generateMessageBox(window_title='Electricity bill', msg_text='Please select a bill from the list!')

    def addElectricityBill(self):
        enel_file_full_path = QFileDialog.getOpenFileName(self, 'OpenFile')
        enel_file_path = enel_file_full_path[0]
        self.enel_bill_content = self.readBillContent(enel_file_path)
        # Get the year from the selected bill for ENEL and create a directory if it doesn't exist
        try:
            # Bill year for directory creation
            self.enel_bill_year = re.search(r"(\d+)(?!.*\d)+\n\nFURNIZOR Enel", self.enel_bill_content)[0].split()[0]
            # Bill enel electricity bill data
            self.enel_id_bill = re.findall(r"ID factură:\s*([^\n\r]*)", self.enel_bill_content)[0]
            self.enel_address = re.findall(r"Adresa de corespondenţă\n([^\n\r]*\n[^\n\r]*)", self.enel_bill_content)[0]
            self.enel_client = re.findall(r"Client:\s([^\n\r]*)", self.enel_bill_content)[0]
            self.enel_client_code = re.findall(r"Cod Client:\s([^\n\r]*)", self.enel_bill_content)[0]
            self.enel_pay_code = re.findall(r"Cod plata:\s([^\n\r]*)", self.enel_bill_content)[0]
            self.enel_total_pay = re.findall(r"([^\n\r]*)Lei", self.enel_bill_content)[0]
            self.enel_issue_date = re.findall(r"([0-9]{2}.[0-9]{2}.[0-9]{4})\n\nFURNIZOR Enel", self.enel_bill_content)[0]
            self.enel_due_date = re.findall(r"Dată scadenţă:\s([^\n\r]*)", self.enel_bill_content)[0]            
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("SELECT * FROM enel_bills WHERE id_bill = ?",(self.enel_id_bill,))
            if(len(result.fetchall()) > 0):
                self.generateMessageBox(window_title='Add bill information', msg_text='The selected bill is already added!')
                connection.commit()
                connection.close()
            else:
                db_connection.execute("INSERT INTO enel_bills(username, email, bill_year, id_bill, address, client, client_code, pay_code,\
                    total_pay, issue_date, due_date ) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(self.username, self.email, self.enel_bill_year, self.enel_id_bill,\
                    self.enel_address, self.enel_client, self.enel_client_code, self.enel_pay_code, self.enel_total_pay, self.enel_issue_date, self.enel_due_date))
                connection.commit()
                connection.close()
                pathlib.Path(str(pathlib.Path().absolute())+f'/Bills/{self.username}/Electricity/{self.enel_bill_year}').mkdir(parents=True, exist_ok=True)
                enel_new_file_path = str(pathlib.Path().absolute())+f'/Bills/{self.username}/Electricity/{self.enel_bill_year}'
                shutil.copy2(enel_file_path, enel_new_file_path, follow_symlinks=True)
                self.ui.lblElectricityLastBillID.setText(self.enel_id_bill)
                self.ui.lblElectricityLastBillAddress.setText(self.enel_address)
                self.ui.lblElectricityLastBillIssueDate.setText(self.enel_issue_date)
                self.ui.lblElectricityLastBillDueDate.setText(self.enel_due_date)
                self.ui.lblElectricityLastBillTotalPay.setText(self.enel_total_pay)
        except:
            self.generateMessageBox(window_title='Electricity bill', msg_text='Added electricity bill is not a(n) Enel bill!') 

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
        # Updating the electricity field for the logged in user in the db
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
        # Updating the natural gas field for the logged in user in the db
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
        # Updating the internet field for the logged in user in the db
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
        # Updating the subscription field for the logged in user in the db
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
        # Updating the subscription field for the logged in user in the db
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