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
from datetime import date
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
import speedtest
from currency_converter import CurrencyConverter

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

        # Electricit page chart widgets
        self.laydonutElectricityLastBill = QtWidgets.QVBoxLayout(self.ui.donutElectricityLastBill)
        self.ui.donutElectricityLastBill.setContentsMargins(0, 0, 0, 0)
        self.laydonutElectricityLastBill.setContentsMargins(0, 0, 0, 0)
        self.chartviewElectricityLastBill = QtCharts.QChartView()
        self.laydonutElectricityLastBill.addWidget(self.chartviewElectricityLastBill)

        self.laylineElectricityAllBills = QtWidgets.QVBoxLayout(self.ui.lineElectricityAllBillsPlot)
        self.ui.lineElectricityAllBillsPlot.setContentsMargins(0, 0, 0, 0)
        self.laylineElectricityAllBills.setContentsMargins(0, 0, 0, 0)
        self.chartviewElectricityAllBillsPlot = QtCharts.QChartView()
        self.laylineElectricityAllBills.addWidget(self.chartviewElectricityAllBillsPlot)

        # Natural gas page chart widgets
        self.laydonutNaturalGasLastBill = QtWidgets.QVBoxLayout(self.ui.donutNaturalGasLastBill)
        self.ui.donutNaturalGasLastBill.setContentsMargins(0, 0, 0, 0)
        self.laydonutNaturalGasLastBill.setContentsMargins(0, 0, 0, 0)
        self.chartviewNaturalGasLastBill = QtCharts.QChartView()
        self.laydonutNaturalGasLastBill.addWidget(self.chartviewNaturalGasLastBill)

        self.laylineNaturalGasAllBills = QtWidgets.QVBoxLayout(self.ui.lineNaturalGasAllBillsPlot)
        self.ui.lineNaturalGasAllBillsPlot.setContentsMargins(0, 0, 0, 0)
        self.laylineNaturalGasAllBills.setContentsMargins(0, 0, 0, 0)
        self.chartviewNaturalGasAllBillsPlot = QtCharts.QChartView()
        self.laylineNaturalGasAllBills.addWidget(self.chartviewNaturalGasAllBillsPlot)

        # Internet TV page chart widgets
        self.laydonutInternetTVLastBill = QtWidgets.QVBoxLayout(self.ui.donutInternetTVLastBill)
        self.ui.donutInternetTVLastBill.setContentsMargins(0, 0, 0, 0)
        self.laydonutInternetTVLastBill.setContentsMargins(0, 0, 0, 0)
        self.chartviewInternetTVLastBill = QtCharts.QChartView()
        self.laydonutInternetTVLastBill.addWidget(self.chartviewInternetTVLastBill)
        
        # Subscriptions page chart widgets
        self.laydonutSubscriptionsAll = QtWidgets.QVBoxLayout(self.ui.donutSubscriptionsAll)
        self.ui.donutSubscriptionsAll.setContentsMargins(0, 0, 0, 0)
        self.laydonutSubscriptionsAll.setContentsMargins(0, 0, 0, 0)
        self.chartviewSubscriptionsAll = QtCharts.QChartView()
        self.laydonutSubscriptionsAll.addWidget(self.chartviewSubscriptionsAll)

        self.laydonutSubscriptionsComparison = QtWidgets.QVBoxLayout(self.ui.barChartSubscriptionsComparison)
        self.ui.barChartSubscriptionsComparison.setContentsMargins(0, 0, 0, 0)
        self.laydonutSubscriptionsComparison.setContentsMargins(0, 0, 0, 0)
        self.chartviewSubscriptionsComparison = QtCharts.QChartView()
        self.laydonutSubscriptionsComparison.addWidget(self.chartviewSubscriptionsComparison)

        # Dashboard page chart widgets
        self.laydonutDashboard = QtWidgets.QVBoxLayout(self.ui.donutDashAllBills)
        self.ui.donutDashAllBills.setContentsMargins(0, 0, 0, 0)
        self.laydonutDashboard.setContentsMargins(0, 0, 0, 0)
        self.chartviewDonutDashboard = QtCharts.QChartView()
        self.laydonutDashboard.addWidget(self.chartviewDonutDashboard)

        self.layBarDashAllBills = QtWidgets.QVBoxLayout(self.ui.barDashAllBills)
        self.ui.barDashAllBills.setContentsMargins(0, 0, 0, 0)
        self.layBarDashAllBills.setContentsMargins(0, 0, 0, 0)
        self.chartviewBarDashboard = QtCharts.QChartView()
        self.layBarDashAllBills.addWidget(self.chartviewBarDashboard)

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
            [issue_date] date,\
            [due_date] date)")
        # Creating the engie electricity table
        connection.execute("CREATE TABLE IF NOT EXISTS engie_bills([id_counter] integer PRIMARY KEY,\
            [username] text,\
            [email] text,\
            [bill_year] text,\
            [id_bill] text,\
            [address] text,\
            [client] text,\
            [client_code] text,\
            [total_pay] text,\
            [issue_date] date,\
            [due_date] date)")
        # Creating the digi internet tv table
        connection.execute("CREATE TABLE IF NOT EXISTS digi_bills([id_counter] integer PRIMARY KEY,\
            [username] text,\
            [email] text,\
            [bill_year] text,\
            [id_bill] text,\
            [address] text,\
            [client] text,\
            [client_code] text,\
            [total_pay] text,\
            [issue_date] date,\
            [due_date] date)")
        # Creating the netflix table
        connection.execute("CREATE TABLE IF NOT EXISTS netflix_data([id_counter] integer PRIMARY KEY,\
            [username] text,\
            [email] text,\
            [start_day] integer,\
            [start_month] integer,\
            [start_year] integer,\
            [currency] text,\
            [pay] text,\
            [total_pay] text)")
        # Creating the spotify table
        connection.execute("CREATE TABLE IF NOT EXISTS spotify_data([id_counter] integer PRIMARY KEY,\
            [username] text,\
            [email] text,\
            [start_day] integer,\
            [start_month] integer,\
            [start_year] integer,\
            [currency] text,\
            [pay] text,\
            [total_pay] text)")
        # Creating the telecom table
        connection.execute("CREATE TABLE IF NOT EXISTS telecom_data([id_counter] integer PRIMARY KEY,\
            [username] text,\
            [email] text,\
            [start_day] integer,\
            [start_month] integer,\
            [start_year] integer,\
            [currency] text,\
            [pay] text,\
            [total_pay] text)")
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
        # Setting the Vodafone subscription
        vodafone_result = db_connection.execute("SELECT subscription_vodafone FROM accounts WHERE username = ?",(self.username,))
        vodafone = vodafone_result.fetchone()[0]
        if (vodafone == 1):
            self.ui.btnVodafoneSelection.setChecked(True)
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

        # Append data in the subscriptions comboboxes
        for day in range(1,32):
            self.ui.comboBoxNetflixDay.addItem(str(day))
            self.ui.comboBoxSpotifyDay.addItem(str(day))
            self.ui.comboBoxTelecomDay.addItem(str(day))

        for month in range (1,13):
            self.ui.comboBoxNetflixMonth.addItem(str(month))
            self.ui.comboBoxSpotifyMonth.addItem(str(month))
            self.ui.comboBoxTelecomMonth.addItem(str(month))

        for year in range(1990, now.year+1):
            self.ui.comboBoxNetflixYear.addItem(str(year))
            self.ui.comboBoxSpotifyYear.addItem(str(year))
            self.ui.comboBoxTelecomYear.addItem(str(year))

        currencies = ['RON', 'EUR']
        for currency in currencies:
            self.ui.comboBoxNetflixCurrency.addItem(currency)
            self.ui.comboBoxSpotifyCurrency.addItem(currency)
            self.ui.comboBoxTelecomCurrency.addItem(currency)

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

        # Set title name
        self.setWindowTitle("Billy")

        # Set window icon
        self.setWindowIcon(QtGui.QIcon(":/images/Resources/billy_logo.png"))

        # Set UI Definitions
        UIFunctions.uiDefinitions(self)

        # Set the default opened page
        # Call click on Dashboard button in order to load data
        self.dashboardButton()
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageDashboard)

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
        self.ui.btnVodafoneSelection.clicked.connect(self.setSubscriptionVodafone)

        # Tree view context
        self.ui.treeElectricityDirectory.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeElectricityDirectory.customContextMenuRequested.connect(self.contextMenuElectricity)

        self.ui.treeNaturalGasDirectory.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeNaturalGasDirectory.customContextMenuRequested.connect(self.contextMenuNaturalGas)

        self.ui.treeInternetTVDirectory.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeInternetTVDirectory.customContextMenuRequested.connect(self.contextMenuInternetTV)

        # Electricity page buttons
        self.ui.btnAddElectricityBill.clicked.connect(self.addElectricityBill)
        self.ui.comboBoxElectricityBillYear.currentIndexChanged.connect(self.plotElectricityLineChart)

        # Natural gas buttons
        self.ui.btnAddNaturalGasBill.clicked.connect(self.addNaturalGasBill)
        self.ui.comboBoxNaturalGasBillYear.currentIndexChanged.connect(self.plotNaturalGasLineChart)

        # Internet TV buttons
        self.ui.btnAddInternetTVBill.clicked.connect(self.addInternetTVBill)
        self.ui.btnTestInternetSpeed.clicked.connect(self.testInternetSpeed)

        # Subscriptions set buttons
        self.ui.btnSetNetflixData.clicked.connect(self.setNetflixData)
        self.ui.btnSetSpotifyData.clicked.connect(self.setSpotifyData)
        self.ui.btnSetTelecomData.clicked.connect(self.setTelecomData)

        # Dashboard info button
        self.ui.btnInformation.clicked.connect(self.dashboardInformation)
        self.ui.btnDashboardToAccountPreferences.clicked.connect(self.profilePage)

        # Information buttons
        self.ui.btnInformationElectricity.clicked.connect(self.electricityInformation)
        self.ui.btnInformationNaturalGas.clicked.connect(self.naturalGasInformation)
        self.ui.btnInformationInternetTV.clicked.connect(self.internetTVInformation)

        # App information button
        self.ui.btnAppInfo.clicked.connect(self.applicationInformation)

        # Center the app in the middle of the display
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

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

    # Display the Dashboard message box
    def dashboardInformation(self):
        username = self.username
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(username,))
        earnings = earnings_result.fetchone()[0]
        if earnings is None:
            self.generateMessageBox(window_title='Dashboard page', msg_text='Please start by adding the earnings from the Account preferences!\
    Adding the earnings per month is necessary in order to display data throughout the application!')
        else:
            self.generateMessageBox(window_title='Dashboard page', msg_text='Continue by adding bills for the selected providers/suppliers!')
        connection.commit()
        connection.close()

    # Click on the Dashboard button
    def dashboardButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageDashboard, self.ui.btnDashboard, [self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions])

        # Setting the current date
        date = datetime.datetime.now()
        self.ui.txtDashCurrentDate.setText(date.strftime("%d %b %Y"))

        username = self.username
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()

        db_connection.execute("SELECT due_date, total_pay FROM enel_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
        electricity_bill = db_connection.fetchall()
        if (electricity_bill != []):
            self.ui.txtElectricityDueDateDash.setText(datetime.datetime.strptime(f"{electricity_bill[0][0]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
            self.ui.txtElectricityPayDash.setText(electricity_bill[0][1] + "  RON")
        db_connection.execute("SELECT due_date, total_pay FROM engie_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
        natural_gas_bill = db_connection.fetchall()
        if (natural_gas_bill != []):
            self.ui.txtNaturalGasDueDateDash.setText(datetime.datetime.strptime(f"{natural_gas_bill[0][0]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
            self.ui.txtNaturalGasPayDash.setText(natural_gas_bill[0][1] + "  RON")
        db_connection.execute("SELECT due_date, total_pay FROM digi_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
        internetTV_bill = db_connection.fetchall()
        if (internetTV_bill != []):
            self.ui.txtInternetDueDateDash.setText(datetime.datetime.strptime(f"{internetTV_bill[0][0]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
            self.ui.txtInternetPayDash.setText(internetTV_bill[0][1] + "  RON")

        # Populate the subscription frames
        netflix_result = db_connection.execute("SELECT subscription_netflix FROM accounts WHERE username = ?",(username,))
        netflix = netflix_result.fetchone()[0]
        spotify_result = db_connection.execute("SELECT subscription_spotify FROM accounts WHERE username = ?",(username,))
        spotify = spotify_result.fetchone()[0]
        vodafone_result = db_connection.execute("SELECT subscription_vodafone FROM accounts WHERE username = ?",(username,))
        vodafone = vodafone_result.fetchone()[0]
        if netflix == 1:
                self.ui.txtNetflixDash.setStyleSheet("background-image: url(:/images/Resources/dash_netflix.png);\
                                                                        background-color: #202528;\
                                                                        border-radius: 5px;\
                                                                        background-repeat: none;\
                                                                        background-position: center;")
        if spotify == 1:
                self.ui.txtSpotifyDash.setStyleSheet("background-image: url(:/images/Resources/dash_spotify.png);\
                                                                        background-color: #202528;\
                                                                        border-radius: 5px;\
                                                                        background-repeat: none;\
                                                                        background-position: center;")
        if vodafone == 1:
                self.ui.txtVodafoneDash.setStyleSheet("background-image: url(:/images/Resources/dash_vodafone.png);\
                                                                        background-color: #202528;\
                                                                        border-radius: 5px;\
                                                                        background-repeat: none;\
                                                                        background-position: center;")

        # Set the earnings text form and plotting charts
        earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(username,))
        earnings = earnings_result.fetchone()[0]
        if earnings is not None:
            self.ui.txtDashEarnings.setText(earnings + "  RON")

            if (electricity_bill != [] and natural_gas_bill == [] and internetTV_bill == []):
                # Plot the donut chart
                electricity_bill_value_strip = electricity_bill[0][1].strip()
                electricity_bill_value_string = electricity_bill_value_strip.replace(',','.')
                electricity_total_pay_float = float(electricity_bill_value_string)

                earnings_strip = earnings.strip()
                earnings_float = float(earnings_strip)
                electricity_bill_percentage = round((electricity_total_pay_float/earnings_float)*100, 2)
                remaining_earnings_percentage = round(100 - electricity_bill_percentage, 2)

                seriesDonutDashboard = QtCharts.QPieSeries()
                seriesDonutDashboard.setHoleSize(0.35)
                slice1 = QtCharts.QPieSlice()
                slice1 = seriesDonutDashboard.append(f"Electricity {electricity_bill_percentage}%", electricity_bill_percentage+25)
                slice1.setBrush(QColor('#F7CA18'))
                slice1.setExploded()
                slice1.setLabelColor(QColor('#F7CA18'))
                slice1.setLabelFont(QFont("SF UI Display", 7))
                slice1.setLabelVisible()

                slice2 = QtCharts.QPieSlice()
                slice2 = seriesDonutDashboard.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
                slice2.setBrush(QColor('#6c6e71'))
                slice2.setLabelColor(QColor('#6c6e71'))
                slice2.setLabelFont(QFont("SF UI Display", 7))
                slice2.setLabelVisible()
                            
                # Create Chart and set General Chart setting
                chartDonutDashboard = QtCharts.QChart()
                chartDonutDashboard.addSeries(seriesDonutDashboard)
                chartDonutDashboard.legend().setAlignment(QtCore.Qt.AlignBottom)
                chartDonutDashboard.legend().setFont(QtGui.QFont("SF UI Display", 10))
                chartDonutDashboard.legend().setColor(QtGui.QColor('#EE4540'))
         
                chartDonutDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                chartDonutDashboard.setBackgroundBrush(QBrush(QColor("transparent")))

                self.chartviewDonutDashboard.setChart(chartDonutDashboard)
                self.chartviewDonutDashboard.setRenderHint(QPainter.Antialiasing)

                # Plot the bar char for the bills
                set0 = QtCharts.QBarSet('Electricity')

                set0.append(electricity_total_pay_float)
                set0.setBrush(QColor('#F7CA18'))

                seriesBarDashboard = QtCharts.QBarSeries()
                seriesBarDashboard.append(set0)

                chartBarDashboard = QtCharts.QChart()
                chartBarDashboard.addSeries(seriesBarDashboard)
                chartBarDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

                axisX = QtCharts.QBarCategoryAxis()
                axis_x_brush = QBrush(QColor("#EE4540"))
                axisX.setLabelsBrush(axis_x_brush)
                axisX.setTitleBrush(axis_x_brush)
                axisX.setTitleText("Suppliers")

                axisY = QtCharts.QValueAxis()
                axisY.setLabelFormat("%i")
                axisY.setTitleText("Bill cost")
                axisY.setMax(500)
                axisY.setMin(0)
                axisY.setTickCount(4)
                axis_y_brush = QBrush(QColor("#EE4540"))
                axisY.setLabelsBrush(axis_y_brush)            
                axisY.setTitleBrush(axis_y_brush)

                chartBarDashboard.addAxis(axisX, Qt.AlignBottom)
                chartBarDashboard.addAxis(axisY, Qt.AlignLeft)

                seriesBarDashboard.attachAxis(axisY)            

                chartBarDashboard.setBackgroundBrush(QBrush(QColor("transparent")))
                chartBarDashboard.setTitleBrush(QBrush(Qt.white));

                chartBarDashboard.legend().setVisible(True)
                chartBarDashboard.legend().setBrush(QBrush(Qt.white))
                chartBarDashboard.legend().setAlignment(Qt.AlignBottom)

                self.chartviewBarDashboard.setChart(chartBarDashboard)
                self.chartviewBarDashboard.setRenderHint(QPainter.Antialiasing)

            elif (electricity_bill != [] and natural_gas_bill != [] and internetTV_bill == []):
                # Plot the donut chart
                electricity_bill_value_strip = electricity_bill[0][1].strip()
                electricity_bill_value_string = electricity_bill_value_strip.replace(',','.')
                electricity_total_pay_float = float(electricity_bill_value_string)

                natural_gas_bill_value_strip = natural_gas_bill[0][1].strip()
                natural_gas_bill_value_string = natural_gas_bill_value_strip.replace(',','.')
                natural_gas_total_pay_float = float(natural_gas_bill_value_string)

                earnings_strip = earnings.strip()
                earnings_float = float(earnings_strip)
                electricity_bill_percentage = round((electricity_total_pay_float/earnings_float)*100, 2)
                natural_gas_bill_percentage = round((natural_gas_total_pay_float/earnings_float)*100, 2)
                remaining_earnings_percentage = round(100 - electricity_bill_percentage - natural_gas_bill_percentage, 2)

                seriesDonutDashboard = QtCharts.QPieSeries()
                seriesDonutDashboard.setHoleSize(0.35)
                slice1 = QtCharts.QPieSlice()
                slice1 = seriesDonutDashboard.append(f"Electricity {electricity_bill_percentage}%", electricity_bill_percentage+25)
                slice1.setBrush(QColor('#F7CA18'))
                slice1.setExploded()
                slice1.setLabelColor(QColor('#F7CA18'))
                slice1.setLabelFont(QFont("SF UI Display", 7))
                slice1.setLabelVisible()

                slice2 = QtCharts.QPieSlice()
                slice2 = seriesDonutDashboard.append(f"Natural Gas {natural_gas_bill_percentage}%", natural_gas_bill_percentage+25)
                slice2.setBrush(QColor('#DC3023'))
                slice2.setExploded()
                slice2.setLabelColor(QColor('#DC3023'))
                slice2.setLabelFont(QFont("SF UI Display", 7))
                slice2.setLabelVisible()

                slice3 = QtCharts.QPieSlice()
                slice3 = seriesDonutDashboard.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
                slice3.setBrush(QColor('#6c6e71'))
                slice3.setLabelColor(QColor('#6c6e71'))
                slice3.setLabelFont(QFont("SF UI Display", 7))
                slice3.setLabelVisible()
                            
                # Create Chart and set General Chart setting
                chartDonutDashboard = QtCharts.QChart()
                chartDonutDashboard.addSeries(seriesDonutDashboard)
                chartDonutDashboard.legend().setAlignment(QtCore.Qt.AlignBottom)
                chartDonutDashboard.legend().setFont(QtGui.QFont("SF UI Display", 10))
                chartDonutDashboard.legend().setColor(QtGui.QColor('#EE4540'))
         
                chartDonutDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                chartDonutDashboard.setBackgroundBrush(QBrush(QColor("transparent")))

                self.chartviewDonutDashboard.setChart(chartDonutDashboard)
                self.chartviewDonutDashboard.setRenderHint(QPainter.Antialiasing)

                # Plot the bar char for the bills
                set0 = QtCharts.QBarSet('Electricity')
                set1 = QtCharts.QBarSet('Natural Gas')

                set0.append(electricity_total_pay_float)
                set0.setBrush(QColor('#F7CA18'))
                set1.append(natural_gas_total_pay_float)
                set1.setBrush(QColor('#DC3023'))

                seriesBarDashboard = QtCharts.QBarSeries()
                seriesBarDashboard.append(set0)
                seriesBarDashboard.append(set1)

                chartBarDashboard = QtCharts.QChart()
                chartBarDashboard.addSeries(seriesBarDashboard)
                chartBarDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

                axisX = QtCharts.QBarCategoryAxis()
                axis_x_brush = QBrush(QColor("#EE4540"))
                axisX.setLabelsBrush(axis_x_brush)
                axisX.setTitleBrush(axis_x_brush)
                axisX.setTitleText("Suppliers")

                axisY = QtCharts.QValueAxis()
                axisY.setLabelFormat("%i")
                axisY.setTitleText("Bill cost")
                axisY.setMax(500)
                axisY.setMin(0)
                axisY.setTickCount(4)
                axis_y_brush = QBrush(QColor("#EE4540"))
                axisY.setLabelsBrush(axis_y_brush)            
                axisY.setTitleBrush(axis_y_brush)

                chartBarDashboard.addAxis(axisX, Qt.AlignBottom)
                chartBarDashboard.addAxis(axisY, Qt.AlignLeft)

                seriesBarDashboard.attachAxis(axisY)            

                chartBarDashboard.setBackgroundBrush(QBrush(QColor("transparent")))
                chartBarDashboard.setTitleBrush(QBrush(Qt.white));

                chartBarDashboard.legend().setVisible(True)
                chartBarDashboard.legend().setBrush(QBrush(Qt.white))
                chartBarDashboard.legend().setAlignment(Qt.AlignBottom)

                self.chartviewBarDashboard.setChart(chartBarDashboard)
                self.chartviewBarDashboard.setRenderHint(QPainter.Antialiasing)

            elif (electricity_bill != [] and natural_gas_bill != [] and internetTV_bill != []):
                # Plot the donut chart
                electricity_bill_value_strip = electricity_bill[0][1].strip()
                electricity_bill_value_string = electricity_bill_value_strip.replace(',','.')
                electricity_total_pay_float = float(electricity_bill_value_string)

                natural_gas_bill_value_strip = natural_gas_bill[0][1].strip()
                natural_gas_bill_value_string = natural_gas_bill_value_strip.replace(',','.')
                natural_gas_total_pay_float = float(natural_gas_bill_value_string)

                internetTV_bill_value_strip = internetTV_bill[0][1].strip()
                internetTV_bill_value_string = internetTV_bill_value_strip.replace(',','.')
                internetTV_total_pay_float = float(internetTV_bill_value_string)

                earnings_strip = earnings.strip()
                earnings_float = float(earnings_strip)
                electricity_bill_percentage = round((electricity_total_pay_float/earnings_float)*100, 2)
                natural_gas_bill_percentage = round((natural_gas_total_pay_float/earnings_float)*100, 2)
                internetTV_bill_percentage = round((internetTV_total_pay_float/earnings_float)*100, 2)
                remaining_earnings_percentage = round(100 - electricity_bill_percentage - natural_gas_bill_percentage - internetTV_bill_percentage, 2)

                seriesDonutDashboard = QtCharts.QPieSeries()
                seriesDonutDashboard.setHoleSize(0.35)
                slice1 = QtCharts.QPieSlice()
                slice1 = seriesDonutDashboard.append(f"Electricity {electricity_bill_percentage}%", electricity_bill_percentage+25)
                slice1.setBrush(QColor('#F7CA18'))
                slice1.setExploded()
                slice1.setLabelColor(QColor('#F7CA18'))
                slice1.setLabelFont(QFont("SF UI Display", 7))
                slice1.setLabelVisible()

                slice2 = QtCharts.QPieSlice()
                slice2 = seriesDonutDashboard.append(f"Natural Gas {natural_gas_bill_percentage}%", natural_gas_bill_percentage+25)
                slice2.setBrush(QColor('#DC3023'))
                slice2.setExploded()
                slice2.setLabelColor(QColor('#DC3023'))
                slice2.setLabelFont(QFont("SF UI Display", 7))
                slice2.setLabelVisible()

                slice3 = QtCharts.QPieSlice()
                slice3 = seriesDonutDashboard.append(f"InternetTV {internetTV_bill_percentage}%", internetTV_bill_percentage+25)
                slice3.setBrush(QColor('#22A7F0'))
                slice3.setExploded()
                slice3.setLabelColor(QColor('#22A7F0'))
                slice3.setLabelFont(QFont("SF UI Display", 7))
                slice3.setLabelVisible()

                slice4 = QtCharts.QPieSlice()
                slice4 = seriesDonutDashboard.append(f"Earnings{remaining_earnings_percentage}%", remaining_earnings_percentage)
                slice4.setBrush(QColor('#6c6e71'))
                slice4.setLabelColor(QColor('#6c6e71'))
                slice4.setLabelFont(QFont("SF UI Display", 7))
                slice4.setLabelVisible()
                            
                # Create Chart and set General Chart setting
                chartDonutDashboard = QtCharts.QChart()
                chartDonutDashboard.addSeries(seriesDonutDashboard)
                chartDonutDashboard.legend().setAlignment(QtCore.Qt.AlignBottom)
                chartDonutDashboard.legend().setFont(QtGui.QFont("SF UI Display", 10))
                chartDonutDashboard.legend().setColor(QtGui.QColor('#EE4540'))
         
                chartDonutDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                chartDonutDashboard.setBackgroundBrush(QBrush(QColor("transparent")))

                self.chartviewDonutDashboard.setChart(chartDonutDashboard)
                self.chartviewDonutDashboard.setRenderHint(QPainter.Antialiasing)

                # Plot the bar char for the bills
                set0 = QtCharts.QBarSet('Electricity')
                set1 = QtCharts.QBarSet('Natural Gas')
                set2 = QtCharts.QBarSet('Internet & TV')

                set0.append(electricity_total_pay_float)
                set0.setBrush(QColor('#F7CA18'))
                set1.append(natural_gas_total_pay_float)
                set1.setBrush(QColor('#DC3023'))
                set2.append(internetTV_total_pay_float)
                set2.setBrush(QColor('#22A7F0'))

                seriesBarDashboard = QtCharts.QBarSeries()
                seriesBarDashboard.append(set0)
                seriesBarDashboard.append(set1)
                seriesBarDashboard.append(set2)

                chartBarDashboard = QtCharts.QChart()
                chartBarDashboard.addSeries(seriesBarDashboard)
                chartBarDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

                axisX = QtCharts.QBarCategoryAxis()
                axis_x_brush = QBrush(QColor("#EE4540"))
                axisX.setLabelsBrush(axis_x_brush)
                axisX.setTitleBrush(axis_x_brush)
                axisX.setTitleText("Suppliers")

                axisY = QtCharts.QValueAxis()
                axisY.setLabelFormat("%i")
                axisY.setTitleText("Bill cost")
                axisY.setMax(500)
                axisY.setMin(0)
                axisY.setTickCount(4)
                axis_y_brush = QBrush(QColor("#EE4540"))
                axisY.setLabelsBrush(axis_y_brush)            
                axisY.setTitleBrush(axis_y_brush)

                chartBarDashboard.addAxis(axisX, Qt.AlignBottom)
                chartBarDashboard.addAxis(axisY, Qt.AlignLeft)

                seriesBarDashboard.attachAxis(axisY)            

                chartBarDashboard.setBackgroundBrush(QBrush(QColor("transparent")))
                chartBarDashboard.setTitleBrush(QBrush(Qt.white));

                chartBarDashboard.legend().setVisible(True)
                chartBarDashboard.legend().setBrush(QBrush(Qt.white))
                chartBarDashboard.legend().setAlignment(Qt.AlignBottom)

                self.chartviewBarDashboard.setChart(chartBarDashboard)
                self.chartviewBarDashboard.setRenderHint(QPainter.Antialiasing)

            elif (electricity_bill == [] and natural_gas_bill != [] and internetTV_bill != []):
                # Plot the donut chart
                natural_gas_bill_value_strip = natural_gas_bill[0][1].strip()
                natural_gas_bill_value_string = natural_gas_bill_value_strip.replace(',','.')
                natural_gas_total_pay_float = float(natural_gas_bill_value_string)

                internetTV_bill_value_strip = internetTV_bill[0][1].strip()
                internetTV_bill_value_string = internetTV_bill_value_strip.replace(',','.')
                internetTV_total_pay_float = float(internetTV_bill_value_string)

                earnings_strip = earnings.strip()
                earnings_float = float(earnings_strip)
                natural_gas_bill_percentage = round((natural_gas_total_pay_float/earnings_float)*100, 2)
                internetTV_bill_percentage = round((internetTV_total_pay_float/earnings_float)*100, 2)
                remaining_earnings_percentage = round(100 - natural_gas_bill_percentage - internetTV_bill_percentage, 2)

                seriesDonutDashboard = QtCharts.QPieSeries()
                seriesDonutDashboard.setHoleSize(0.35)
                slice1 = QtCharts.QPieSlice()
                slice1 = seriesDonutDashboard.append(f"Natural Gas {natural_gas_bill_percentage}%", natural_gas_bill_percentage+25)
                slice1.setBrush(QColor('#DC3023'))
                slice1.setExploded()
                slice1.setLabelColor(QColor('#DC3023'))
                slice1.setLabelFont(QFont("SF UI Display", 7))
                slice1.setLabelVisible()

                slice2 = QtCharts.QPieSlice()
                slice2 = seriesDonutDashboard.append(f"InternetTV {internetTV_bill_percentage}%", internetTV_bill_percentage+25)
                slice2.setBrush(QColor('#22A7F0'))
                slice2.setExploded()
                slice2.setLabelColor(QColor('#22A7F0'))
                slice2.setLabelFont(QFont("SF UI Display", 7))
                slice2.setLabelVisible()

                slice3 = QtCharts.QPieSlice()
                slice3 = seriesDonutDashboard.append(f"Earnings{remaining_earnings_percentage}%", remaining_earnings_percentage)
                slice3.setBrush(QColor('#6c6e71'))
                slice3.setLabelColor(QColor('#6c6e71'))
                slice3.setLabelFont(QFont("SF UI Display", 7))
                slice3.setLabelVisible()
                            
                # Create Chart and set General Chart setting
                chartDonutDashboard = QtCharts.QChart()
                chartDonutDashboard.addSeries(seriesDonutDashboard)
                chartDonutDashboard.legend().setAlignment(QtCore.Qt.AlignBottom)
                chartDonutDashboard.legend().setFont(QtGui.QFont("SF UI Display", 10))
                chartDonutDashboard.legend().setColor(QtGui.QColor('#EE4540'))
         
                chartDonutDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                chartDonutDashboard.setBackgroundBrush(QBrush(QColor("transparent")))

                self.chartviewDonutDashboard.setChart(chartDonutDashboard)
                self.chartviewDonutDashboard.setRenderHint(QPainter.Antialiasing)

                # Plot the bar char for the bills
                set0 = QtCharts.QBarSet('Natural Gas')
                set1 = QtCharts.QBarSet('Internet & TV')

                set0.append(natural_gas_total_pay_float)
                set0.setBrush(QColor('#DC3023'))
                set1.append(internetTV_total_pay_float)
                set1.setBrush(QColor('#22A7F0'))

                seriesBarDashboard = QtCharts.QBarSeries()
                seriesBarDashboard.append(set0)
                seriesBarDashboard.append(set1)

                chartBarDashboard = QtCharts.QChart()
                chartBarDashboard.addSeries(seriesBarDashboard)
                chartBarDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

                axisX = QtCharts.QBarCategoryAxis()
                axis_x_brush = QBrush(QColor("#EE4540"))
                axisX.setLabelsBrush(axis_x_brush)
                axisX.setTitleBrush(axis_x_brush)
                axisX.setTitleText("Suppliers")

                axisY = QtCharts.QValueAxis()
                axisY.setLabelFormat("%i")
                axisY.setTitleText("Bill cost")
                axisY.setMax(500)
                axisY.setMin(0)
                axisY.setTickCount(4)
                axis_y_brush = QBrush(QColor("#EE4540"))
                axisY.setLabelsBrush(axis_y_brush)            
                axisY.setTitleBrush(axis_y_brush)

                chartBarDashboard.addAxis(axisX, Qt.AlignBottom)
                chartBarDashboard.addAxis(axisY, Qt.AlignLeft)

                seriesBarDashboard.attachAxis(axisY)            

                chartBarDashboard.setBackgroundBrush(QBrush(QColor("transparent")))
                chartBarDashboard.setTitleBrush(QBrush(Qt.white));

                chartBarDashboard.legend().setVisible(True)
                chartBarDashboard.legend().setBrush(QBrush(Qt.white))
                chartBarDashboard.legend().setAlignment(Qt.AlignBottom)

                self.chartviewBarDashboard.setChart(chartBarDashboard)
                self.chartviewBarDashboard.setRenderHint(QPainter.Antialiasing)

            elif (electricity_bill == [] and natural_gas_bill == [] and internetTV_bill != []):
                # Plot the donut chart
                internetTV_bill_value_strip = internetTV_bill[0][1].strip()
                internetTV_bill_value_string = internetTV_bill_value_strip.replace(',','.')
                internetTV_total_pay_float = float(internetTV_bill_value_string)

                earnings_strip = earnings.strip()
                earnings_float = float(earnings_strip)
                internetTV_bill_percentage = round((internetTV_total_pay_float/earnings_float)*100, 2)
                remaining_earnings_percentage = round(100 - internetTV_bill_percentage, 2)

                seriesDonutDashboard = QtCharts.QPieSeries()
                seriesDonutDashboard.setHoleSize(0.35)
                slice1 = QtCharts.QPieSlice()
                slice1 = seriesDonutDashboard.append(f"InternetTV {internetTV_bill_percentage}%", internetTV_bill_percentage+25)
                slice1.setBrush(QColor('#22A7F0'))
                slice1.setExploded()
                slice1.setLabelColor(QColor('#22A7F0'))
                slice1.setLabelFont(QFont("SF UI Display", 7))
                slice1.setLabelVisible()

                slice2 = QtCharts.QPieSlice()
                slice2 = seriesDonutDashboard.append(f"Earnings{remaining_earnings_percentage}%", remaining_earnings_percentage)
                slice2.setBrush(QColor('#6c6e71'))
                slice2.setLabelColor(QColor('#6c6e71'))
                slice2.setLabelFont(QFont("SF UI Display", 7))
                slice2.setLabelVisible()
                            
                # Create Chart and set General Chart setting
                chartDonutDashboard = QtCharts.QChart()
                chartDonutDashboard.addSeries(seriesDonutDashboard)
                chartDonutDashboard.legend().setAlignment(QtCore.Qt.AlignBottom)
                chartDonutDashboard.legend().setFont(QtGui.QFont("SF UI Display", 10))
                chartDonutDashboard.legend().setColor(QtGui.QColor('#EE4540'))
         
                chartDonutDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                chartDonutDashboard.setBackgroundBrush(QBrush(QColor("transparent")))

                self.chartviewDonutDashboard.setChart(chartDonutDashboard)
                self.chartviewDonutDashboard.setRenderHint(QPainter.Antialiasing)

                # Plot the bar char for the bills
                set0 = QtCharts.QBarSet('Internet & TV')

                set0.append(internetTV_total_pay_float)
                set0.setBrush(QColor('#22A7F0'))

                seriesBarDashboard = QtCharts.QBarSeries()
                seriesBarDashboard.append(set0)

                chartBarDashboard = QtCharts.QChart()
                chartBarDashboard.addSeries(seriesBarDashboard)
                chartBarDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

                axisX = QtCharts.QBarCategoryAxis()
                axis_x_brush = QBrush(QColor("#EE4540"))
                axisX.setLabelsBrush(axis_x_brush)
                axisX.setTitleBrush(axis_x_brush)
                axisX.setTitleText("Suppliers")

                axisY = QtCharts.QValueAxis()
                axisY.setLabelFormat("%i")
                axisY.setTitleText("Bill cost")
                axisY.setMax(500)
                axisY.setMin(0)
                axisY.setTickCount(4)
                axis_y_brush = QBrush(QColor("#EE4540"))
                axisY.setLabelsBrush(axis_y_brush)            
                axisY.setTitleBrush(axis_y_brush)

                chartBarDashboard.addAxis(axisX, Qt.AlignBottom)
                chartBarDashboard.addAxis(axisY, Qt.AlignLeft)

                seriesBarDashboard.attachAxis(axisY)            

                chartBarDashboard.setBackgroundBrush(QBrush(QColor("transparent")))
                chartBarDashboard.setTitleBrush(QBrush(Qt.white));

                chartBarDashboard.legend().setVisible(True)
                chartBarDashboard.legend().setBrush(QBrush(Qt.white))
                chartBarDashboard.legend().setAlignment(Qt.AlignBottom)

                self.chartviewBarDashboard.setChart(chartBarDashboard)
                self.chartviewBarDashboard.setRenderHint(QPainter.Antialiasing)

            elif (electricity_bill == [] and natural_gas_bill != [] and internetTV_bill == []):
                # Plot the donut chart
                natural_gas_bill_value_strip = natural_gas_bill[0][1].strip()
                natural_gas_bill_value_string = natural_gas_bill_value_strip.replace(',','.')
                natural_gas_total_pay_float = float(natural_gas_bill_value_string)

                earnings_strip = earnings.strip()
                earnings_float = float(earnings_strip)
                natural_gas_bill_percentage = round((natural_gas_total_pay_float/earnings_float)*100, 2)
                remaining_earnings_percentage = round(100 - natural_gas_bill_percentage, 2)

                seriesDonutDashboard = QtCharts.QPieSeries()
                seriesDonutDashboard.setHoleSize(0.35)
                slice1 = QtCharts.QPieSlice()
                slice1 = seriesDonutDashboard.append(f"Natural Gas {natural_gas_bill_percentage}%", natural_gas_bill_percentage+25)
                slice1.setBrush(QColor('#DC3023'))
                slice1.setExploded()
                slice1.setLabelColor(QColor('#DC3023'))
                slice1.setLabelFont(QFont("SF UI Display", 7))
                slice1.setLabelVisible()

                slice2 = QtCharts.QPieSlice()
                slice2 = seriesDonutDashboard.append(f"Earnings{remaining_earnings_percentage}%", remaining_earnings_percentage)
                slice2.setBrush(QColor('#6c6e71'))
                slice2.setLabelColor(QColor('#6c6e71'))
                slice2.setLabelFont(QFont("SF UI Display", 7))
                slice2.setLabelVisible()
                            
                # Create Chart and set General Chart setting
                chartDonutDashboard = QtCharts.QChart()
                chartDonutDashboard.addSeries(seriesDonutDashboard)
                chartDonutDashboard.legend().setAlignment(QtCore.Qt.AlignBottom)
                chartDonutDashboard.legend().setFont(QtGui.QFont("SF UI Display", 10))
                chartDonutDashboard.legend().setColor(QtGui.QColor('#EE4540'))
         
                chartDonutDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                chartDonutDashboard.setBackgroundBrush(QBrush(QColor("transparent")))

                self.chartviewDonutDashboard.setChart(chartDonutDashboard)
                self.chartviewDonutDashboard.setRenderHint(QPainter.Antialiasing)

                # Plot the bar char for the bills
                set0 = QtCharts.QBarSet('Natural Gas')

                set0.append(natural_gas_total_pay_float)
                set0.setBrush(QColor('#DC3023'))

                seriesBarDashboard = QtCharts.QBarSeries()
                seriesBarDashboard.append(set0)

                chartBarDashboard = QtCharts.QChart()
                chartBarDashboard.addSeries(seriesBarDashboard)
                chartBarDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

                axisX = QtCharts.QBarCategoryAxis()
                axis_x_brush = QBrush(QColor("#EE4540"))
                axisX.setLabelsBrush(axis_x_brush)
                axisX.setTitleBrush(axis_x_brush)
                axisX.setTitleText("Suppliers")

                axisY = QtCharts.QValueAxis()
                axisY.setLabelFormat("%i")
                axisY.setTitleText("Bill cost")
                axisY.setMax(500)
                axisY.setMin(0)
                axisY.setTickCount(4)
                axis_y_brush = QBrush(QColor("#EE4540"))
                axisY.setLabelsBrush(axis_y_brush)            
                axisY.setTitleBrush(axis_y_brush)

                chartBarDashboard.addAxis(axisX, Qt.AlignBottom)
                chartBarDashboard.addAxis(axisY, Qt.AlignLeft)

                seriesBarDashboard.attachAxis(axisY)            

                chartBarDashboard.setBackgroundBrush(QBrush(QColor("transparent")))
                chartBarDashboard.setTitleBrush(QBrush(Qt.white));

                chartBarDashboard.legend().setVisible(True)
                chartBarDashboard.legend().setBrush(QBrush(Qt.white))
                chartBarDashboard.legend().setAlignment(Qt.AlignBottom)

                self.chartviewBarDashboard.setChart(chartBarDashboard)
                self.chartviewBarDashboard.setRenderHint(QPainter.Antialiasing)

            elif (electricity_bill != [] and natural_gas_bill == [] and internetTV_bill != []):
                # Plot the donut chart
                electricity_bill_value_strip = electricity_bill[0][1].strip()
                electricity_bill_value_string = electricity_bill_value_strip.replace(',','.')
                electricity_total_pay_float = float(electricity_bill_value_string)

                internetTV_bill_value_strip = internetTV_bill[0][1].strip()
                internetTV_bill_value_string = internetTV_bill_value_strip.replace(',','.')
                internetTV_total_pay_float = float(internetTV_bill_value_string)

                earnings_strip = earnings.strip()
                earnings_float = float(earnings_strip)
                electricity_bill_percentage = round((electricity_total_pay_float/earnings_float)*100, 2)
                internetTV_bill_percentage = round((internetTV_total_pay_float/earnings_float)*100, 2)
                remaining_earnings_percentage = round(100 - electricity_bill_percentage - internetTV_bill_percentage, 2)

                seriesDonutDashboard = QtCharts.QPieSeries()
                seriesDonutDashboard.setHoleSize(0.35)
                slice1 = QtCharts.QPieSlice()
                slice1 = seriesDonutDashboard.append(f"Electricity {electricity_bill_percentage}%", electricity_bill_percentage+25)
                slice1.setBrush(QColor('#F7CA18'))
                slice1.setExploded()
                slice1.setLabelColor(QColor('#F7CA18'))
                slice1.setLabelFont(QFont("SF UI Display", 7))
                slice1.setLabelVisible()

                slice2 = QtCharts.QPieSlice()
                slice2 = seriesDonutDashboard.append(f"InternetTV {internetTV_bill_percentage}%", internetTV_bill_percentage+25)
                slice2.setBrush(QColor('#22A7F0'))
                slice2.setExploded()
                slice2.setLabelColor(QColor('#22A7F0'))
                slice2.setLabelFont(QFont("SF UI Display", 7))
                slice2.setLabelVisible()

                slice3 = QtCharts.QPieSlice()
                slice3 = seriesDonutDashboard.append(f"Earnings{remaining_earnings_percentage}%", remaining_earnings_percentage)
                slice3.setBrush(QColor('#6c6e71'))
                slice3.setLabelColor(QColor('#6c6e71'))
                slice3.setLabelFont(QFont("SF UI Display", 7))
                slice3.setLabelVisible()
                            
                # Create Chart and set General Chart setting
                chartDonutDashboard = QtCharts.QChart()
                chartDonutDashboard.addSeries(seriesDonutDashboard)
                chartDonutDashboard.legend().setAlignment(QtCore.Qt.AlignBottom)
                chartDonutDashboard.legend().setFont(QtGui.QFont("SF UI Display", 10))
                chartDonutDashboard.legend().setColor(QtGui.QColor('#EE4540'))
         
                chartDonutDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                chartDonutDashboard.setBackgroundBrush(QBrush(QColor("transparent")))

                self.chartviewDonutDashboard.setChart(chartDonutDashboard)
                self.chartviewDonutDashboard.setRenderHint(QPainter.Antialiasing)

                # Plot the bar char for the bills
                set0 = QtCharts.QBarSet('Electricity')
                set1 = QtCharts.QBarSet('Internet & TV')

                set0.append(electricity_total_pay_float)
                set0.setBrush(QColor('#F7CA18'))
                set1.append(internetTV_total_pay_float)
                set1.setBrush(QColor('#22A7F0'))

                seriesBarDashboard = QtCharts.QBarSeries()
                seriesBarDashboard.append(set0)
                seriesBarDashboard.append(set1)

                chartBarDashboard = QtCharts.QChart()
                chartBarDashboard.addSeries(seriesBarDashboard)
                chartBarDashboard.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

                axisX = QtCharts.QBarCategoryAxis()
                axis_x_brush = QBrush(QColor("#EE4540"))
                axisX.setLabelsBrush(axis_x_brush)
                axisX.setTitleBrush(axis_x_brush)
                axisX.setTitleText("Suppliers")

                axisY = QtCharts.QValueAxis()
                axisY.setLabelFormat("%i")
                axisY.setTitleText("Bill cost")
                axisY.setMax(500)
                axisY.setMin(0)
                axisY.setTickCount(4)
                axis_y_brush = QBrush(QColor("#EE4540"))
                axisY.setLabelsBrush(axis_y_brush)            
                axisY.setTitleBrush(axis_y_brush)

                chartBarDashboard.addAxis(axisX, Qt.AlignBottom)
                chartBarDashboard.addAxis(axisY, Qt.AlignLeft)

                seriesBarDashboard.attachAxis(axisY)            

                chartBarDashboard.setBackgroundBrush(QBrush(QColor("transparent")))
                chartBarDashboard.setTitleBrush(QBrush(Qt.white));

                chartBarDashboard.legend().setVisible(True)
                chartBarDashboard.legend().setBrush(QBrush(Qt.white))
                chartBarDashboard.legend().setAlignment(Qt.AlignBottom)

                self.chartviewBarDashboard.setChart(chartBarDashboard)
                self.chartviewBarDashboard.setRenderHint(QPainter.Antialiasing)

        connection.commit()
        connection.close()

    def applicationInformation(self):
        self.generateMessageBox(window_title='Application info', msg_text='BILLY version 1.0\n\nDeveloped by Tiberiu Matei')

    # Click on the Calendar button
    def calendarButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageCalendar, self.ui.btnCalendar, [self.ui.btnDashboard, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions])
        
        calendar = self.ui.calendarWidget
        # Check if there is available data to display
        username = self.username
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()

        db_connection.execute("SELECT issue_date, due_date FROM enel_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
        electricity_bill_data = db_connection.fetchall()
        if (electricity_bill_data != []):
            electricity_issue_date_raw = electricity_bill_data[0][0]
            electricity_due_date_raw = electricity_bill_data[0][1]

            electricity_issue_date = QtCore.QDate.fromString(electricity_issue_date_raw, "yyyy-MM-dd")
            cell_format_electricity_issue_date = QtGui.QTextCharFormat()
            cell_format_electricity_issue_date.setBackground(QtGui.QColor("#a2ded0"))
            calendar.setDateTextFormat(electricity_issue_date, cell_format_electricity_issue_date)

            electricity_due_date = QtCore.QDate.fromString(electricity_due_date_raw, "yyyy-MM-dd")
            cell_format_electricity_due_date = QtGui.QTextCharFormat()
            cell_format_electricity_due_date.setBackground(QtGui.QColor("#00b16a"))
            calendar.setDateTextFormat(electricity_due_date, cell_format_electricity_due_date)

        db_connection.execute("SELECT issue_date, due_date FROM engie_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
        natural_gas_bill_data = db_connection.fetchall()
        if (natural_gas_bill_data != []):
            natural_gas_issue_date_raw = natural_gas_bill_data[0][0]
            natural_gas_due_date_raw = natural_gas_bill_data[0][1]

            natural_gas_issue_date = QtCore.QDate.fromString(natural_gas_issue_date_raw, "yyyy-MM-dd")
            cell_format_natural_gas_issue_date = QtGui.QTextCharFormat()
            cell_format_natural_gas_issue_date.setBackground(QtGui.QColor("#6bb9f0"))
            calendar.setDateTextFormat(natural_gas_issue_date, cell_format_natural_gas_issue_date)

            natural_gas_due_date = QtCore.QDate.fromString(natural_gas_due_date_raw, "yyyy-MM-dd")
            cell_format_natural_gas_due_date = QtGui.QTextCharFormat()
            cell_format_natural_gas_due_date.setBackground(QtGui.QColor("#5333ed"))
            calendar.setDateTextFormat(natural_gas_due_date, cell_format_natural_gas_due_date)

        db_connection.execute("SELECT issue_date, due_date FROM digi_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
        internet_tv_bill_data = db_connection.fetchall()
        if (internet_tv_bill_data != []):
            internet_tv_issue_date_raw = internet_tv_bill_data[0][0]
            internet_tv_due_date_raw = internet_tv_bill_data[0][1]

            internet_tv_issue_date = QtCore.QDate.fromString(internet_tv_issue_date_raw, "yyyy-MM-dd")
            cell_format_internet_tv_issue_date = QtGui.QTextCharFormat()
            cell_format_internet_tv_issue_date.setBackground(QtGui.QColor("#f1a9a0"))
            calendar.setDateTextFormat(internet_tv_issue_date, cell_format_internet_tv_issue_date)

            internet_tv_due_date = QtCore.QDate.fromString(internet_tv_due_date_raw, "yyyy-MM-dd")
            cell_format_internet_tv_due_date = QtGui.QTextCharFormat()
            cell_format_internet_tv_due_date.setBackground(QtGui.QColor("#ec644b"))
            calendar.setDateTextFormat(internet_tv_due_date, cell_format_internet_tv_due_date)

        connection.commit()
        connection.close()


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
            # Checking the selected Electricity supplier else display message box
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
                db_connection = connection.cursor()
                earnings_result_check = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(username,))
                earnings_check = earnings_result_check.fetchone()[0]
                connection.commit()
                connection.close()
                # Checking if the earnings field has data else display message box
                if earnings_check is not None:
                    try:
                        currpath = pathlib.Path().absolute()
                        electricity_path = str(currpath)+f'\\Bills\\{self.username}\\Electricity'
                        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
                        connection = sqlite3.connect(f'{db_path}')
                        db_connection = connection.cursor()
                        db_connection.execute("SELECT id_bill, address, issue_date, due_date, total_pay, bill_year FROM enel_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
                        latest_bill_info = db_connection.fetchall()
                        earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(username,))
                        earnings = earnings_result.fetchone()[0]
                        self.ui.lblElectricityLastBillID.setText(latest_bill_info[0][0])
                        self.ui.lblElectricityLastBillAddress.setText(latest_bill_info[0][1])
                        self.ui.lblElectricityLastBillIssueDate.setText(datetime.datetime.strptime(f"{latest_bill_info[0][2]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
                        self.ui.lblElectricityLastBillDueDate.setText(datetime.datetime.strptime(f"{latest_bill_info[0][3]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
                        self.ui.lblElectricityLastBillTotalPay.setText(latest_bill_info[0][4])
                        latest_bill_year = latest_bill_info[0][5]

                        # Plot the donut chart for clicking on the Electricity page button
                        bill_value_strip = latest_bill_info[0][4].strip()
                        bill_value_string = bill_value_strip.replace(',','.')
                        total_pay_float = float(bill_value_string)

                        earnings_strip = earnings.strip()
                        earnings_float = float(earnings_strip)

                        bill_percentage = round((total_pay_float/earnings_float)*100, 2)
                        remaining_earnings_percentage = round(100 - bill_percentage, 2)
                        seriesDonutElectricityLastBill = QtCharts.QPieSeries()
                        seriesDonutElectricityLastBill.setHoleSize(0.35)
                        slice1 = QtCharts.QPieSlice()
                        slice1 = seriesDonutElectricityLastBill.append(f"Bill {bill_percentage}%", bill_percentage+25)
                        slice1.setBrush(QColor('#EE4540'))
                        slice1.setExploded()
                        slice1.setLabelColor(QColor('#EE4540'))
                        slice1.setLabelFont(QFont("SF UI Display", 8))
                        slice1.setLabelVisible()
                        slice2 = QtCharts.QPieSlice()
                        slice2 = seriesDonutElectricityLastBill.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
                        slice2.setBrush(QColor('#6c6e71'))
                        slice2.setLabelColor(QColor('#6c6e71'))
                        slice2.setLabelFont(QFont("SF UI Display", 8))
                        slice2.setLabelVisible()
                                    
                        # Create Chart and set General Chart setting
                        chartDonutElectricityLastBill = QtCharts.QChart()
                        chartDonutElectricityLastBill.addSeries(seriesDonutElectricityLastBill)
                        chartDonutElectricityLastBill.legend().setAlignment(QtCore.Qt.AlignBottom)
                        chartDonutElectricityLastBill.legend().setFont(QtGui.QFont("SF UI Display", 10))
                        chartDonutElectricityLastBill.legend().setColor(QtGui.QColor('#EE4540'))
                 
                        chartDonutElectricityLastBill.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                        chartDonutElectricityLastBill.setBackgroundBrush(QBrush(QColor("transparent")))
               
                        self.chartviewElectricityLastBill.setChart(chartDonutElectricityLastBill)
                        self.chartviewElectricityLastBill.setRenderHint(QPainter.Antialiasing)
                        # Add plotting the line chart
                        self.ui.comboBoxElectricityBillYear.clear()
                        db_connection.execute("SELECT DISTINCT bill_year FROM enel_bills WHERE username = ?",(username,))
                        bill_years = db_connection.fetchall()
                        for year in bill_years:
                            self.ui.comboBoxElectricityBillYear.addItems(year)

                        # add here the charts
                        selected_year = latest_bill_year
                        self.ui.comboBoxElectricityBillYear.setCurrentText(selected_year)
                        db_connection.execute("SELECT issue_date,total_pay FROM enel_bills WHERE username = ? AND bill_year = ? ORDER BY due_date ASC", (self.username, selected_year))
                        query_result = db_connection.fetchall()
                        query_result.reverse()

                        # Line Electricity chart
                        seriesLineElectricityAllBills = QtCharts.QLineSeries()
                         # Create Chart and set General Chart setting
                        chartLineElectricityAllBills = QtCharts.QChart()
                        chartLineElectricityAllBills.addSeries(seriesLineElectricityAllBills)        

                         # Setting X-axis
                        axis_x = QtCharts.QDateTimeAxis()
                        axis_x.setTickCount(12)
                        axis_x.setLabelsAngle(70)
                        axis_x.setFormat("MM.yyyy")
                        axis_x.setTitleText("Date")
                        axis_x.setMin(QDate(int(f"{selected_year}"), 1 , 1))
                        axis_x.setMax(QDate(int(f"{selected_year}"), 12 , 31))        
                        axis_x_brush = QBrush(QColor("#EE4540"))
                        axis_x.setLabelsBrush(axis_x_brush)
                        axis_x.setTitleBrush(axis_x_brush)

                        # Setting Y-axis
                        axis_y = QtCharts.QValueAxis()
                        axis_y.setTickCount(5)
                        axis_y.setLabelFormat("%i")
                        axis_y.setTitleText("Bill cost [RON]")
                        axis_y.setMax(250)
                        axis_y.setMin(0)
                        axis_y_brush = QBrush(QColor("#EE4540"))
                        axis_y.setLabelsBrush(axis_y_brush)            
                        axis_y.setTitleBrush(axis_y_brush)

                        chartLineElectricityAllBills.addAxis(axis_x, Qt.AlignBottom)
                        chartLineElectricityAllBills.addAxis(axis_y, Qt.AlignLeft)
                        seriesLineElectricityAllBills.attachAxis(axis_x)
                        seriesLineElectricityAllBills.attachAxis(axis_y)

                        for item in query_result:
                            electricity_issue_time = QtCore.QDateTime()
                            correct_date = datetime.datetime.strptime(f"{item[0]}", "%Y-%m-%d").strftime("%d.%m.%Y")
                            list_of_date_info = correct_date.split(".")
                            bill_value_strip = item[1].strip()
                            bill_value_string = bill_value_strip.replace(',','.')
                            total_pay_float = float(bill_value_string)
                            # QDate - year, month, day
                            electricity_issue_time.setDate(QDate(int(f"{list_of_date_info[2]}"), int(f"{list_of_date_info[1]}") , int(f"{list_of_date_info[0]}")))
                            seriesLineElectricityAllBills.append(float(electricity_issue_time.toMSecsSinceEpoch()), total_pay_float)

                        seriesLineElectricityAllBills.setColor(QtGui.QColor('#EE4540'))

                        chartLineElectricityAllBills.legend().setVisible(False)            
                        chartLineElectricityAllBills.setBackgroundBrush(QBrush(QColor("transparent")))
                        chartLineElectricityAllBills.setTitleBrush(QBrush(Qt.white));

                        self.chartviewElectricityAllBillsPlot.setChart(chartLineElectricityAllBills)
                        self.chartviewElectricityAllBillsPlot.setRenderHint(QPainter.Antialiasing)

                        connection.commit()
                        connection.close()

                    except:
                        self.generateMessageBox(window_title='Electricity page', msg_text='Please add electricity bills in order to view data!')
                    self.modelElectricity = QtWidgets.QFileSystemModel()
                    self.modelElectricity.setRootPath(electricity_path)
                    self.ui.treeElectricityDirectory.setModel(self.modelElectricity)
                    self.ui.treeElectricityDirectory.setRootIndex(self.modelElectricity.index(electricity_path))
                    self.ui.treeElectricityDirectory.setSortingEnabled(True)
                else:
                    self.generateMessageBox(window_title='Electricity page', msg_text='Please add the earnings from the Account preferences!')
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
        file_path = self.modelElectricity.filePath(index)
        os.startfile(file_path)

    def deleteFileElectricity(self):
        index = self.ui.treeElectricityDirectory.currentIndex()
        path = self.modelElectricity.filePath(index)
        try:
            self.bill_content = self.readBillContent(path)
            self.enel_id_bill_to_delete = re.findall(r"ID factură:\s*([^\n\r]*)", self.bill_content)[0]
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("DELETE FROM enel_bills WHERE id_bill = ?",(self.enel_id_bill_to_delete,))

            # Updating the dropdown menu as well
            self.ui.comboBoxElectricityBillYear.clear()
            db_connection.execute("SELECT DISTINCT bill_year FROM enel_bills WHERE username = ?",(self.username,))
            bill_years = db_connection.fetchall()
            for year in bill_years:
                self.ui.comboBoxElectricityBillYear.addItems(year)

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
            
            # Updating the dropdown menu as well
            self.ui.comboBoxElectricityBillYear.clear()
            db_connection.execute("SELECT DISTINCT bill_year FROM enel_bills WHERE username = ?",(self.username,))
            bill_years = db_connection.fetchall()
            for year in bill_years:
                self.ui.comboBoxElectricityBillYear.addItems(year)

            connection.commit()
            connection.close()
            shutil.rmtree(path)

    def getInfoElectricity(self):
        index = self.ui.treeElectricityDirectory.currentIndex()
        path = self.modelElectricity.filePath(index)
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
            self.ui.lblElectricityLastBillIssueDate.setText(datetime.datetime.strptime(f"{bill_info[0][2]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
            self.ui.lblElectricityLastBillDueDate.setText(datetime.datetime.strptime(f"{bill_info[0][3]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
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

            # Donut Electricity chart
            seriesDonutElectricityLastBill = QtCharts.QPieSeries()
            seriesDonutElectricityLastBill.setHoleSize(0.35)
            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutElectricityLastBill.append(f"Bill {bill_percentage}%", bill_percentage+25)
            slice1.setBrush(QColor('#EE4540'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#EE4540'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutElectricityLastBill.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice2.setBrush(QColor('#6c6e71'))
            slice2.setLabelColor(QColor('#6c6e71'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutElectricityLastBill = QtCharts.QChart()
            chartDonutElectricityLastBill.addSeries(seriesDonutElectricityLastBill)
            chartDonutElectricityLastBill.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutElectricityLastBill.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutElectricityLastBill.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutElectricityLastBill.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutElectricityLastBill.setBackgroundBrush(QBrush(QColor("transparent")))
   
            self.chartviewElectricityLastBill.setChart(chartDonutElectricityLastBill)
            self.chartviewElectricityLastBill.setRenderHint(QPainter.Antialiasing)

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
            enel_issue_date_raw = re.findall(r"([0-9]{2}.[0-9]{2}.[0-9]{4})\n\nFURNIZOR Enel", self.enel_bill_content)[0]
            enel_due_date_raw = re.findall(r"Dată scadenţă:\s([^\n\r]*)", self.enel_bill_content)[0]
            self.enel_issue_date = datetime.datetime.strptime(f"{enel_issue_date_raw}", "%d.%m.%Y").strftime("%Y-%m-%d")
            self.enel_due_date = datetime.datetime.strptime(f"{enel_due_date_raw}", "%d.%m.%Y").strftime("%Y-%m-%d")
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("SELECT * FROM enel_bills WHERE id_bill = ? AND username = ?",(self.enel_id_bill, self.username))
            if(len(result.fetchall()) > 0):
                self.generateMessageBox(window_title='Add bill information', msg_text='The selected bill is already added!')
                connection.commit()
                connection.close()
            else:
                db_connection.execute("INSERT INTO enel_bills(username, email, bill_year, id_bill, address, client, client_code, pay_code,\
                    total_pay, issue_date, due_date ) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(self.username, self.email, self.enel_bill_year, self.enel_id_bill,\
                    self.enel_address, self.enel_client, self.enel_client_code, self.enel_pay_code, self.enel_total_pay, self.enel_issue_date, self.enel_due_date))
                
                # Adding the newly inserted year in the dropdown menu as well
                self.ui.comboBoxElectricityBillYear.clear()
                db_connection.execute("SELECT DISTINCT bill_year FROM enel_bills WHERE username = ?",(self.username,))
                bill_years = db_connection.fetchall()
                for year in bill_years:
                    self.ui.comboBoxElectricityBillYear.addItems(year)

                connection.commit()
                connection.close()
                pathlib.Path(str(pathlib.Path().absolute())+f'/Bills/{self.username}/Electricity/{self.enel_bill_year}').mkdir(parents=True, exist_ok=True)
                enel_new_file_path = str(pathlib.Path().absolute())+f'/Bills/{self.username}/Electricity/{self.enel_bill_year}'
                shutil.copy2(enel_file_path, enel_new_file_path, follow_symlinks=True)
                enel_issue_date_correct = datetime.datetime.strptime(f"{self.enel_issue_date}", "%Y-%m-%d").strftime("%d.%m.%Y")
                enel_due_date_correct = datetime.datetime.strptime(f"{self.enel_due_date}", "%Y-%m-%d").strftime("%d.%m.%Y")
                self.ui.lblElectricityLastBillID.setText(self.enel_id_bill)
                self.ui.lblElectricityLastBillAddress.setText(self.enel_address)
                self.ui.lblElectricityLastBillIssueDate.setText(enel_issue_date_correct)
                self.ui.lblElectricityLastBillDueDate.setText(enel_due_date_correct)
                self.ui.lblElectricityLastBillTotalPay.setText(self.enel_total_pay)
        except:
            self.generateMessageBox(window_title='Electricity bill', msg_text='Added electricity bill is not a(n) Enel bill!')

    def plotElectricityLineChart(self):
        selected_year = self.ui.comboBoxElectricityBillYear.currentText()

        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        db_connection.execute("SELECT issue_date,total_pay FROM enel_bills WHERE username = ? AND bill_year = ? ORDER BY due_date ASC", (self.username, selected_year))
        query_result = db_connection.fetchall()
        query_result.reverse()

        # Line Electricity chart
        seriesLineElectricityAllBills = QtCharts.QLineSeries()
         # Create Chart and set General Chart setting
        chartLineElectricityAllBills = QtCharts.QChart()
        chartLineElectricityAllBills.addSeries(seriesLineElectricityAllBills)        

         # Setting X-axis
        axis_x = QtCharts.QDateTimeAxis()
        axis_x.setTickCount(12)
        axis_x.setLabelsAngle(70)
        axis_x.setFormat("MM.yyyy")
        axis_x.setTitleText("Date")
        axis_x.setMin(QDate(int(f"{selected_year}"), 1 , 1))
        axis_x.setMax(QDate(int(f"{selected_year}"), 12 , 31))        
        axis_x_brush = QBrush(QColor("#EE4540"))
        axis_x.setLabelsBrush(axis_x_brush)
        axis_x.setTitleBrush(axis_x_brush)

        # Setting Y-axis
        axis_y = QtCharts.QValueAxis()
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%i")
        axis_y.setTitleText("Bill cost [RON]")
        axis_y.setMax(250)
        axis_y.setMin(0)
        axis_y_brush = QBrush(QColor("#EE4540"))
        axis_y.setLabelsBrush(axis_y_brush)            
        axis_y.setTitleBrush(axis_y_brush)

        chartLineElectricityAllBills.addAxis(axis_x, Qt.AlignBottom)
        chartLineElectricityAllBills.addAxis(axis_y, Qt.AlignLeft)
        seriesLineElectricityAllBills.attachAxis(axis_x)
        seriesLineElectricityAllBills.attachAxis(axis_y)

        for item in query_result:
            electricity_issue_time = QtCore.QDateTime()
            correct_date = datetime.datetime.strptime(f"{item[0]}", "%Y-%m-%d").strftime("%d.%m.%Y")
            list_of_date_info = correct_date.split(".")
            bill_value_strip = item[1].strip()
            bill_value_string = bill_value_strip.replace(',','.')
            total_pay_float = float(bill_value_string)
            # QDate - year, month, day
            electricity_issue_time.setDate(QDate(int(f"{list_of_date_info[2]}"), int(f"{list_of_date_info[1]}") , int(f"{list_of_date_info[0]}")))
            seriesLineElectricityAllBills.append(float(electricity_issue_time.toMSecsSinceEpoch()), total_pay_float)

        seriesLineElectricityAllBills.setColor(QtGui.QColor('#EE4540'))

        chartLineElectricityAllBills.legend().setVisible(False)            
        chartLineElectricityAllBills.setBackgroundBrush(QBrush(QColor("transparent")))
        chartLineElectricityAllBills.setTitleBrush(QBrush(Qt.white));

        self.chartviewElectricityAllBillsPlot.setChart(chartLineElectricityAllBills)
        self.chartviewElectricityAllBillsPlot.setRenderHint(QPainter.Antialiasing)
        connection.commit()
        connection.close()

    def electricityInformation(self):
        self.generateMessageBox(window_title='Electricity page', msg_text='Add electricity bill in order to be able to open, delete or get information from the bill!\nOpen, delete or get information by right-clicking on an added bill!')

    # Click on the NaturalGas button
    def naturalGasButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageNaturalGas, self.ui.btnNaturalGas, [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnInternetTV, self.ui.btnSubscriptions])

        username = self.username
        email = self.email
        # Checking the selected Natural gas supplier
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Setting the earnings data fields from db if it exists
        engie_result = db_connection.execute("SELECT gas_engie FROM accounts WHERE username = ?",(username,))
        engie = engie_result.fetchone()[0]
        cez_result = db_connection.execute("SELECT gas_cez FROM accounts WHERE username = ?",(username,))
        cez = cez_result.fetchone()[0]
        enel_result = db_connection.execute("SELECT gas_enel FROM accounts WHERE username = ?",(username,))
        enel = enel_result.fetchone()[0]
        eon_result = db_connection.execute("SELECT gas_eon FROM accounts WHERE username = ?",(username,))
        eon = eon_result.fetchone()[0]
        connection.commit()
        connection.close()
        if enel == 1 or cez == 1 or eon == 1 or engie == 1:
            # Checking the selected Natural gas supplier else display message box
            if engie == 1:
                self.ui.btnNaturalGasSupplierDisplay.setStyleSheet("background-image: url(:/images/Resources/engie_supplier.png);\
                                                                        background-color: #202528;\
                                                                        border-radius: 5px;\
                                                                        background-repeat: none;\
                                                                        background-position: center;")
                currpath = pathlib.Path().absolute()
                natural_gas_path = str(currpath)+f'\\Bills\\{self.username}\\NaturalGas'
                db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
                connection = sqlite3.connect(f'{db_path}')
                db_connection = connection.cursor()
                earnings_result_check = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(username,))
                earnings_check = earnings_result_check.fetchone()[0]
                connection.commit()
                connection.close()
                # Checking if the earnings field has data else display message box
                if earnings_check is not None:
                    try:
                        currpath = pathlib.Path().absolute()
                        natural_gas_path = str(currpath)+f'\\Bills\\{self.username}\\NaturalGas'
                        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
                        connection = sqlite3.connect(f'{db_path}')
                        db_connection = connection.cursor()
                        db_connection.execute("SELECT id_bill, address, issue_date, due_date, total_pay, bill_year FROM engie_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
                        latest_bill_info = db_connection.fetchall()
                        earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(username,))
                        earnings = earnings_result.fetchone()[0]
                        self.ui.lblNaturalGasLastBillID.setText(latest_bill_info[0][0])
                        self.ui.lblNaturalGasLastBillAddress.setText(latest_bill_info[0][1])
                        self.ui.lblNaturalGasLastBillIssueDate.setText(datetime.datetime.strptime(f"{latest_bill_info[0][2]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
                        self.ui.lblNaturalGasLastBillDueDate.setText(datetime.datetime.strptime(f"{latest_bill_info[0][3]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
                        self.ui.lblNaturalGasLastBillTotalPay.setText(latest_bill_info[0][4])
                        latest_bill_year = latest_bill_info[0][5]

                        # Plot the donut chart for clicking on the Natural gas page button
                        bill_value_strip = latest_bill_info[0][4].strip()
                        bill_value_string = bill_value_strip.replace(',','.')
                        total_pay_float = float(bill_value_string)

                        earnings_strip = earnings.strip()
                        earnings_float = float(earnings_strip)

                        bill_percentage = round((total_pay_float/earnings_float)*100, 2)
                        remaining_earnings_percentage = round(100 - bill_percentage, 2)

                        seriesDonutNaturalGasLastBill = QtCharts.QPieSeries()
                        seriesDonutNaturalGasLastBill.setHoleSize(0.35)
                        slice1 = QtCharts.QPieSlice()
                        slice1 = seriesDonutNaturalGasLastBill.append(f"Bill {bill_percentage}%", bill_percentage+25)
                        slice1.setBrush(QColor('#EE4540'))
                        slice1.setExploded()
                        slice1.setLabelColor(QColor('#EE4540'))
                        slice1.setLabelFont(QFont("SF UI Display", 8))
                        slice1.setLabelVisible()
                        slice2 = QtCharts.QPieSlice()
                        slice2 = seriesDonutNaturalGasLastBill.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
                        slice2.setBrush(QColor('#6c6e71'))
                        slice2.setLabelColor(QColor('#6c6e71'))
                        slice2.setLabelFont(QFont("SF UI Display", 8))
                        slice2.setLabelVisible()
                                    
                        # Create Chart and set General Chart setting
                        chartDonutNaturalGasLastBill = QtCharts.QChart()
                        chartDonutNaturalGasLastBill.addSeries(seriesDonutNaturalGasLastBill)
                        chartDonutNaturalGasLastBill.legend().setAlignment(QtCore.Qt.AlignBottom)
                        chartDonutNaturalGasLastBill.legend().setFont(QtGui.QFont("SF UI Display", 10))
                        chartDonutNaturalGasLastBill.legend().setColor(QtGui.QColor('#EE4540'))
                 
                        chartDonutNaturalGasLastBill.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                        chartDonutNaturalGasLastBill.setBackgroundBrush(QBrush(QColor("transparent")))
               
                        self.chartviewNaturalGasLastBill.setChart(chartDonutNaturalGasLastBill)
                        self.chartviewNaturalGasLastBill.setRenderHint(QPainter.Antialiasing)

                        # Add plotting the line chart
                        self.ui.comboBoxNaturalGasBillYear.clear()
                        db_connection.execute("SELECT DISTINCT bill_year FROM engie_bills WHERE username = ?",(username,))
                        bill_years = db_connection.fetchall()
                        for year in bill_years:
                            self.ui.comboBoxNaturalGasBillYear.addItems(year)

                        selected_year = latest_bill_year
                        self.ui.comboBoxNaturalGasBillYear.setCurrentText(selected_year)
                        db_connection.execute("SELECT issue_date,total_pay FROM engie_bills WHERE username = ? AND bill_year = ? ORDER BY due_date ASC", (self.username, selected_year))
                        query_result = db_connection.fetchall()
                        query_result.reverse()

                        # Line Natural gas chart
                        seriesLineNaturalGasAllBills = QtCharts.QLineSeries()
                         # Create Chart and set General Chart setting
                        chartLineNaturalGasAllBills = QtCharts.QChart()
                        chartLineNaturalGasAllBills.addSeries(seriesLineNaturalGasAllBills)        

                         # Setting X-axis
                        axis_x = QtCharts.QDateTimeAxis()
                        axis_x.setTickCount(12)
                        axis_x.setLabelsAngle(70)
                        axis_x.setFormat("MM.yyyy")
                        axis_x.setTitleText("Date")
                        axis_x.setMin(QDate(int(f"{selected_year}"), 1 , 1))
                        axis_x.setMax(QDate(int(f"{selected_year}"), 12 , 31))        
                        axis_x_brush = QBrush(QColor("#EE4540"))
                        axis_x.setLabelsBrush(axis_x_brush)
                        axis_x.setTitleBrush(axis_x_brush)

                        # Setting Y-axis
                        axis_y = QtCharts.QValueAxis()
                        axis_y.setTickCount(5)
                        axis_y.setLabelFormat("%i")
                        axis_y.setTitleText("Bill cost [RON]")
                        axis_y.setMax(500)
                        axis_y.setMin(0)
                        axis_y_brush = QBrush(QColor("#EE4540"))
                        axis_y.setLabelsBrush(axis_y_brush)            
                        axis_y.setTitleBrush(axis_y_brush)

                        chartLineNaturalGasAllBills.addAxis(axis_x, Qt.AlignBottom)
                        chartLineNaturalGasAllBills.addAxis(axis_y, Qt.AlignLeft)
                        seriesLineNaturalGasAllBills.attachAxis(axis_x)
                        seriesLineNaturalGasAllBills.attachAxis(axis_y)

                        for item in query_result:
                            natural_gas_issue_time = QtCore.QDateTime()
                            correct_date = datetime.datetime.strptime(f"{item[0]}", "%Y-%m-%d").strftime("%d.%m.%Y")
                            list_of_date_info = correct_date.split(".")
                            bill_value_strip = item[1].strip()
                            bill_value_string = bill_value_strip.replace(',','.')
                            total_pay_float = float(bill_value_string)
                            # QDate - year, month, day
                            natural_gas_issue_time.setDate(QDate(int(f"{list_of_date_info[2]}"), int(f"{list_of_date_info[1]}") , int(f"{list_of_date_info[0]}")))
                            seriesLineNaturalGasAllBills.append(float(natural_gas_issue_time.toMSecsSinceEpoch()), total_pay_float)

                        seriesLineNaturalGasAllBills.setColor(QtGui.QColor('#EE4540'))

                        chartLineNaturalGasAllBills.legend().setVisible(False)            
                        chartLineNaturalGasAllBills.setBackgroundBrush(QBrush(QColor("transparent")))
                        chartLineNaturalGasAllBills.setTitleBrush(QBrush(Qt.white));

                        self.chartviewNaturalGasAllBillsPlot.setChart(chartLineNaturalGasAllBills)
                        self.chartviewNaturalGasAllBillsPlot.setRenderHint(QPainter.Antialiasing)

                        connection.commit()
                        connection.close()

                    except:
                        self.generateMessageBox(window_title='Natural Gas page', msg_text='Please add natural gas bills in order to view data!')
                    self.modelNaturalGas = QtWidgets.QFileSystemModel()
                    self.modelNaturalGas.setRootPath(natural_gas_path)
                    self.ui.treeNaturalGasDirectory.setModel(self.modelNaturalGas)
                    self.ui.treeNaturalGasDirectory.setRootIndex(self.modelNaturalGas.index(natural_gas_path))
                    self.ui.treeNaturalGasDirectory.setSortingEnabled(True)
                else:
                    self.generateMessageBox(window_title='Natural Gas page', msg_text='Please add the earnings from the Account preferences!')
        else:
            self.generateMessageBox(window_title='Natural Gas page', msg_text='Please select the desired Natural gas supplier from the Account preferences!')

    # Tree view open menu
    def contextMenuNaturalGas(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        delete = menu.addAction("Delete")
        get_info = menu.addAction("Get info")
        menu.setStyleSheet("QMenu{height: 81px; width: 80px; background-color: #2a2e32;} QMenu::item {height: 25px; width: 80px; font-family: \"SF UI Display\"; font-size: 10pt; color: #f3f5f6;} QMenu::item:selected {height: 25px; width: 80px; background-color: #EE4540; color: #f3f5f6;}")
        open.triggered.connect(self.openFileNaturalGas)
        delete.triggered.connect(self.deleteFileNaturalGas)
        get_info.triggered.connect(self.getInfoNaturalGas)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def openFileNaturalGas(self):
        index = self.ui.treeNaturalGasDirectory.currentIndex()
        file_path = self.modelNaturalGas.filePath(index)
        os.startfile(file_path)

    def deleteFileNaturalGas(self):
        index = self.ui.treeNaturalGasDirectory.currentIndex()
        path = self.modelNaturalGas.filePath(index)
        try:
            self.bill_content_natural_gas = self.readBillContent(path)
            self.engie_id_bill_to_delete = re.findall(r"(\d+)(?!.*\d)+\nData facturii", self.bill_content_natural_gas)[0]
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("DELETE FROM engie_bills WHERE id_bill = ?",(self.engie_id_bill_to_delete,))

            # Updating the dropdown menu as well
            self.ui.comboBoxNaturalGasBillYear.clear()
            db_connection.execute("SELECT DISTINCT bill_year FROM engie_bills WHERE username = ?",(self.username,))
            bill_years = db_connection.fetchall()
            for year in bill_years:
                self.ui.comboBoxNaturalGasBillYear.addItems(year)

            connection.commit()
            connection.close()
            os.remove(path)
        except:
            directory_to_delete = os.path.basename(os.path.normpath(path))
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("DELETE FROM engie_bills WHERE bill_year = ?",(directory_to_delete,))
            
            # Updating the dropdown menu as well
            self.ui.comboBoxNaturalGasBillYear.clear()
            db_connection.execute("SELECT DISTINCT bill_year FROM engie_bills WHERE username = ?",(self.username,))
            bill_years = db_connection.fetchall()
            for year in bill_years:
                self.ui.comboBoxNaturalGasBillYear.addItems(year)

            connection.commit()
            connection.close()
            shutil.rmtree(path)

    def getInfoNaturalGas(self):
        index = self.ui.treeNaturalGasDirectory.currentIndex()
        path = self.modelNaturalGas.filePath(index)
        try:
            self.bill_content_natural_gas = self.readBillContent(path)
            self.engie_id_bill = re.findall(r"(\d+)(?!.*\d)+\nData facturii", self.bill_content_natural_gas)[0]
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            db_connection.execute("SELECT id_bill, address, issue_date, due_date, total_pay FROM engie_bills WHERE id_bill = ?",(self.engie_id_bill,))
            bill_info = db_connection.fetchall()
            earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(self.username,))
            earnings = earnings_result.fetchone()[0]
            self.ui.lblNaturalGasLastBillID.setText(bill_info[0][0])
            self.ui.lblNaturalGasLastBillAddress.setText(bill_info[0][1])
            self.ui.lblNaturalGasLastBillIssueDate.setText(datetime.datetime.strptime(f"{bill_info[0][2]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
            self.ui.lblNaturalGasLastBillDueDate.setText(datetime.datetime.strptime(f"{bill_info[0][3]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
            self.ui.lblNaturalGasLastBillTotalPay.setText(bill_info[0][4])
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

            # Donut NaturalGas chart
            seriesDonutNaturalGasLastBill = QtCharts.QPieSeries()
            seriesDonutNaturalGasLastBill.setHoleSize(0.35)
            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutNaturalGasLastBill.append(f"Bill {bill_percentage}%", bill_percentage+25)
            slice1.setBrush(QColor('#EE4540'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#EE4540'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutNaturalGasLastBill.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice2.setBrush(QColor('#6c6e71'))
            slice2.setLabelColor(QColor('#6c6e71'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutNaturalGasLastBill = QtCharts.QChart()
            chartDonutNaturalGasLastBill.addSeries(seriesDonutNaturalGasLastBill)
            chartDonutNaturalGasLastBill.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutNaturalGasLastBill.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutNaturalGasLastBill.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutNaturalGasLastBill.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutNaturalGasLastBill.setBackgroundBrush(QBrush(QColor("transparent")))
   
            self.chartviewNaturalGasLastBill.setChart(chartDonutNaturalGasLastBill)
            self.chartviewNaturalGasLastBill.setRenderHint(QPainter.Antialiasing)

            connection.commit()
            connection.close()

        except:
            self.generateMessageBox(window_title='Natural gas bill', msg_text='Please select a bill from the list!')

    def addNaturalGasBill(self):
        engie_file_full_path = QFileDialog.getOpenFileName(self, 'OpenFile')
        engie_file_path = engie_file_full_path[0]
        self.engie_bill_content = self.readBillContent(engie_file_path)
        # Get the year from the selected bill for ENGIE and create a directory if it doesn't exist
        try:
            # Bill year for directory creation
            self.engie_bill_year = re.search(r"(\d+)(?!.*\d)+\n\nFactura transmisa", self.engie_bill_content)[0].split()[0]            
            # Bill engie natural gas bill data
            self.engie_id_bill = re.findall(r"(\d+)(?!.*\d)+\nData facturii", self.engie_bill_content)[0]
            self.engie_address = re.findall(r"Adresa: ([^\n\r]*\n[^\n\r]*\n[^\n\r]*)", self.engie_bill_content)[0]
            self.engie_client = re.findall(r"Nume client:\s([^\n\r]*)", self.engie_bill_content)[0]
            client_code = re.findall(r"(\d+)(?!.*\d)\n\nFAC", self.engie_bill_content)[0]
            self.engie_client_code = client_code[0:13]
            self.engie_total_pay = re.findall(r"([^\n\r]*) LEI\n\nDATA", self.engie_bill_content)[0]
            engie_issue_date_raw = re.findall(r"([0-9]{2}.[0-9]{2}.[0-9]{4})\n\nFactura", self.engie_bill_content)[0]
            engie_due_date_raw = re.findall(r"DATA SCADENTĂ\n\s([^\n\r]*)", self.engie_bill_content)[0]
            self.engie_issue_date = datetime.datetime.strptime(f"{engie_issue_date_raw}", "%d.%m.%Y").strftime("%Y-%m-%d")
            self.engie_due_date = datetime.datetime.strptime(f"{engie_due_date_raw}", "%d.%m.%Y").strftime("%Y-%m-%d")
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            # Check if the bill is already added
            result = db_connection.execute("SELECT * FROM engie_bills WHERE id_bill = ? AND username = ?",(self.engie_id_bill, self.username))
            if(len(result.fetchall()) > 0):
                self.generateMessageBox(window_title='Add bill information', msg_text='The selected bill is already added!')
                connection.commit()
                connection.close()
            else:
                db_connection.execute("INSERT INTO engie_bills(username, email, bill_year, id_bill, address, client, client_code,\
                    total_pay, issue_date, due_date ) VALUES (?,?,?,?,?,?,?,?,?,?)",(self.username, self.email, self.engie_bill_year, self.engie_id_bill,\
                    self.engie_address, self.engie_client, self.engie_client_code, self.engie_total_pay, self.engie_issue_date, self.engie_due_date))
                
                # Adding the newly inserted year in the dropdown menu as well
                self.ui.comboBoxNaturalGasBillYear.clear()
                db_connection.execute("SELECT DISTINCT bill_year FROM engie_bills WHERE username = ?",(self.username,))
                bill_years = db_connection.fetchall()
                for year in bill_years:
                    self.ui.comboBoxNaturalGasBillYear.addItems(year)

                connection.commit()
                connection.close()
                pathlib.Path(str(pathlib.Path().absolute())+f'/Bills/{self.username}/NaturalGas/{self.engie_bill_year}').mkdir(parents=True, exist_ok=True)
                engie_new_file_path = str(pathlib.Path().absolute())+f'/Bills/{self.username}/NaturalGas/{self.engie_bill_year}'
                shutil.copy2(engie_file_path, engie_new_file_path, follow_symlinks=True)
                engie_issue_date_correct = datetime.datetime.strptime(f"{self.engie_issue_date}", "%Y-%m-%d").strftime("%d.%m.%Y")
                engie_due_date_correct = datetime.datetime.strptime(f"{self.engie_due_date}", "%Y-%m-%d").strftime("%d.%m.%Y")
                self.ui.lblNaturalGasLastBillID.setText(self.engie_id_bill)
                self.ui.lblNaturalGasLastBillAddress.setText(self.engie_address)
                self.ui.lblNaturalGasLastBillIssueDate.setText(engie_issue_date_correct)
                self.ui.lblNaturalGasLastBillDueDate.setText(engie_due_date_correct)
                self.ui.lblNaturalGasLastBillTotalPay.setText(self.engie_total_pay)
        except:
            self.generateMessageBox(window_title='Natural gas bill', msg_text='Added natural gas bill is not a(n) Engie bill!')

    def plotNaturalGasLineChart(self):
        selected_year = self.ui.comboBoxNaturalGasBillYear.currentText()

        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        db_connection.execute("SELECT issue_date,total_pay FROM engie_bills WHERE username = ? AND bill_year = ? ORDER BY due_date ASC", (self.username, selected_year))
        query_result = db_connection.fetchall()
        query_result.reverse()
        # Line natural gas chart
        seriesLineNaturalGasAllBills = QtCharts.QLineSeries()
         # Create Chart and set General Chart setting
        chartLineNaturalGasAllBills = QtCharts.QChart()
        chartLineNaturalGasAllBills.addSeries(seriesLineNaturalGasAllBills)        

         # Setting X-axis
        axis_x = QtCharts.QDateTimeAxis()
        axis_x.setTickCount(12)
        axis_x.setLabelsAngle(70)
        axis_x.setFormat("MM.yyyy")
        axis_x.setTitleText("Date")
        axis_x.setMin(QDate(int(f"{selected_year}"), 1 , 1))
        axis_x.setMax(QDate(int(f"{selected_year}"), 12 , 31))        
        axis_x_brush = QBrush(QColor("#EE4540"))
        axis_x.setLabelsBrush(axis_x_brush)
        axis_x.setTitleBrush(axis_x_brush)

        # Setting Y-axis
        axis_y = QtCharts.QValueAxis()
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%i")
        axis_y.setTitleText("Bill cost [RON]")
        axis_y.setMax(500)
        axis_y.setMin(0)
        axis_y_brush = QBrush(QColor("#EE4540"))
        axis_y.setLabelsBrush(axis_y_brush)            
        axis_y.setTitleBrush(axis_y_brush)

        chartLineNaturalGasAllBills.addAxis(axis_x, Qt.AlignBottom)
        chartLineNaturalGasAllBills.addAxis(axis_y, Qt.AlignLeft)
        seriesLineNaturalGasAllBills.attachAxis(axis_x)
        seriesLineNaturalGasAllBills.attachAxis(axis_y)

        for item in query_result:
            natural_gas_issue_time = QtCore.QDateTime()
            correct_date = datetime.datetime.strptime(f"{item[0]}", "%Y-%m-%d").strftime("%d.%m.%Y")
            list_of_date_info = correct_date.split(".")
            bill_value_strip = item[1].strip()
            bill_value_string = bill_value_strip.replace(',','.')
            total_pay_float = float(bill_value_string)
            # QDate - year, month, day
            natural_gas_issue_time.setDate(QDate(int(f"{list_of_date_info[2]}"), int(f"{list_of_date_info[1]}") , int(f"{list_of_date_info[0]}")))
            seriesLineNaturalGasAllBills.append(float(natural_gas_issue_time.toMSecsSinceEpoch()), total_pay_float)

        seriesLineNaturalGasAllBills.setColor(QtGui.QColor('#EE4540'))

        chartLineNaturalGasAllBills.legend().setVisible(False)            
        chartLineNaturalGasAllBills.setBackgroundBrush(QBrush(QColor("transparent")))
        chartLineNaturalGasAllBills.setTitleBrush(QBrush(Qt.white));

        self.chartviewNaturalGasAllBillsPlot.setChart(chartLineNaturalGasAllBills)
        self.chartviewNaturalGasAllBillsPlot.setRenderHint(QPainter.Antialiasing)
        connection.commit()
        connection.close()

    def naturalGasInformation(self):
        self.generateMessageBox(window_title='Natural Gas page', msg_text='Add natural gas bill in order to be able to open, delete or get information from the bill!\nOpen, delete or get information by right-clicking on an added bill!')

    # Click on the InternetTV button
    def internetTVButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageInternetTV, self.ui.btnInternetTV, [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnSubscriptions])

        username = self.username
        email = self.email
        # Checking the selected Natural gas supplier
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Setting the earnings data fields from db if it exists
        digi_result = db_connection.execute("SELECT internet_rds FROM accounts WHERE username = ?",(username,))
        digi = digi_result.fetchone()[0]
        upc_result = db_connection.execute("SELECT internet_upc FROM accounts WHERE username = ?",(username,))
        upc = upc_result.fetchone()[0]
        telekom_result = db_connection.execute("SELECT internet_telekom FROM accounts WHERE username = ?",(username,))
        telekom = telekom_result.fetchone()[0]
        gts_result = db_connection.execute("SELECT internet_gts FROM accounts WHERE username = ?",(username,))
        gts = gts_result.fetchone()[0]
        connection.commit()
        connection.close()
        if digi == 1 or upc == 1 or telekom == 1 or gts == 1:
            # Checking the selected Natural gas supplier else display message box
            if digi == 1:
                self.ui.btnInternetProviderDisplay.setStyleSheet("background-image: url(:/images/Resources/rcsrds_supplier.png);\
                                                                        background-color: #202528;\
                                                                        border-radius: 5px;\
                                                                        background-repeat: none;\
                                                                        background-position: center;")
                currpath = pathlib.Path().absolute()
                internet_tv_path = str(currpath)+f'\\Bills\\{self.username}\\InternetTV'
                db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
                connection = sqlite3.connect(f'{db_path}')
                db_connection = connection.cursor()
                earnings_result_check = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(username,))
                earnings_check = earnings_result_check.fetchone()[0]
                connection.commit()
                connection.close()
                # Checking if the earnings field has data else display message box
                if earnings_check is not None:
                    try:
                        currpath = pathlib.Path().absolute()
                        internet_tv_path = str(currpath)+f'\\Bills\\{self.username}\\InternetTV'
                        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
                        connection = sqlite3.connect(f'{db_path}')
                        db_connection = connection.cursor()
                        db_connection.execute("SELECT id_bill, address, issue_date, due_date, total_pay, bill_year FROM digi_bills WHERE username = ? ORDER BY due_date desc LIMIT 1",(username,))
                        latest_bill_info = db_connection.fetchall()
                        earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(username,))
                        earnings = earnings_result.fetchone()[0]
                        self.ui.lblInternetTVLastBillID.setText(latest_bill_info[0][0])
                        self.ui.lblInternetTVLastBillAddress.setText(latest_bill_info[0][1])
                        self.ui.lblInternetTVLastBillIssueDate.setText(datetime.datetime.strptime(f"{latest_bill_info[0][2]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
                        self.ui.lblInternetTVLastBillDueDate.setText(datetime.datetime.strptime(f"{latest_bill_info[0][3]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
                        self.ui.lblInternetTVLastBillTotalPay.setText(latest_bill_info[0][4])
                        latest_bill_year = latest_bill_info[0][5]

                        # Plot the donut chart for clicking on the Natural gas page button
                        bill_value_strip = latest_bill_info[0][4].strip()
                        bill_value_string = bill_value_strip.replace(',','.')
                        total_pay_float = float(bill_value_string)

                        earnings_strip = earnings.strip()
                        earnings_float = float(earnings_strip)

                        bill_percentage = round((total_pay_float/earnings_float)*100, 2)
                        remaining_earnings_percentage = round(100 - bill_percentage, 2)

                        seriesDonutInternetTVLastBill = QtCharts.QPieSeries()
                        seriesDonutInternetTVLastBill.setHoleSize(0.35)
                        slice1 = QtCharts.QPieSlice()
                        slice1 = seriesDonutInternetTVLastBill.append(f"Bill {bill_percentage}%", bill_percentage+25)
                        slice1.setBrush(QColor('#EE4540'))
                        slice1.setExploded()
                        slice1.setLabelColor(QColor('#EE4540'))
                        slice1.setLabelFont(QFont("SF UI Display", 8))
                        slice1.setLabelVisible()

                        slice2 = QtCharts.QPieSlice()
                        slice2 = seriesDonutInternetTVLastBill.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
                        slice2.setBrush(QColor('#6c6e71'))
                        slice2.setLabelColor(QColor('#6c6e71'))
                        slice2.setLabelFont(QFont("SF UI Display", 8))
                        slice2.setLabelVisible()
                                    
                        # Create Chart and set General Chart setting
                        chartDonutInternetTVLastBill = QtCharts.QChart()
                        chartDonutInternetTVLastBill.addSeries(seriesDonutInternetTVLastBill)
                        chartDonutInternetTVLastBill.legend().setAlignment(QtCore.Qt.AlignBottom)
                        chartDonutInternetTVLastBill.legend().setFont(QtGui.QFont("SF UI Display", 10))
                        chartDonutInternetTVLastBill.legend().setColor(QtGui.QColor('#EE4540'))
                 
                        chartDonutInternetTVLastBill.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
                        chartDonutInternetTVLastBill.setBackgroundBrush(QBrush(QColor("transparent")))
               
                        self.chartviewInternetTVLastBill.setChart(chartDonutInternetTVLastBill)
                        self.chartviewInternetTVLastBill.setRenderHint(QPainter.Antialiasing)
                        connection.commit()
                        connection.close()

                    except:
                        self.generateMessageBox(window_title='InternetTV page', msg_text='Please add internet tv bills in order to view data!')
                    self.modelInternetTV = QtWidgets.QFileSystemModel()
                    self.modelInternetTV.setRootPath(internet_tv_path)
                    self.ui.treeInternetTVDirectory.setModel(self.modelInternetTV)
                    self.ui.treeInternetTVDirectory.setRootIndex(self.modelInternetTV.index(internet_tv_path))
                    self.ui.treeInternetTVDirectory.setSortingEnabled(True)
                else:
                    self.generateMessageBox(window_title='InternetTV page', msg_text='Please add the earnings from the Account preferences!')
        else:
            self.generateMessageBox(window_title='InternetTV page', msg_text='Please select the desired InternetTV provider from the Account preferences!')

    # Tree view open menu
    def contextMenuInternetTV(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open")
        delete = menu.addAction("Delete")
        get_info = menu.addAction("Get info")
        menu.setStyleSheet("QMenu{height: 81px; width: 80px; background-color: #2a2e32;} QMenu::item {height: 25px; width: 80px; font-family: \"SF UI Display\"; font-size: 10pt; color: #f3f5f6;} QMenu::item:selected {height: 25px; width: 80px; background-color: #EE4540; color: #f3f5f6;}")
        open.triggered.connect(self.openFileInternetTV)
        delete.triggered.connect(self.deleteFileInternetTV)
        get_info.triggered.connect(self.getInfoInternetTV)
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def openFileInternetTV(self):
        index = self.ui.treeInternetTVDirectory.currentIndex()
        file_path = self.modelInternetTV.filePath(index)
        os.startfile(file_path)

    def deleteFileInternetTV(self):
        index = self.ui.treeInternetTVDirectory.currentIndex()
        path = self.modelInternetTV.filePath(index)
        try:
            self.bill_content_internet_tv = self.readBillContent(path)
            self.digi_id_bill_to_delete = re.findall(r"plată:\n\n.*/.(\d+)(?!.*\d)+\n", self.bill_content_internet_tv)[0]
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("DELETE FROM digi_bills WHERE id_bill = ?",(self.digi_id_bill_to_delete,))

            connection.commit()
            connection.close()
            os.remove(path)
        except:
            directory_to_delete = os.path.basename(os.path.normpath(path))
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("DELETE FROM digi_bills WHERE bill_year = ?",(directory_to_delete,))

            connection.commit()
            connection.close()
            shutil.rmtree(path)

    def getInfoInternetTV(self):
        index = self.ui.treeInternetTVDirectory.currentIndex()
        path = self.modelInternetTV.filePath(index)
        try:
            self.bill_content_internet_tv = self.readBillContent(path)
            self.digi_id_bill = re.findall(r"plată:\n\n.*/.(\d+)(?!.*\d)+\n", self.bill_content_internet_tv)[0]
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            db_connection.execute("SELECT id_bill, address, issue_date, due_date, total_pay FROM digi_bills WHERE id_bill = ?",(self.digi_id_bill,))
            bill_info = db_connection.fetchall()
            earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(self.username,))
            earnings = earnings_result.fetchone()[0]
            self.ui.lblInternetTVLastBillID.setText(bill_info[0][0])
            self.ui.lblInternetTVLastBillAddress.setText(bill_info[0][1])
            self.ui.lblInternetTVLastBillIssueDate.setText(datetime.datetime.strptime(f"{bill_info[0][2]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
            self.ui.lblInternetTVLastBillDueDate.setText(datetime.datetime.strptime(f"{bill_info[0][3]}", "%Y-%m-%d").strftime("%d.%m.%Y"))
            self.ui.lblInternetTVLastBillTotalPay.setText(bill_info[0][4])
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

            # Donut Internet TV chart
            seriesDonutInternetTVLastBill = QtCharts.QPieSeries()
            seriesDonutInternetTVLastBill.setHoleSize(0.35)
            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutInternetTVLastBill.append(f"Bill {bill_percentage}%", bill_percentage+25)
            slice1.setBrush(QColor('#EE4540'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#EE4540'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutInternetTVLastBill.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice2.setBrush(QColor('#6c6e71'))
            slice2.setLabelColor(QColor('#6c6e71'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutInternetTVLastBill = QtCharts.QChart()
            chartDonutInternetTVLastBill.addSeries(seriesDonutInternetTVLastBill)
            chartDonutInternetTVLastBill.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutInternetTVLastBill.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutInternetTVLastBill.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutInternetTVLastBill.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutInternetTVLastBill.setBackgroundBrush(QBrush(QColor("transparent")))
   
            self.chartviewInternetTVLastBill.setChart(chartDonutInternetTVLastBill)
            self.chartviewInternetTVLastBill.setRenderHint(QPainter.Antialiasing)

            connection.commit()
            connection.close()

        except:
            self.generateMessageBox(window_title='InternetTV bill', msg_text='Please select a bill from the list!')

    def addInternetTVBill(self):
        digi_file_full_path = QFileDialog.getOpenFileName(self, 'OpenFile')
        digi_file_path = digi_file_full_path[0]
        self.digi_bill_content = self.readBillContent(digi_file_path)
        # Get the year from the selected bill for DIGI and create a directory if it doesn't exist
        try:
            # Bill year for directory creation
            self.digi_bill_year = re.search(r"(\d+)(?!.*\d)\n\nProduse si", self.digi_bill_content)[0].split()[0]
            # Bill digi internet tv bill data
            self.digi_id_bill = re.findall(r"plată:\n\n.*/.(\d+)(?!.*\d)+\n", self.digi_bill_content)[0]
            self.digi_address = re.findall(r"([^\n\r]*\n[^\n\r]*\n[^\n\r]*)\nJudet", self.digi_bill_content)[0]
            self.digi_client = re.findall(r"Cod client:\n.*\n.*\n.*\n\s([^\n\r]*)", self.digi_bill_content)[0]
            self.digi_client_code = re.findall(r"Cod client:\n.*\n.*\s([^\n\r]*)", self.digi_bill_content)[0][0]
            self.digi_total_pay = re.findall(r"Total de achitat:\n\n([^\n\r]*)", self.digi_bill_content)[0]
            digi_issue_date_raw = re.findall(r"plată:\n\n.*\n([0-9]{2}.[0-9]{2}.[0-9]{4})", self.digi_bill_content)[0]
            digi_due_date_raw = re.findall(r"([0-9]{2}.[0-9]{2}.[0-9]{4})\n\nProduse si", self.digi_bill_content)[0]
            self.digi_issue_date = datetime.datetime.strptime(f"{digi_issue_date_raw}", "%d.%m.%Y").strftime("%Y-%m-%d")
            self.digi_due_date = datetime.datetime.strptime(f"{digi_due_date_raw}", "%d.%m.%Y").strftime("%Y-%m-%d")
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            # Check if the bill is already added
            result = db_connection.execute("SELECT * FROM digi_bills WHERE id_bill = ? AND username = ?",(self.digi_id_bill, self.username))
            if(len(result.fetchall()) > 0):
                self.generateMessageBox(window_title='Add bill information', msg_text='The selected bill is already added!')
                connection.commit()
                connection.close()
            else:
                db_connection.execute("INSERT INTO digi_bills(username, email, bill_year, id_bill, address, client, client_code,\
                    total_pay, issue_date, due_date ) VALUES (?,?,?,?,?,?,?,?,?,?)",(self.username, self.email, self.digi_bill_year, self.digi_id_bill,\
                    self.digi_address, self.digi_client, self.digi_client_code, self.digi_total_pay, self.digi_issue_date, self.digi_due_date))

                connection.commit()
                connection.close()
                pathlib.Path(str(pathlib.Path().absolute())+f'/Bills/{self.username}/InternetTV/{self.digi_bill_year}').mkdir(parents=True, exist_ok=True)
                digi_new_file_path = str(pathlib.Path().absolute())+f'/Bills/{self.username}/InternetTV/{self.digi_bill_year}'
                shutil.copy2(digi_file_path, digi_new_file_path, follow_symlinks=True)
                digi_issue_date_correct = datetime.datetime.strptime(f"{self.digi_issue_date}", "%Y-%m-%d").strftime("%d.%m.%Y")
                digi_due_date_correct = datetime.datetime.strptime(f"{self.digi_due_date}", "%Y-%m-%d").strftime("%d.%m.%Y")
                self.ui.lblInternetTVLastBillID.setText(self.digi_id_bill)
                self.ui.lblInternetTVLastBillAddress.setText(self.digi_address)
                self.ui.lblInternetTVLastBillIssueDate.setText(digi_issue_date_correct)
                self.ui.lblInternetTVLastBillDueDate.setText(digi_due_date_correct)
                self.ui.lblInternetTVLastBillTotalPay.setText(self.digi_total_pay)
        except:
            self.generateMessageBox(window_title='InternetTV bill', msg_text='Added internet tv bill is not a(n) DIGI bill!')

    def testInternetSpeed(self):
        print("aa")
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        print(s)
        res = s.results.dict()
        self.ui.lblTestInternetPingData.setText('{} ms'.format(res["ping"]))
        self.ui.lblTestInternetDownloadData.setText('{:.2f} Mb/s'.format(res["download"] / 1024/1024))
        self.ui.lblTestInternetUploadData.setText('{:.2f} Mb/s'.format(res["upload"] / 1024/1024))

    def internetTVInformation(self):
        self.generateMessageBox(window_title='InternetTV page', msg_text='Add internetTV bill in order to be able to open, delete or get information from the bill!\nOpen, delete or get information by right-clicking on an added bill!')

    # Click on the Subscriptions button
    def subscriptionsButton(self):
        # Select the page in focus
        MainWindow.clickLeftMenuButton(self, self.ui.pageSubscriptions, self.ui.btnSubscriptions, [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV])
        # Setting up db connection
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Checking the netflix data
        result = db_connection.execute("SELECT * FROM netflix_data WHERE username = ?",(self.username,))
        netflix_result = result.fetchall()
        if(len(netflix_result) > 0):            
            self.ui.comboBoxNetflixDay.setCurrentText(str(netflix_result[0][3]))
            self.ui.comboBoxNetflixMonth.setCurrentText(str(netflix_result[0][4]))
            self.ui.comboBoxNetflixYear.setCurrentText(str(netflix_result[0][5]))
            self.ui.comboBoxNetflixCurrency.setCurrentText(str(netflix_result[0][6]))
            self.ui.txtNetflixPayment.setText(netflix_result[0][7])
            self.ui.txtNetflixTotalPayment.setText("{:.2f} {}".format(float(netflix_result[0][8]), str(netflix_result[0][6])))
            payment = self.ui.txtNetflixPayment.text()
            # Updating the value if the month changes
            if ',' in payment:
                payment_real = payment.replace(',','.')
                start_date = datetime.datetime(int(self.ui.comboBoxNetflixYear.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()), int(self.ui.comboBoxNetflixDay.currentText()))
                end_date = datetime.datetime.now()
                num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                total_pay = float(payment_real) * num_months
                correct_total_pay = "{:.2f}".format(total_pay)
                self.ui.txtNetflixTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxNetflixCurrency.currentText()))
                db_connection.execute("UPDATE netflix_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                WHERE username = ?",(int(self.ui.comboBoxNetflixDay.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()),\
                                 int(self.ui.comboBoxNetflixYear.currentText()), self.ui.comboBoxNetflixCurrency.currentText()\
                                 , self.ui.txtNetflixPayment.text(), correct_total_pay, self.username))
                connection.commit()
                connection.close()
            else:
                start_date = datetime.datetime(int(self.ui.comboBoxNetflixYear.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()), int(self.ui.comboBoxNetflixDay.currentText()))
                end_date = datetime.datetime.now()
                num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                total_pay = float(payment) * num_months
                correct_total_pay = "{:.2f}".format(total_pay)
                self.ui.txtNetflixTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxNetflixCurrency.currentText()))
                db_connection.execute("UPDATE netflix_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                WHERE username = ?",(int(self.ui.comboBoxNetflixDay.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()),\
                                 int(self.ui.comboBoxNetflixYear.currentText()), self.ui.comboBoxNetflixCurrency.currentText()\
                                 , self.ui.txtNetflixPayment.text(), correct_total_pay, self.username))
                connection.commit()
                connection.close()

            self.ui.comboBoxNetflixDay.setCurrentText(str(netflix_result[0][3]))
            self.ui.comboBoxNetflixMonth.setCurrentText(str(netflix_result[0][4]))
            self.ui.comboBoxNetflixYear.setCurrentText(str(netflix_result[0][5]))
            self.ui.comboBoxNetflixCurrency.setCurrentText(str(netflix_result[0][6]))
            self.ui.txtNetflixPayment.setText(netflix_result[0][7])
            self.ui.txtNetflixTotalPayment.setText("{:.2f} {}".format(float(netflix_result[0][8]), str(netflix_result[0][6])))

        # Setting up db connection
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Checking the spotify data
        result = db_connection.execute("SELECT * FROM spotify_data WHERE username = ?",(self.username,))
        spotify_result = result.fetchall()
        if(len(spotify_result) > 0):            
            self.ui.comboBoxSpotifyDay.setCurrentText(str(spotify_result[0][3]))
            self.ui.comboBoxSpotifyMonth.setCurrentText(str(spotify_result[0][4]))
            self.ui.comboBoxSpotifyYear.setCurrentText(str(spotify_result[0][5]))
            self.ui.comboBoxSpotifyCurrency.setCurrentText(str(spotify_result[0][6]))
            self.ui.txtSpotifyPayment.setText(spotify_result[0][7])
            self.ui.txtSpotifyTotalPayment.setText("{:.2f} {}".format(float(spotify_result[0][8]), str(spotify_result[0][6])))
            payment = self.ui.txtSpotifyPayment.text()
            # Updating the value if the month changes
            if ',' in payment:
                payment_real = payment.replace(',','.')
                start_date = datetime.datetime(int(self.ui.comboBoxSpotifyYear.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()), int(self.ui.comboBoxSpotifyDay.currentText()))
                end_date = datetime.datetime.now()
                num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                total_pay = float(payment_real) * num_months
                correct_total_pay = "{:.2f}".format(total_pay)
                self.ui.txtSpotifyTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxSpotifyCurrency.currentText()))
                db_connection.execute("UPDATE spotify_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                WHERE username = ?",(int(self.ui.comboBoxSpotifyDay.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()),\
                                 int(self.ui.comboBoxSpotifyYear.currentText()), self.ui.comboBoxSpotifyCurrency.currentText()\
                                 , self.ui.txtSpotifyPayment.text(), correct_total_pay, self.username))
                connection.commit()
                connection.close()
            else:
                start_date = datetime.datetime(int(self.ui.comboBoxSpotifyYear.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()), int(self.ui.comboBoxSpotifyDay.currentText()))
                end_date = datetime.datetime.now()
                num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                total_pay = float(payment) * num_months
                correct_total_pay = "{:.2f}".format(total_pay)
                self.ui.txtSpotifyTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxSpotifyCurrency.currentText()))
                db_connection.execute("UPDATE spotify_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                WHERE username = ?",(int(self.ui.comboBoxSpotifyDay.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()),\
                                 int(self.ui.comboBoxSpotifyYear.currentText()), self.ui.comboBoxSpotifyCurrency.currentText()\
                                 , self.ui.txtSpotifyPayment.text(), correct_total_pay, self.username))
                connection.commit()
                connection.close()

            self.ui.comboBoxSpotifyDay.setCurrentText(str(spotify_result[0][3]))
            self.ui.comboBoxSpotifyMonth.setCurrentText(str(spotify_result[0][4]))
            self.ui.comboBoxSpotifyYear.setCurrentText(str(spotify_result[0][5]))
            self.ui.comboBoxSpotifyCurrency.setCurrentText(str(spotify_result[0][6]))
            self.ui.txtSpotifyPayment.setText(spotify_result[0][7])
            self.ui.txtSpotifyTotalPayment.setText("{:.2f} {}".format(float(spotify_result[0][8]), str(spotify_result[0][6])))

        # Setting up db connection
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Checking the telecom data
        result = db_connection.execute("SELECT * FROM telecom_data WHERE username = ?",(self.username,))
        telecom_result = result.fetchall()
        if(len(telecom_result) > 0):            
            self.ui.comboBoxTelecomDay.setCurrentText(str(telecom_result[0][3]))
            self.ui.comboBoxTelecomMonth.setCurrentText(str(telecom_result[0][4]))
            self.ui.comboBoxTelecomYear.setCurrentText(str(telecom_result[0][5]))
            self.ui.comboBoxTelecomCurrency.setCurrentText(str(telecom_result[0][6]))
            self.ui.txtTelecomPayment.setText(telecom_result[0][7])
            self.ui.txtTelecomTotalPayment.setText("{:.2f} {}".format(float(telecom_result[0][8]), str(telecom_result[0][6])))
            payment = self.ui.txtTelecomPayment.text()
            # Updating the value if the month changes
            if ',' in payment:
                payment_real = payment.replace(',','.')
                start_date = datetime.datetime(int(self.ui.comboBoxTelecomYear.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()), int(self.ui.comboBoxTelecomDay.currentText()))
                end_date = datetime.datetime.now()
                num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                total_pay = float(payment_real) * num_months
                correct_total_pay = "{:.2f}".format(total_pay)
                self.ui.txtTelecomTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxTelecomCurrency.currentText()))
                db_connection.execute("UPDATE telecom_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                WHERE username = ?",(int(self.ui.comboBoxTelecomDay.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()),\
                                 int(self.ui.comboBoxTelecomYear.currentText()), self.ui.comboBoxTelecomCurrency.currentText()\
                                 , self.ui.txtTelecomPayment.text(), correct_total_pay, self.username))
                connection.commit()
                connection.close()
            else:
                start_date = datetime.datetime(int(self.ui.comboBoxTelecomYear.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()), int(self.ui.comboBoxTelecomDay.currentText()))
                end_date = datetime.datetime.now()
                num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                total_pay = float(payment) * num_months
                correct_total_pay = "{:.2f}".format(total_pay)
                self.ui.txtTelecomTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxTelecomCurrency.currentText()))
                db_connection.execute("UPDATE telecom_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                WHERE username = ?",(int(self.ui.comboBoxTelecomDay.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()),\
                                 int(self.ui.comboBoxTelecomYear.currentText()), self.ui.comboBoxTelecomCurrency.currentText()\
                                 , self.ui.txtTelecomPayment.text(), correct_total_pay, self.username))
                connection.commit()
                connection.close()

            self.ui.comboBoxTelecomDay.setCurrentText(str(telecom_result[0][3]))
            self.ui.comboBoxTelecomMonth.setCurrentText(str(telecom_result[0][4]))
            self.ui.comboBoxTelecomYear.setCurrentText(str(telecom_result[0][5]))
            self.ui.comboBoxTelecomCurrency.setCurrentText(str(telecom_result[0][6]))
            self.ui.txtTelecomPayment.setText(telecom_result[0][7])
            self.ui.txtTelecomTotalPayment.setText("{:.2f} {}".format(float(telecom_result[0][8]), str(telecom_result[0][6])))

        # Plot the donut chart for the subscriptions page
        try:
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()   
            earnings_result = db_connection.execute("SELECT earnings FROM accounts WHERE username = ?",(self.username,))
            earnings = earnings_result.fetchone()[0]
            earnings_strip = earnings.strip()
            earnings_float = float(earnings_strip)
            connection.commit()
            connection.close()
        except:
            self.generateMessageBox(window_title='Subscription information', msg_text='Please add the earnings from the Account preferences!')
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()        
        netflix_pay_db = db_connection.execute("SELECT pay FROM netflix_data WHERE username = ?",(self.username,))
        netflix_pay_raw = netflix_pay_db.fetchone()
        spotify_pay_db = db_connection.execute("SELECT pay FROM spotify_data WHERE username = ?",(self.username,))
        spotify_pay_raw = spotify_pay_db.fetchone()
        telecom_pay_db = db_connection.execute("SELECT pay FROM telecom_data WHERE username = ?",(self.username,))
        telecom_pay_raw = telecom_pay_db.fetchone()

        spotify_ron_value = None
        netflix_ron_value = None
        telecom_ron_value = None

        if (spotify_pay_raw != None):
            spotify_pay = spotify_pay_raw[0]
            if ',' in spotify_pay:
                spotify_pay_string = spotify_pay.replace(',','.')
            else:
                spotify_pay_string = spotify_pay
            spotify_pay_float = float(spotify_pay_string)
            # Check for currency and convert to RON if needed
            spotify_currency = db_connection.execute("SELECT currency FROM spotify_data WHERE username = ?",(self.username,))
            spotify_currency_value = spotify_currency.fetchone()[0]
            if (spotify_currency_value == 'EUR'):
                today = datetime.datetime.now()
                c = CurrencyConverter(fallback_on_wrong_date=True)
                spotify_ron_value_all = c.convert(spotify_pay_float, 'EUR', 'RON', date=date(today.year, today.month, today.day))
                spotify_ron_value_string = "{:.2f}".format(spotify_ron_value_all)
                spotify_ron_value = float(spotify_ron_value_string)
            else:
                spotify_ron_value = spotify_pay_float

        if (netflix_pay_raw != None):
            netflix_pay = netflix_pay_raw[0]
            if ',' in netflix_pay:
                netflix_pay_string = netflix_pay.replace(',','.')
            else:
                netflix_pay_string = netflix_pay
            netflix_pay_float = float(netflix_pay_string)
            # Check for currency and convert to RON if needed
            netflix_currency = db_connection.execute("SELECT currency FROM netflix_data WHERE username = ?",(self.username,))
            netflix_currency_value = netflix_currency.fetchone()[0]
            if (netflix_currency_value == 'EUR'):
                today = datetime.datetime.now()
                c = CurrencyConverter(fallback_on_wrong_date=True)
                netflix_ron_value_all = c.convert(netflix_pay_float, 'EUR', 'RON', date=date(today.year, today.month, today.day))
                netflix_ron_value_string = "{:.2f}".format(netflix_ron_value_all)
                netflix_ron_value = float(netflix_ron_value_string)
            else:
                netflix_ron_value = netflix_pay_float

        if (telecom_pay_raw != None):
            telecom_pay = telecom_pay_raw[0]
            if ',' in telecom_pay:
                telecom_pay_string = telecom_pay.replace(',','.')
            else:
                telecom_pay_string = telecom_pay
            telecom_pay_float = float(telecom_pay_string)
            # Check for currency and convert to RON if needed
            telecom_currency = db_connection.execute("SELECT currency FROM telecom_data WHERE username = ?",(self.username,))
            telecom_currency_value = telecom_currency.fetchone()[0]
            if (telecom_currency_value == 'EUR'):
                today = datetime.datetime.now()
                c = CurrencyConverter(fallback_on_wrong_date=True)
                telecom_ron_value_all = c.convert(telecom_pay_float, 'EUR', 'RON', date=date(today.year, today.month, today.day))
                telecom_ron_value_string = "{:.2f}".format(telecom_ron_value_all)
                telecom_ron_value = float(telecom_ron_value_string)
            else:
                telecom_ron_value = telecom_pay_float

        # Generate donut chart considering all cases of active data for each subscription
        if (spotify_ron_value != None and netflix_ron_value != None and telecom_ron_value != None):

            spotify_percentage = round((spotify_ron_value/earnings_float)*100, 2)
            netflix_percentage = round((netflix_ron_value/earnings_float)*100, 2)
            telecom_percentage = round((telecom_ron_value/earnings_float)*100, 2)

            remaining_earnings_percentage = round(100 - spotify_percentage - netflix_percentage - telecom_percentage, 2)

            # Donut Subscriptions chart
            seriesDonutSubscriptionsAll = QtCharts.QPieSeries()
            seriesDonutSubscriptionsAll.setHoleSize(0.35)
            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutSubscriptionsAll.append(f"Netflix {netflix_percentage}%", netflix_percentage + 20)
            slice1.setBrush(QColor('#E50914'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#E50914'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutSubscriptionsAll.append(f"Spotify {spotify_percentage}%", spotify_percentage + 20)
            slice2.setBrush(QColor('#1DB954'))
            slice2.setExploded()
            slice2.setLabelColor(QColor('#1DB954'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()

            slice3 = QtCharts.QPieSlice()
            slice3 = seriesDonutSubscriptionsAll.append(f"Telecom {telecom_percentage}%", telecom_percentage + 20)
            slice3.setBrush(QColor('#3c73a8'))
            slice3.setExploded()
            slice3.setLabelColor(QColor('#3c73a8'))
            slice3.setLabelFont(QFont("SF UI Display", 8))
            slice3.setLabelVisible()

            slice4 = QtCharts.QPieSlice()
            slice4 = seriesDonutSubscriptionsAll.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice4.setBrush(QColor('#6c6e71'))
            slice4.setLabelColor(QColor('#6c6e71'))
            slice4.setLabelFont(QFont("SF UI Display", 8))
            slice4.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutSubscriptionsAll = QtCharts.QChart()
            chartDonutSubscriptionsAll.addSeries(seriesDonutSubscriptionsAll)
            chartDonutSubscriptionsAll.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutSubscriptionsAll.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutSubscriptionsAll.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutSubscriptionsAll.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutSubscriptionsAll.setBackgroundBrush(QBrush(QColor("transparent")))

            self.chartviewSubscriptionsAll.setChart(chartDonutSubscriptionsAll)
            self.chartviewSubscriptionsAll.setRenderHint(QPainter.Antialiasing)

            set0 = QtCharts.QBarSet('Netflix')
            set1 = QtCharts.QBarSet('Spotify')
            set2 = QtCharts.QBarSet('Telecom')

            set0.append(netflix_ron_value)
            set0.setBrush(QColor('#E50914'))
            set1.append(spotify_ron_value)
            set1.setBrush(QColor('#1DB954'))
            set2.append(telecom_ron_value)
            set2.setBrush(QColor('#3c73a8'))

            seriesSubscriptionsComparison = QtCharts.QBarSeries()
            seriesSubscriptionsComparison.append(set0)
            seriesSubscriptionsComparison.append(set1)
            seriesSubscriptionsComparison.append(set2)

            chartSubscriptionsComparison = QtCharts.QChart()
            chartSubscriptionsComparison.addSeries(seriesSubscriptionsComparison)
            chartSubscriptionsComparison.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            axisX = QtCharts.QBarCategoryAxis()
            axis_x_brush = QBrush(QColor("#EE4540"))
            axisX.setLabelsBrush(axis_x_brush)
            axisX.setTitleBrush(axis_x_brush)
            axisX.setTitleText("Subscriptions")

            axisY = QtCharts.QValueAxis()
            axisY.setLabelFormat("%i")
            axisY.setTitleText("Subscription cost [RON]")
            axisY.setMax(100)
            axisY.setMin(0)
            axisY.setTickCount(5)
            axis_y_brush = QBrush(QColor("#EE4540"))
            axisY.setLabelsBrush(axis_y_brush)            
            axisY.setTitleBrush(axis_y_brush)

            chartSubscriptionsComparison.addAxis(axisX, Qt.AlignBottom)
            chartSubscriptionsComparison.addAxis(axisY, Qt.AlignLeft)

            seriesSubscriptionsComparison.attachAxis(axisY)            

            chartSubscriptionsComparison.setBackgroundBrush(QBrush(QColor("transparent")))
            chartSubscriptionsComparison.setTitleBrush(QBrush(Qt.white));

            chartSubscriptionsComparison.legend().setVisible(True)
            chartSubscriptionsComparison.legend().setBrush(QBrush(Qt.white))
            chartSubscriptionsComparison.legend().setAlignment(Qt.AlignBottom)

            self.chartviewSubscriptionsComparison.setChart(chartSubscriptionsComparison)
            self.chartviewSubscriptionsComparison.setRenderHint(QPainter.Antialiasing)


        elif (spotify_ron_value != None and netflix_ron_value == None and telecom_ron_value != None):

            spotify_percentage = round((spotify_ron_value/earnings_float)*100, 2)
            telecom_percentage = round((telecom_ron_value/earnings_float)*100, 2)

            remaining_earnings_percentage = round(100 - spotify_percentage - telecom_percentage, 2)

            # Donut Subscriptions chart
            seriesDonutSubscriptionsAll = QtCharts.QPieSeries()
            seriesDonutSubscriptionsAll.setHoleSize(0.35)

            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutSubscriptionsAll.append(f"Spotify {spotify_percentage}%", spotify_percentage + 20)
            slice1.setBrush(QColor('#1DB954'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#1DB954'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutSubscriptionsAll.append(f"Telecom {telecom_percentage}%", telecom_percentage + 20)
            slice2.setBrush(QColor('#3c73a8'))
            slice2.setExploded()
            slice2.setLabelColor(QColor('#3c73a8'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()

            slice3 = QtCharts.QPieSlice()
            slice3 = seriesDonutSubscriptionsAll.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice3.setBrush(QColor('#6c6e71'))
            slice3.setLabelColor(QColor('#6c6e71'))
            slice3.setLabelFont(QFont("SF UI Display", 8))
            slice3.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutSubscriptionsAll = QtCharts.QChart()
            chartDonutSubscriptionsAll.addSeries(seriesDonutSubscriptionsAll)
            chartDonutSubscriptionsAll.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutSubscriptionsAll.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutSubscriptionsAll.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutSubscriptionsAll.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutSubscriptionsAll.setBackgroundBrush(QBrush(QColor("transparent")))

            self.chartviewSubscriptionsAll.setChart(chartDonutSubscriptionsAll)
            self.chartviewSubscriptionsAll.setRenderHint(QPainter.Antialiasing)

            set0 = QtCharts.QBarSet('Spotify')
            set1 = QtCharts.QBarSet('Telecom')

            set0.append(spotify_ron_value)
            set0.setBrush(QColor('#1DB954'))
            set1.append(telecom_ron_value)
            set1.setBrush(QColor('#3c73a8'))

            seriesSubscriptionsComparison = QtCharts.QBarSeries()
            seriesSubscriptionsComparison.append(set0)
            seriesSubscriptionsComparison.append(set1)

            chartSubscriptionsComparison = QtCharts.QChart()
            chartSubscriptionsComparison.addSeries(seriesSubscriptionsComparison)
            chartSubscriptionsComparison.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            axisX = QtCharts.QBarCategoryAxis()
            axis_x_brush = QBrush(QColor("#EE4540"))
            axisX.setLabelsBrush(axis_x_brush)
            axisX.setTitleBrush(axis_x_brush)
            axisX.setTitleText("Subscriptions")

            axisY = QtCharts.QValueAxis()
            axisY.setLabelFormat("%i")
            axisY.setTitleText("Subscription cost [RON]")
            axisY.setMax(100)
            axisY.setMin(0)
            axisY.setTickCount(5)
            axis_y_brush = QBrush(QColor("#EE4540"))
            axisY.setLabelsBrush(axis_y_brush)            
            axisY.setTitleBrush(axis_y_brush)

            chartSubscriptionsComparison.addAxis(axisX, Qt.AlignBottom)
            chartSubscriptionsComparison.addAxis(axisY, Qt.AlignLeft)

            seriesSubscriptionsComparison.attachAxis(axisY)            

            chartSubscriptionsComparison.setBackgroundBrush(QBrush(QColor("transparent")))
            chartSubscriptionsComparison.setTitleBrush(QBrush(Qt.white));

            chartSubscriptionsComparison.legend().setVisible(True)
            chartSubscriptionsComparison.legend().setBrush(QBrush(Qt.white))
            chartSubscriptionsComparison.legend().setAlignment(Qt.AlignBottom)

            self.chartviewSubscriptionsComparison.setChart(chartSubscriptionsComparison)
            self.chartviewSubscriptionsComparison.setRenderHint(QPainter.Antialiasing)

        elif (spotify_ron_value == None and netflix_ron_value == None and telecom_ron_value != None):

            telecom_percentage = round((telecom_ron_value/earnings_float)*100, 2)

            remaining_earnings_percentage = round(100 - telecom_percentage, 2)

            # Donut Subscriptions chart
            seriesDonutSubscriptionsAll = QtCharts.QPieSeries()
            seriesDonutSubscriptionsAll.setHoleSize(0.35)

            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutSubscriptionsAll.append(f"Telecom {telecom_percentage}%", telecom_percentage + 20)
            slice1.setBrush(QColor('#3c73a8'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#3c73a8'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutSubscriptionsAll.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice2.setBrush(QColor('#6c6e71'))
            slice2.setLabelColor(QColor('#6c6e71'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutSubscriptionsAll = QtCharts.QChart()
            chartDonutSubscriptionsAll.addSeries(seriesDonutSubscriptionsAll)
            chartDonutSubscriptionsAll.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutSubscriptionsAll.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutSubscriptionsAll.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutSubscriptionsAll.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutSubscriptionsAll.setBackgroundBrush(QBrush(QColor("transparent")))

            self.chartviewSubscriptionsAll.setChart(chartDonutSubscriptionsAll)
            self.chartviewSubscriptionsAll.setRenderHint(QPainter.Antialiasing)

            set0 = QtCharts.QBarSet('Telecom')

            set0.append(telecom_ron_value)
            set0.setBrush(QColor('#3c73a8'))

            seriesSubscriptionsComparison = QtCharts.QBarSeries()
            seriesSubscriptionsComparison.append(set0)

            chartSubscriptionsComparison = QtCharts.QChart()
            chartSubscriptionsComparison.addSeries(seriesSubscriptionsComparison)
            chartSubscriptionsComparison.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            axisX = QtCharts.QBarCategoryAxis()
            axis_x_brush = QBrush(QColor("#EE4540"))
            axisX.setLabelsBrush(axis_x_brush)
            axisX.setTitleBrush(axis_x_brush)
            axisX.setTitleText("Subscriptions")

            axisY = QtCharts.QValueAxis()
            axisY.setLabelFormat("%i")
            axisY.setTitleText("Subscription cost [RON]")
            axisY.setMax(100)
            axisY.setMin(0)
            axisY.setTickCount(5)
            axis_y_brush = QBrush(QColor("#EE4540"))
            axisY.setLabelsBrush(axis_y_brush)            
            axisY.setTitleBrush(axis_y_brush)

            chartSubscriptionsComparison.addAxis(axisX, Qt.AlignBottom)
            chartSubscriptionsComparison.addAxis(axisY, Qt.AlignLeft)

            seriesSubscriptionsComparison.attachAxis(axisY)            

            chartSubscriptionsComparison.setBackgroundBrush(QBrush(QColor("transparent")))
            chartSubscriptionsComparison.setTitleBrush(QBrush(Qt.white));

            chartSubscriptionsComparison.legend().setVisible(True)
            chartSubscriptionsComparison.legend().setBrush(QBrush(Qt.white))
            chartSubscriptionsComparison.legend().setAlignment(Qt.AlignBottom)

            self.chartviewSubscriptionsComparison.setChart(chartSubscriptionsComparison)
            self.chartviewSubscriptionsComparison.setRenderHint(QPainter.Antialiasing)

        elif (spotify_ron_value != None and netflix_ron_value != None and telecom_ron_value == None):

            spotify_percentage = round((spotify_ron_value/earnings_float)*100, 2)
            netflix_percentage = round((netflix_ron_value/earnings_float)*100, 2)

            remaining_earnings_percentage = round(100 - spotify_percentage - netflix_percentage, 2)

            # Donut Subscriptions chart
            seriesDonutSubscriptionsAll = QtCharts.QPieSeries()
            seriesDonutSubscriptionsAll.setHoleSize(0.35)
            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutSubscriptionsAll.append(f"Netflix {netflix_percentage}%", netflix_percentage + 20)
            slice1.setBrush(QColor('#E50914'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#E50914'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutSubscriptionsAll.append(f"Spotify {spotify_percentage}%", spotify_percentage + 20)
            slice2.setBrush(QColor('#1DB954'))
            slice2.setExploded()
            slice2.setLabelColor(QColor('#1DB954'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()

            slice3 = QtCharts.QPieSlice()
            slice3 = seriesDonutSubscriptionsAll.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice3.setBrush(QColor('#6c6e71'))
            slice3.setLabelColor(QColor('#6c6e71'))
            slice3.setLabelFont(QFont("SF UI Display", 8))
            slice3.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutSubscriptionsAll = QtCharts.QChart()
            chartDonutSubscriptionsAll.addSeries(seriesDonutSubscriptionsAll)
            chartDonutSubscriptionsAll.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutSubscriptionsAll.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutSubscriptionsAll.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutSubscriptionsAll.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutSubscriptionsAll.setBackgroundBrush(QBrush(QColor("transparent")))

            self.chartviewSubscriptionsAll.setChart(chartDonutSubscriptionsAll)
            self.chartviewSubscriptionsAll.setRenderHint(QPainter.Antialiasing)

            set0 = QtCharts.QBarSet('Netflix')
            set1 = QtCharts.QBarSet('Spotify')

            set0.append(netflix_ron_value)
            set0.setBrush(QColor('#E50914'))
            set1.append(spotify_ron_value)
            set1.setBrush(QColor('#1DB954'))

            seriesSubscriptionsComparison = QtCharts.QBarSeries()
            seriesSubscriptionsComparison.append(set0)
            seriesSubscriptionsComparison.append(set1)

            chartSubscriptionsComparison = QtCharts.QChart()
            chartSubscriptionsComparison.addSeries(seriesSubscriptionsComparison)
            chartSubscriptionsComparison.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            axisX = QtCharts.QBarCategoryAxis()
            axis_x_brush = QBrush(QColor("#EE4540"))
            axisX.setLabelsBrush(axis_x_brush)
            axisX.setTitleBrush(axis_x_brush)
            axisX.setTitleText("Subscriptions")

            axisY = QtCharts.QValueAxis()
            axisY.setLabelFormat("%i")
            axisY.setTitleText("Subscription cost [RON]")
            axisY.setMax(100)
            axisY.setMin(0)
            axisY.setTickCount(5)
            axis_y_brush = QBrush(QColor("#EE4540"))
            axisY.setLabelsBrush(axis_y_brush)            
            axisY.setTitleBrush(axis_y_brush)

            chartSubscriptionsComparison.addAxis(axisX, Qt.AlignBottom)
            chartSubscriptionsComparison.addAxis(axisY, Qt.AlignLeft)

            seriesSubscriptionsComparison.attachAxis(axisY)            

            chartSubscriptionsComparison.setBackgroundBrush(QBrush(QColor("transparent")))
            chartSubscriptionsComparison.setTitleBrush(QBrush(Qt.white));

            chartSubscriptionsComparison.legend().setVisible(True)
            chartSubscriptionsComparison.legend().setBrush(QBrush(Qt.white))
            chartSubscriptionsComparison.legend().setAlignment(Qt.AlignBottom)

            self.chartviewSubscriptionsComparison.setChart(chartSubscriptionsComparison)
            self.chartviewSubscriptionsComparison.setRenderHint(QPainter.Antialiasing)

        elif (spotify_ron_value == None and netflix_ron_value != None and telecom_ron_value == None):

            netflix_percentage = round((netflix_ron_value/earnings_float)*100, 2)

            remaining_earnings_percentage = round(100 - netflix_percentage, 2)

            # Donut Subscriptions chart
            seriesDonutSubscriptionsAll = QtCharts.QPieSeries()
            seriesDonutSubscriptionsAll.setHoleSize(0.35)
            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutSubscriptionsAll.append(f"Netflix {netflix_percentage}%", netflix_percentage + 20)
            slice1.setBrush(QColor('#E50914'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#E50914'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutSubscriptionsAll.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice2.setBrush(QColor('#6c6e71'))
            slice2.setLabelColor(QColor('#6c6e71'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutSubscriptionsAll = QtCharts.QChart()
            chartDonutSubscriptionsAll.addSeries(seriesDonutSubscriptionsAll)
            chartDonutSubscriptionsAll.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutSubscriptionsAll.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutSubscriptionsAll.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutSubscriptionsAll.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutSubscriptionsAll.setBackgroundBrush(QBrush(QColor("transparent")))

            self.chartviewSubscriptionsAll.setChart(chartDonutSubscriptionsAll)
            self.chartviewSubscriptionsAll.setRenderHint(QPainter.Antialiasing)

            set0 = QtCharts.QBarSet('Netflix')

            set0.append(netflix_ron_value)
            set0.setBrush(QColor('#E50914'))

            seriesSubscriptionsComparison = QtCharts.QBarSeries()
            seriesSubscriptionsComparison.append(set0)

            chartSubscriptionsComparison = QtCharts.QChart()
            chartSubscriptionsComparison.addSeries(seriesSubscriptionsComparison)
            chartSubscriptionsComparison.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            axisX = QtCharts.QBarCategoryAxis()
            axis_x_brush = QBrush(QColor("#EE4540"))
            axisX.setLabelsBrush(axis_x_brush)
            axisX.setTitleBrush(axis_x_brush)
            axisX.setTitleText("Subscriptions")

            axisY = QtCharts.QValueAxis()
            axisY.setLabelFormat("%i")
            axisY.setTitleText("Subscription cost [RON]")
            axisY.setMax(100)
            axisY.setMin(0)
            axisY.setTickCount(5)
            axis_y_brush = QBrush(QColor("#EE4540"))
            axisY.setLabelsBrush(axis_y_brush)            
            axisY.setTitleBrush(axis_y_brush)

            chartSubscriptionsComparison.addAxis(axisX, Qt.AlignBottom)
            chartSubscriptionsComparison.addAxis(axisY, Qt.AlignLeft)

            seriesSubscriptionsComparison.attachAxis(axisY)            

            chartSubscriptionsComparison.setBackgroundBrush(QBrush(QColor("transparent")))
            chartSubscriptionsComparison.setTitleBrush(QBrush(Qt.white));

            chartSubscriptionsComparison.legend().setVisible(True)
            chartSubscriptionsComparison.legend().setBrush(QBrush(Qt.white))
            chartSubscriptionsComparison.legend().setAlignment(Qt.AlignBottom)

            self.chartviewSubscriptionsComparison.setChart(chartSubscriptionsComparison)
            self.chartviewSubscriptionsComparison.setRenderHint(QPainter.Antialiasing)

        elif (spotify_ron_value == None and netflix_ron_value != None and telecom_ron_value != None):

            netflix_percentage = round((netflix_ron_value/earnings_float)*100, 2)
            telecom_percentage = round((telecom_ron_value/earnings_float)*100, 2)

            remaining_earnings_percentage = round(100 - netflix_percentage - telecom_percentage, 2)

            # Donut Subscriptions chart
            seriesDonutSubscriptionsAll = QtCharts.QPieSeries()
            seriesDonutSubscriptionsAll.setHoleSize(0.35)
            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutSubscriptionsAll.append(f"Netflix {netflix_percentage}%", netflix_percentage + 20)
            slice1.setBrush(QColor('#E50914'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#E50914'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutSubscriptionsAll.append(f"Telecom {telecom_percentage}%", telecom_percentage + 20)
            slice2.setBrush(QColor('#3c73a8'))
            slice2.setExploded()
            slice2.setLabelColor(QColor('#3c73a8'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()

            slice3 = QtCharts.QPieSlice()
            slice3 = seriesDonutSubscriptionsAll.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice3.setBrush(QColor('#6c6e71'))
            slice3.setLabelColor(QColor('#6c6e71'))
            slice3.setLabelFont(QFont("SF UI Display", 8))
            slice3.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutSubscriptionsAll = QtCharts.QChart()
            chartDonutSubscriptionsAll.addSeries(seriesDonutSubscriptionsAll)
            chartDonutSubscriptionsAll.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutSubscriptionsAll.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutSubscriptionsAll.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutSubscriptionsAll.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutSubscriptionsAll.setBackgroundBrush(QBrush(QColor("transparent")))

            self.chartviewSubscriptionsAll.setChart(chartDonutSubscriptionsAll)
            self.chartviewSubscriptionsAll.setRenderHint(QPainter.Antialiasing)

            set0 = QtCharts.QBarSet('Netflix')
            set1 = QtCharts.QBarSet('Telecom')

            set0.append(netflix_ron_value)
            set0.setBrush(QColor('#E50914'))
            set1.append(telecom_ron_value)
            set1.setBrush(QColor('#3c73a8'))

            seriesSubscriptionsComparison = QtCharts.QBarSeries()
            seriesSubscriptionsComparison.append(set0)
            seriesSubscriptionsComparison.append(set1)

            chartSubscriptionsComparison = QtCharts.QChart()
            chartSubscriptionsComparison.addSeries(seriesSubscriptionsComparison)
            chartSubscriptionsComparison.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            axisX = QtCharts.QBarCategoryAxis()
            axis_x_brush = QBrush(QColor("#EE4540"))
            axisX.setLabelsBrush(axis_x_brush)
            axisX.setTitleBrush(axis_x_brush)
            axisX.setTitleText("Subscriptions")

            axisY = QtCharts.QValueAxis()
            axisY.setLabelFormat("%i")
            axisY.setTitleText("Subscription cost [RON]")
            axisY.setMax(100)
            axisY.setMin(0)
            axisY.setTickCount(5)
            axis_y_brush = QBrush(QColor("#EE4540"))
            axisY.setLabelsBrush(axis_y_brush)            
            axisY.setTitleBrush(axis_y_brush)

            chartSubscriptionsComparison.addAxis(axisX, Qt.AlignBottom)
            chartSubscriptionsComparison.addAxis(axisY, Qt.AlignLeft)

            seriesSubscriptionsComparison.attachAxis(axisY)            

            chartSubscriptionsComparison.setBackgroundBrush(QBrush(QColor("transparent")))
            chartSubscriptionsComparison.setTitleBrush(QBrush(Qt.white));

            chartSubscriptionsComparison.legend().setVisible(True)
            chartSubscriptionsComparison.legend().setBrush(QBrush(Qt.white))
            chartSubscriptionsComparison.legend().setAlignment(Qt.AlignBottom)

            self.chartviewSubscriptionsComparison.setChart(chartSubscriptionsComparison)
            self.chartviewSubscriptionsComparison.setRenderHint(QPainter.Antialiasing)

        elif (spotify_ron_value != None and netflix_ron_value == None and telecom_ron_value == None):

            spotify_percentage = round((spotify_ron_value/earnings_float)*100, 2)

            remaining_earnings_percentage = round(100 - spotify_percentage, 2)

            # Donut Subscriptions chart
            slice1 = QtCharts.QPieSlice()
            slice1 = seriesDonutSubscriptionsAll.append(f"Spotify {spotify_percentage}%", spotify_percentage + 20)
            slice1.setBrush(QColor('#1DB954'))
            slice1.setExploded()
            slice1.setLabelColor(QColor('#1DB954'))
            slice1.setLabelFont(QFont("SF UI Display", 8))
            slice1.setLabelVisible()

            slice2 = QtCharts.QPieSlice()
            slice2 = seriesDonutSubscriptionsAll.append(f"Earnings {remaining_earnings_percentage}%", remaining_earnings_percentage)
            slice2.setBrush(QColor('#6c6e71'))
            slice2.setLabelColor(QColor('#6c6e71'))
            slice2.setLabelFont(QFont("SF UI Display", 8))
            slice2.setLabelVisible()
                        
            # Create Chart and set General Chart setting
            chartDonutSubscriptionsAll = QtCharts.QChart()
            chartDonutSubscriptionsAll.addSeries(seriesDonutSubscriptionsAll)
            chartDonutSubscriptionsAll.legend().setAlignment(QtCore.Qt.AlignBottom)
            chartDonutSubscriptionsAll.legend().setFont(QtGui.QFont("SF UI Display", 10))
            chartDonutSubscriptionsAll.legend().setColor(QtGui.QColor('#EE4540'))
     
            chartDonutSubscriptionsAll.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            chartDonutSubscriptionsAll.setBackgroundBrush(QBrush(QColor("transparent")))

            self.chartviewSubscriptionsAll.setChart(chartDonutSubscriptionsAll)
            self.chartviewSubscriptionsAll.setRenderHint(QPainter.Antialiasing)

            set0 = QtCharts.QBarSet('Spotify')

            set0.append(spotify_ron_value)
            set0.setBrush(QColor('#1DB954'))

            seriesSubscriptionsComparison = QtCharts.QBarSeries()
            seriesSubscriptionsComparison.append(set0)

            chartSubscriptionsComparison = QtCharts.QChart()
            chartSubscriptionsComparison.addSeries(seriesSubscriptionsComparison)
            chartSubscriptionsComparison.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            axisX = QtCharts.QBarCategoryAxis()
            axis_x_brush = QBrush(QColor("#EE4540"))
            axisX.setLabelsBrush(axis_x_brush)
            axisX.setTitleBrush(axis_x_brush)
            axisX.setTitleText("Subscriptions")

            axisY = QtCharts.QValueAxis()
            axisY.setLabelFormat("%i")
            axisY.setTitleText("Subscription cost [RON]")
            axisY.setMax(100)
            axisY.setMin(0)
            axisY.setTickCount(5)
            axis_y_brush = QBrush(QColor("#EE4540"))
            axisY.setLabelsBrush(axis_y_brush)            
            axisY.setTitleBrush(axis_y_brush)

            chartSubscriptionsComparison.addAxis(axisX, Qt.AlignBottom)
            chartSubscriptionsComparison.addAxis(axisY, Qt.AlignLeft)

            seriesSubscriptionsComparison.attachAxis(axisY)            

            chartSubscriptionsComparison.setBackgroundBrush(QBrush(QColor("transparent")))
            chartSubscriptionsComparison.setTitleBrush(QBrush(Qt.white));

            chartSubscriptionsComparison.legend().setVisible(True)
            chartSubscriptionsComparison.legend().setBrush(QBrush(Qt.white))
            chartSubscriptionsComparison.legend().setAlignment(Qt.AlignBottom)

            self.chartviewSubscriptionsComparison.setChart(chartSubscriptionsComparison)
            self.chartviewSubscriptionsComparison.setRenderHint(QPainter.Antialiasing)

        connection.commit()
        connection.close()

    def setNetflixData(self):
        if (self.ui.comboBoxNetflixDay.currentText() != 'Day' and self.ui.comboBoxNetflixMonth.currentText() != 'Month' and \
            self.ui.comboBoxNetflixYear.currentText() != 'Year' and self.ui.comboBoxNetflixCurrency.currentText() != 'Currency' and \
            self.ui.txtNetflixPayment.text() != ''):
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("SELECT * FROM netflix_data WHERE username = ?",(self.username,))

            if(len(result.fetchall()) > 0):
                payment = self.ui.txtNetflixPayment.text()
                if ',' in payment:
                    payment_real = payment.replace(',','.')
                    start_date = datetime.datetime(int(self.ui.comboBoxNetflixYear.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()), int(self.ui.comboBoxNetflixDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment_real) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtNetflixTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxNetflixCurrency.currentText()))
                    db_connection.execute("UPDATE netflix_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                    WHERE username = ?",(int(self.ui.comboBoxNetflixDay.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()),\
                                     int(self.ui.comboBoxNetflixYear.currentText()), self.ui.comboBoxNetflixCurrency.currentText()\
                                     , self.ui.txtNetflixPayment.text(), correct_total_pay, self.username))
                    connection.commit()
                    connection.close()
                else:
                    start_date = datetime.datetime(int(self.ui.comboBoxNetflixYear.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()), int(self.ui.comboBoxNetflixDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtNetflixTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxNetflixCurrency.currentText()))
                    db_connection.execute("UPDATE netflix_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                    WHERE username = ?",(int(self.ui.comboBoxNetflixDay.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()),\
                                     int(self.ui.comboBoxNetflixYear.currentText()), self.ui.comboBoxNetflixCurrency.currentText()\
                                     , self.ui.txtNetflixPayment.text(), correct_total_pay, self.username))
                    connection.commit()
                    connection.close()
            else:
                payment = self.ui.txtNetflixPayment.text()
                if ',' in payment:
                    payment_real = payment.replace(',','.')
                    start_date = datetime.datetime(int(self.ui.comboBoxNetflixYear.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()), int(self.ui.comboBoxNetflixDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment_real) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtNetflixTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxNetflixCurrency.currentText()))
                    db_connection.execute("INSERT INTO netflix_data(username, email, start_day, start_month, start_year, currency, pay, total_pay)\
                    VALUES (?,?,?,?,?,?,?,?)",(self.username, self.email, int(self.ui.comboBoxNetflixDay.currentText()),\
                    int(self.ui.comboBoxNetflixMonth.currentText()), int(self.ui.comboBoxNetflixYear.currentText()), \
                    self.ui.comboBoxNetflixCurrency.currentText(), self.ui.txtNetflixPayment.text(), correct_total_pay))
                    connection.commit()
                    connection.close()
                else:
                    start_date = datetime.datetime(int(self.ui.comboBoxNetflixYear.currentText()), int(self.ui.comboBoxNetflixMonth.currentText()), int(self.ui.comboBoxNetflixDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtNetflixTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxNetflixCurrency.currentText()))
                    db_connection.execute("INSERT INTO netflix_data(username, email, start_day, start_month, start_year, currency, pay, total_pay)\
                    VALUES (?,?,?,?,?,?,?,?)",(self.username, self.email, int(self.ui.comboBoxNetflixDay.currentText()),\
                    int(self.ui.comboBoxNetflixMonth.currentText()), int(self.ui.comboBoxNetflixYear.currentText()), \
                    self.ui.comboBoxNetflixCurrency.currentText(), self.ui.txtNetflixPayment.text(), correct_total_pay))
                    connection.commit()
                    connection.close()
        else:
            self.generateMessageBox(window_title='Subscription information', msg_text='Please make sure you have added all the requested information!')


    def setSpotifyData(self):
        if (self.ui.comboBoxSpotifyDay.currentText() != 'Day' and self.ui.comboBoxSpotifyMonth.currentText() != 'Month' and \
            self.ui.comboBoxSpotifyYear.currentText() != 'Year' and self.ui.comboBoxSpotifyCurrency.currentText() != 'Currency' and \
            self.ui.txtSpotifyPayment.text() != ''):
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("SELECT * FROM spotify_data WHERE username = ?",(self.username,))

            if(len(result.fetchall()) > 0):
                payment = self.ui.txtSpotifyPayment.text()                
                if ',' in payment:
                    payment_real = payment.replace(',','.')
                    start_date = datetime.datetime(int(self.ui.comboBoxSpotifyYear.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()), int(self.ui.comboBoxSpotifyDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment_real) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtSpotifyTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxSpotifyCurrency.currentText()))
                    db_connection.execute("UPDATE spotify_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                    WHERE username = ?",(int(self.ui.comboBoxSpotifyDay.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()),\
                                     int(self.ui.comboBoxSpotifyYear.currentText()), self.ui.comboBoxSpotifyCurrency.currentText()\
                                     , self.ui.txtSpotifyPayment.text(), correct_total_pay, self.username))
                    connection.commit()
                    connection.close()
                else:
                    start_date = datetime.datetime(int(self.ui.comboBoxSpotifyYear.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()), int(self.ui.comboBoxSpotifyDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtSpotifyTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxSpotifyCurrency.currentText()))
                    db_connection.execute("UPDATE spotify_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                    WHERE username = ?",(int(self.ui.comboBoxSpotifyDay.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()),\
                                     int(self.ui.comboBoxSpotifyYear.currentText()), self.ui.comboBoxSpotifyCurrency.currentText()\
                                     , self.ui.txtSpotifyPayment.text(), correct_total_pay, self.username))
                    connection.commit()
                    connection.close()
            else:
                payment = self.ui.txtSpotifyPayment.text()
                if ',' in payment:
                    payment_real = payment.replace(',','.')
                    start_date = datetime.datetime(int(self.ui.comboBoxSpotifyYear.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()), int(self.ui.comboBoxSpotifyDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment_real) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtSpotifyTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxSpotifyCurrency.currentText()))
                    db_connection.execute("INSERT INTO spotify_data(username, email, start_day, start_month, start_year, currency, pay, total_pay)\
                    VALUES (?,?,?,?,?,?,?,?)",(self.username, self.email, int(self.ui.comboBoxSpotifyDay.currentText()),\
                    int(self.ui.comboBoxSpotifyMonth.currentText()), int(self.ui.comboBoxSpotifyYear.currentText()), \
                    self.ui.comboBoxSpotifyCurrency.currentText(), self.ui.txtSpotifyPayment.text(), correct_total_pay))
                    connection.commit()
                    connection.close()
                else:
                    start_date = datetime.datetime(int(self.ui.comboBoxSpotifyYear.currentText()), int(self.ui.comboBoxSpotifyMonth.currentText()), int(self.ui.comboBoxSpotifyDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtSpotifyTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxSpotifyCurrency.currentText()))
                    db_connection.execute("INSERT INTO spotify_data(username, email, start_day, start_month, start_year, currency, pay, total_pay)\
                    VALUES (?,?,?,?,?,?,?,?)",(self.username, self.email, int(self.ui.comboBoxSpotifyDay.currentText()),\
                    int(self.ui.comboBoxSpotifyMonth.currentText()), int(self.ui.comboBoxSpotifyYear.currentText()), \
                    self.ui.comboBoxSpotifyCurrency.currentText(), self.ui.txtSpotifyPayment.text(), correct_total_pay))
                    connection.commit()
                    connection.close()
        else:
            self.generateMessageBox(window_title='Subscription information', msg_text='Please make sure you have added all the requested information!')


    def setTelecomData(self):
        if (self.ui.comboBoxTelecomDay.currentText() != 'Day' and self.ui.comboBoxTelecomMonth.currentText() != 'Month' and \
            self.ui.comboBoxTelecomYear.currentText() != 'Year' and self.ui.comboBoxTelecomCurrency.currentText() != 'Currency' and \
            self.ui.txtTelecomPayment.text() != ''):
            currpath = pathlib.Path().absolute()
            db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
            connection = sqlite3.connect(f'{db_path}')
            db_connection = connection.cursor()
            result = db_connection.execute("SELECT * FROM telecom_data WHERE username = ?",(self.username,))

            if(len(result.fetchall()) > 0):
                payment = self.ui.txtTelecomPayment.text()
                if ',' in payment:
                    payment_real = payment.replace(',','.')
                    start_date = datetime.datetime(int(self.ui.comboBoxTelecomYear.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()), int(self.ui.comboBoxTelecomDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment_real) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtTelecomTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxTelecomCurrency.currentText()))
                    db_connection.execute("UPDATE telecom_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                    WHERE username = ?",(int(self.ui.comboBoxTelecomDay.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()),\
                                     int(self.ui.comboBoxTelecomYear.currentText()), self.ui.comboBoxTelecomCurrency.currentText()\
                                     , self.ui.txtTelecomPayment.text(), correct_total_pay, self.username))
                    connection.commit()
                    connection.close()
                else:
                    start_date = datetime.datetime(int(self.ui.comboBoxTelecomYear.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()), int(self.ui.comboBoxTelecomDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtTelecomTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxTelecomCurrency.currentText()))
                    db_connection.execute("UPDATE telecom_data SET start_day = ?, start_month = ?, start_year = ?, currency = ?, pay = ?, total_pay = ?\
                                    WHERE username = ?",(int(self.ui.comboBoxTelecomDay.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()),\
                                     int(self.ui.comboBoxTelecomYear.currentText()), self.ui.comboBoxTelecomCurrency.currentText()\
                                     , self.ui.txtTelecomPayment.text(), correct_total_pay, self.username))
                    connection.commit()
                    connection.close()
            else:
                payment = self.ui.txtTelecomPayment.text()
                if ',' in payment:
                    payment_real = payment.replace(',','.')
                    start_date = datetime.datetime(int(self.ui.comboBoxTelecomYear.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()), int(self.ui.comboBoxTelecomDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment_real) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtTelecomTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxTelecomCurrency.currentText()))
                    db_connection.execute("INSERT INTO telecom_data(username, email, start_day, start_month, start_year, currency, pay, total_pay)\
                    VALUES (?,?,?,?,?,?,?,?)",(self.username, self.email, int(self.ui.comboBoxTelecomDay.currentText()),\
                    int(self.ui.comboBoxTelecomMonth.currentText()), int(self.ui.comboBoxTelecomYear.currentText()), \
                    self.ui.comboBoxTelecomCurrency.currentText(), self.ui.txtTelecomPayment.text(), correct_total_pay))
                    connection.commit()
                    connection.close()
                else:
                    start_date = datetime.datetime(int(self.ui.comboBoxTelecomYear.currentText()), int(self.ui.comboBoxTelecomMonth.currentText()), int(self.ui.comboBoxTelecomDay.currentText()))
                    end_date = datetime.datetime.now()
                    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                    total_pay = float(payment) * num_months
                    correct_total_pay = "{:.2f}".format(total_pay)
                    self.ui.txtTelecomTotalPayment.setText("{:.2f} {}".format(total_pay, self.ui.comboBoxTelecomCurrency.currentText()))
                    db_connection.execute("INSERT INTO telecom_data(username, email, start_day, start_month, start_year, currency, pay, total_pay)\
                    VALUES (?,?,?,?,?,?,?,?)",(self.username, self.email, int(self.ui.comboBoxTelecomDay.currentText()),\
                    int(self.ui.comboBoxTelecomMonth.currentText()), int(self.ui.comboBoxTelecomYear.currentText()), \
                    self.ui.comboBoxTelecomCurrency.currentText(), self.ui.txtTelecomPayment.text(), correct_total_pay))
                    connection.commit()
                    connection.close()
        else:
            self.generateMessageBox(window_title='Subscription information', msg_text='Please make sure you have added all the requested information!')


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

    def setSubscriptionVodafone(self):
        self.ui.btnVodafoneSelection.setChecked(True)
        username = self.ui.txtUsername.text()
        currpath = pathlib.Path().absolute()
        db_path = pathlib.Path(f'{currpath}'+r'\db\billy.db')
        connection = sqlite3.connect(f'{db_path}')
        db_connection = connection.cursor()
        # Updating the subscription field for the logged in user in the db
        db_connection.execute("UPDATE accounts SET subscription_vodafone = 1 WHERE username = '{}'".format(username))
        connection.commit()
        connection.close()

    def mainBillyDashboard(self):
        # Animate left side menu upon pressing the main logo button and focus on Dashboard
        self.ui.frameMenuContent.setGeometry(250, 250, 0, 670)
        self.animation2 = QPropertyAnimation(self.ui.frameMenuContent, b"geometry")
        self.animation2.setDuration(500)
        self.animation2.setEndValue(QRect(0, 250, 200, 670))
        self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        self.animation2.start()
        self.dashboardButton()

    def usernameProfilePage(self):
        mainButtonsList = [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions]
        for button in mainButtonsList:
            button.setChecked(False)
        MainWindow.profilePage(self)

    # Profile Page content and buttons
    def profilePage(self):
        mainButtonsList = [self.ui.btnDashboard, self.ui.btnCalendar, self.ui.btnElectricity, self.ui.btnNaturalGas, self.ui.btnInternetTV, self.ui.btnSubscriptions]
        for button in mainButtonsList:
            button.setChecked(False)
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageProfile)

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