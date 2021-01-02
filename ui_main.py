# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billy_uiXfXeyM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import billy_app_qrc

class Ui_BillyAppMain(object):
    def setupUiMain(self, BillyAppMain):
        if not BillyAppMain.objectName():
            BillyAppMain.setObjectName(u"BillyAppMain")
        BillyAppMain.resize(1304, 920)
        BillyAppMain.setMinimumSize(QSize(1200, 800))
        self.mainCentralWidget = QWidget(BillyAppMain)
        self.mainCentralWidget.setObjectName(u"mainCentralWidget")
        self.mainCentralWidget.setStyleSheet(u"background-color: rgb(39, 43, 47);")
        self.horizontalLayout = QHBoxLayout(self.mainCentralWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameLeftMenu = QFrame(self.mainCentralWidget)
        self.frameLeftMenu.setObjectName(u"frameLeftMenu")
        self.frameLeftMenu.setMaximumSize(QSize(200, 16777215))
        self.frameLeftMenu.setStyleSheet(u"QFrame{\n"
"   background-color: #272b2f;\n"
"}")
        self.frameLeftMenu.setFrameShape(QFrame.NoFrame)
        self.frameLeftMenu.setFrameShadow(QFrame.Raised)
        self.frameLeftMenu.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frameLeftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameTitleLogo = QFrame(self.frameLeftMenu)
        self.frameTitleLogo.setObjectName(u"frameTitleLogo")
        self.frameTitleLogo.setMaximumSize(QSize(200, 180))
        self.frameTitleLogo.setStyleSheet(u"")
        self.frameTitleLogo.setFrameShape(QFrame.NoFrame)
        self.frameTitleLogo.setFrameShadow(QFrame.Raised)
        self.frameTitleLogo.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frameTitleLogo)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameTitleSmall = QFrame(self.frameTitleLogo)
        self.frameTitleSmall.setObjectName(u"frameTitleSmall")
        self.frameTitleSmall.setMaximumSize(QSize(16777215, 40))
        self.frameTitleSmall.setFrameShape(QFrame.StyledPanel)
        self.frameTitleSmall.setFrameShadow(QFrame.Raised)
        self.frameTitleSmall.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.frameTitleSmall)

        self.frameLogo = QFrame(self.frameTitleLogo)
        self.frameLogo.setObjectName(u"frameLogo")
        self.frameLogo.setMaximumSize(QSize(200, 150))
        self.frameLogo.setStyleSheet(u"background-color: #272b2f;")
        self.frameLogo.setFrameShape(QFrame.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Raised)
        self.frameLogo.setLineWidth(0)
        self.btnBillyMain = QPushButton(self.frameLogo)
        self.btnBillyMain.setObjectName(u"btnBillyMain")
        self.btnBillyMain.setGeometry(QRect(0, 0, 200, 150))
        self.btnBillyMain.setMaximumSize(QSize(200, 150))
        self.btnBillyMain.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBillyMain.setStyleSheet(u"QPushButton{      \n"
"   background-image: url(:/images/Resources/logo_clear.png);\n"
"   border-radius: 5px;\n"
"   background-repeat: none;\n"
"   background-position: center;\n"
"}\n"
"QPushButton:hover{\n"
"   background-image: url(:/images/Resources/logo_hover.png);\n"
"   border-radius: 5px;\n"
"   background-repeat: none;\n"
"   background-position: center;\n"
"}")
        self.btnBillyMain.setAutoDefault(False)
        self.btnBillyMain.setFlat(True)

        self.verticalLayout_3.addWidget(self.frameLogo)


        self.verticalLayout.addWidget(self.frameTitleLogo)

        self.frameUsername = QFrame(self.frameLeftMenu)
        self.frameUsername.setObjectName(u"frameUsername")
        self.frameUsername.setMaximumSize(QSize(200, 70))
        self.frameUsername.setStyleSheet(u"background-color: #272b2f;")
        self.frameUsername.setFrameShape(QFrame.StyledPanel)
        self.frameUsername.setFrameShadow(QFrame.Raised)
        self.frameUsername.setLineWidth(0)
        self.btnUsername = QPushButton(self.frameUsername)
        self.btnUsername.setObjectName(u"btnUsername")
        self.btnUsername.setGeometry(QRect(0, 10, 200, 50))
        font = QFont()
        font.setFamily(u"SF UI Display")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btnUsername.setFont(font)
        self.btnUsername.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnUsername.setStyleSheet(u"QPushButton\n"
"{\n"
"   color: #C72C41;\n"
"   border: none;\n"
"}\n"
"QPushButton:pressed\n"
"{  \n"
"   color: #EE4540;\n"
"   border: none;\n"
"}\n"
"QPushButton:hover\n"
"{  \n"
"   color: #EE4540;\n"
"   border: none;\n"
"}")
        self.btnUsername.setCheckable(False)
        self.btnUsername.setAutoDefault(False)
        self.btnUsername.setFlat(True)

        self.verticalLayout.addWidget(self.frameUsername)

        self.frameMenuContent = QFrame(self.frameLeftMenu)
        self.frameMenuContent.setObjectName(u"frameMenuContent")
        self.frameMenuContent.setEnabled(True)
        self.frameMenuContent.setMaximumSize(QSize(200, 16777215))
        self.frameMenuContent.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: #272b2f;\n"
"   color: #fafbfb;\n"
"}\n"
"QPushButton:checked{\n"
"   background-color: #202528;\n"
"   color: #EE4540;\n"
"}\n"
"QPushButton:hover{\n"
"   color: #EE4540;\n"
"}")
        self.frameMenuContent.setFrameShape(QFrame.NoFrame)
        self.frameMenuContent.setFrameShadow(QFrame.Plain)
        self.frameMenuContent.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frameMenuContent)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnDashboard = QPushButton(self.frameMenuContent)
        self.btnDashboard.setObjectName(u"btnDashboard")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDashboard.sizePolicy().hasHeightForWidth())
        self.btnDashboard.setSizePolicy(sizePolicy)
        self.btnDashboard.setMinimumSize(QSize(0, 0))
        self.btnDashboard.setMaximumSize(QSize(200, 50))
        font1 = QFont()
        font1.setFamily(u"SF UI Display")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnDashboard.setFont(font1)
        self.btnDashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDashboard.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/images/Resources/dashboard_not_clicked.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"}\n"
"QPushButton:checked{   \n"
"   background-image: url(:/images/Resources/dashboard_clicked.png);\n"
"}\n"
"")
        self.btnDashboard.setIconSize(QSize(16, 16))
        self.btnDashboard.setCheckable(True)
        self.btnDashboard.setChecked(False)
        self.btnDashboard.setAutoDefault(False)
        self.btnDashboard.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnDashboard)

        self.btnCalendar = QPushButton(self.frameMenuContent)
        self.btnCalendar.setObjectName(u"btnCalendar")
        sizePolicy.setHeightForWidth(self.btnCalendar.sizePolicy().hasHeightForWidth())
        self.btnCalendar.setSizePolicy(sizePolicy)
        self.btnCalendar.setMaximumSize(QSize(200, 50))
        self.btnCalendar.setFont(font1)
        self.btnCalendar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCalendar.setStyleSheet(u"QPushButton{\n"
"   background-image: url(:/images/Resources/calendar_not_clicked.png);\n"
"   background-repeat: none;\n"
"   padding-left: 50px;\n"
"}\n"
"QPushButton:checked{   \n"
"   background-image: url(:/images/Resources/calendar_clicked.png);\n"
"}\n"
"")
        self.btnCalendar.setCheckable(True)
        self.btnCalendar.setChecked(False)
        self.btnCalendar.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnCalendar)

        self.btnElectricity = QPushButton(self.frameMenuContent)
        self.btnElectricity.setObjectName(u"btnElectricity")
        sizePolicy.setHeightForWidth(self.btnElectricity.sizePolicy().hasHeightForWidth())
        self.btnElectricity.setSizePolicy(sizePolicy)
        self.btnElectricity.setMaximumSize(QSize(200, 50))
        self.btnElectricity.setFont(font1)
        self.btnElectricity.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElectricity.setStyleSheet(u"QPushButton{\n"
"   background-image: url(:/images/Resources/electricity_not_clicked.png);\n"
"   background-repeat: none;\n"
"   padding-left: 50px;\n"
"}\n"
"QPushButton:checked{\n"
"background-image: url(:/images/Resources/electricity_clicked.png);\n"
"}")
        self.btnElectricity.setIconSize(QSize(16, 16))
        self.btnElectricity.setCheckable(True)
        self.btnElectricity.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnElectricity)

        self.btnNaturalGas = QPushButton(self.frameMenuContent)
        self.btnNaturalGas.setObjectName(u"btnNaturalGas")
        sizePolicy.setHeightForWidth(self.btnNaturalGas.sizePolicy().hasHeightForWidth())
        self.btnNaturalGas.setSizePolicy(sizePolicy)
        self.btnNaturalGas.setMaximumSize(QSize(200, 50))
        self.btnNaturalGas.setFont(font1)
        self.btnNaturalGas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNaturalGas.setStyleSheet(u"QPushButton{\n"
"   background-image: url(:/images/Resources/gas_not_clicked.png);\n"
"   background-repeat: none;\n"
"   padding-left: 50px;\n"
"}\n"
"QPushButton:checked{   \n"
"   background-image: url(:/images/Resources/gas_clicked.png);\n"
"}\n"
"")
        self.btnNaturalGas.setCheckable(True)
        self.btnNaturalGas.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnNaturalGas)

        self.btnInternetTV = QPushButton(self.frameMenuContent)
        self.btnInternetTV.setObjectName(u"btnInternetTV")
        sizePolicy.setHeightForWidth(self.btnInternetTV.sizePolicy().hasHeightForWidth())
        self.btnInternetTV.setSizePolicy(sizePolicy)
        self.btnInternetTV.setMaximumSize(QSize(200, 50))
        self.btnInternetTV.setFont(font1)
        self.btnInternetTV.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnInternetTV.setStyleSheet(u"QPushButton{\n"
"   background-image: url(:/images/Resources/internet_not_clicked.png);\n"
"   background-repeat: none;\n"
"   padding-left: 50px;\n"
"}\n"
"QPushButton:checked{   \n"
"   background-image: url(:/images/Resources/internet_clicked.png);\n"
"}\n"
"")
        self.btnInternetTV.setCheckable(True)
        self.btnInternetTV.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnInternetTV)

        self.btnSubscriptions = QPushButton(self.frameMenuContent)
        self.btnSubscriptions.setObjectName(u"btnSubscriptions")
        sizePolicy.setHeightForWidth(self.btnSubscriptions.sizePolicy().hasHeightForWidth())
        self.btnSubscriptions.setSizePolicy(sizePolicy)
        self.btnSubscriptions.setMaximumSize(QSize(200, 50))
        self.btnSubscriptions.setFont(font1)
        self.btnSubscriptions.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSubscriptions.setStyleSheet(u"QPushButton{\n"
"   background-image: url(:/images/Resources/subscriptions_not_clicked.png);\n"
"   background-repeat: none;\n"
"   padding-left: 50px;\n"
"}\n"
"QPushButton:checked{   \n"
"   background-image: url(:/images/Resources/subscriptions_clicked.png);\n"
"}\n"
"")
        self.btnSubscriptions.setCheckable(True)
        self.btnSubscriptions.setFlat(True)

        self.verticalLayout_4.addWidget(self.btnSubscriptions)


        self.verticalLayout.addWidget(self.frameMenuContent)


        self.horizontalLayout.addWidget(self.frameLeftMenu)

        self.frameMainContentArea = QFrame(self.mainCentralWidget)
        self.frameMainContentArea.setObjectName(u"frameMainContentArea")
        self.frameMainContentArea.setFrameShape(QFrame.NoFrame)
        self.frameMainContentArea.setFrameShadow(QFrame.Raised)
        self.frameMainContentArea.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frameMainContentArea)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameHeader = QFrame(self.frameMainContentArea)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setMaximumSize(QSize(16777215, 40))
        self.frameHeader.setFrameShape(QFrame.NoFrame)
        self.frameHeader.setFrameShadow(QFrame.Raised)
        self.frameHeader.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frameHeader)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameTitle = QFrame(self.frameHeader)
        self.frameTitle.setObjectName(u"frameTitle")
        self.frameTitle.setMaximumSize(QSize(16777215, 40))
        self.frameTitle.setStyleSheet(u"QFrame{\n"
"   background-color: rgb(32, 37, 40);\n"
"}")
        self.frameTitle.setFrameShape(QFrame.NoFrame)
        self.frameTitle.setFrameShadow(QFrame.Raised)
        self.frameTitle.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frameTitle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.headerButtons = QFrame(self.frameTitle)
        self.headerButtons.setObjectName(u"headerButtons")
        self.headerButtons.setFrameShape(QFrame.StyledPanel)
        self.headerButtons.setFrameShadow(QFrame.Raised)
        self.btnProfile = QPushButton(self.headerButtons)
        self.btnProfile.setObjectName(u"btnProfile")
        self.btnProfile.setGeometry(QRect(0, 0, 40, 40))
        self.btnProfile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnProfile.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: rgb(32, 37, 40);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: rgb(39, 43, 47);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/Resources/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnProfile.setIcon(icon)
        self.btnProfile.setIconSize(QSize(40, 40))
        self.btnProfile.setCheckable(True)
        self.btnProfile.setFlat(True)
        self.lblSetProfileEmail = QLabel(self.headerButtons)
        self.lblSetProfileEmail.setObjectName(u"lblSetProfileEmail")
        self.lblSetProfileEmail.setGeometry(QRect(50, 0, 400, 40))
        font2 = QFont()
        font2.setFamily(u"SF UI Display")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.lblSetProfileEmail.setFont(font2)
        self.lblSetProfileEmail.setCursor(QCursor(Qt.ArrowCursor))
        self.lblSetProfileEmail.setStyleSheet(u"color: #d0cfd0; \n"
"background-color:#202528;  ")

        self.horizontalLayout_4.addWidget(self.headerButtons)

        self.headerInfo = QFrame(self.frameTitle)
        self.headerInfo.setObjectName(u"headerInfo")
        self.headerInfo.setMaximumSize(QSize(400, 16777215))
        self.headerInfo.setFrameShape(QFrame.StyledPanel)
        self.headerInfo.setFrameShadow(QFrame.Raised)
        self.lblBillingFlag = QLabel(self.headerInfo)
        self.lblBillingFlag.setObjectName(u"lblBillingFlag")
        self.lblBillingFlag.setGeometry(QRect(320, 0, 40, 40))
        self.lblBillingFlag.setStyleSheet(u"background-image: url(:/images/Resources/billing_country.png);")
        self.lblBillingCountry = QLabel(self.headerInfo)
        self.lblBillingCountry.setObjectName(u"lblBillingCountry")
        self.lblBillingCountry.setGeometry(QRect(220, 0, 100, 40))
        font3 = QFont()
        font3.setFamily(u"SF UI Display")
        font3.setPointSize(10)
        self.lblBillingCountry.setFont(font3)
        self.lblBillingCountry.setStyleSheet(u"color: #6c6e71;")

        self.horizontalLayout_4.addWidget(self.headerInfo)


        self.horizontalLayout_2.addWidget(self.frameTitle)

        self.frameControlButtons = QFrame(self.frameHeader)
        self.frameControlButtons.setObjectName(u"frameControlButtons")
        self.frameControlButtons.setMaximumSize(QSize(120, 16777215))
        self.frameControlButtons.setStyleSheet(u"QFrame{\n"
"   background-color: rgb(32, 37, 40);\n"
"}")
        self.frameControlButtons.setFrameShape(QFrame.NoFrame)
        self.frameControlButtons.setFrameShadow(QFrame.Raised)
        self.frameControlButtons.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frameControlButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnMinimize = QPushButton(self.frameControlButtons)
        self.btnMinimize.setObjectName(u"btnMinimize")
        font4 = QFont()
        font4.setKerning(False)
        self.btnMinimize.setFont(font4)
        self.btnMinimize.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: rgb(32, 37, 40);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:#2a2e32;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/Resources/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMinimize.setIcon(icon1)
        self.btnMinimize.setIconSize(QSize(40, 40))
        self.btnMinimize.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnMinimize)

        self.btnMaximizeRestore = QPushButton(self.frameControlButtons)
        self.btnMaximizeRestore.setObjectName(u"btnMaximizeRestore")
        self.btnMaximizeRestore.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: rgb(32, 37, 40);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:#2a2e32;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/Resources/maximize_restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMaximizeRestore.setIcon(icon2)
        self.btnMaximizeRestore.setIconSize(QSize(40, 40))
        self.btnMaximizeRestore.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnMaximizeRestore)

        self.btnClose = QPushButton(self.frameControlButtons)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: rgb(32, 37, 40);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:#C72C41;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/Resources/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon3)
        self.btnClose.setIconSize(QSize(40, 40))
        self.btnClose.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnClose)


        self.horizontalLayout_2.addWidget(self.frameControlButtons)


        self.verticalLayout_2.addWidget(self.frameHeader)

        self.frameContentArea = QFrame(self.frameMainContentArea)
        self.frameContentArea.setObjectName(u"frameContentArea")
        self.frameContentArea.setStyleSheet(u"QFrame{\n"
"   background-color:#202528;\n"
"}")
        self.frameContentArea.setFrameShape(QFrame.StyledPanel)
        self.frameContentArea.setFrameShadow(QFrame.Raised)
        self.frameContentArea.setLineWidth(0)
        self.stackedWidget = QStackedWidget(self.frameContentArea)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1091, 871))
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"   background-color: rgb(32, 37, 40);\n"
"}")
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName(u"pageDashboard")
        self.lblDashTitle = QLabel(self.pageDashboard)
        self.lblDashTitle.setObjectName(u"lblDashTitle")
        self.lblDashTitle.setGeometry(QRect(30, 10, 281, 41))
        font5 = QFont()
        font5.setFamily(u"SF UI Display")
        font5.setPointSize(18)
        font5.setBold(True)
        font5.setWeight(75)
        self.lblDashTitle.setFont(font5)
        self.lblDashTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblDashTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageDashboard)
        self.pageCalendar = QWidget()
        self.pageCalendar.setObjectName(u"pageCalendar")
        self.lblCalendarTitle = QLabel(self.pageCalendar)
        self.lblCalendarTitle.setObjectName(u"lblCalendarTitle")
        self.lblCalendarTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblCalendarTitle.setFont(font5)
        self.lblCalendarTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblCalendarTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageCalendar)
        self.pageElectricity = QWidget()
        self.pageElectricity.setObjectName(u"pageElectricity")
        self.lblElectricityTitle = QLabel(self.pageElectricity)
        self.lblElectricityTitle.setObjectName(u"lblElectricityTitle")
        self.lblElectricityTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblElectricityTitle.setFont(font5)
        self.lblElectricityTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblElectricityTitle.setTextFormat(Qt.MarkdownText)
        self.electricitySupplierSelection = QFrame(self.pageElectricity)
        self.electricitySupplierSelection.setObjectName(u"electricitySupplierSelection")
        self.electricitySupplierSelection.setGeometry(QRect(20, 80, 381, 71))
        self.electricitySupplierSelection.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.electricitySupplierSelection.setFrameShape(QFrame.StyledPanel)
        self.electricitySupplierSelection.setFrameShadow(QFrame.Raised)
        self.lblElectricitySupplierSelection = QLabel(self.electricitySupplierSelection)
        self.lblElectricitySupplierSelection.setObjectName(u"lblElectricitySupplierSelection")
        self.lblElectricitySupplierSelection.setGeometry(QRect(20, 10, 181, 21))
        font6 = QFont()
        font6.setFamily(u"SF UI Display")
        font6.setPointSize(14)
        self.lblElectricitySupplierSelection.setFont(font6)
        self.lblElectricitySupplierSelection.setStyleSheet(u"color: #f3f5f6;")
        self.lblElectricitySupplierSelectionInfo = QLabel(self.electricitySupplierSelection)
        self.lblElectricitySupplierSelectionInfo.setObjectName(u"lblElectricitySupplierSelectionInfo")
        self.lblElectricitySupplierSelectionInfo.setGeometry(QRect(20, 40, 231, 21))
        self.lblElectricitySupplierSelectionInfo.setFont(font3)
        self.lblElectricitySupplierSelectionInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnElectricitySupplierDisplay = QPushButton(self.electricitySupplierSelection)
        self.btnElectricitySupplierDisplay.setObjectName(u"btnElectricitySupplierDisplay")
        self.btnElectricitySupplierDisplay.setEnabled(False)
        self.btnElectricitySupplierDisplay.setGeometry(QRect(210, 10, 151, 50))
        self.btnElectricitySupplierDisplay.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElectricitySupplierDisplay.setFocusPolicy(Qt.StrongFocus)
        self.btnElectricitySupplierDisplay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnElectricitySupplierDisplay.setStyleSheet(u"background-color: #202528;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;")
        self.btnElectricitySupplierDisplay.setCheckable(True)
        self.btnElectricitySupplierDisplay.setChecked(False)
        self.btnElectricitySupplierDisplay.setAutoDefault(True)
        self.btnElectricitySupplierDisplay.setFlat(True)
        self.stackedWidget.addWidget(self.pageElectricity)
        self.pageNaturalGas = QWidget()
        self.pageNaturalGas.setObjectName(u"pageNaturalGas")
        self.lblNaturalGasTitle = QLabel(self.pageNaturalGas)
        self.lblNaturalGasTitle.setObjectName(u"lblNaturalGasTitle")
        self.lblNaturalGasTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblNaturalGasTitle.setFont(font5)
        self.lblNaturalGasTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblNaturalGasTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageNaturalGas)
        self.pageInternetTV = QWidget()
        self.pageInternetTV.setObjectName(u"pageInternetTV")
        self.lblInternetTVTitle = QLabel(self.pageInternetTV)
        self.lblInternetTVTitle.setObjectName(u"lblInternetTVTitle")
        self.lblInternetTVTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblInternetTVTitle.setFont(font5)
        self.lblInternetTVTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblInternetTVTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageInternetTV)
        self.pageSubscriptions = QWidget()
        self.pageSubscriptions.setObjectName(u"pageSubscriptions")
        self.lblSubscriptionsTitle = QLabel(self.pageSubscriptions)
        self.lblSubscriptionsTitle.setObjectName(u"lblSubscriptionsTitle")
        self.lblSubscriptionsTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblSubscriptionsTitle.setFont(font5)
        self.lblSubscriptionsTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblSubscriptionsTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageSubscriptions)
        self.pageProfile = QWidget()
        self.pageProfile.setObjectName(u"pageProfile")
        self.lblAccountPreferences = QLabel(self.pageProfile)
        self.lblAccountPreferences.setObjectName(u"lblAccountPreferences")
        self.lblAccountPreferences.setGeometry(QRect(30, 10, 281, 41))
        self.lblAccountPreferences.setFont(font5)
        self.lblAccountPreferences.setStyleSheet(u"color: #6c6e71;")
        self.lblAccountPreferences.setTextFormat(Qt.MarkdownText)
        self.profileName = QFrame(self.pageProfile)
        self.profileName.setObjectName(u"profileName")
        self.profileName.setGeometry(QRect(30, 80, 731, 130))
        self.profileName.setCursor(QCursor(Qt.ArrowCursor))
        self.profileName.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.profileName.setFrameShape(QFrame.NoFrame)
        self.profileName.setFrameShadow(QFrame.Raised)
        self.lblProfileName = QLabel(self.profileName)
        self.lblProfileName.setObjectName(u"lblProfileName")
        self.lblProfileName.setGeometry(QRect(20, 10, 191, 21))
        self.lblProfileName.setFont(font6)
        self.lblProfileName.setStyleSheet(u"color: #f3f5f6;")
        self.txtUsername = QLineEdit(self.profileName)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setEnabled(False)
        self.txtUsername.setGeometry(QRect(20, 60, 280, 50))
        font7 = QFont()
        font7.setFamily(u"SF UI Display")
        font7.setPointSize(12)
        self.txtUsername.setFont(font7)
        self.txtUsername.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;   \n"
"   background-image: url(:/images/Resources/username.png);\n"
"   background-repeat: none;\n"
"}")
        self.txtEarnings = QLineEdit(self.profileName)
        self.txtEarnings.setObjectName(u"txtEarnings")
        self.txtEarnings.setGeometry(QRect(320, 60, 280, 50))
        self.txtEarnings.setFont(font7)
        self.txtEarnings.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;   \n"
"   background-image: url(:/images/Resources/set_earnings.png);\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.btnSetProfileName = QPushButton(self.profileName)
        self.btnSetProfileName.setObjectName(u"btnSetProfileName")
        self.btnSetProfileName.setGeometry(QRect(630, 60, 75, 50))
        self.btnSetProfileName.setFont(font1)
        self.btnSetProfileName.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSetProfileName.setStyleSheet(u"QPushButton{\n"
"   background-color: #EE4540;\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:pressed\n"
"{  \n"
"   border-style:solid;\n"
"   border-width:2px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnSetProfileName.setAutoDefault(True)
        self.btnSetProfileName.setFlat(True)
        self.electricitySupplier = QFrame(self.pageProfile)
        self.electricitySupplier.setObjectName(u"electricitySupplier")
        self.electricitySupplier.setGeometry(QRect(30, 230, 1050, 140))
        self.electricitySupplier.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.electricitySupplier.setFrameShape(QFrame.StyledPanel)
        self.electricitySupplier.setFrameShadow(QFrame.Raised)
        self.lblElectricitySupplier = QLabel(self.electricitySupplier)
        self.lblElectricitySupplier.setObjectName(u"lblElectricitySupplier")
        self.lblElectricitySupplier.setGeometry(QRect(20, 10, 181, 21))
        self.lblElectricitySupplier.setFont(font6)
        self.lblElectricitySupplier.setStyleSheet(u"color: #f3f5f6;")
        self.lblElectricitySupplierInfo = QLabel(self.electricitySupplier)
        self.lblElectricitySupplierInfo.setObjectName(u"lblElectricitySupplierInfo")
        self.lblElectricitySupplierInfo.setGeometry(QRect(20, 40, 231, 21))
        self.lblElectricitySupplierInfo.setFont(font3)
        self.lblElectricitySupplierInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnEnelSelection = QPushButton(self.electricitySupplier)
        self.btnEnelSelection.setObjectName(u"btnEnelSelection")
        self.btnEnelSelection.setGeometry(QRect(20, 70, 230, 50))
        self.btnEnelSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEnelSelection.setFocusPolicy(Qt.StrongFocus)
        self.btnEnelSelection.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnEnelSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/enel_supplier.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnEnelSelection.setCheckable(True)
        self.btnEnelSelection.setChecked(False)
        self.btnEnelSelection.setAutoDefault(True)
        self.btnEnelSelection.setFlat(True)
        self.btnCEZSelection = QPushButton(self.electricitySupplier)
        self.btnCEZSelection.setObjectName(u"btnCEZSelection")
        self.btnCEZSelection.setEnabled(False)
        self.btnCEZSelection.setGeometry(QRect(280, 70, 230, 50))
        self.btnCEZSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCEZSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/cez_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnCEZSelection.setCheckable(True)
        self.btnCEZSelection.setFlat(True)
        self.btnEONSelection = QPushButton(self.electricitySupplier)
        self.btnEONSelection.setObjectName(u"btnEONSelection")
        self.btnEONSelection.setEnabled(False)
        self.btnEONSelection.setGeometry(QRect(540, 70, 230, 50))
        self.btnEONSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEONSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/eon_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnEONSelection.setCheckable(True)
        self.btnEONSelection.setFlat(True)
        self.btnDigiEnergySelection = QPushButton(self.electricitySupplier)
        self.btnDigiEnergySelection.setObjectName(u"btnDigiEnergySelection")
        self.btnDigiEnergySelection.setEnabled(False)
        self.btnDigiEnergySelection.setGeometry(QRect(800, 70, 230, 50))
        self.btnDigiEnergySelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDigiEnergySelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/digiEnergy_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnDigiEnergySelection.setCheckable(True)
        self.btnDigiEnergySelection.setFlat(True)
        self.naturalGasSupplier = QFrame(self.pageProfile)
        self.naturalGasSupplier.setObjectName(u"naturalGasSupplier")
        self.naturalGasSupplier.setGeometry(QRect(30, 390, 1050, 140))
        self.naturalGasSupplier.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.naturalGasSupplier.setFrameShape(QFrame.StyledPanel)
        self.naturalGasSupplier.setFrameShadow(QFrame.Raised)
        self.lblNaturalGasSupplier = QLabel(self.naturalGasSupplier)
        self.lblNaturalGasSupplier.setObjectName(u"lblNaturalGasSupplier")
        self.lblNaturalGasSupplier.setGeometry(QRect(20, 10, 201, 21))
        self.lblNaturalGasSupplier.setFont(font6)
        self.lblNaturalGasSupplier.setStyleSheet(u"color: #f3f5f6;")
        self.lblNaturalGasSupplierInfo = QLabel(self.naturalGasSupplier)
        self.lblNaturalGasSupplierInfo.setObjectName(u"lblNaturalGasSupplierInfo")
        self.lblNaturalGasSupplierInfo.setGeometry(QRect(20, 40, 241, 21))
        self.lblNaturalGasSupplierInfo.setFont(font3)
        self.lblNaturalGasSupplierInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnEngieSelection = QPushButton(self.naturalGasSupplier)
        self.btnEngieSelection.setObjectName(u"btnEngieSelection")
        self.btnEngieSelection.setGeometry(QRect(20, 70, 230, 50))
        self.btnEngieSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEngieSelection.setFocusPolicy(Qt.StrongFocus)
        self.btnEngieSelection.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnEngieSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/engie_supplier.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnEngieSelection.setCheckable(True)
        self.btnEngieSelection.setChecked(False)
        self.btnEngieSelection.setAutoDefault(True)
        self.btnEngieSelection.setFlat(True)
        self.btnCEZGasSelection = QPushButton(self.naturalGasSupplier)
        self.btnCEZGasSelection.setObjectName(u"btnCEZGasSelection")
        self.btnCEZGasSelection.setEnabled(False)
        self.btnCEZGasSelection.setGeometry(QRect(280, 70, 230, 50))
        self.btnCEZGasSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCEZGasSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/cez_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnCEZGasSelection.setCheckable(True)
        self.btnCEZGasSelection.setFlat(True)
        self.btnEONGasSelection = QPushButton(self.naturalGasSupplier)
        self.btnEONGasSelection.setObjectName(u"btnEONGasSelection")
        self.btnEONGasSelection.setEnabled(False)
        self.btnEONGasSelection.setGeometry(QRect(540, 70, 230, 50))
        self.btnEONGasSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEONGasSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/eon_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnEONGasSelection.setCheckable(True)
        self.btnEONGasSelection.setFlat(True)
        self.btnEnelGasSelection = QPushButton(self.naturalGasSupplier)
        self.btnEnelGasSelection.setObjectName(u"btnEnelGasSelection")
        self.btnEnelGasSelection.setEnabled(False)
        self.btnEnelGasSelection.setGeometry(QRect(800, 70, 230, 50))
        self.btnEnelGasSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnEnelGasSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/enel_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnEnelGasSelection.setCheckable(True)
        self.btnEnelGasSelection.setFlat(True)
        self.internetProvider = QFrame(self.pageProfile)
        self.internetProvider.setObjectName(u"internetProvider")
        self.internetProvider.setGeometry(QRect(30, 550, 1050, 140))
        self.internetProvider.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.internetProvider.setFrameShape(QFrame.StyledPanel)
        self.internetProvider.setFrameShadow(QFrame.Raised)
        self.lblInternetProvider = QLabel(self.internetProvider)
        self.lblInternetProvider.setObjectName(u"lblInternetProvider")
        self.lblInternetProvider.setGeometry(QRect(20, 10, 201, 21))
        self.lblInternetProvider.setFont(font6)
        self.lblInternetProvider.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetProviderInfo = QLabel(self.internetProvider)
        self.lblInternetProviderInfo.setObjectName(u"lblInternetProviderInfo")
        self.lblInternetProviderInfo.setGeometry(QRect(20, 40, 251, 21))
        self.lblInternetProviderInfo.setFont(font3)
        self.lblInternetProviderInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnRCSRDSSelection = QPushButton(self.internetProvider)
        self.btnRCSRDSSelection.setObjectName(u"btnRCSRDSSelection")
        self.btnRCSRDSSelection.setGeometry(QRect(20, 70, 230, 50))
        self.btnRCSRDSSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRCSRDSSelection.setFocusPolicy(Qt.StrongFocus)
        self.btnRCSRDSSelection.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnRCSRDSSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/rcsrds_supplier.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnRCSRDSSelection.setCheckable(True)
        self.btnRCSRDSSelection.setChecked(False)
        self.btnRCSRDSSelection.setAutoDefault(True)
        self.btnRCSRDSSelection.setFlat(True)
        self.btnUPCSelection = QPushButton(self.internetProvider)
        self.btnUPCSelection.setObjectName(u"btnUPCSelection")
        self.btnUPCSelection.setEnabled(False)
        self.btnUPCSelection.setGeometry(QRect(280, 70, 230, 50))
        self.btnUPCSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnUPCSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/upc_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnUPCSelection.setCheckable(True)
        self.btnUPCSelection.setFlat(True)
        self.btnTelekomSelection = QPushButton(self.internetProvider)
        self.btnTelekomSelection.setObjectName(u"btnTelekomSelection")
        self.btnTelekomSelection.setEnabled(False)
        self.btnTelekomSelection.setGeometry(QRect(540, 70, 230, 50))
        self.btnTelekomSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnTelekomSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/telekom_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnTelekomSelection.setCheckable(True)
        self.btnTelekomSelection.setFlat(True)
        self.btnGTSSelection = QPushButton(self.internetProvider)
        self.btnGTSSelection.setObjectName(u"btnGTSSelection")
        self.btnGTSSelection.setEnabled(False)
        self.btnGTSSelection.setGeometry(QRect(800, 70, 230, 50))
        self.btnGTSSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGTSSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/gts_supplier_not_available.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnGTSSelection.setCheckable(True)
        self.btnGTSSelection.setFlat(True)
        self.earnings = QFrame(self.pageProfile)
        self.earnings.setObjectName(u"earnings")
        self.earnings.setGeometry(QRect(780, 80, 300, 130))
        self.earnings.setCursor(QCursor(Qt.ArrowCursor))
        self.earnings.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"   background-image: url(:/images/Resources/earnigns.png);\n"
"}")
        self.earnings.setFrameShape(QFrame.NoFrame)
        self.earnings.setFrameShadow(QFrame.Raised)
        self.lblEarnings = QLabel(self.earnings)
        self.lblEarnings.setObjectName(u"lblEarnings")
        self.lblEarnings.setGeometry(QRect(20, 10, 121, 21))
        self.lblEarnings.setFont(font6)
        self.lblEarnings.setStyleSheet(u"color: #f3f5f6;")
        self.lblEarningsPerMonth = QLabel(self.earnings)
        self.lblEarningsPerMonth.setObjectName(u"lblEarningsPerMonth")
        self.lblEarningsPerMonth.setGeometry(QRect(20, 100, 71, 21))
        self.lblEarningsPerMonth.setFont(font3)
        self.lblEarningsPerMonth.setStyleSheet(u"color: #6c6e71;")
        self.lblEarningsCurrency = QLabel(self.earnings)
        self.lblEarningsCurrency.setObjectName(u"lblEarningsCurrency")
        self.lblEarningsCurrency.setGeometry(QRect(20, 70, 61, 21))
        font8 = QFont()
        font8.setFamily(u"SF UI Display")
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setWeight(75)
        self.lblEarningsCurrency.setFont(font8)
        self.lblEarningsCurrency.setStyleSheet(u"color: #C72C41;")
        self.lblEarningsValue = QLabel(self.earnings)
        self.lblEarningsValue.setObjectName(u"lblEarningsValue")
        self.lblEarningsValue.setGeometry(QRect(80, 70, 121, 21))
        self.lblEarningsValue.setFont(font8)
        self.lblEarningsValue.setStyleSheet(u"color: #EE4540;")
        self.subscriptionsPage = QFrame(self.pageProfile)
        self.subscriptionsPage.setObjectName(u"subscriptionsPage")
        self.subscriptionsPage.setGeometry(QRect(30, 710, 530, 140))
        self.subscriptionsPage.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.subscriptionsPage.setFrameShape(QFrame.StyledPanel)
        self.subscriptionsPage.setFrameShadow(QFrame.Raised)
        self.lblSubscriptionsPage = QLabel(self.subscriptionsPage)
        self.lblSubscriptionsPage.setObjectName(u"lblSubscriptionsPage")
        self.lblSubscriptionsPage.setGeometry(QRect(20, 10, 201, 21))
        self.lblSubscriptionsPage.setFont(font6)
        self.lblSubscriptionsPage.setStyleSheet(u"color: #f3f5f6;")
        self.lblSubscriptionsPageInfo = QLabel(self.subscriptionsPage)
        self.lblSubscriptionsPageInfo.setObjectName(u"lblSubscriptionsPageInfo")
        self.lblSubscriptionsPageInfo.setGeometry(QRect(20, 40, 421, 21))
        self.lblSubscriptionsPageInfo.setFont(font3)
        self.lblSubscriptionsPageInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnNetflixSelection = QPushButton(self.subscriptionsPage)
        self.btnNetflixSelection.setObjectName(u"btnNetflixSelection")
        self.btnNetflixSelection.setGeometry(QRect(20, 70, 230, 50))
        self.btnNetflixSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNetflixSelection.setFocusPolicy(Qt.StrongFocus)
        self.btnNetflixSelection.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnNetflixSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/netflix_sub_selection.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnNetflixSelection.setCheckable(True)
        self.btnNetflixSelection.setChecked(False)
        self.btnNetflixSelection.setAutoDefault(True)
        self.btnNetflixSelection.setFlat(True)
        self.btnSpotifySelection = QPushButton(self.subscriptionsPage)
        self.btnSpotifySelection.setObjectName(u"btnSpotifySelection")
        self.btnSpotifySelection.setGeometry(QRect(280, 70, 230, 50))
        self.btnSpotifySelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSpotifySelection.setFocusPolicy(Qt.StrongFocus)
        self.btnSpotifySelection.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnSpotifySelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;\n"
"   background-image: url(:/images/Resources/spotify_sub_selection.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnSpotifySelection.setCheckable(True)
        self.btnSpotifySelection.setChecked(False)
        self.btnSpotifySelection.setAutoDefault(True)
        self.btnSpotifySelection.setFlat(True)
        self.stackedWidget.addWidget(self.pageProfile)

        self.verticalLayout_2.addWidget(self.frameContentArea)


        self.horizontalLayout.addWidget(self.frameMainContentArea)

        BillyAppMain.setCentralWidget(self.mainCentralWidget)

        self.retranslateUi(BillyAppMain)

        self.btnDashboard.setDefault(False)
        self.btnElectricitySupplierDisplay.setDefault(False)
        self.btnSetProfileName.setDefault(False)
        self.btnEnelSelection.setDefault(False)
        self.btnEngieSelection.setDefault(False)
        self.btnRCSRDSSelection.setDefault(False)
        self.btnNetflixSelection.setDefault(False)
        self.btnSpotifySelection.setDefault(False)


        QMetaObject.connectSlotsByName(BillyAppMain)
    # setupUi

    def retranslateUi(self, BillyAppMain):
        BillyAppMain.setWindowTitle(QCoreApplication.translate("BillyAppMain", u"Billy", None))
        self.btnBillyMain.setText("")
        self.btnUsername.setText("")
        self.btnDashboard.setText(QCoreApplication.translate("BillyAppMain", u"Dashboard", None))
        self.btnCalendar.setText(QCoreApplication.translate("BillyAppMain", u"Calendar", None))
        self.btnElectricity.setText(QCoreApplication.translate("BillyAppMain", u"Electricity", None))
        self.btnNaturalGas.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas", None))
        self.btnInternetTV.setText(QCoreApplication.translate("BillyAppMain", u"Internet && TV", None))
        self.btnSubscriptions.setText(QCoreApplication.translate("BillyAppMain", u"Subscriptions", None))
        self.btnProfile.setText("")
        self.lblSetProfileEmail.setText("")
        self.lblBillingFlag.setText("")
        self.lblBillingCountry.setText(QCoreApplication.translate("BillyAppMain", u"Billing Country", None))
        self.btnMinimize.setText("")
        self.btnMaximizeRestore.setText("")
        self.btnClose.setText("")
        self.lblDashTitle.setText(QCoreApplication.translate("BillyAppMain", u"Dashboard", None))
        self.lblCalendarTitle.setText(QCoreApplication.translate("BillyAppMain", u"Calendar", None))
        self.lblElectricityTitle.setText(QCoreApplication.translate("BillyAppMain", u"Electricity", None))
        self.lblElectricitySupplierSelection.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Supplier", None))
        self.lblElectricitySupplierSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Selected electricity supplier", None))
        self.btnElectricitySupplierDisplay.setText("")
        self.lblNaturalGasTitle.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas", None))
        self.lblInternetTVTitle.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV", None))
        self.lblSubscriptionsTitle.setText(QCoreApplication.translate("BillyAppMain", u"Subscriptions", None))
        self.lblAccountPreferences.setText(QCoreApplication.translate("BillyAppMain", u"Account preferences", None))
        self.lblProfileName.setText(QCoreApplication.translate("BillyAppMain", u"Account information", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Username", None))
        self.txtEarnings.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Earnings", None))
        self.btnSetProfileName.setText(QCoreApplication.translate("BillyAppMain", u"Set", None))
        self.lblElectricitySupplier.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Supplier", None))
        self.lblElectricitySupplierInfo.setText(QCoreApplication.translate("BillyAppMain", u"Please select the electricity supplier", None))
        self.btnEnelSelection.setText("")
        self.btnCEZSelection.setText("")
        self.btnEONSelection.setText("")
        self.btnDigiEnergySelection.setText("")
        self.lblNaturalGasSupplier.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas Supplier", None))
        self.lblNaturalGasSupplierInfo.setText(QCoreApplication.translate("BillyAppMain", u"Please select the natural gas supplier", None))
        self.btnEngieSelection.setText("")
        self.btnCEZGasSelection.setText("")
        self.btnEONGasSelection.setText("")
        self.btnEnelGasSelection.setText("")
        self.lblInternetProvider.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV Provider", None))
        self.lblInternetProviderInfo.setText(QCoreApplication.translate("BillyAppMain", u"Please select the internet & TV provider", None))
        self.btnRCSRDSSelection.setText("")
        self.btnUPCSelection.setText("")
        self.btnTelekomSelection.setText("")
        self.btnGTSSelection.setText("")
        self.lblEarnings.setText(QCoreApplication.translate("BillyAppMain", u"Earnings", None))
        self.lblEarningsPerMonth.setText(QCoreApplication.translate("BillyAppMain", u"Per month", None))
        self.lblEarningsCurrency.setText(QCoreApplication.translate("BillyAppMain", u"RON", None))
        self.lblEarningsValue.setText("")
        self.lblSubscriptionsPage.setText(QCoreApplication.translate("BillyAppMain", u"Subscriptions", None))
        self.lblSubscriptionsPageInfo.setText(QCoreApplication.translate("BillyAppMain", u"Please select the services for which you have an active subscription", None))
        self.btnNetflixSelection.setText("")
        self.btnSpotifySelection.setText("")
    # retranslateUi

