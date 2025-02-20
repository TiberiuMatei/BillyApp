# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billy_uixqHhwD.ui'
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
        BillyAppMain.resize(1304, 959)
        BillyAppMain.setMinimumSize(QSize(1200, 800))
        self.mainCentralWidget = QWidget(BillyAppMain)
        self.mainCentralWidget.setObjectName(u"mainCentralWidget")
        self.mainCentralWidget.setStyleSheet(u"background-color: rgb(39, 43, 47);\n"
"outline: none;")
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
        self.stackedWidget.setGeometry(QRect(0, 0, 1091, 911))
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
        self.txtDashEarnings = QLineEdit(self.pageDashboard)
        self.txtDashEarnings.setObjectName(u"txtDashEarnings")
        self.txtDashEarnings.setEnabled(False)
        self.txtDashEarnings.setGeometry(QRect(280, 80, 241, 51))
        font6 = QFont()
        font6.setFamily(u"SF UI Display")
        font6.setPointSize(12)
        self.txtDashEarnings.setFont(font6)
        self.txtDashEarnings.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 10px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 70px; \n"
"   background-color: #2a2e32;  \n"
"   background-image: url(:/images/Resources/set_earnings.png);\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.dashDonutAllBills = QFrame(self.pageDashboard)
        self.dashDonutAllBills.setObjectName(u"dashDonutAllBills")
        self.dashDonutAllBills.setGeometry(QRect(540, 80, 541, 481))
        self.dashDonutAllBills.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.dashDonutAllBills.setFrameShape(QFrame.StyledPanel)
        self.dashDonutAllBills.setFrameShadow(QFrame.Raised)
        self.lblDashDonutAllBills = QLabel(self.dashDonutAllBills)
        self.lblDashDonutAllBills.setObjectName(u"lblDashDonutAllBills")
        self.lblDashDonutAllBills.setGeometry(QRect(20, 10, 341, 23))
        self.lblDashDonutAllBills.setMaximumSize(QSize(500, 16777215))
        font7 = QFont()
        font7.setFamily(u"SF UI Display")
        font7.setPointSize(14)
        self.lblDashDonutAllBills.setFont(font7)
        self.lblDashDonutAllBills.setStyleSheet(u"color: #f3f5f6;")
        self.donutDashAllBills = QWidget(self.dashDonutAllBills)
        self.donutDashAllBills.setObjectName(u"donutDashAllBills")
        self.donutDashAllBills.setGeometry(QRect(-40, 50, 621, 431))
        self.donutDashAllBills.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.dashBarAllBills = QFrame(self.pageDashboard)
        self.dashBarAllBills.setObjectName(u"dashBarAllBills")
        self.dashBarAllBills.setGeometry(QRect(540, 580, 541, 281))
        self.dashBarAllBills.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.dashBarAllBills.setFrameShape(QFrame.StyledPanel)
        self.dashBarAllBills.setFrameShadow(QFrame.Raised)
        self.lblDashBarAllBills = QLabel(self.dashBarAllBills)
        self.lblDashBarAllBills.setObjectName(u"lblDashBarAllBills")
        self.lblDashBarAllBills.setGeometry(QRect(20, 10, 371, 23))
        self.lblDashBarAllBills.setMaximumSize(QSize(500, 16777215))
        self.lblDashBarAllBills.setFont(font7)
        self.lblDashBarAllBills.setStyleSheet(u"color: #f3f5f6;")
        self.barDashAllBills = QWidget(self.dashBarAllBills)
        self.barDashAllBills.setObjectName(u"barDashAllBills")
        self.barDashAllBills.setGeometry(QRect(0, 40, 541, 231))
        self.barDashAllBills.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.txtDashCurrentDate = QLineEdit(self.pageDashboard)
        self.txtDashCurrentDate.setObjectName(u"txtDashCurrentDate")
        self.txtDashCurrentDate.setEnabled(False)
        self.txtDashCurrentDate.setGeometry(QRect(20, 80, 241, 51))
        self.txtDashCurrentDate.setFont(font6)
        self.txtDashCurrentDate.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 10px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 70px; \n"
"   background-color: #2a2e32;\n"
"   background-image: url(:/images/Resources/calendar_dash.png);\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.electricityDashFrame = QFrame(self.pageDashboard)
        self.electricityDashFrame.setObjectName(u"electricityDashFrame")
        self.electricityDashFrame.setGeometry(QRect(20, 360, 501, 111))
        self.electricityDashFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.electricityDashFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.electricityDashFrame.setFrameShape(QFrame.NoFrame)
        self.electricityDashFrame.setFrameShadow(QFrame.Raised)
        self.lblElectricityDash = QLabel(self.electricityDashFrame)
        self.lblElectricityDash.setObjectName(u"lblElectricityDash")
        self.lblElectricityDash.setGeometry(QRect(20, 10, 441, 21))
        self.lblElectricityDash.setFont(font7)
        self.lblElectricityDash.setStyleSheet(u"color: #f3f5f6;")
        self.txtElectricityPayDash = QLineEdit(self.electricityDashFrame)
        self.txtElectricityPayDash.setObjectName(u"txtElectricityPayDash")
        self.txtElectricityPayDash.setEnabled(False)
        self.txtElectricityPayDash.setGeometry(QRect(20, 50, 220, 50))
        self.txtElectricityPayDash.setFont(font6)
        self.txtElectricityPayDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #F7CA18;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/dash_electricity.png);\n"
"   background-repeat: none;\n"
"}")
        self.txtElectricityDueDateDash = QLineEdit(self.electricityDashFrame)
        self.txtElectricityDueDateDash.setObjectName(u"txtElectricityDueDateDash")
        self.txtElectricityDueDateDash.setEnabled(False)
        self.txtElectricityDueDateDash.setGeometry(QRect(260, 50, 220, 50))
        self.txtElectricityDueDateDash.setFont(font6)
        self.txtElectricityDueDateDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 80px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/dash_due_date.png);\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.naturalGasDashFrame = QFrame(self.pageDashboard)
        self.naturalGasDashFrame.setObjectName(u"naturalGasDashFrame")
        self.naturalGasDashFrame.setGeometry(QRect(20, 490, 501, 111))
        self.naturalGasDashFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.naturalGasDashFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.naturalGasDashFrame.setFrameShape(QFrame.NoFrame)
        self.naturalGasDashFrame.setFrameShadow(QFrame.Raised)
        self.lblNaturalGasDash = QLabel(self.naturalGasDashFrame)
        self.lblNaturalGasDash.setObjectName(u"lblNaturalGasDash")
        self.lblNaturalGasDash.setGeometry(QRect(20, 10, 451, 21))
        self.lblNaturalGasDash.setFont(font7)
        self.lblNaturalGasDash.setStyleSheet(u"color: #f3f5f6;")
        self.txtNaturalGasPayDash = QLineEdit(self.naturalGasDashFrame)
        self.txtNaturalGasPayDash.setObjectName(u"txtNaturalGasPayDash")
        self.txtNaturalGasPayDash.setEnabled(False)
        self.txtNaturalGasPayDash.setGeometry(QRect(20, 50, 220, 50))
        self.txtNaturalGasPayDash.setFont(font6)
        self.txtNaturalGasPayDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #DC3023;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/dash_gas.png);\n"
"   background-repeat: none;\n"
"}")
        self.txtNaturalGasDueDateDash = QLineEdit(self.naturalGasDashFrame)
        self.txtNaturalGasDueDateDash.setObjectName(u"txtNaturalGasDueDateDash")
        self.txtNaturalGasDueDateDash.setEnabled(False)
        self.txtNaturalGasDueDateDash.setGeometry(QRect(260, 50, 220, 50))
        self.txtNaturalGasDueDateDash.setFont(font6)
        self.txtNaturalGasDueDateDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 80px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/dash_due_date.png);\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.internetDashFrame = QFrame(self.pageDashboard)
        self.internetDashFrame.setObjectName(u"internetDashFrame")
        self.internetDashFrame.setGeometry(QRect(20, 620, 501, 111))
        self.internetDashFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.internetDashFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.internetDashFrame.setFrameShape(QFrame.NoFrame)
        self.internetDashFrame.setFrameShadow(QFrame.Raised)
        self.lblInternetDash = QLabel(self.internetDashFrame)
        self.lblInternetDash.setObjectName(u"lblInternetDash")
        self.lblInternetDash.setGeometry(QRect(20, 10, 491, 21))
        self.lblInternetDash.setFont(font7)
        self.lblInternetDash.setStyleSheet(u"color: #f3f5f6;")
        self.txtInternetPayDash = QLineEdit(self.internetDashFrame)
        self.txtInternetPayDash.setObjectName(u"txtInternetPayDash")
        self.txtInternetPayDash.setEnabled(False)
        self.txtInternetPayDash.setGeometry(QRect(20, 50, 220, 50))
        self.txtInternetPayDash.setFont(font6)
        self.txtInternetPayDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #22A7F0;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/dash_internet.png);\n"
"   background-repeat: none;\n"
"}")
        self.txtInternetDueDateDash = QLineEdit(self.internetDashFrame)
        self.txtInternetDueDateDash.setObjectName(u"txtInternetDueDateDash")
        self.txtInternetDueDateDash.setEnabled(False)
        self.txtInternetDueDateDash.setGeometry(QRect(260, 50, 220, 50))
        self.txtInternetDueDateDash.setFont(font6)
        self.txtInternetDueDateDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 80px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/dash_due_date.png);\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.subscriptionsDashFrame = QFrame(self.pageDashboard)
        self.subscriptionsDashFrame.setObjectName(u"subscriptionsDashFrame")
        self.subscriptionsDashFrame.setGeometry(QRect(20, 750, 501, 111))
        self.subscriptionsDashFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.subscriptionsDashFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.subscriptionsDashFrame.setFrameShape(QFrame.NoFrame)
        self.subscriptionsDashFrame.setFrameShadow(QFrame.Raised)
        self.lblSubscriptionsDash = QLabel(self.subscriptionsDashFrame)
        self.lblSubscriptionsDash.setObjectName(u"lblSubscriptionsDash")
        self.lblSubscriptionsDash.setGeometry(QRect(20, 10, 191, 21))
        self.lblSubscriptionsDash.setFont(font7)
        self.lblSubscriptionsDash.setStyleSheet(u"color: #f3f5f6;")
        self.txtNetflixDash = QLineEdit(self.subscriptionsDashFrame)
        self.txtNetflixDash.setObjectName(u"txtNetflixDash")
        self.txtNetflixDash.setEnabled(False)
        self.txtNetflixDash.setGeometry(QRect(10, 50, 150, 50))
        self.txtNetflixDash.setFont(font6)
        self.txtNetflixDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.txtSpotifyDash = QLineEdit(self.subscriptionsDashFrame)
        self.txtSpotifyDash.setObjectName(u"txtSpotifyDash")
        self.txtSpotifyDash.setEnabled(False)
        self.txtSpotifyDash.setGeometry(QRect(175, 50, 150, 50))
        self.txtSpotifyDash.setFont(font6)
        self.txtSpotifyDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.txtVodafoneDash = QLineEdit(self.subscriptionsDashFrame)
        self.txtVodafoneDash.setObjectName(u"txtVodafoneDash")
        self.txtVodafoneDash.setEnabled(False)
        self.txtVodafoneDash.setGeometry(QRect(340, 50, 150, 50))
        self.txtVodafoneDash.setFont(font6)
        self.txtVodafoneDash.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.btnInformation = QPushButton(self.pageDashboard)
        self.btnInformation.setObjectName(u"btnInformation")
        self.btnInformation.setGeometry(QRect(170, 18, 25, 25))
        self.btnInformation.setFont(font1)
        self.btnInformation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnInformation.setStyleSheet(u"QPushButton{\n"
"   background-color: #EE4540;\n"
"   background-image: url(:/images/Resources/info_button.png);\n"
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
        self.btnInformation.setAutoDefault(True)
        self.btnInformation.setFlat(True)
        self.informationBillyDashFrame = QFrame(self.pageDashboard)
        self.informationBillyDashFrame.setObjectName(u"informationBillyDashFrame")
        self.informationBillyDashFrame.setGeometry(QRect(20, 150, 501, 191))
        self.informationBillyDashFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.informationBillyDashFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.informationBillyDashFrame.setFrameShape(QFrame.NoFrame)
        self.informationBillyDashFrame.setFrameShadow(QFrame.Raised)
        self.lblDashboardWelcome = QLabel(self.informationBillyDashFrame)
        self.lblDashboardWelcome.setObjectName(u"lblDashboardWelcome")
        self.lblDashboardWelcome.setGeometry(QRect(10, 10, 481, 171))
        self.lblDashboardWelcome.setFont(font3)
        self.lblDashboardWelcome.setStyleSheet(u"color: #6c6e71;")
        self.lblDashboardWelcome.setTextFormat(Qt.RichText)
        self.lblDashboardWelcome.setScaledContents(False)
        self.lblDashboardWelcome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblDashboardWelcome.setWordWrap(False)
        self.btnDashboardToAccountPreferences = QPushButton(self.informationBillyDashFrame)
        self.btnDashboardToAccountPreferences.setObjectName(u"btnDashboardToAccountPreferences")
        self.btnDashboardToAccountPreferences.setGeometry(QRect(459, 67, 35, 35))
        self.btnDashboardToAccountPreferences.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnDashboardToAccountPreferences.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: rgb(42, 46, 50);\n"
"}")
        self.btnDashboardToAccountPreferences.setIcon(icon)
        self.btnDashboardToAccountPreferences.setIconSize(QSize(40, 40))
        self.btnDashboardToAccountPreferences.setCheckable(True)
        self.btnDashboardToAccountPreferences.setFlat(True)
        self.generalDashboardInformationFrame = QFrame(self.pageDashboard)
        self.generalDashboardInformationFrame.setObjectName(u"generalDashboardInformationFrame")
        self.generalDashboardInformationFrame.setGeometry(QRect(20, 880, 1061, 21))
        self.generalDashboardInformationFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.generalDashboardInformationFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 5px; \n"
"   background-color: #2a2e32;\n"
"}")
        self.generalDashboardInformationFrame.setFrameShape(QFrame.NoFrame)
        self.generalDashboardInformationFrame.setFrameShadow(QFrame.Raised)
        self.lblGeneralDashboardInformation = QLabel(self.generalDashboardInformationFrame)
        self.lblGeneralDashboardInformation.setObjectName(u"lblGeneralDashboardInformation")
        self.lblGeneralDashboardInformation.setGeometry(QRect(10, 3, 1041, 16))
        self.lblGeneralDashboardInformation.setFont(font3)
        self.lblGeneralDashboardInformation.setStyleSheet(u"color: #6c6e71;")
        self.lblGeneralDashboardInformation.setAlignment(Qt.AlignCenter)
        self.btnAppInfo = QPushButton(self.pageDashboard)
        self.btnAppInfo.setObjectName(u"btnAppInfo")
        self.btnAppInfo.setGeometry(QRect(1040, 20, 40, 40))
        self.btnAppInfo.setFont(font1)
        self.btnAppInfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAppInfo.setStyleSheet(u"QPushButton{\n"
"   background-color: #EE4540;\n"
"   background-image: url(:/images/Resources/app_info_button.png);\n"
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
        self.btnAppInfo.setAutoDefault(True)
        self.btnAppInfo.setFlat(True)
        self.stackedWidget.addWidget(self.pageDashboard)
        self.pageCalendar = QWidget()
        self.pageCalendar.setObjectName(u"pageCalendar")
        self.lblCalendarTitle = QLabel(self.pageCalendar)
        self.lblCalendarTitle.setObjectName(u"lblCalendarTitle")
        self.lblCalendarTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblCalendarTitle.setFont(font5)
        self.lblCalendarTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblCalendarTitle.setTextFormat(Qt.MarkdownText)
        self.calendarFrame = QFrame(self.pageCalendar)
        self.calendarFrame.setObjectName(u"calendarFrame")
        self.calendarFrame.setGeometry(QRect(20, 70, 1061, 691))
        self.calendarFrame.setFrameShape(QFrame.StyledPanel)
        self.calendarFrame.setFrameShadow(QFrame.Raised)
        self.calendarWidget = QCalendarWidget(self.calendarFrame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(0, 0, 1061, 691))
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"height: 50 px;\n"
"color: #C72C41;\n"
"font-size: 20px;\n"
"font-family: \"SF UI Display\";\n"
"icon-size: 30px,30px;\n"
"selection-background-color: #C72C41;\n"
"selection-color: #C72C41;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"   alternate-background-color: #272b2f;\n"
"   font-size:20px;\n"
"   font-family: \"SF UI Display\";\n"
"   selection-background-color: #C72C41;\n"
"   selection-color: #f3f5f6;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"   font-size: 20px;\n"
"   font-family: \"SF UI Display\";\n"
"   color: #f3f5f6;\n"
"   selection-color: #f3f5f6;\n"
"   selection-background-color: #C72C41;\n"
"}\n"
"\n"
" QCalendarWidget QSpinBox {\n"
"   color:#b6b7b7;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"   font-size:20px;\n"
"   font-family: \"SF UI Display\";\n"
"   background-color: #202528;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button {\n"
"   subcontrol-origin: border;  subcontrol-position: top right;  width:65px;\n"
"}\n"
"QCal"
                        "endarWidget QSpinBox::down-button {\n"
"   subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;\n"
"}\n"
"QCalendarWidget QSpinBox::up-arrow {\n"
"   width:30px;  height:30px;\n"
"}\n"
"QCalendarWidget QSpinBox::down-arrow {\n"
"   width:30px;  height:30px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth\n"
"{\n"
"  qproperty-icon: url(:/images/Resources/prev_month.png);\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth\n"
"{\n"
"   qproperty-icon: url(:/images/Resources/next_month.png);\n"
"}\n"
"")
        self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QCalendarWidget.NoSelection)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarLegendFrame = QFrame(self.pageCalendar)
        self.calendarLegendFrame.setObjectName(u"calendarLegendFrame")
        self.calendarLegendFrame.setGeometry(QRect(20, 780, 1071, 91))
        self.calendarLegendFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.calendarLegendFrame.setFrameShape(QFrame.StyledPanel)
        self.calendarLegendFrame.setFrameShadow(QFrame.Raised)
        self.electricityLegendIssueColor = QPushButton(self.calendarLegendFrame)
        self.electricityLegendIssueColor.setObjectName(u"electricityLegendIssueColor")
        self.electricityLegendIssueColor.setEnabled(False)
        self.electricityLegendIssueColor.setGeometry(QRect(10, 10, 330, 31))
        self.electricityLegendIssueColor.setCursor(QCursor(Qt.PointingHandCursor))
        self.electricityLegendIssueColor.setFocusPolicy(Qt.StrongFocus)
        self.electricityLegendIssueColor.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.electricityLegendIssueColor.setStyleSheet(u"background-color: #a2ded0;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"font-size: 15px;\n"
"font-family: \"SF UI Display\";\n"
"color: #202528;")
        self.electricityLegendIssueColor.setCheckable(True)
        self.electricityLegendIssueColor.setChecked(False)
        self.electricityLegendIssueColor.setAutoDefault(True)
        self.electricityLegendIssueColor.setFlat(True)
        self.electricityLegendDueColor = QPushButton(self.calendarLegendFrame)
        self.electricityLegendDueColor.setObjectName(u"electricityLegendDueColor")
        self.electricityLegendDueColor.setEnabled(False)
        self.electricityLegendDueColor.setGeometry(QRect(10, 50, 330, 31))
        self.electricityLegendDueColor.setCursor(QCursor(Qt.PointingHandCursor))
        self.electricityLegendDueColor.setFocusPolicy(Qt.StrongFocus)
        self.electricityLegendDueColor.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.electricityLegendDueColor.setStyleSheet(u"background-color: #00b16a;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"font-size: 15px;\n"
"font-family: \"SF UI Display\";\n"
"color: #202528;")
        self.electricityLegendDueColor.setCheckable(True)
        self.electricityLegendDueColor.setChecked(False)
        self.electricityLegendDueColor.setAutoDefault(True)
        self.electricityLegendDueColor.setFlat(True)
        self.naturalGasLegendIssueColor = QPushButton(self.calendarLegendFrame)
        self.naturalGasLegendIssueColor.setObjectName(u"naturalGasLegendIssueColor")
        self.naturalGasLegendIssueColor.setEnabled(False)
        self.naturalGasLegendIssueColor.setGeometry(QRect(370, 10, 330, 31))
        self.naturalGasLegendIssueColor.setCursor(QCursor(Qt.PointingHandCursor))
        self.naturalGasLegendIssueColor.setFocusPolicy(Qt.StrongFocus)
        self.naturalGasLegendIssueColor.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.naturalGasLegendIssueColor.setStyleSheet(u"background-color: #6bb9f0;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"font-size: 15px;\n"
"font-family: \"SF UI Display\";\n"
"color: #202528;")
        self.naturalGasLegendIssueColor.setCheckable(True)
        self.naturalGasLegendIssueColor.setChecked(False)
        self.naturalGasLegendIssueColor.setAutoDefault(True)
        self.naturalGasLegendIssueColor.setFlat(True)
        self.naturalGasLegendDueColor = QPushButton(self.calendarLegendFrame)
        self.naturalGasLegendDueColor.setObjectName(u"naturalGasLegendDueColor")
        self.naturalGasLegendDueColor.setEnabled(False)
        self.naturalGasLegendDueColor.setGeometry(QRect(370, 50, 330, 31))
        self.naturalGasLegendDueColor.setCursor(QCursor(Qt.PointingHandCursor))
        self.naturalGasLegendDueColor.setFocusPolicy(Qt.StrongFocus)
        self.naturalGasLegendDueColor.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.naturalGasLegendDueColor.setStyleSheet(u"background-color: #5333ed;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"font-size: 15px;\n"
"font-family: \"SF UI Display\";\n"
"color: #202528;")
        self.naturalGasLegendDueColor.setCheckable(True)
        self.naturalGasLegendDueColor.setChecked(False)
        self.naturalGasLegendDueColor.setAutoDefault(True)
        self.naturalGasLegendDueColor.setFlat(True)
        self.internetTVLegendIssueColor = QPushButton(self.calendarLegendFrame)
        self.internetTVLegendIssueColor.setObjectName(u"internetTVLegendIssueColor")
        self.internetTVLegendIssueColor.setEnabled(False)
        self.internetTVLegendIssueColor.setGeometry(QRect(730, 10, 330, 31))
        self.internetTVLegendIssueColor.setCursor(QCursor(Qt.PointingHandCursor))
        self.internetTVLegendIssueColor.setFocusPolicy(Qt.StrongFocus)
        self.internetTVLegendIssueColor.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.internetTVLegendIssueColor.setStyleSheet(u"background-color: #f1a9a0;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"font-size: 15px;\n"
"font-family: \"SF UI Display\";\n"
"color: #202528;")
        self.internetTVLegendIssueColor.setCheckable(True)
        self.internetTVLegendIssueColor.setChecked(False)
        self.internetTVLegendIssueColor.setAutoDefault(True)
        self.internetTVLegendIssueColor.setFlat(True)
        self.internetTVLegendDueColor = QPushButton(self.calendarLegendFrame)
        self.internetTVLegendDueColor.setObjectName(u"internetTVLegendDueColor")
        self.internetTVLegendDueColor.setEnabled(False)
        self.internetTVLegendDueColor.setGeometry(QRect(730, 50, 330, 31))
        self.internetTVLegendDueColor.setCursor(QCursor(Qt.PointingHandCursor))
        self.internetTVLegendDueColor.setFocusPolicy(Qt.StrongFocus)
        self.internetTVLegendDueColor.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.internetTVLegendDueColor.setStyleSheet(u"background-color: #ec644b;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"font-size: 15px;\n"
"font-family: \"SF UI Display\";\n"
"color: #202528;")
        self.internetTVLegendDueColor.setCheckable(True)
        self.internetTVLegendDueColor.setChecked(False)
        self.internetTVLegendDueColor.setAutoDefault(True)
        self.internetTVLegendDueColor.setFlat(True)
        self.generalCalendarInformationFrame = QFrame(self.pageCalendar)
        self.generalCalendarInformationFrame.setObjectName(u"generalCalendarInformationFrame")
        self.generalCalendarInformationFrame.setGeometry(QRect(20, 890, 1061, 21))
        self.generalCalendarInformationFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.generalCalendarInformationFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 5px; \n"
"   background-color: #2a2e32;\n"
"}")
        self.generalCalendarInformationFrame.setFrameShape(QFrame.NoFrame)
        self.generalCalendarInformationFrame.setFrameShadow(QFrame.Raised)
        self.lblGeneralCalendarInformation = QLabel(self.generalCalendarInformationFrame)
        self.lblGeneralCalendarInformation.setObjectName(u"lblGeneralCalendarInformation")
        self.lblGeneralCalendarInformation.setGeometry(QRect(10, 3, 1041, 16))
        self.lblGeneralCalendarInformation.setFont(font3)
        self.lblGeneralCalendarInformation.setStyleSheet(u"color: #6c6e71;")
        self.lblGeneralCalendarInformation.setAlignment(Qt.AlignCenter)
        self.lblCurrentDayColor = QLabel(self.generalCalendarInformationFrame)
        self.lblCurrentDayColor.setObjectName(u"lblCurrentDayColor")
        self.lblCurrentDayColor.setGeometry(QRect(925, 3, 15, 15))
        self.lblCurrentDayColor.setStyleSheet(u"background-color: rgb(199, 44, 65);\n"
"border-radius: none;")
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
        self.electricitySupplierSelection.setGeometry(QRect(20, 70, 381, 71))
        self.electricitySupplierSelection.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.electricitySupplierSelection.setFrameShape(QFrame.StyledPanel)
        self.electricitySupplierSelection.setFrameShadow(QFrame.Raised)
        self.lblElectricitySupplierSelection = QLabel(self.electricitySupplierSelection)
        self.lblElectricitySupplierSelection.setObjectName(u"lblElectricitySupplierSelection")
        self.lblElectricitySupplierSelection.setGeometry(QRect(20, 10, 181, 21))
        self.lblElectricitySupplierSelection.setFont(font7)
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
        self.btnElectricitySupplierDisplay.setCursor(QCursor(Qt.ArrowCursor))
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
        self.electricityDirectoryFrame = QFrame(self.pageElectricity)
        self.electricityDirectoryFrame.setObjectName(u"electricityDirectoryFrame")
        self.electricityDirectoryFrame.setGeometry(QRect(20, 160, 601, 381))
        self.electricityDirectoryFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.electricityDirectoryFrame.setFrameShape(QFrame.StyledPanel)
        self.electricityDirectoryFrame.setFrameShadow(QFrame.Raised)
        self.lblElectricityDirectoryInfo = QLabel(self.electricityDirectoryFrame)
        self.lblElectricityDirectoryInfo.setObjectName(u"lblElectricityDirectoryInfo")
        self.lblElectricityDirectoryInfo.setGeometry(QRect(20, 40, 231, 16))
        self.lblElectricityDirectoryInfo.setFont(font3)
        self.lblElectricityDirectoryInfo.setStyleSheet(u"color: #6c6e71;")
        self.treeElectricityDirectory = QTreeView(self.electricityDirectoryFrame)
        self.treeElectricityDirectory.setObjectName(u"treeElectricityDirectory")
        self.treeElectricityDirectory.setGeometry(QRect(10, 81, 581, 224))
        self.treeElectricityDirectory.setMaximumSize(QSize(16777215, 300))
        self.treeElectricityDirectory.setFont(font3)
        self.treeElectricityDirectory.setStyleSheet(u"QTreeView {\n"
"    background: #2a2e32;\n"
"   color: #f3f5f6;\n"
"}\n"
"QTreeView::item:open {\n"
"   background-color: #EE4540;\n"
"    color: #f3f5f6;\n"
"}\n"
"QTreeView::item:hover {\n"
"   background-color: #6c6e71;\n"
"}\n"
"QTreeView::item:selected {\n"
"   background-color: #C72C41;\n"
"    color: #f3f5f6;\n"
"}\n"
"QTreeView::branch:open {\n"
"   image: url(:/images/Resources/branch-open.png);\n"
"}\n"
"QTreeView::branch:closed:has-children {    \n"
"   image: url(:/images/Resources/branch-closed.png);\n"
"}\n"
"QTreeView::branch:hover {\n"
"   background-color: #6c6e71;\n"
"}\n"
"QHeaderView::section {\n"
"   font-family: \"SF UI Display\";\n"
"   font-size: 10pt;\n"
"    background-color: #2a2e32;\n"
"    color: #f3f5f6;\n"
"}\n"
"")
        self.treeElectricityDirectory.setSortingEnabled(True)
        self.addElectricityBillFrame = QFrame(self.electricityDirectoryFrame)
        self.addElectricityBillFrame.setObjectName(u"addElectricityBillFrame")
        self.addElectricityBillFrame.setGeometry(QRect(10, 320, 591, 60))
        self.addElectricityBillFrame.setMaximumSize(QSize(16777215, 60))
        self.addElectricityBillFrame.setStyleSheet(u"")
        self.addElectricityBillFrame.setFrameShape(QFrame.StyledPanel)
        self.addElectricityBillFrame.setFrameShadow(QFrame.Raised)
        self.btnAddElectricityBill = QPushButton(self.addElectricityBillFrame)
        self.btnAddElectricityBill.setObjectName(u"btnAddElectricityBill")
        self.btnAddElectricityBill.setGeometry(QRect(510, 0, 75, 50))
        self.btnAddElectricityBill.setFont(font1)
        self.btnAddElectricityBill.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddElectricityBill.setStyleSheet(u"QPushButton{\n"
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
        self.btnAddElectricityBill.setAutoDefault(True)
        self.btnAddElectricityBill.setFlat(True)
        self.lblElectricityDirectory = QLabel(self.electricityDirectoryFrame)
        self.lblElectricityDirectory.setObjectName(u"lblElectricityDirectory")
        self.lblElectricityDirectory.setGeometry(QRect(20, 10, 132, 23))
        self.lblElectricityDirectory.setMaximumSize(QSize(200, 16777215))
        self.lblElectricityDirectory.setFont(font7)
        self.lblElectricityDirectory.setStyleSheet(u"color: #f3f5f6;")
        self.btnInformationElectricity = QPushButton(self.electricityDirectoryFrame)
        self.btnInformationElectricity.setObjectName(u"btnInformationElectricity")
        self.btnInformationElectricity.setGeometry(QRect(165, 10, 25, 25))
        self.btnInformationElectricity.setFont(font1)
        self.btnInformationElectricity.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnInformationElectricity.setStyleSheet(u"QPushButton{\n"
"   background-color: #EE4540;\n"
"   background-image: url(:/images/Resources/info_button.png);\n"
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
        self.btnInformationElectricity.setAutoDefault(True)
        self.btnInformationElectricity.setFlat(True)
        self.electricityLastBillData = QFrame(self.pageElectricity)
        self.electricityLastBillData.setObjectName(u"electricityLastBillData")
        self.electricityLastBillData.setGeometry(QRect(640, 160, 441, 281))
        self.electricityLastBillData.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.electricityLastBillData.setFrameShape(QFrame.StyledPanel)
        self.electricityLastBillData.setFrameShadow(QFrame.Raised)
        self.lblElectricityLastBilltipID = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBilltipID.setObjectName(u"lblElectricityLastBilltipID")
        self.lblElectricityLastBilltipID.setGeometry(QRect(20, 70, 166, 16))
        self.lblElectricityLastBilltipID.setFont(font3)
        self.lblElectricityLastBilltipID.setStyleSheet(u"color: #6c6e71;")
        self.lblElectricityLastBillI = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillI.setObjectName(u"lblElectricityLastBillI")
        self.lblElectricityLastBillI.setGeometry(QRect(20, 10, 291, 23))
        self.lblElectricityLastBillI.setMaximumSize(QSize(500, 16777215))
        self.lblElectricityLastBillI.setFont(font7)
        self.lblElectricityLastBillI.setStyleSheet(u"color: #f3f5f6;")
        self.lblElectricityLastBillID = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillID.setObjectName(u"lblElectricityLastBillID")
        self.lblElectricityLastBillID.setGeometry(QRect(20, 40, 391, 31))
        font8 = QFont()
        font8.setFamily(u"SF UI Display")
        font8.setPointSize(20)
        self.lblElectricityLastBillID.setFont(font8)
        self.lblElectricityLastBillID.setStyleSheet(u"color: #EE4540;")
        self.lblElectricityLastBillAddress = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillAddress.setObjectName(u"lblElectricityLastBillAddress")
        self.lblElectricityLastBillAddress.setGeometry(QRect(20, 90, 401, 41))
        self.lblElectricityLastBillAddress.setFont(font6)
        self.lblElectricityLastBillAddress.setStyleSheet(u"color: #EE4540;")
        self.lblElectricityLastBilltipAddress = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBilltipAddress.setObjectName(u"lblElectricityLastBilltipAddress")
        self.lblElectricityLastBilltipAddress.setGeometry(QRect(20, 130, 166, 16))
        self.lblElectricityLastBilltipAddress.setFont(font3)
        self.lblElectricityLastBilltipAddress.setStyleSheet(u"color: #6c6e71;")
        self.lblElectricityLastBillIssueDate = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillIssueDate.setObjectName(u"lblElectricityLastBillIssueDate")
        self.lblElectricityLastBillIssueDate.setGeometry(QRect(20, 160, 301, 31))
        self.lblElectricityLastBillIssueDate.setFont(font8)
        self.lblElectricityLastBillIssueDate.setStyleSheet(u"color: #EE4540;")
        self.lblElectricityLastBilltipIssueDate = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBilltipIssueDate.setObjectName(u"lblElectricityLastBilltipIssueDate")
        self.lblElectricityLastBilltipIssueDate.setGeometry(QRect(20, 190, 166, 16))
        self.lblElectricityLastBilltipIssueDate.setFont(font3)
        self.lblElectricityLastBilltipIssueDate.setStyleSheet(u"color: #6c6e71;")
        self.lblElectricityLastBillDueDate = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillDueDate.setObjectName(u"lblElectricityLastBillDueDate")
        self.lblElectricityLastBillDueDate.setGeometry(QRect(20, 220, 301, 31))
        self.lblElectricityLastBillDueDate.setFont(font8)
        self.lblElectricityLastBillDueDate.setStyleSheet(u"color: #EE4540;")
        self.lblElectricityLastBilltipDueDate = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBilltipDueDate.setObjectName(u"lblElectricityLastBilltipDueDate")
        self.lblElectricityLastBilltipDueDate.setGeometry(QRect(20, 250, 166, 16))
        self.lblElectricityLastBilltipDueDate.setFont(font3)
        self.lblElectricityLastBilltipDueDate.setStyleSheet(u"color: #6c6e71;")
        self.lblElectricityLastBillI.raise_()
        self.lblElectricityLastBillID.raise_()
        self.lblElectricityLastBillAddress.raise_()
        self.lblElectricityLastBilltipAddress.raise_()
        self.lblElectricityLastBillIssueDate.raise_()
        self.lblElectricityLastBilltipIssueDate.raise_()
        self.lblElectricityLastBillDueDate.raise_()
        self.lblElectricityLastBilltipDueDate.raise_()
        self.lblElectricityLastBilltipID.raise_()
        self.electricityLastBillTotalPay = QFrame(self.pageElectricity)
        self.electricityLastBillTotalPay.setObjectName(u"electricityLastBillTotalPay")
        self.electricityLastBillTotalPay.setGeometry(QRect(640, 460, 441, 81))
        self.electricityLastBillTotalPay.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #C72C41;;\n"
"}")
        self.electricityLastBillTotalPay.setFrameShape(QFrame.StyledPanel)
        self.electricityLastBillTotalPay.setFrameShadow(QFrame.Raised)
        self.lblElectricityLastBillTotalPayInfo = QLabel(self.electricityLastBillTotalPay)
        self.lblElectricityLastBillTotalPayInfo.setObjectName(u"lblElectricityLastBillTotalPayInfo")
        self.lblElectricityLastBillTotalPayInfo.setGeometry(QRect(20, 10, 331, 23))
        self.lblElectricityLastBillTotalPayInfo.setMaximumSize(QSize(500, 16777215))
        self.lblElectricityLastBillTotalPayInfo.setFont(font7)
        self.lblElectricityLastBillTotalPayInfo.setStyleSheet(u"color: #f3f5f6;")
        self.lblElectricityLastBillTotalPay = QLabel(self.electricityLastBillTotalPay)
        self.lblElectricityLastBillTotalPay.setObjectName(u"lblElectricityLastBillTotalPay")
        self.lblElectricityLastBillTotalPay.setGeometry(QRect(90, 40, 191, 31))
        self.lblElectricityLastBillTotalPay.setFont(font8)
        self.lblElectricityLastBillTotalPay.setStyleSheet(u"color: #f3f5f6;")
        self.lblElectricityBillCurrency = QLabel(self.electricityLastBillTotalPay)
        self.lblElectricityBillCurrency.setObjectName(u"lblElectricityBillCurrency")
        self.lblElectricityBillCurrency.setGeometry(QRect(20, 40, 61, 31))
        font9 = QFont()
        font9.setFamily(u"SF UI Display")
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setWeight(75)
        self.lblElectricityBillCurrency.setFont(font9)
        self.lblElectricityBillCurrency.setStyleSheet(u"color: #2a2e32;")
        self.electricityLastBill = QFrame(self.pageElectricity)
        self.electricityLastBill.setObjectName(u"electricityLastBill")
        self.electricityLastBill.setGeometry(QRect(20, 560, 391, 311))
        self.electricityLastBill.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.electricityLastBill.setFrameShape(QFrame.StyledPanel)
        self.electricityLastBill.setFrameShadow(QFrame.Raised)
        self.lblElectricityLastBillPlotTitle = QLabel(self.electricityLastBill)
        self.lblElectricityLastBillPlotTitle.setObjectName(u"lblElectricityLastBillPlotTitle")
        self.lblElectricityLastBillPlotTitle.setGeometry(QRect(20, 10, 341, 23))
        self.lblElectricityLastBillPlotTitle.setMaximumSize(QSize(500, 16777215))
        self.lblElectricityLastBillPlotTitle.setFont(font7)
        self.lblElectricityLastBillPlotTitle.setStyleSheet(u"color: #f3f5f6;")
        self.donutElectricityLastBill = QWidget(self.electricityLastBill)
        self.donutElectricityLastBill.setObjectName(u"donutElectricityLastBill")
        self.donutElectricityLastBill.setGeometry(QRect(0, 40, 391, 261))
        self.donutElectricityLastBill.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.electricityBillsCosts = QFrame(self.pageElectricity)
        self.electricityBillsCosts.setObjectName(u"electricityBillsCosts")
        self.electricityBillsCosts.setGeometry(QRect(430, 560, 651, 311))
        self.electricityBillsCosts.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.electricityBillsCosts.setFrameShape(QFrame.StyledPanel)
        self.electricityBillsCosts.setFrameShadow(QFrame.Raised)
        self.lblElectricityAllBillsPlot = QLabel(self.electricityBillsCosts)
        self.lblElectricityAllBillsPlot.setObjectName(u"lblElectricityAllBillsPlot")
        self.lblElectricityAllBillsPlot.setGeometry(QRect(20, 10, 181, 23))
        self.lblElectricityAllBillsPlot.setMaximumSize(QSize(500, 16777215))
        self.lblElectricityAllBillsPlot.setFont(font7)
        self.lblElectricityAllBillsPlot.setStyleSheet(u"color: #f3f5f6;")
        self.lineElectricityAllBillsPlot = QWidget(self.electricityBillsCosts)
        self.lineElectricityAllBillsPlot.setObjectName(u"lineElectricityAllBillsPlot")
        self.lineElectricityAllBillsPlot.setGeometry(QRect(0, 40, 651, 261))
        self.lineElectricityAllBillsPlot.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.comboBoxElectricityBillYear = QComboBox(self.electricityBillsCosts)
        self.comboBoxElectricityBillYear.setObjectName(u"comboBoxElectricityBillYear")
        self.comboBoxElectricityBillYear.setGeometry(QRect(210, 10, 131, 22))
        self.comboBoxElectricityBillYear.setFont(font3)
        self.comboBoxElectricityBillYear.setStyleSheet(u"QComboBox {    \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxElectricityBillYear.setEditable(False)
        self.generalElectricityInformationFrame = QFrame(self.pageElectricity)
        self.generalElectricityInformationFrame.setObjectName(u"generalElectricityInformationFrame")
        self.generalElectricityInformationFrame.setGeometry(QRect(20, 890, 1061, 21))
        self.generalElectricityInformationFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.generalElectricityInformationFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 5px; \n"
"   background-color: #2a2e32;\n"
"}")
        self.generalElectricityInformationFrame.setFrameShape(QFrame.NoFrame)
        self.generalElectricityInformationFrame.setFrameShadow(QFrame.Raised)
        self.lblGeneralElectricityInformation = QLabel(self.generalElectricityInformationFrame)
        self.lblGeneralElectricityInformation.setObjectName(u"lblGeneralElectricityInformation")
        self.lblGeneralElectricityInformation.setGeometry(QRect(10, 3, 1041, 16))
        self.lblGeneralElectricityInformation.setFont(font3)
        self.lblGeneralElectricityInformation.setStyleSheet(u"color: #6c6e71;")
        self.lblGeneralElectricityInformation.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.pageElectricity)
        self.pageNaturalGas = QWidget()
        self.pageNaturalGas.setObjectName(u"pageNaturalGas")
        self.lblNaturalGasTitle = QLabel(self.pageNaturalGas)
        self.lblNaturalGasTitle.setObjectName(u"lblNaturalGasTitle")
        self.lblNaturalGasTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblNaturalGasTitle.setFont(font5)
        self.lblNaturalGasTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblNaturalGasTitle.setTextFormat(Qt.MarkdownText)
        self.naturalGasSupplierSelection = QFrame(self.pageNaturalGas)
        self.naturalGasSupplierSelection.setObjectName(u"naturalGasSupplierSelection")
        self.naturalGasSupplierSelection.setGeometry(QRect(20, 70, 391, 71))
        self.naturalGasSupplierSelection.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.naturalGasSupplierSelection.setFrameShape(QFrame.StyledPanel)
        self.naturalGasSupplierSelection.setFrameShadow(QFrame.Raised)
        self.lblNaturalGasSupplierSelection = QLabel(self.naturalGasSupplierSelection)
        self.lblNaturalGasSupplierSelection.setObjectName(u"lblNaturalGasSupplierSelection")
        self.lblNaturalGasSupplierSelection.setGeometry(QRect(20, 10, 191, 21))
        self.lblNaturalGasSupplierSelection.setFont(font7)
        self.lblNaturalGasSupplierSelection.setStyleSheet(u"color: #f3f5f6;")
        self.lblNaturalGasSupplierSelectionInfo = QLabel(self.naturalGasSupplierSelection)
        self.lblNaturalGasSupplierSelectionInfo.setObjectName(u"lblNaturalGasSupplierSelectionInfo")
        self.lblNaturalGasSupplierSelectionInfo.setGeometry(QRect(20, 40, 231, 21))
        self.lblNaturalGasSupplierSelectionInfo.setFont(font3)
        self.lblNaturalGasSupplierSelectionInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnNaturalGasSupplierDisplay = QPushButton(self.naturalGasSupplierSelection)
        self.btnNaturalGasSupplierDisplay.setObjectName(u"btnNaturalGasSupplierDisplay")
        self.btnNaturalGasSupplierDisplay.setEnabled(False)
        self.btnNaturalGasSupplierDisplay.setGeometry(QRect(220, 10, 151, 50))
        self.btnNaturalGasSupplierDisplay.setCursor(QCursor(Qt.ArrowCursor))
        self.btnNaturalGasSupplierDisplay.setFocusPolicy(Qt.StrongFocus)
        self.btnNaturalGasSupplierDisplay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnNaturalGasSupplierDisplay.setStyleSheet(u"background-color: #202528;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;")
        self.btnNaturalGasSupplierDisplay.setCheckable(True)
        self.btnNaturalGasSupplierDisplay.setChecked(False)
        self.btnNaturalGasSupplierDisplay.setAutoDefault(True)
        self.btnNaturalGasSupplierDisplay.setFlat(True)
        self.naturalGasDirectoryFrame = QFrame(self.pageNaturalGas)
        self.naturalGasDirectoryFrame.setObjectName(u"naturalGasDirectoryFrame")
        self.naturalGasDirectoryFrame.setGeometry(QRect(20, 160, 601, 381))
        self.naturalGasDirectoryFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.naturalGasDirectoryFrame.setFrameShape(QFrame.StyledPanel)
        self.naturalGasDirectoryFrame.setFrameShadow(QFrame.Raised)
        self.lblNaturalGasDirectoryInfo = QLabel(self.naturalGasDirectoryFrame)
        self.lblNaturalGasDirectoryInfo.setObjectName(u"lblNaturalGasDirectoryInfo")
        self.lblNaturalGasDirectoryInfo.setGeometry(QRect(20, 40, 241, 16))
        self.lblNaturalGasDirectoryInfo.setFont(font3)
        self.lblNaturalGasDirectoryInfo.setStyleSheet(u"color: #6c6e71;")
        self.treeNaturalGasDirectory = QTreeView(self.naturalGasDirectoryFrame)
        self.treeNaturalGasDirectory.setObjectName(u"treeNaturalGasDirectory")
        self.treeNaturalGasDirectory.setGeometry(QRect(10, 81, 581, 224))
        self.treeNaturalGasDirectory.setMaximumSize(QSize(16777215, 300))
        self.treeNaturalGasDirectory.setFont(font3)
        self.treeNaturalGasDirectory.setStyleSheet(u"QTreeView {\n"
"    background: #2a2e32;\n"
"   color: #f3f5f6;\n"
"}\n"
"QTreeView::item:open {\n"
"   background-color: #EE4540;\n"
"    color: #f3f5f6;\n"
"}\n"
"QTreeView::item:hover {\n"
"   background-color: #6c6e71;\n"
"}\n"
"QTreeView::item:selected {\n"
"   background-color: #C72C41;\n"
"    color: #f3f5f6;\n"
"}\n"
"QTreeView::branch:open {\n"
"   image: url(:/images/Resources/branch-open.png);\n"
"}\n"
"QTreeView::branch:closed:has-children {    \n"
"   image: url(:/images/Resources/branch-closed.png);\n"
"}\n"
"QTreeView::branch:hover {\n"
"   background-color: #6c6e71;\n"
"}\n"
"QHeaderView::section {\n"
"   font-family: \"SF UI Display\";\n"
"   font-size: 10pt;\n"
"    background-color: #2a2e32;\n"
"    color: #f3f5f6;\n"
"}\n"
"")
        self.treeNaturalGasDirectory.setSortingEnabled(True)
        self.addNaturalGasBillFrame = QFrame(self.naturalGasDirectoryFrame)
        self.addNaturalGasBillFrame.setObjectName(u"addNaturalGasBillFrame")
        self.addNaturalGasBillFrame.setGeometry(QRect(10, 320, 591, 60))
        self.addNaturalGasBillFrame.setMaximumSize(QSize(16777215, 60))
        self.addNaturalGasBillFrame.setStyleSheet(u"")
        self.addNaturalGasBillFrame.setFrameShape(QFrame.StyledPanel)
        self.addNaturalGasBillFrame.setFrameShadow(QFrame.Raised)
        self.btnAddNaturalGasBill = QPushButton(self.addNaturalGasBillFrame)
        self.btnAddNaturalGasBill.setObjectName(u"btnAddNaturalGasBill")
        self.btnAddNaturalGasBill.setGeometry(QRect(510, 0, 75, 50))
        self.btnAddNaturalGasBill.setFont(font1)
        self.btnAddNaturalGasBill.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddNaturalGasBill.setStyleSheet(u"QPushButton{\n"
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
        self.btnAddNaturalGasBill.setAutoDefault(True)
        self.btnAddNaturalGasBill.setFlat(True)
        self.lblNaturalGasDirectory = QLabel(self.naturalGasDirectoryFrame)
        self.lblNaturalGasDirectory.setObjectName(u"lblNaturalGasDirectory")
        self.lblNaturalGasDirectory.setGeometry(QRect(20, 10, 151, 23))
        self.lblNaturalGasDirectory.setMaximumSize(QSize(200, 16777215))
        self.lblNaturalGasDirectory.setFont(font7)
        self.lblNaturalGasDirectory.setStyleSheet(u"color: #f3f5f6;")
        self.btnInformationNaturalGas = QPushButton(self.naturalGasDirectoryFrame)
        self.btnInformationNaturalGas.setObjectName(u"btnInformationNaturalGas")
        self.btnInformationNaturalGas.setGeometry(QRect(180, 10, 25, 25))
        self.btnInformationNaturalGas.setFont(font1)
        self.btnInformationNaturalGas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnInformationNaturalGas.setStyleSheet(u"QPushButton{\n"
"   background-color: #EE4540;\n"
"   background-image: url(:/images/Resources/info_button.png);\n"
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
        self.btnInformationNaturalGas.setAutoDefault(True)
        self.btnInformationNaturalGas.setFlat(True)
        self.naturalGasLastBillData = QFrame(self.pageNaturalGas)
        self.naturalGasLastBillData.setObjectName(u"naturalGasLastBillData")
        self.naturalGasLastBillData.setGeometry(QRect(640, 160, 441, 281))
        self.naturalGasLastBillData.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.naturalGasLastBillData.setFrameShape(QFrame.StyledPanel)
        self.naturalGasLastBillData.setFrameShadow(QFrame.Raised)
        self.lblNaturalGasLastBilltipID = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBilltipID.setObjectName(u"lblNaturalGasLastBilltipID")
        self.lblNaturalGasLastBilltipID.setGeometry(QRect(20, 70, 166, 16))
        self.lblNaturalGasLastBilltipID.setFont(font3)
        self.lblNaturalGasLastBilltipID.setStyleSheet(u"color: #6c6e71;")
        self.lblNaturalGasLastBillI = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillI.setObjectName(u"lblNaturalGasLastBillI")
        self.lblNaturalGasLastBillI.setGeometry(QRect(20, 10, 291, 23))
        self.lblNaturalGasLastBillI.setMaximumSize(QSize(500, 16777215))
        self.lblNaturalGasLastBillI.setFont(font7)
        self.lblNaturalGasLastBillI.setStyleSheet(u"color: #f3f5f6;")
        self.lblNaturalGasLastBillID = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillID.setObjectName(u"lblNaturalGasLastBillID")
        self.lblNaturalGasLastBillID.setGeometry(QRect(20, 40, 391, 31))
        self.lblNaturalGasLastBillID.setFont(font8)
        self.lblNaturalGasLastBillID.setStyleSheet(u"color: #EE4540;")
        self.lblNaturalGasLastBillAddress = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillAddress.setObjectName(u"lblNaturalGasLastBillAddress")
        self.lblNaturalGasLastBillAddress.setGeometry(QRect(20, 100, 401, 51))
        self.lblNaturalGasLastBillAddress.setFont(font6)
        self.lblNaturalGasLastBillAddress.setStyleSheet(u"color: #EE4540;")
        self.lblNaturalGasLastBilltipAddress = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBilltipAddress.setObjectName(u"lblNaturalGasLastBilltipAddress")
        self.lblNaturalGasLastBilltipAddress.setGeometry(QRect(20, 150, 166, 16))
        self.lblNaturalGasLastBilltipAddress.setFont(font3)
        self.lblNaturalGasLastBilltipAddress.setStyleSheet(u"color: #6c6e71;")
        self.lblNaturalGasLastBillIssueDate = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillIssueDate.setObjectName(u"lblNaturalGasLastBillIssueDate")
        self.lblNaturalGasLastBillIssueDate.setGeometry(QRect(20, 170, 301, 31))
        self.lblNaturalGasLastBillIssueDate.setFont(font8)
        self.lblNaturalGasLastBillIssueDate.setStyleSheet(u"color: #EE4540;")
        self.lblNaturalGasLastBilltipIssueDate = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBilltipIssueDate.setObjectName(u"lblNaturalGasLastBilltipIssueDate")
        self.lblNaturalGasLastBilltipIssueDate.setGeometry(QRect(20, 200, 166, 16))
        self.lblNaturalGasLastBilltipIssueDate.setFont(font3)
        self.lblNaturalGasLastBilltipIssueDate.setStyleSheet(u"color: #6c6e71;")
        self.lblNaturalGasLastBillDueDate = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillDueDate.setObjectName(u"lblNaturalGasLastBillDueDate")
        self.lblNaturalGasLastBillDueDate.setGeometry(QRect(20, 230, 301, 31))
        self.lblNaturalGasLastBillDueDate.setFont(font8)
        self.lblNaturalGasLastBillDueDate.setStyleSheet(u"color: #EE4540;")
        self.lblNaturalGasLastBilltipDueDate = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBilltipDueDate.setObjectName(u"lblNaturalGasLastBilltipDueDate")
        self.lblNaturalGasLastBilltipDueDate.setGeometry(QRect(20, 260, 166, 16))
        self.lblNaturalGasLastBilltipDueDate.setFont(font3)
        self.lblNaturalGasLastBilltipDueDate.setStyleSheet(u"color: #6c6e71;")
        self.naturalGasLastBillTotalPay = QFrame(self.pageNaturalGas)
        self.naturalGasLastBillTotalPay.setObjectName(u"naturalGasLastBillTotalPay")
        self.naturalGasLastBillTotalPay.setGeometry(QRect(640, 460, 441, 81))
        self.naturalGasLastBillTotalPay.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #C72C41;;\n"
"}")
        self.naturalGasLastBillTotalPay.setFrameShape(QFrame.StyledPanel)
        self.naturalGasLastBillTotalPay.setFrameShadow(QFrame.Raised)
        self.lblNaturalGasLastBillTotalPayInfo = QLabel(self.naturalGasLastBillTotalPay)
        self.lblNaturalGasLastBillTotalPayInfo.setObjectName(u"lblNaturalGasLastBillTotalPayInfo")
        self.lblNaturalGasLastBillTotalPayInfo.setGeometry(QRect(20, 10, 331, 23))
        self.lblNaturalGasLastBillTotalPayInfo.setMaximumSize(QSize(500, 16777215))
        self.lblNaturalGasLastBillTotalPayInfo.setFont(font7)
        self.lblNaturalGasLastBillTotalPayInfo.setStyleSheet(u"color: #f3f5f6;")
        self.lblNaturalGasLastBillTotalPay = QLabel(self.naturalGasLastBillTotalPay)
        self.lblNaturalGasLastBillTotalPay.setObjectName(u"lblNaturalGasLastBillTotalPay")
        self.lblNaturalGasLastBillTotalPay.setGeometry(QRect(90, 40, 191, 31))
        self.lblNaturalGasLastBillTotalPay.setFont(font8)
        self.lblNaturalGasLastBillTotalPay.setStyleSheet(u"color: #f3f5f6;")
        self.lblNaturalGasBillCurrency = QLabel(self.naturalGasLastBillTotalPay)
        self.lblNaturalGasBillCurrency.setObjectName(u"lblNaturalGasBillCurrency")
        self.lblNaturalGasBillCurrency.setGeometry(QRect(20, 40, 61, 31))
        self.lblNaturalGasBillCurrency.setFont(font9)
        self.lblNaturalGasBillCurrency.setStyleSheet(u"color: #2a2e32;")
        self.naturalGasLastBill = QFrame(self.pageNaturalGas)
        self.naturalGasLastBill.setObjectName(u"naturalGasLastBill")
        self.naturalGasLastBill.setGeometry(QRect(20, 560, 391, 311))
        self.naturalGasLastBill.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.naturalGasLastBill.setFrameShape(QFrame.StyledPanel)
        self.naturalGasLastBill.setFrameShadow(QFrame.Raised)
        self.lblNaturalGasLastBillPlotTitle = QLabel(self.naturalGasLastBill)
        self.lblNaturalGasLastBillPlotTitle.setObjectName(u"lblNaturalGasLastBillPlotTitle")
        self.lblNaturalGasLastBillPlotTitle.setGeometry(QRect(20, 10, 341, 23))
        self.lblNaturalGasLastBillPlotTitle.setMaximumSize(QSize(500, 16777215))
        self.lblNaturalGasLastBillPlotTitle.setFont(font7)
        self.lblNaturalGasLastBillPlotTitle.setStyleSheet(u"color: #f3f5f6;")
        self.donutNaturalGasLastBill = QWidget(self.naturalGasLastBill)
        self.donutNaturalGasLastBill.setObjectName(u"donutNaturalGasLastBill")
        self.donutNaturalGasLastBill.setGeometry(QRect(0, 40, 391, 261))
        self.donutNaturalGasLastBill.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.naturalGasBillsCosts = QFrame(self.pageNaturalGas)
        self.naturalGasBillsCosts.setObjectName(u"naturalGasBillsCosts")
        self.naturalGasBillsCosts.setGeometry(QRect(430, 560, 651, 311))
        self.naturalGasBillsCosts.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.naturalGasBillsCosts.setFrameShape(QFrame.StyledPanel)
        self.naturalGasBillsCosts.setFrameShadow(QFrame.Raised)
        self.lblNaturalAllBillsPlot = QLabel(self.naturalGasBillsCosts)
        self.lblNaturalAllBillsPlot.setObjectName(u"lblNaturalAllBillsPlot")
        self.lblNaturalAllBillsPlot.setGeometry(QRect(20, 10, 181, 23))
        self.lblNaturalAllBillsPlot.setMaximumSize(QSize(500, 16777215))
        self.lblNaturalAllBillsPlot.setFont(font7)
        self.lblNaturalAllBillsPlot.setStyleSheet(u"color: #f3f5f6;")
        self.lineNaturalGasAllBillsPlot = QWidget(self.naturalGasBillsCosts)
        self.lineNaturalGasAllBillsPlot.setObjectName(u"lineNaturalGasAllBillsPlot")
        self.lineNaturalGasAllBillsPlot.setGeometry(QRect(0, 40, 651, 261))
        self.lineNaturalGasAllBillsPlot.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.comboBoxNaturalGasBillYear = QComboBox(self.naturalGasBillsCosts)
        self.comboBoxNaturalGasBillYear.setObjectName(u"comboBoxNaturalGasBillYear")
        self.comboBoxNaturalGasBillYear.setGeometry(QRect(210, 10, 131, 22))
        self.comboBoxNaturalGasBillYear.setFont(font3)
        self.comboBoxNaturalGasBillYear.setStyleSheet(u"QComboBox { \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxNaturalGasBillYear.setEditable(False)
        self.generalNaturalGasInformationFrame = QFrame(self.pageNaturalGas)
        self.generalNaturalGasInformationFrame.setObjectName(u"generalNaturalGasInformationFrame")
        self.generalNaturalGasInformationFrame.setGeometry(QRect(20, 890, 1061, 21))
        self.generalNaturalGasInformationFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.generalNaturalGasInformationFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 5px; \n"
"   background-color: #2a2e32;\n"
"}")
        self.generalNaturalGasInformationFrame.setFrameShape(QFrame.NoFrame)
        self.generalNaturalGasInformationFrame.setFrameShadow(QFrame.Raised)
        self.lblGeneralNaturalGasInformation = QLabel(self.generalNaturalGasInformationFrame)
        self.lblGeneralNaturalGasInformation.setObjectName(u"lblGeneralNaturalGasInformation")
        self.lblGeneralNaturalGasInformation.setGeometry(QRect(10, 3, 1041, 16))
        self.lblGeneralNaturalGasInformation.setFont(font3)
        self.lblGeneralNaturalGasInformation.setStyleSheet(u"color: #6c6e71;")
        self.lblGeneralNaturalGasInformation.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.pageNaturalGas)
        self.pageInternetTV = QWidget()
        self.pageInternetTV.setObjectName(u"pageInternetTV")
        self.lblInternetTVTitle = QLabel(self.pageInternetTV)
        self.lblInternetTVTitle.setObjectName(u"lblInternetTVTitle")
        self.lblInternetTVTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblInternetTVTitle.setFont(font5)
        self.lblInternetTVTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblInternetTVTitle.setTextFormat(Qt.MarkdownText)
        self.internetProviderSelection = QFrame(self.pageInternetTV)
        self.internetProviderSelection.setObjectName(u"internetProviderSelection")
        self.internetProviderSelection.setGeometry(QRect(20, 70, 401, 71))
        self.internetProviderSelection.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.internetProviderSelection.setFrameShape(QFrame.StyledPanel)
        self.internetProviderSelection.setFrameShadow(QFrame.Raised)
        self.lblInternetProviderSelection = QLabel(self.internetProviderSelection)
        self.lblInternetProviderSelection.setObjectName(u"lblInternetProviderSelection")
        self.lblInternetProviderSelection.setGeometry(QRect(20, 10, 201, 21))
        self.lblInternetProviderSelection.setFont(font7)
        self.lblInternetProviderSelection.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetProviderSelectionInfo = QLabel(self.internetProviderSelection)
        self.lblInternetProviderSelectionInfo.setObjectName(u"lblInternetProviderSelectionInfo")
        self.lblInternetProviderSelectionInfo.setGeometry(QRect(20, 40, 231, 21))
        self.lblInternetProviderSelectionInfo.setFont(font3)
        self.lblInternetProviderSelectionInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnInternetProviderDisplay = QPushButton(self.internetProviderSelection)
        self.btnInternetProviderDisplay.setObjectName(u"btnInternetProviderDisplay")
        self.btnInternetProviderDisplay.setEnabled(False)
        self.btnInternetProviderDisplay.setGeometry(QRect(230, 10, 151, 50))
        self.btnInternetProviderDisplay.setCursor(QCursor(Qt.ArrowCursor))
        self.btnInternetProviderDisplay.setFocusPolicy(Qt.StrongFocus)
        self.btnInternetProviderDisplay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnInternetProviderDisplay.setStyleSheet(u"background-color: #202528;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;")
        self.btnInternetProviderDisplay.setCheckable(True)
        self.btnInternetProviderDisplay.setChecked(False)
        self.btnInternetProviderDisplay.setAutoDefault(True)
        self.btnInternetProviderDisplay.setFlat(True)
        self.internetTVDirectoryFrame = QFrame(self.pageInternetTV)
        self.internetTVDirectoryFrame.setObjectName(u"internetTVDirectoryFrame")
        self.internetTVDirectoryFrame.setGeometry(QRect(20, 160, 601, 381))
        self.internetTVDirectoryFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.internetTVDirectoryFrame.setFrameShape(QFrame.StyledPanel)
        self.internetTVDirectoryFrame.setFrameShadow(QFrame.Raised)
        self.lblInternetTVDirectoryInfo = QLabel(self.internetTVDirectoryFrame)
        self.lblInternetTVDirectoryInfo.setObjectName(u"lblInternetTVDirectoryInfo")
        self.lblInternetTVDirectoryInfo.setGeometry(QRect(20, 40, 251, 16))
        self.lblInternetTVDirectoryInfo.setFont(font3)
        self.lblInternetTVDirectoryInfo.setStyleSheet(u"color: #6c6e71;")
        self.treeInternetTVDirectory = QTreeView(self.internetTVDirectoryFrame)
        self.treeInternetTVDirectory.setObjectName(u"treeInternetTVDirectory")
        self.treeInternetTVDirectory.setGeometry(QRect(10, 81, 581, 224))
        self.treeInternetTVDirectory.setMaximumSize(QSize(16777215, 300))
        self.treeInternetTVDirectory.setFont(font3)
        self.treeInternetTVDirectory.setStyleSheet(u"QTreeView {\n"
"    background: #2a2e32;\n"
"   color: #f3f5f6;\n"
"}\n"
"QTreeView::item:open {\n"
"   background-color: #EE4540;\n"
"    color: #f3f5f6;\n"
"}\n"
"QTreeView::item:hover {\n"
"   background-color: #6c6e71;\n"
"}\n"
"QTreeView::item:selected {\n"
"   background-color: #C72C41;\n"
"    color: #f3f5f6;\n"
"}\n"
"QTreeView::branch:open {\n"
"   image: url(:/images/Resources/branch-open.png);\n"
"}\n"
"QTreeView::branch:closed:has-children {    \n"
"   image: url(:/images/Resources/branch-closed.png);\n"
"}\n"
"QTreeView::branch:hover {\n"
"   background-color: #6c6e71;\n"
"}\n"
"QHeaderView::section {\n"
"   font-family: \"SF UI Display\";\n"
"   font-size: 10pt;\n"
"    background-color: #2a2e32;\n"
"    color: #f3f5f6;\n"
"}\n"
"")
        self.treeInternetTVDirectory.setSortingEnabled(True)
        self.addInternetTVBillFrame = QFrame(self.internetTVDirectoryFrame)
        self.addInternetTVBillFrame.setObjectName(u"addInternetTVBillFrame")
        self.addInternetTVBillFrame.setGeometry(QRect(10, 320, 591, 60))
        self.addInternetTVBillFrame.setMaximumSize(QSize(16777215, 60))
        self.addInternetTVBillFrame.setStyleSheet(u"")
        self.addInternetTVBillFrame.setFrameShape(QFrame.StyledPanel)
        self.addInternetTVBillFrame.setFrameShadow(QFrame.Raised)
        self.btnAddInternetTVBill = QPushButton(self.addInternetTVBillFrame)
        self.btnAddInternetTVBill.setObjectName(u"btnAddInternetTVBill")
        self.btnAddInternetTVBill.setGeometry(QRect(510, 0, 75, 50))
        self.btnAddInternetTVBill.setFont(font1)
        self.btnAddInternetTVBill.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddInternetTVBill.setStyleSheet(u"QPushButton{\n"
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
        self.btnAddInternetTVBill.setAutoDefault(True)
        self.btnAddInternetTVBill.setFlat(True)
        self.lblInternetTVDirectory = QLabel(self.internetTVDirectoryFrame)
        self.lblInternetTVDirectory.setObjectName(u"lblInternetTVDirectory")
        self.lblInternetTVDirectory.setGeometry(QRect(20, 10, 161, 23))
        self.lblInternetTVDirectory.setMaximumSize(QSize(200, 16777215))
        self.lblInternetTVDirectory.setFont(font7)
        self.lblInternetTVDirectory.setStyleSheet(u"color: #f3f5f6;")
        self.btnInformationInternetTV = QPushButton(self.internetTVDirectoryFrame)
        self.btnInformationInternetTV.setObjectName(u"btnInformationInternetTV")
        self.btnInformationInternetTV.setGeometry(QRect(190, 10, 25, 25))
        self.btnInformationInternetTV.setFont(font1)
        self.btnInformationInternetTV.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnInformationInternetTV.setStyleSheet(u"QPushButton{\n"
"   background-color: #EE4540;\n"
"   background-image: url(:/images/Resources/info_button.png);\n"
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
        self.btnInformationInternetTV.setAutoDefault(True)
        self.btnInformationInternetTV.setFlat(True)
        self.internetTVLastBillData = QFrame(self.pageInternetTV)
        self.internetTVLastBillData.setObjectName(u"internetTVLastBillData")
        self.internetTVLastBillData.setGeometry(QRect(640, 160, 441, 281))
        self.internetTVLastBillData.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.internetTVLastBillData.setFrameShape(QFrame.StyledPanel)
        self.internetTVLastBillData.setFrameShadow(QFrame.Raised)
        self.lblInternetTVLastBilltipID = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBilltipID.setObjectName(u"lblInternetTVLastBilltipID")
        self.lblInternetTVLastBilltipID.setGeometry(QRect(20, 70, 166, 16))
        self.lblInternetTVLastBilltipID.setFont(font3)
        self.lblInternetTVLastBilltipID.setStyleSheet(u"color: #6c6e71;")
        self.lblInternetTVLastBillI = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillI.setObjectName(u"lblInternetTVLastBillI")
        self.lblInternetTVLastBillI.setGeometry(QRect(20, 10, 291, 23))
        self.lblInternetTVLastBillI.setMaximumSize(QSize(500, 16777215))
        self.lblInternetTVLastBillI.setFont(font7)
        self.lblInternetTVLastBillI.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetTVLastBillID = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillID.setObjectName(u"lblInternetTVLastBillID")
        self.lblInternetTVLastBillID.setGeometry(QRect(20, 40, 391, 31))
        self.lblInternetTVLastBillID.setFont(font8)
        self.lblInternetTVLastBillID.setStyleSheet(u"color: #EE4540;")
        self.lblInternetTVLastBillAddress = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillAddress.setObjectName(u"lblInternetTVLastBillAddress")
        self.lblInternetTVLastBillAddress.setGeometry(QRect(20, 100, 401, 51))
        self.lblInternetTVLastBillAddress.setFont(font6)
        self.lblInternetTVLastBillAddress.setStyleSheet(u"color: #EE4540;")
        self.lblInternetTVLastBilltipAddress = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBilltipAddress.setObjectName(u"lblInternetTVLastBilltipAddress")
        self.lblInternetTVLastBilltipAddress.setGeometry(QRect(20, 140, 166, 16))
        self.lblInternetTVLastBilltipAddress.setFont(font3)
        self.lblInternetTVLastBilltipAddress.setStyleSheet(u"color: #6c6e71;")
        self.lblInternetTVLastBillIssueDate = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillIssueDate.setObjectName(u"lblInternetTVLastBillIssueDate")
        self.lblInternetTVLastBillIssueDate.setGeometry(QRect(20, 170, 301, 31))
        self.lblInternetTVLastBillIssueDate.setFont(font8)
        self.lblInternetTVLastBillIssueDate.setStyleSheet(u"color: #EE4540;")
        self.lblInternetTVLastBilltipIssueDate = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBilltipIssueDate.setObjectName(u"lblInternetTVLastBilltipIssueDate")
        self.lblInternetTVLastBilltipIssueDate.setGeometry(QRect(20, 200, 166, 16))
        self.lblInternetTVLastBilltipIssueDate.setFont(font3)
        self.lblInternetTVLastBilltipIssueDate.setStyleSheet(u"color: #6c6e71;")
        self.lblInternetTVLastBillDueDate = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillDueDate.setObjectName(u"lblInternetTVLastBillDueDate")
        self.lblInternetTVLastBillDueDate.setGeometry(QRect(20, 230, 301, 31))
        self.lblInternetTVLastBillDueDate.setFont(font8)
        self.lblInternetTVLastBillDueDate.setStyleSheet(u"color: #EE4540;")
        self.lblInternetTVLastBilltipDueDate = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBilltipDueDate.setObjectName(u"lblInternetTVLastBilltipDueDate")
        self.lblInternetTVLastBilltipDueDate.setGeometry(QRect(20, 260, 166, 16))
        self.lblInternetTVLastBilltipDueDate.setFont(font3)
        self.lblInternetTVLastBilltipDueDate.setStyleSheet(u"color: #6c6e71;")
        self.internetTVLastBillTotalPay = QFrame(self.pageInternetTV)
        self.internetTVLastBillTotalPay.setObjectName(u"internetTVLastBillTotalPay")
        self.internetTVLastBillTotalPay.setGeometry(QRect(640, 460, 441, 81))
        self.internetTVLastBillTotalPay.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #C72C41;;\n"
"}")
        self.internetTVLastBillTotalPay.setFrameShape(QFrame.StyledPanel)
        self.internetTVLastBillTotalPay.setFrameShadow(QFrame.Raised)
        self.lblInternetTVLastBillTotalPayInfo = QLabel(self.internetTVLastBillTotalPay)
        self.lblInternetTVLastBillTotalPayInfo.setObjectName(u"lblInternetTVLastBillTotalPayInfo")
        self.lblInternetTVLastBillTotalPayInfo.setGeometry(QRect(20, 10, 331, 23))
        self.lblInternetTVLastBillTotalPayInfo.setMaximumSize(QSize(500, 16777215))
        self.lblInternetTVLastBillTotalPayInfo.setFont(font7)
        self.lblInternetTVLastBillTotalPayInfo.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetTVLastBillTotalPay = QLabel(self.internetTVLastBillTotalPay)
        self.lblInternetTVLastBillTotalPay.setObjectName(u"lblInternetTVLastBillTotalPay")
        self.lblInternetTVLastBillTotalPay.setGeometry(QRect(90, 40, 191, 31))
        self.lblInternetTVLastBillTotalPay.setFont(font8)
        self.lblInternetTVLastBillTotalPay.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetTVBillCurrency = QLabel(self.internetTVLastBillTotalPay)
        self.lblInternetTVBillCurrency.setObjectName(u"lblInternetTVBillCurrency")
        self.lblInternetTVBillCurrency.setGeometry(QRect(20, 40, 61, 31))
        self.lblInternetTVBillCurrency.setFont(font9)
        self.lblInternetTVBillCurrency.setStyleSheet(u"color: #2a2e32;")
        self.internetTVLastBill = QFrame(self.pageInternetTV)
        self.internetTVLastBill.setObjectName(u"internetTVLastBill")
        self.internetTVLastBill.setGeometry(QRect(20, 560, 391, 311))
        self.internetTVLastBill.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.internetTVLastBill.setFrameShape(QFrame.StyledPanel)
        self.internetTVLastBill.setFrameShadow(QFrame.Raised)
        self.lblInternetTVLastBillPlotTitle = QLabel(self.internetTVLastBill)
        self.lblInternetTVLastBillPlotTitle.setObjectName(u"lblInternetTVLastBillPlotTitle")
        self.lblInternetTVLastBillPlotTitle.setGeometry(QRect(20, 10, 341, 23))
        self.lblInternetTVLastBillPlotTitle.setMaximumSize(QSize(500, 16777215))
        self.lblInternetTVLastBillPlotTitle.setFont(font7)
        self.lblInternetTVLastBillPlotTitle.setStyleSheet(u"color: #f3f5f6;")
        self.donutInternetTVLastBill = QWidget(self.internetTVLastBill)
        self.donutInternetTVLastBill.setObjectName(u"donutInternetTVLastBill")
        self.donutInternetTVLastBill.setGeometry(QRect(0, 40, 391, 261))
        self.donutInternetTVLastBill.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.internetSpeedtest = QFrame(self.pageInternetTV)
        self.internetSpeedtest.setObjectName(u"internetSpeedtest")
        self.internetSpeedtest.setGeometry(QRect(430, 560, 651, 311))
        self.internetSpeedtest.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"   background-image: url(:/images/Resources/internet-speed.png);\n"
"}")
        self.internetSpeedtest.setFrameShape(QFrame.StyledPanel)
        self.internetSpeedtest.setFrameShadow(QFrame.Raised)
        self.lblTestInternetSpeed = QLabel(self.internetSpeedtest)
        self.lblTestInternetSpeed.setObjectName(u"lblTestInternetSpeed")
        self.lblTestInternetSpeed.setGeometry(QRect(20, 10, 181, 23))
        self.lblTestInternetSpeed.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetSpeed.setFont(font7)
        self.lblTestInternetSpeed.setStyleSheet(u"color: #f3f5f6;")
        self.btnTestInternetSpeed = QPushButton(self.internetSpeedtest)
        self.btnTestInternetSpeed.setObjectName(u"btnTestInternetSpeed")
        self.btnTestInternetSpeed.setGeometry(QRect(30, 240, 111, 50))
        self.btnTestInternetSpeed.setFont(font1)
        self.btnTestInternetSpeed.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnTestInternetSpeed.setStyleSheet(u"QPushButton{\n"
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
        self.btnTestInternetSpeed.setAutoDefault(True)
        self.btnTestInternetSpeed.setFlat(True)
        self.lblTestInternetPing = QLabel(self.internetSpeedtest)
        self.lblTestInternetPing.setObjectName(u"lblTestInternetPing")
        self.lblTestInternetPing.setGeometry(QRect(70, 75, 51, 23))
        self.lblTestInternetPing.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetPing.setFont(font7)
        self.lblTestInternetPing.setStyleSheet(u"color: #C72C41;")
        self.lblTestInternetDownload = QLabel(self.internetSpeedtest)
        self.lblTestInternetDownload.setObjectName(u"lblTestInternetDownload")
        self.lblTestInternetDownload.setGeometry(QRect(70, 130, 101, 23))
        self.lblTestInternetDownload.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetDownload.setFont(font7)
        self.lblTestInternetDownload.setStyleSheet(u"color: #C72C41;")
        self.lblTestInternetUpload = QLabel(self.internetSpeedtest)
        self.lblTestInternetUpload.setObjectName(u"lblTestInternetUpload")
        self.lblTestInternetUpload.setGeometry(QRect(70, 185, 71, 23))
        self.lblTestInternetUpload.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetUpload.setFont(font7)
        self.lblTestInternetUpload.setStyleSheet(u"color: #C72C41;")
        self.lblTestInternetPingData = QLabel(self.internetSpeedtest)
        self.lblTestInternetPingData.setObjectName(u"lblTestInternetPingData")
        self.lblTestInternetPingData.setGeometry(QRect(125, 75, 181, 23))
        self.lblTestInternetPingData.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetPingData.setFont(font7)
        self.lblTestInternetPingData.setStyleSheet(u"color: #f3f5f6;")
        self.lblTestInternetDownloadData = QLabel(self.internetSpeedtest)
        self.lblTestInternetDownloadData.setObjectName(u"lblTestInternetDownloadData")
        self.lblTestInternetDownloadData.setGeometry(QRect(175, 130, 151, 23))
        self.lblTestInternetDownloadData.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetDownloadData.setFont(font7)
        self.lblTestInternetDownloadData.setStyleSheet(u"color: #f3f5f6;")
        self.lblTestInternetUploadData = QLabel(self.internetSpeedtest)
        self.lblTestInternetUploadData.setObjectName(u"lblTestInternetUploadData")
        self.lblTestInternetUploadData.setGeometry(QRect(150, 185, 181, 23))
        self.lblTestInternetUploadData.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetUploadData.setFont(font7)
        self.lblTestInternetUploadData.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetSpeedAdditionalInfo = QLabel(self.internetSpeedtest)
        self.lblInternetSpeedAdditionalInfo.setObjectName(u"lblInternetSpeedAdditionalInfo")
        self.lblInternetSpeedAdditionalInfo.setGeometry(QRect(20, 37, 291, 16))
        self.lblInternetSpeedAdditionalInfo.setFont(font3)
        self.lblInternetSpeedAdditionalInfo.setStyleSheet(u"color: #6c6e71;")
        self.generalInternetTVInformationFrame = QFrame(self.pageInternetTV)
        self.generalInternetTVInformationFrame.setObjectName(u"generalInternetTVInformationFrame")
        self.generalInternetTVInformationFrame.setGeometry(QRect(20, 890, 1061, 21))
        self.generalInternetTVInformationFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.generalInternetTVInformationFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 5px; \n"
"   background-color: #2a2e32;\n"
"}")
        self.generalInternetTVInformationFrame.setFrameShape(QFrame.NoFrame)
        self.generalInternetTVInformationFrame.setFrameShadow(QFrame.Raised)
        self.lblGeneralInternetTVInformation = QLabel(self.generalInternetTVInformationFrame)
        self.lblGeneralInternetTVInformation.setObjectName(u"lblGeneralInternetTVInformation")
        self.lblGeneralInternetTVInformation.setGeometry(QRect(0, 3, 1061, 16))
        self.lblGeneralInternetTVInformation.setFont(font3)
        self.lblGeneralInternetTVInformation.setStyleSheet(u"color: #6c6e71;")
        self.lblGeneralInternetTVInformation.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.pageInternetTV)
        self.pageSubscriptions = QWidget()
        self.pageSubscriptions.setObjectName(u"pageSubscriptions")
        self.lblSubscriptionsTitle = QLabel(self.pageSubscriptions)
        self.lblSubscriptionsTitle.setObjectName(u"lblSubscriptionsTitle")
        self.lblSubscriptionsTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblSubscriptionsTitle.setFont(font5)
        self.lblSubscriptionsTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblSubscriptionsTitle.setTextFormat(Qt.MarkdownText)
        self.netflixSelection = QFrame(self.pageSubscriptions)
        self.netflixSelection.setObjectName(u"netflixSelection")
        self.netflixSelection.setGeometry(QRect(20, 70, 571, 251))
        self.netflixSelection.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.netflixSelection.setFrameShape(QFrame.StyledPanel)
        self.netflixSelection.setFrameShadow(QFrame.Raised)
        self.lblNetflixSelection = QLabel(self.netflixSelection)
        self.lblNetflixSelection.setObjectName(u"lblNetflixSelection")
        self.lblNetflixSelection.setGeometry(QRect(20, 10, 201, 21))
        self.lblNetflixSelection.setFont(font7)
        self.lblNetflixSelection.setStyleSheet(u"color: #f3f5f6;")
        self.lblNetflixSelectionInfo = QLabel(self.netflixSelection)
        self.lblNetflixSelectionInfo.setObjectName(u"lblNetflixSelectionInfo")
        self.lblNetflixSelectionInfo.setGeometry(QRect(20, 40, 231, 21))
        self.lblNetflixSelectionInfo.setFont(font3)
        self.lblNetflixSelectionInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnNetflixDisplay = QPushButton(self.netflixSelection)
        self.btnNetflixDisplay.setObjectName(u"btnNetflixDisplay")
        self.btnNetflixDisplay.setEnabled(True)
        self.btnNetflixDisplay.setGeometry(QRect(180, 10, 371, 50))
        self.btnNetflixDisplay.setCursor(QCursor(Qt.ArrowCursor))
        self.btnNetflixDisplay.setFocusPolicy(Qt.StrongFocus)
        self.btnNetflixDisplay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnNetflixDisplay.setStyleSheet(u"background-color: #202528;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"background-image: url(:/images/Resources/netflix_sub_selection.png);")
        self.btnNetflixDisplay.setCheckable(True)
        self.btnNetflixDisplay.setChecked(False)
        self.btnNetflixDisplay.setAutoDefault(True)
        self.btnNetflixDisplay.setFlat(True)
        self.txtNetflixPayment = QLineEdit(self.netflixSelection)
        self.txtNetflixPayment.setObjectName(u"txtNetflixPayment")
        self.txtNetflixPayment.setGeometry(QRect(170, 140, 121, 35))
        self.txtNetflixPayment.setFont(font6)
        self.txtNetflixPayment.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.comboBoxNetflixDay = QComboBox(self.netflixSelection)
        self.comboBoxNetflixDay.setObjectName(u"comboBoxNetflixDay")
        self.comboBoxNetflixDay.setGeometry(QRect(250, 80, 70, 35))
        self.comboBoxNetflixDay.setFont(font3)
        self.comboBoxNetflixDay.setStyleSheet(u"QComboBox { \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxNetflixDay.setEditable(False)
        self.comboBoxNetflixDay.setMinimumContentsLength(0)
        self.comboBoxNetflixMonth = QComboBox(self.netflixSelection)
        self.comboBoxNetflixMonth.setObjectName(u"comboBoxNetflixMonth")
        self.comboBoxNetflixMonth.setGeometry(QRect(330, 80, 70, 35))
        self.comboBoxNetflixMonth.setFont(font3)
        self.comboBoxNetflixMonth.setStyleSheet(u"QComboBox {   \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxNetflixMonth.setEditable(False)
        self.comboBoxNetflixYear = QComboBox(self.netflixSelection)
        self.comboBoxNetflixYear.setObjectName(u"comboBoxNetflixYear")
        self.comboBoxNetflixYear.setGeometry(QRect(410, 80, 70, 35))
        self.comboBoxNetflixYear.setFont(font3)
        self.comboBoxNetflixYear.setStyleSheet(u"QComboBox {    \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxNetflixYear.setEditable(False)
        self.btnSetNetflixData = QPushButton(self.netflixSelection)
        self.btnSetNetflixData.setObjectName(u"btnSetNetflixData")
        self.btnSetNetflixData.setGeometry(QRect(470, 140, 75, 35))
        self.btnSetNetflixData.setFont(font1)
        self.btnSetNetflixData.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSetNetflixData.setStyleSheet(u"QPushButton{\n"
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
        self.btnSetNetflixData.setAutoDefault(True)
        self.btnSetNetflixData.setFlat(True)
        self.lblNetflixPaymentValue = QLabel(self.netflixSelection)
        self.lblNetflixPaymentValue.setObjectName(u"lblNetflixPaymentValue")
        self.lblNetflixPaymentValue.setGeometry(QRect(20, 145, 141, 21))
        self.lblNetflixPaymentValue.setFont(font3)
        self.lblNetflixPaymentValue.setStyleSheet(u"color: #b6b7b7;")
        self.lblNetflixStartDate = QLabel(self.netflixSelection)
        self.lblNetflixStartDate.setObjectName(u"lblNetflixStartDate")
        self.lblNetflixStartDate.setGeometry(QRect(20, 90, 211, 21))
        self.lblNetflixStartDate.setFont(font3)
        self.lblNetflixStartDate.setStyleSheet(u"color: #b6b7b7;")
        self.lblNetflixPerMonth = QLabel(self.netflixSelection)
        self.lblNetflixPerMonth.setObjectName(u"lblNetflixPerMonth")
        self.lblNetflixPerMonth.setGeometry(QRect(390, 145, 71, 21))
        self.lblNetflixPerMonth.setFont(font3)
        self.lblNetflixPerMonth.setStyleSheet(u"color: #6c6e71;")
        self.comboBoxNetflixCurrency = QComboBox(self.netflixSelection)
        self.comboBoxNetflixCurrency.setObjectName(u"comboBoxNetflixCurrency")
        self.comboBoxNetflixCurrency.setGeometry(QRect(300, 140, 80, 35))
        self.comboBoxNetflixCurrency.setFont(font3)
        self.comboBoxNetflixCurrency.setStyleSheet(u"QComboBox {    \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxNetflixCurrency.setEditable(False)
        self.lblNetflixTotalPaySinceStart = QLabel(self.netflixSelection)
        self.lblNetflixTotalPaySinceStart.setObjectName(u"lblNetflixTotalPaySinceStart")
        self.lblNetflixTotalPaySinceStart.setGeometry(QRect(20, 200, 321, 21))
        self.lblNetflixTotalPaySinceStart.setFont(font3)
        self.lblNetflixTotalPaySinceStart.setStyleSheet(u"color: #b6b7b7;")
        self.txtNetflixTotalPayment = QLineEdit(self.netflixSelection)
        self.txtNetflixTotalPayment.setObjectName(u"txtNetflixTotalPayment")
        self.txtNetflixTotalPayment.setEnabled(False)
        self.txtNetflixTotalPayment.setGeometry(QRect(340, 195, 211, 35))
        self.txtNetflixTotalPayment.setFont(font6)
        self.txtNetflixTotalPayment.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.spotifySelection = QFrame(self.pageSubscriptions)
        self.spotifySelection.setObjectName(u"spotifySelection")
        self.spotifySelection.setGeometry(QRect(20, 340, 571, 251))
        self.spotifySelection.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.spotifySelection.setFrameShape(QFrame.StyledPanel)
        self.spotifySelection.setFrameShadow(QFrame.Raised)
        self.lblSpotifySelection = QLabel(self.spotifySelection)
        self.lblSpotifySelection.setObjectName(u"lblSpotifySelection")
        self.lblSpotifySelection.setGeometry(QRect(20, 10, 201, 21))
        self.lblSpotifySelection.setFont(font7)
        self.lblSpotifySelection.setStyleSheet(u"color: #f3f5f6;")
        self.lblSpotifySelectionInfo = QLabel(self.spotifySelection)
        self.lblSpotifySelectionInfo.setObjectName(u"lblSpotifySelectionInfo")
        self.lblSpotifySelectionInfo.setGeometry(QRect(20, 40, 231, 21))
        self.lblSpotifySelectionInfo.setFont(font3)
        self.lblSpotifySelectionInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnSpotifyDisplay = QPushButton(self.spotifySelection)
        self.btnSpotifyDisplay.setObjectName(u"btnSpotifyDisplay")
        self.btnSpotifyDisplay.setEnabled(True)
        self.btnSpotifyDisplay.setGeometry(QRect(170, 10, 371, 50))
        self.btnSpotifyDisplay.setCursor(QCursor(Qt.ArrowCursor))
        self.btnSpotifyDisplay.setFocusPolicy(Qt.StrongFocus)
        self.btnSpotifyDisplay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnSpotifyDisplay.setStyleSheet(u"background-color: #202528;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"background-image: url(:/images/Resources/spotify_sub_selection.png);")
        self.btnSpotifyDisplay.setCheckable(True)
        self.btnSpotifyDisplay.setChecked(False)
        self.btnSpotifyDisplay.setAutoDefault(True)
        self.btnSpotifyDisplay.setFlat(True)
        self.lblSpotifyStartDate = QLabel(self.spotifySelection)
        self.lblSpotifyStartDate.setObjectName(u"lblSpotifyStartDate")
        self.lblSpotifyStartDate.setGeometry(QRect(20, 90, 211, 21))
        self.lblSpotifyStartDate.setFont(font3)
        self.lblSpotifyStartDate.setStyleSheet(u"color: #b6b7b7;")
        self.comboBoxSpotifyDay = QComboBox(self.spotifySelection)
        self.comboBoxSpotifyDay.setObjectName(u"comboBoxSpotifyDay")
        self.comboBoxSpotifyDay.setGeometry(QRect(250, 80, 70, 35))
        self.comboBoxSpotifyDay.setFont(font3)
        self.comboBoxSpotifyDay.setStyleSheet(u"QComboBox { \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxSpotifyDay.setEditable(False)
        self.comboBoxSpotifyMonth = QComboBox(self.spotifySelection)
        self.comboBoxSpotifyMonth.setObjectName(u"comboBoxSpotifyMonth")
        self.comboBoxSpotifyMonth.setGeometry(QRect(330, 80, 70, 35))
        self.comboBoxSpotifyMonth.setFont(font3)
        self.comboBoxSpotifyMonth.setStyleSheet(u"QComboBox {   \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxSpotifyMonth.setEditable(False)
        self.comboBoxSpotifyYear = QComboBox(self.spotifySelection)
        self.comboBoxSpotifyYear.setObjectName(u"comboBoxSpotifyYear")
        self.comboBoxSpotifyYear.setGeometry(QRect(410, 80, 70, 35))
        self.comboBoxSpotifyYear.setFont(font3)
        self.comboBoxSpotifyYear.setStyleSheet(u"QComboBox {    \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxSpotifyYear.setEditable(False)
        self.lblSpotifyPaymentValue = QLabel(self.spotifySelection)
        self.lblSpotifyPaymentValue.setObjectName(u"lblSpotifyPaymentValue")
        self.lblSpotifyPaymentValue.setGeometry(QRect(20, 145, 141, 21))
        self.lblSpotifyPaymentValue.setFont(font3)
        self.lblSpotifyPaymentValue.setStyleSheet(u"color: #b6b7b7;")
        self.txtSpotifyPayment = QLineEdit(self.spotifySelection)
        self.txtSpotifyPayment.setObjectName(u"txtSpotifyPayment")
        self.txtSpotifyPayment.setGeometry(QRect(170, 140, 121, 35))
        self.txtSpotifyPayment.setFont(font6)
        self.txtSpotifyPayment.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.comboBoxSpotifyCurrency = QComboBox(self.spotifySelection)
        self.comboBoxSpotifyCurrency.setObjectName(u"comboBoxSpotifyCurrency")
        self.comboBoxSpotifyCurrency.setGeometry(QRect(300, 140, 80, 35))
        self.comboBoxSpotifyCurrency.setFont(font3)
        self.comboBoxSpotifyCurrency.setStyleSheet(u"QComboBox {    \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxSpotifyCurrency.setEditable(False)
        self.lblSpotifyPerMonth = QLabel(self.spotifySelection)
        self.lblSpotifyPerMonth.setObjectName(u"lblSpotifyPerMonth")
        self.lblSpotifyPerMonth.setGeometry(QRect(390, 145, 71, 21))
        self.lblSpotifyPerMonth.setFont(font3)
        self.lblSpotifyPerMonth.setStyleSheet(u"color: #6c6e71;")
        self.btnSetSpotifyData = QPushButton(self.spotifySelection)
        self.btnSetSpotifyData.setObjectName(u"btnSetSpotifyData")
        self.btnSetSpotifyData.setGeometry(QRect(470, 140, 75, 35))
        self.btnSetSpotifyData.setFont(font1)
        self.btnSetSpotifyData.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSetSpotifyData.setStyleSheet(u"QPushButton{\n"
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
        self.btnSetSpotifyData.setAutoDefault(True)
        self.btnSetSpotifyData.setFlat(True)
        self.lblSpotifyTotalPaySinceStart = QLabel(self.spotifySelection)
        self.lblSpotifyTotalPaySinceStart.setObjectName(u"lblSpotifyTotalPaySinceStart")
        self.lblSpotifyTotalPaySinceStart.setGeometry(QRect(20, 200, 321, 21))
        self.lblSpotifyTotalPaySinceStart.setFont(font3)
        self.lblSpotifyTotalPaySinceStart.setStyleSheet(u"color: #b6b7b7;")
        self.txtSpotifyTotalPayment = QLineEdit(self.spotifySelection)
        self.txtSpotifyTotalPayment.setObjectName(u"txtSpotifyTotalPayment")
        self.txtSpotifyTotalPayment.setEnabled(False)
        self.txtSpotifyTotalPayment.setGeometry(QRect(340, 195, 211, 35))
        self.txtSpotifyTotalPayment.setFont(font6)
        self.txtSpotifyTotalPayment.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.telecomSelection = QFrame(self.pageSubscriptions)
        self.telecomSelection.setObjectName(u"telecomSelection")
        self.telecomSelection.setGeometry(QRect(20, 610, 571, 251))
        self.telecomSelection.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.telecomSelection.setFrameShape(QFrame.StyledPanel)
        self.telecomSelection.setFrameShadow(QFrame.Raised)
        self.lblTelecomSelection = QLabel(self.telecomSelection)
        self.lblTelecomSelection.setObjectName(u"lblTelecomSelection")
        self.lblTelecomSelection.setGeometry(QRect(20, 10, 201, 21))
        self.lblTelecomSelection.setFont(font7)
        self.lblTelecomSelection.setStyleSheet(u"color: #f3f5f6;")
        self.lblTelecomSelectionInfo = QLabel(self.telecomSelection)
        self.lblTelecomSelectionInfo.setObjectName(u"lblTelecomSelectionInfo")
        self.lblTelecomSelectionInfo.setGeometry(QRect(20, 40, 231, 21))
        self.lblTelecomSelectionInfo.setFont(font3)
        self.lblTelecomSelectionInfo.setStyleSheet(u"color: #6c6e71;")
        self.btnTelecomDisplay = QPushButton(self.telecomSelection)
        self.btnTelecomDisplay.setObjectName(u"btnTelecomDisplay")
        self.btnTelecomDisplay.setEnabled(True)
        self.btnTelecomDisplay.setGeometry(QRect(170, 10, 371, 50))
        self.btnTelecomDisplay.setCursor(QCursor(Qt.ArrowCursor))
        self.btnTelecomDisplay.setFocusPolicy(Qt.StrongFocus)
        self.btnTelecomDisplay.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnTelecomDisplay.setStyleSheet(u"background-color: #202528;\n"
"border-radius: 5px;\n"
"background-repeat: none;\n"
"background-position: center;\n"
"background-image: url(:/images/Resources/vodafone_sub_selection.png);")
        self.btnTelecomDisplay.setCheckable(True)
        self.btnTelecomDisplay.setChecked(False)
        self.btnTelecomDisplay.setAutoDefault(True)
        self.btnTelecomDisplay.setFlat(True)
        self.lblTelecomStartDate = QLabel(self.telecomSelection)
        self.lblTelecomStartDate.setObjectName(u"lblTelecomStartDate")
        self.lblTelecomStartDate.setGeometry(QRect(20, 90, 211, 21))
        self.lblTelecomStartDate.setFont(font3)
        self.lblTelecomStartDate.setStyleSheet(u"color: #b6b7b7;")
        self.comboBoxTelecomDay = QComboBox(self.telecomSelection)
        self.comboBoxTelecomDay.setObjectName(u"comboBoxTelecomDay")
        self.comboBoxTelecomDay.setGeometry(QRect(250, 80, 70, 35))
        self.comboBoxTelecomDay.setFont(font3)
        self.comboBoxTelecomDay.setStyleSheet(u"QComboBox { \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxTelecomDay.setEditable(False)
        self.comboBoxTelecomMonth = QComboBox(self.telecomSelection)
        self.comboBoxTelecomMonth.setObjectName(u"comboBoxTelecomMonth")
        self.comboBoxTelecomMonth.setGeometry(QRect(330, 80, 70, 35))
        self.comboBoxTelecomMonth.setFont(font3)
        self.comboBoxTelecomMonth.setStyleSheet(u"QComboBox {   \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxTelecomMonth.setEditable(False)
        self.comboBoxTelecomYear = QComboBox(self.telecomSelection)
        self.comboBoxTelecomYear.setObjectName(u"comboBoxTelecomYear")
        self.comboBoxTelecomYear.setGeometry(QRect(410, 80, 70, 35))
        self.comboBoxTelecomYear.setFont(font3)
        self.comboBoxTelecomYear.setStyleSheet(u"QComboBox {    \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxTelecomYear.setEditable(False)
        self.lblTelecomPaymentValue = QLabel(self.telecomSelection)
        self.lblTelecomPaymentValue.setObjectName(u"lblTelecomPaymentValue")
        self.lblTelecomPaymentValue.setGeometry(QRect(20, 145, 141, 21))
        self.lblTelecomPaymentValue.setFont(font3)
        self.lblTelecomPaymentValue.setStyleSheet(u"color: #b6b7b7;")
        self.txtTelecomPayment = QLineEdit(self.telecomSelection)
        self.txtTelecomPayment.setObjectName(u"txtTelecomPayment")
        self.txtTelecomPayment.setGeometry(QRect(170, 140, 121, 35))
        self.txtTelecomPayment.setFont(font6)
        self.txtTelecomPayment.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.comboBoxTelecomCurrency = QComboBox(self.telecomSelection)
        self.comboBoxTelecomCurrency.setObjectName(u"comboBoxTelecomCurrency")
        self.comboBoxTelecomCurrency.setGeometry(QRect(300, 140, 80, 35))
        self.comboBoxTelecomCurrency.setFont(font3)
        self.comboBoxTelecomCurrency.setStyleSheet(u"QComboBox {    \n"
"   color: #C72C41;\n"
"   selection-background-color: #202528;\n"
"   selection-color: #C72C41;\n"
"}\n"
"QListView {    \n"
"   color: #C72C41;\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"background-color:#202528;\n"
"selection-background-color: #202528;\n"
"color:#C72C41;\n"
"}")
        self.comboBoxTelecomCurrency.setEditable(False)
        self.lblTelecomPerMonth = QLabel(self.telecomSelection)
        self.lblTelecomPerMonth.setObjectName(u"lblTelecomPerMonth")
        self.lblTelecomPerMonth.setGeometry(QRect(390, 145, 71, 21))
        self.lblTelecomPerMonth.setFont(font3)
        self.lblTelecomPerMonth.setStyleSheet(u"color: #6c6e71;")
        self.btnSetTelecomData = QPushButton(self.telecomSelection)
        self.btnSetTelecomData.setObjectName(u"btnSetTelecomData")
        self.btnSetTelecomData.setGeometry(QRect(470, 140, 75, 35))
        self.btnSetTelecomData.setFont(font1)
        self.btnSetTelecomData.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSetTelecomData.setStyleSheet(u"QPushButton{\n"
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
        self.btnSetTelecomData.setAutoDefault(True)
        self.btnSetTelecomData.setFlat(True)
        self.lblTelecomTotalPaySinceStart = QLabel(self.telecomSelection)
        self.lblTelecomTotalPaySinceStart.setObjectName(u"lblTelecomTotalPaySinceStart")
        self.lblTelecomTotalPaySinceStart.setGeometry(QRect(20, 200, 321, 21))
        self.lblTelecomTotalPaySinceStart.setFont(font3)
        self.lblTelecomTotalPaySinceStart.setStyleSheet(u"color: #b6b7b7;")
        self.txtTelecomTotalPayment = QLineEdit(self.telecomSelection)
        self.txtTelecomTotalPayment.setObjectName(u"txtTelecomTotalPayment")
        self.txtTelecomTotalPayment.setEnabled(False)
        self.txtTelecomTotalPayment.setGeometry(QRect(340, 195, 211, 35))
        self.txtTelecomTotalPayment.setFont(font6)
        self.txtTelecomTotalPayment.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   background-color:#202528;\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.subscriptionsEarningsImpact = QFrame(self.pageSubscriptions)
        self.subscriptionsEarningsImpact.setObjectName(u"subscriptionsEarningsImpact")
        self.subscriptionsEarningsImpact.setGeometry(QRect(610, 70, 471, 381))
        self.subscriptionsEarningsImpact.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.subscriptionsEarningsImpact.setFrameShape(QFrame.StyledPanel)
        self.subscriptionsEarningsImpact.setFrameShadow(QFrame.Raised)
        self.lblSubscriptionsImpact = QLabel(self.subscriptionsEarningsImpact)
        self.lblSubscriptionsImpact.setObjectName(u"lblSubscriptionsImpact")
        self.lblSubscriptionsImpact.setGeometry(QRect(20, 10, 391, 23))
        self.lblSubscriptionsImpact.setMaximumSize(QSize(500, 16777215))
        self.lblSubscriptionsImpact.setFont(font7)
        self.lblSubscriptionsImpact.setStyleSheet(u"color: #f3f5f6;")
        self.donutSubscriptionsAll = QWidget(self.subscriptionsEarningsImpact)
        self.donutSubscriptionsAll.setObjectName(u"donutSubscriptionsAll")
        self.donutSubscriptionsAll.setGeometry(QRect(0, 40, 471, 331))
        self.donutSubscriptionsAll.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.subscriptionsComparison = QFrame(self.pageSubscriptions)
        self.subscriptionsComparison.setObjectName(u"subscriptionsComparison")
        self.subscriptionsComparison.setGeometry(QRect(610, 470, 471, 391))
        self.subscriptionsComparison.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.subscriptionsComparison.setFrameShape(QFrame.StyledPanel)
        self.subscriptionsComparison.setFrameShadow(QFrame.Raised)
        self.lblSubscriptionsComparison = QLabel(self.subscriptionsComparison)
        self.lblSubscriptionsComparison.setObjectName(u"lblSubscriptionsComparison")
        self.lblSubscriptionsComparison.setGeometry(QRect(20, 10, 411, 23))
        self.lblSubscriptionsComparison.setMaximumSize(QSize(500, 16777215))
        self.lblSubscriptionsComparison.setFont(font7)
        self.lblSubscriptionsComparison.setStyleSheet(u"color: #f3f5f6;")
        self.barChartSubscriptionsComparison = QWidget(self.subscriptionsComparison)
        self.barChartSubscriptionsComparison.setObjectName(u"barChartSubscriptionsComparison")
        self.barChartSubscriptionsComparison.setGeometry(QRect(0, 40, 471, 341))
        self.barChartSubscriptionsComparison.setStyleSheet(u"border-radius: 0px;\n"
"background-color: #2a2e32;")
        self.generalSubscriptionsInformationFrame = QFrame(self.pageSubscriptions)
        self.generalSubscriptionsInformationFrame.setObjectName(u"generalSubscriptionsInformationFrame")
        self.generalSubscriptionsInformationFrame.setGeometry(QRect(20, 880, 1061, 21))
        self.generalSubscriptionsInformationFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.generalSubscriptionsInformationFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 5px; \n"
"   background-color: #2a2e32;\n"
"}")
        self.generalSubscriptionsInformationFrame.setFrameShape(QFrame.NoFrame)
        self.generalSubscriptionsInformationFrame.setFrameShadow(QFrame.Raised)
        self.lblGeneralSubscriptionInformation = QLabel(self.generalSubscriptionsInformationFrame)
        self.lblGeneralSubscriptionInformation.setObjectName(u"lblGeneralSubscriptionInformation")
        self.lblGeneralSubscriptionInformation.setGeometry(QRect(10, 3, 1041, 16))
        self.lblGeneralSubscriptionInformation.setFont(font3)
        self.lblGeneralSubscriptionInformation.setStyleSheet(u"color: #6c6e71;")
        self.lblGeneralSubscriptionInformation.setAlignment(Qt.AlignCenter)
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
        self.lblProfileName.setFont(font7)
        self.lblProfileName.setStyleSheet(u"color: #f3f5f6;")
        self.txtUsername = QLineEdit(self.profileName)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setEnabled(False)
        self.txtUsername.setGeometry(QRect(20, 60, 280, 50))
        self.txtUsername.setFont(font6)
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
        self.txtEarnings.setFont(font6)
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
        self.lblElectricitySupplier.setFont(font7)
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
        self.lblNaturalGasSupplier.setFont(font7)
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
        self.lblInternetProvider.setFont(font7)
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
        self.lblEarnings.setFont(font7)
        self.lblEarnings.setStyleSheet(u"color: #f3f5f6;")
        self.lblEarningsPerMonth = QLabel(self.earnings)
        self.lblEarningsPerMonth.setObjectName(u"lblEarningsPerMonth")
        self.lblEarningsPerMonth.setGeometry(QRect(20, 100, 71, 21))
        self.lblEarningsPerMonth.setFont(font3)
        self.lblEarningsPerMonth.setStyleSheet(u"color: #6c6e71;")
        self.lblEarningsCurrency = QLabel(self.earnings)
        self.lblEarningsCurrency.setObjectName(u"lblEarningsCurrency")
        self.lblEarningsCurrency.setGeometry(QRect(20, 70, 61, 21))
        self.lblEarningsCurrency.setFont(font9)
        self.lblEarningsCurrency.setStyleSheet(u"color: #C72C41;")
        self.lblEarningsValue = QLabel(self.earnings)
        self.lblEarningsValue.setObjectName(u"lblEarningsValue")
        self.lblEarningsValue.setGeometry(QRect(80, 70, 121, 21))
        self.lblEarningsValue.setFont(font9)
        self.lblEarningsValue.setStyleSheet(u"color: #EE4540;")
        self.subscriptionsPage = QFrame(self.pageProfile)
        self.subscriptionsPage.setObjectName(u"subscriptionsPage")
        self.subscriptionsPage.setGeometry(QRect(30, 710, 791, 140))
        self.subscriptionsPage.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.subscriptionsPage.setFrameShape(QFrame.StyledPanel)
        self.subscriptionsPage.setFrameShadow(QFrame.Raised)
        self.lblSubscriptionsPage = QLabel(self.subscriptionsPage)
        self.lblSubscriptionsPage.setObjectName(u"lblSubscriptionsPage")
        self.lblSubscriptionsPage.setGeometry(QRect(20, 10, 201, 21))
        self.lblSubscriptionsPage.setFont(font7)
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
        self.btnVodafoneSelection = QPushButton(self.subscriptionsPage)
        self.btnVodafoneSelection.setObjectName(u"btnVodafoneSelection")
        self.btnVodafoneSelection.setGeometry(QRect(540, 70, 230, 50))
        self.btnVodafoneSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVodafoneSelection.setFocusPolicy(Qt.StrongFocus)
        self.btnVodafoneSelection.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnVodafoneSelection.setStyleSheet(u"QPushButton:checked{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QPushButton{\n"
"   background-color: #202528;  \n"
"   background-image: url(:/images/Resources/vodafone_sub_selection.png);\n"
"   color: #f3f5f6;\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #C72C41;\n"
"}")
        self.btnVodafoneSelection.setCheckable(True)
        self.btnVodafoneSelection.setChecked(False)
        self.btnVodafoneSelection.setAutoDefault(True)
        self.btnVodafoneSelection.setFlat(True)
        self.generalAccountInformationFrame = QFrame(self.pageProfile)
        self.generalAccountInformationFrame.setObjectName(u"generalAccountInformationFrame")
        self.generalAccountInformationFrame.setGeometry(QRect(30, 870, 1061, 31))
        self.generalAccountInformationFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.generalAccountInformationFrame.setStyleSheet(u"QFrame{\n"
"   border-radius: 5px; \n"
"   background-color: #2a2e32;\n"
"}")
        self.generalAccountInformationFrame.setFrameShape(QFrame.NoFrame)
        self.generalAccountInformationFrame.setFrameShadow(QFrame.Raised)
        self.lblGeneralAccountInformation = QLabel(self.generalAccountInformationFrame)
        self.lblGeneralAccountInformation.setObjectName(u"lblGeneralAccountInformation")
        self.lblGeneralAccountInformation.setGeometry(QRect(10, 4, 1041, 21))
        self.lblGeneralAccountInformation.setFont(font3)
        self.lblGeneralAccountInformation.setStyleSheet(u"color: #6c6e71;")
        self.lblGeneralAccountInformation.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.pageProfile)

        self.verticalLayout_2.addWidget(self.frameContentArea)


        self.horizontalLayout.addWidget(self.frameMainContentArea)

        BillyAppMain.setCentralWidget(self.mainCentralWidget)

        self.retranslateUi(BillyAppMain)

        self.btnDashboard.setDefault(False)
        self.btnInformation.setDefault(False)
        self.btnAppInfo.setDefault(False)
        self.electricityLegendIssueColor.setDefault(False)
        self.electricityLegendDueColor.setDefault(False)
        self.naturalGasLegendIssueColor.setDefault(False)
        self.naturalGasLegendDueColor.setDefault(False)
        self.internetTVLegendIssueColor.setDefault(False)
        self.internetTVLegendDueColor.setDefault(False)
        self.btnElectricitySupplierDisplay.setDefault(False)
        self.btnAddElectricityBill.setDefault(False)
        self.btnInformationElectricity.setDefault(False)
        self.btnNaturalGasSupplierDisplay.setDefault(False)
        self.btnAddNaturalGasBill.setDefault(False)
        self.btnInformationNaturalGas.setDefault(False)
        self.btnInternetProviderDisplay.setDefault(False)
        self.btnAddInternetTVBill.setDefault(False)
        self.btnInformationInternetTV.setDefault(False)
        self.btnTestInternetSpeed.setDefault(False)
        self.btnNetflixDisplay.setDefault(False)
        self.btnSetNetflixData.setDefault(False)
        self.btnSpotifyDisplay.setDefault(False)
        self.btnSetSpotifyData.setDefault(False)
        self.btnTelecomDisplay.setDefault(False)
        self.btnSetTelecomData.setDefault(False)
        self.btnSetProfileName.setDefault(False)
        self.btnEnelSelection.setDefault(False)
        self.btnEngieSelection.setDefault(False)
        self.btnRCSRDSSelection.setDefault(False)
        self.btnNetflixSelection.setDefault(False)
        self.btnSpotifySelection.setDefault(False)
        self.btnVodafoneSelection.setDefault(False)


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
        self.txtDashEarnings.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Earnings", None))
        self.lblDashDonutAllBills.setText(QCoreApplication.translate("BillyAppMain", u"Impact on earnings", None))
        self.lblDashBarAllBills.setText(QCoreApplication.translate("BillyAppMain", u"Latest month amount to pay for each bill", None))
        self.txtDashCurrentDate.setPlaceholderText("")
        self.lblElectricityDash.setText(QCoreApplication.translate("BillyAppMain", u"Electricity latest bill amount to pay and due date", None))
        self.txtElectricityPayDash.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Amount to pay", None))
        self.txtElectricityDueDateDash.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Due date", None))
        self.lblNaturalGasDash.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas latest bill amount to pay and due date", None))
        self.txtNaturalGasPayDash.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Amount to pay", None))
        self.txtNaturalGasDueDateDash.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Due date", None))
        self.lblInternetDash.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV latest bill amount to pay and due date", None))
        self.txtInternetPayDash.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Amount to pay", None))
        self.txtInternetDueDateDash.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Due date", None))
        self.lblSubscriptionsDash.setText(QCoreApplication.translate("BillyAppMain", u"Subscriptions", None))
        self.txtNetflixDash.setPlaceholderText("")
        self.txtSpotifyDash.setPlaceholderText("")
        self.txtVodafoneDash.setPlaceholderText("")
        self.btnInformation.setText("")
        self.lblDashboardWelcome.setText(QCoreApplication.translate("BillyAppMain", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#c72c41;\">Welcome to Billy v1.0 !</span><br/></p><p><span style=\" font-size:18pt; font-weight:600; color:#6c6e71;\">1. </span><span style=\" font-size:12pt; color:#6c6e71;\">Add the monthly earnings from the Account preferences</span></p><p><span style=\" font-size:18pt; font-weight:600; color:#6c6e71;\">2. </span><span style=\" font-size:12pt; color:#6c6e71;\">Select the suppliers/providers for each category</span></p><p><span style=\" font-size:18pt; color:#6c6e71;\">3</span><span style=\" font-size:16pt; color:#6c6e71;\">. </span><span style=\" font-size:12pt; color:#6c6e71;\">Add the bills for each supplier/provider (.pdf file)</span></p></body></html>", None))
        self.btnDashboardToAccountPreferences.setText("")
        self.lblGeneralDashboardInformation.setText(QCoreApplication.translate("BillyAppMain", u"Dashboard page : track the latest added bill amount to pay and due date for each supplier/provider, track the selected subscriptions and track the impact on earnings", None))
        self.btnAppInfo.setText("")
        self.lblCalendarTitle.setText(QCoreApplication.translate("BillyAppMain", u"Calendar", None))
        self.electricityLegendIssueColor.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Issue Day", None))
        self.electricityLegendDueColor.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Due Day", None))
        self.naturalGasLegendIssueColor.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas Issue Day", None))
        self.naturalGasLegendDueColor.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas Due Day", None))
        self.internetTVLegendIssueColor.setText(QCoreApplication.translate("BillyAppMain", u"Internet TV Issue Day", None))
        self.internetTVLegendDueColor.setText(QCoreApplication.translate("BillyAppMain", u"Internet TV Due Day", None))
        self.lblGeneralCalendarInformation.setText(QCoreApplication.translate("BillyAppMain", u"<html><head/><body><p>Calendar page : track the latest added bill issue date and due date for each selected supplier/provider. Current day is marked with</p></body></html>", None))
        self.lblCurrentDayColor.setText("")
        self.lblElectricityTitle.setText(QCoreApplication.translate("BillyAppMain", u"Electricity", None))
        self.lblElectricitySupplierSelection.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Supplier", None))
        self.lblElectricitySupplierSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Selected electricity supplier", None))
        self.btnElectricitySupplierDisplay.setText("")
        self.lblElectricityDirectoryInfo.setText(QCoreApplication.translate("BillyAppMain", u"Management of added electricity bills", None))
        self.btnAddElectricityBill.setText(QCoreApplication.translate("BillyAppMain", u"Add", None))
        self.lblElectricityDirectory.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Bills", None))
        self.btnInformationElectricity.setText("")
        self.lblElectricityLastBilltipID.setText(QCoreApplication.translate("BillyAppMain", u"ID", None))
        self.lblElectricityLastBillI.setText(QCoreApplication.translate("BillyAppMain", u"Bill info", None))
        self.lblElectricityLastBillID.setText("")
        self.lblElectricityLastBillAddress.setText("")
        self.lblElectricityLastBilltipAddress.setText(QCoreApplication.translate("BillyAppMain", u"Address", None))
        self.lblElectricityLastBillIssueDate.setText("")
        self.lblElectricityLastBilltipIssueDate.setText(QCoreApplication.translate("BillyAppMain", u"Issue Date", None))
        self.lblElectricityLastBillDueDate.setText("")
        self.lblElectricityLastBilltipDueDate.setText(QCoreApplication.translate("BillyAppMain", u"Due date", None))
        self.lblElectricityLastBillTotalPayInfo.setText(QCoreApplication.translate("BillyAppMain", u"Bill amount to pay", None))
        self.lblElectricityLastBillTotalPay.setText("")
        self.lblElectricityBillCurrency.setText(QCoreApplication.translate("BillyAppMain", u"RON", None))
        self.lblElectricityLastBillPlotTitle.setText(QCoreApplication.translate("BillyAppMain", u"Bill impact on earnings", None))
        self.lblElectricityAllBillsPlot.setText(QCoreApplication.translate("BillyAppMain", u"Bill costs overview", None))
        self.comboBoxElectricityBillYear.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Select year", None))
        self.comboBoxElectricityBillYear.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Select year", None))
        self.lblGeneralElectricityInformation.setText(QCoreApplication.translate("BillyAppMain", u"<html><head/><body><p>Electricity page: track, manage and view each added electricity bill. Get the main information for a selected bill, track the impact on monthly earnings and the price evolution</p></body></html>", None))
        self.lblNaturalGasTitle.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas", None))
        self.lblNaturalGasSupplierSelection.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas Supplier", None))
        self.lblNaturalGasSupplierSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Selected natural gas supplier", None))
        self.btnNaturalGasSupplierDisplay.setText("")
        self.lblNaturalGasDirectoryInfo.setText(QCoreApplication.translate("BillyAppMain", u"Management of added natural gas bills", None))
        self.btnAddNaturalGasBill.setText(QCoreApplication.translate("BillyAppMain", u"Add", None))
        self.lblNaturalGasDirectory.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas Bills", None))
        self.btnInformationNaturalGas.setText("")
        self.lblNaturalGasLastBilltipID.setText(QCoreApplication.translate("BillyAppMain", u"ID", None))
        self.lblNaturalGasLastBillI.setText(QCoreApplication.translate("BillyAppMain", u"Bill info", None))
        self.lblNaturalGasLastBillID.setText("")
        self.lblNaturalGasLastBillAddress.setText("")
        self.lblNaturalGasLastBilltipAddress.setText(QCoreApplication.translate("BillyAppMain", u"Address", None))
        self.lblNaturalGasLastBillIssueDate.setText("")
        self.lblNaturalGasLastBilltipIssueDate.setText(QCoreApplication.translate("BillyAppMain", u"Issue Date", None))
        self.lblNaturalGasLastBillDueDate.setText("")
        self.lblNaturalGasLastBilltipDueDate.setText(QCoreApplication.translate("BillyAppMain", u"Due date", None))
        self.lblNaturalGasLastBillTotalPayInfo.setText(QCoreApplication.translate("BillyAppMain", u"Bill amount to pay", None))
        self.lblNaturalGasLastBillTotalPay.setText("")
        self.lblNaturalGasBillCurrency.setText(QCoreApplication.translate("BillyAppMain", u"RON", None))
        self.lblNaturalGasLastBillPlotTitle.setText(QCoreApplication.translate("BillyAppMain", u"Bill impact on earnings", None))
        self.lblNaturalAllBillsPlot.setText(QCoreApplication.translate("BillyAppMain", u"Bill costs overview", None))
        self.comboBoxNaturalGasBillYear.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Select year", None))
        self.comboBoxNaturalGasBillYear.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Select year", None))
        self.lblGeneralNaturalGasInformation.setText(QCoreApplication.translate("BillyAppMain", u"<html><head/><body><p>Natural Gas page: track, manage and view each added gas bill. Get the main information for a selected bill, track the impact on monthly earnings and the price evolution</p></body></html>", None))
        self.lblInternetTVTitle.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV", None))
        self.lblInternetProviderSelection.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV Provider", None))
        self.lblInternetProviderSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Selected internet & TV provider", None))
        self.btnInternetProviderDisplay.setText("")
        self.lblInternetTVDirectoryInfo.setText(QCoreApplication.translate("BillyAppMain", u"Management of added internet & TV bills", None))
        self.btnAddInternetTVBill.setText(QCoreApplication.translate("BillyAppMain", u"Add", None))
        self.lblInternetTVDirectory.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV Bills", None))
        self.btnInformationInternetTV.setText("")
        self.lblInternetTVLastBilltipID.setText(QCoreApplication.translate("BillyAppMain", u"ID", None))
        self.lblInternetTVLastBillI.setText(QCoreApplication.translate("BillyAppMain", u"Bill info", None))
        self.lblInternetTVLastBillID.setText("")
        self.lblInternetTVLastBillAddress.setText("")
        self.lblInternetTVLastBilltipAddress.setText(QCoreApplication.translate("BillyAppMain", u"Address", None))
        self.lblInternetTVLastBillIssueDate.setText("")
        self.lblInternetTVLastBilltipIssueDate.setText(QCoreApplication.translate("BillyAppMain", u"Issue Date", None))
        self.lblInternetTVLastBillDueDate.setText("")
        self.lblInternetTVLastBilltipDueDate.setText(QCoreApplication.translate("BillyAppMain", u"Due date", None))
        self.lblInternetTVLastBillTotalPayInfo.setText(QCoreApplication.translate("BillyAppMain", u"Bill amount to pay", None))
        self.lblInternetTVLastBillTotalPay.setText("")
        self.lblInternetTVBillCurrency.setText(QCoreApplication.translate("BillyAppMain", u"RON", None))
        self.lblInternetTVLastBillPlotTitle.setText(QCoreApplication.translate("BillyAppMain", u"Bill impact on earnings", None))
        self.lblTestInternetSpeed.setText(QCoreApplication.translate("BillyAppMain", u"Test Internet Speed", None))
        self.btnTestInternetSpeed.setText(QCoreApplication.translate("BillyAppMain", u"Test", None))
        self.lblTestInternetPing.setText(QCoreApplication.translate("BillyAppMain", u"Ping", None))
        self.lblTestInternetDownload.setText(QCoreApplication.translate("BillyAppMain", u"Download", None))
        self.lblTestInternetUpload.setText(QCoreApplication.translate("BillyAppMain", u"Upload", None))
        self.lblTestInternetPingData.setText("")
        self.lblTestInternetDownloadData.setText("")
        self.lblTestInternetUploadData.setText("")
        self.lblInternetSpeedAdditionalInfo.setText(QCoreApplication.translate("BillyAppMain", u"Running this test will take a couple of seconds", None))
        self.lblGeneralInternetTVInformation.setText(QCoreApplication.translate("BillyAppMain", u"<html><head/><body><p>InternetTV page: track, manage and view each added internet bill. Get the main information for a selected bill, track the impact on monthly earnings and test the internet speed</p></body></html>", None))
        self.lblSubscriptionsTitle.setText(QCoreApplication.translate("BillyAppMain", u"Subscriptions", None))
        self.lblNetflixSelection.setText(QCoreApplication.translate("BillyAppMain", u"Netflix", None))
        self.lblNetflixSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Entertainment", None))
        self.btnNetflixDisplay.setText("")
        self.txtNetflixPayment.setPlaceholderText("")
        self.comboBoxNetflixDay.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Day", None))
        self.comboBoxNetflixDay.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Day", None))
        self.comboBoxNetflixMonth.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Month", None))
        self.comboBoxNetflixMonth.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Month", None))
        self.comboBoxNetflixYear.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Year", None))
        self.comboBoxNetflixYear.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Year", None))
        self.btnSetNetflixData.setText(QCoreApplication.translate("BillyAppMain", u"Set", None))
        self.lblNetflixPaymentValue.setText(QCoreApplication.translate("BillyAppMain", u"Set the payment value:", None))
        self.lblNetflixStartDate.setText(QCoreApplication.translate("BillyAppMain", u"Set the subscription starting date:", None))
        self.lblNetflixPerMonth.setText(QCoreApplication.translate("BillyAppMain", u"Per month", None))
        self.comboBoxNetflixCurrency.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Currency", None))
        self.comboBoxNetflixCurrency.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Currency", None))
        self.lblNetflixTotalPaySinceStart.setText(QCoreApplication.translate("BillyAppMain", u"Total amount payed since the start of subscription:", None))
        self.txtNetflixTotalPayment.setPlaceholderText("")
        self.lblSpotifySelection.setText(QCoreApplication.translate("BillyAppMain", u"Spotify", None))
        self.lblSpotifySelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Audio streaming", None))
        self.btnSpotifyDisplay.setText("")
        self.lblSpotifyStartDate.setText(QCoreApplication.translate("BillyAppMain", u"Set the subscription starting date:", None))
        self.comboBoxSpotifyDay.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Day", None))
        self.comboBoxSpotifyDay.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Day", None))
        self.comboBoxSpotifyMonth.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Month", None))
        self.comboBoxSpotifyMonth.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Month", None))
        self.comboBoxSpotifyYear.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Year", None))
        self.comboBoxSpotifyYear.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Year", None))
        self.lblSpotifyPaymentValue.setText(QCoreApplication.translate("BillyAppMain", u"Set the payment value:", None))
        self.txtSpotifyPayment.setPlaceholderText("")
        self.comboBoxSpotifyCurrency.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Currency", None))
        self.comboBoxSpotifyCurrency.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Currency", None))
        self.lblSpotifyPerMonth.setText(QCoreApplication.translate("BillyAppMain", u"Per month", None))
        self.btnSetSpotifyData.setText(QCoreApplication.translate("BillyAppMain", u"Set", None))
        self.lblSpotifyTotalPaySinceStart.setText(QCoreApplication.translate("BillyAppMain", u"Total amount payed since the start of subscription:", None))
        self.txtSpotifyTotalPayment.setPlaceholderText("")
        self.lblTelecomSelection.setText(QCoreApplication.translate("BillyAppMain", u"Vodafone", None))
        self.lblTelecomSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Telecommunications", None))
        self.btnTelecomDisplay.setText("")
        self.lblTelecomStartDate.setText(QCoreApplication.translate("BillyAppMain", u"Set the subscription starting date:", None))
        self.comboBoxTelecomDay.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Day", None))
        self.comboBoxTelecomDay.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Day", None))
        self.comboBoxTelecomMonth.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Month", None))
        self.comboBoxTelecomMonth.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Month", None))
        self.comboBoxTelecomYear.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Year", None))
        self.comboBoxTelecomYear.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Year", None))
        self.lblTelecomPaymentValue.setText(QCoreApplication.translate("BillyAppMain", u"Set the payment value:", None))
        self.txtTelecomPayment.setPlaceholderText("")
        self.comboBoxTelecomCurrency.setCurrentText(QCoreApplication.translate("BillyAppMain", u"Currency", None))
        self.comboBoxTelecomCurrency.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Currency", None))
        self.lblTelecomPerMonth.setText(QCoreApplication.translate("BillyAppMain", u"Per month", None))
        self.btnSetTelecomData.setText(QCoreApplication.translate("BillyAppMain", u"Set", None))
        self.lblTelecomTotalPaySinceStart.setText(QCoreApplication.translate("BillyAppMain", u"Total amount payed since the start of subscription:", None))
        self.txtTelecomTotalPayment.setPlaceholderText("")
        self.lblSubscriptionsImpact.setText(QCoreApplication.translate("BillyAppMain", u"Subscriptions impact on monthly earnings", None))
        self.lblSubscriptionsComparison.setText(QCoreApplication.translate("BillyAppMain", u"Monthly amount to pay for each subscription", None))
        self.lblGeneralSubscriptionInformation.setText(QCoreApplication.translate("BillyAppMain", u"<html><head/><body><p>Subscriptions page: add the subscription start date and track the total amount that was payed, track the impact on monthly earnings and the price comparison</p></body></html>", None))
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
        self.btnVodafoneSelection.setText("")
        self.lblGeneralAccountInformation.setText(QCoreApplication.translate("BillyAppMain", u"<html><head/><body><p align=\"center\">Account preferences page: add the monthly earnings, select from the available electricity, natural gas, internet &amp; TV suppliers/providers and subscriptions</p></body></html>", None))
    # retranslateUi

