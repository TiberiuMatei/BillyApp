# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billy_uiJAjcsH.ui'
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
        BillyAppMain.resize(1304, 926)
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
        self.stackedWidget.setGeometry(QRect(0, 0, 1091, 881))
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
"selection-background-color: #202528;\n"
"selection-color: #C72C41;\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"   alternate-background-color: #272b2f;\n"
"   font-size:20px;\n"
"   font-family: \"SF UI Display\";\n"
"   selection-background-color: #202528;\n"
"   selection-color: #f3f5f6;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"   font-size: 20px;\n"
"   font-family: \"SF UI Display\";\n"
"   color: #f3f5f6;\n"
"   selection-color: #f3f5f6;\n"
"   selection-background-color: #202528;\n"
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
        self.lblElectricityDirectory.setFont(font6)
        self.lblElectricityDirectory.setStyleSheet(u"color: #f3f5f6;")
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
        self.lblElectricityLastBillI.setFont(font6)
        self.lblElectricityLastBillI.setStyleSheet(u"color: #f3f5f6;")
        self.lblElectricityLastBillID = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillID.setObjectName(u"lblElectricityLastBillID")
        self.lblElectricityLastBillID.setGeometry(QRect(20, 40, 391, 31))
        font7 = QFont()
        font7.setFamily(u"SF UI Display")
        font7.setPointSize(20)
        self.lblElectricityLastBillID.setFont(font7)
        self.lblElectricityLastBillID.setStyleSheet(u"color: #EE4540;")
        self.lblElectricityLastBillAddress = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillAddress.setObjectName(u"lblElectricityLastBillAddress")
        self.lblElectricityLastBillAddress.setGeometry(QRect(20, 90, 401, 41))
        font8 = QFont()
        font8.setFamily(u"SF UI Display")
        font8.setPointSize(12)
        self.lblElectricityLastBillAddress.setFont(font8)
        self.lblElectricityLastBillAddress.setStyleSheet(u"color: #EE4540;")
        self.lblElectricityLastBilltipAddress = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBilltipAddress.setObjectName(u"lblElectricityLastBilltipAddress")
        self.lblElectricityLastBilltipAddress.setGeometry(QRect(20, 130, 166, 16))
        self.lblElectricityLastBilltipAddress.setFont(font3)
        self.lblElectricityLastBilltipAddress.setStyleSheet(u"color: #6c6e71;")
        self.lblElectricityLastBillIssueDate = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillIssueDate.setObjectName(u"lblElectricityLastBillIssueDate")
        self.lblElectricityLastBillIssueDate.setGeometry(QRect(20, 160, 301, 31))
        self.lblElectricityLastBillIssueDate.setFont(font7)
        self.lblElectricityLastBillIssueDate.setStyleSheet(u"color: #EE4540;")
        self.lblElectricityLastBilltipIssueDate = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBilltipIssueDate.setObjectName(u"lblElectricityLastBilltipIssueDate")
        self.lblElectricityLastBilltipIssueDate.setGeometry(QRect(20, 190, 166, 16))
        self.lblElectricityLastBilltipIssueDate.setFont(font3)
        self.lblElectricityLastBilltipIssueDate.setStyleSheet(u"color: #6c6e71;")
        self.lblElectricityLastBillDueDate = QLabel(self.electricityLastBillData)
        self.lblElectricityLastBillDueDate.setObjectName(u"lblElectricityLastBillDueDate")
        self.lblElectricityLastBillDueDate.setGeometry(QRect(20, 220, 301, 31))
        self.lblElectricityLastBillDueDate.setFont(font7)
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
        self.lblElectricityLastBillTotalPayInfo.setFont(font6)
        self.lblElectricityLastBillTotalPayInfo.setStyleSheet(u"color: #f3f5f6;")
        self.lblElectricityLastBillTotalPay = QLabel(self.electricityLastBillTotalPay)
        self.lblElectricityLastBillTotalPay.setObjectName(u"lblElectricityLastBillTotalPay")
        self.lblElectricityLastBillTotalPay.setGeometry(QRect(90, 40, 191, 31))
        self.lblElectricityLastBillTotalPay.setFont(font7)
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
        self.lblElectricityLastBillPlotTitle.setFont(font6)
        self.lblElectricityLastBillPlotTitle.setStyleSheet(u"color: #f3f5f6;")
        self.donutElectricityLastBill = QWidget(self.electricityLastBill)
        self.donutElectricityLastBill.setObjectName(u"donutElectricityLastBill")
        self.donutElectricityLastBill.setGeometry(QRect(0, 40, 391, 271))
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
        self.lblElectricityAllBillsPlot.setFont(font6)
        self.lblElectricityAllBillsPlot.setStyleSheet(u"color: #f3f5f6;")
        self.lineElectricityAllBillsPlot = QWidget(self.electricityBillsCosts)
        self.lineElectricityAllBillsPlot.setObjectName(u"lineElectricityAllBillsPlot")
        self.lineElectricityAllBillsPlot.setGeometry(QRect(0, 40, 651, 271))
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
        self.lblNaturalGasSupplierSelection.setFont(font6)
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
        self.btnNaturalGasSupplierDisplay.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.lblNaturalGasDirectoryInfo.setGeometry(QRect(20, 40, 231, 16))
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
        self.lblNaturalGasDirectory.setGeometry(QRect(20, 10, 132, 23))
        self.lblNaturalGasDirectory.setMaximumSize(QSize(200, 16777215))
        self.lblNaturalGasDirectory.setFont(font6)
        self.lblNaturalGasDirectory.setStyleSheet(u"color: #f3f5f6;")
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
        self.lblNaturalGasLastBillI.setFont(font6)
        self.lblNaturalGasLastBillI.setStyleSheet(u"color: #f3f5f6;")
        self.lblNaturalGasLastBillID = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillID.setObjectName(u"lblNaturalGasLastBillID")
        self.lblNaturalGasLastBillID.setGeometry(QRect(20, 40, 391, 31))
        self.lblNaturalGasLastBillID.setFont(font7)
        self.lblNaturalGasLastBillID.setStyleSheet(u"color: #EE4540;")
        self.lblNaturalGasLastBillAddress = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillAddress.setObjectName(u"lblNaturalGasLastBillAddress")
        self.lblNaturalGasLastBillAddress.setGeometry(QRect(20, 100, 401, 51))
        self.lblNaturalGasLastBillAddress.setFont(font8)
        self.lblNaturalGasLastBillAddress.setStyleSheet(u"color: #EE4540;")
        self.lblNaturalGasLastBilltipAddress = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBilltipAddress.setObjectName(u"lblNaturalGasLastBilltipAddress")
        self.lblNaturalGasLastBilltipAddress.setGeometry(QRect(20, 150, 166, 16))
        self.lblNaturalGasLastBilltipAddress.setFont(font3)
        self.lblNaturalGasLastBilltipAddress.setStyleSheet(u"color: #6c6e71;")
        self.lblNaturalGasLastBillIssueDate = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillIssueDate.setObjectName(u"lblNaturalGasLastBillIssueDate")
        self.lblNaturalGasLastBillIssueDate.setGeometry(QRect(20, 170, 301, 31))
        self.lblNaturalGasLastBillIssueDate.setFont(font7)
        self.lblNaturalGasLastBillIssueDate.setStyleSheet(u"color: #EE4540;")
        self.lblNaturalGasLastBilltipIssueDate = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBilltipIssueDate.setObjectName(u"lblNaturalGasLastBilltipIssueDate")
        self.lblNaturalGasLastBilltipIssueDate.setGeometry(QRect(20, 200, 166, 16))
        self.lblNaturalGasLastBilltipIssueDate.setFont(font3)
        self.lblNaturalGasLastBilltipIssueDate.setStyleSheet(u"color: #6c6e71;")
        self.lblNaturalGasLastBillDueDate = QLabel(self.naturalGasLastBillData)
        self.lblNaturalGasLastBillDueDate.setObjectName(u"lblNaturalGasLastBillDueDate")
        self.lblNaturalGasLastBillDueDate.setGeometry(QRect(20, 230, 301, 31))
        self.lblNaturalGasLastBillDueDate.setFont(font7)
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
        self.lblNaturalGasLastBillTotalPayInfo.setFont(font6)
        self.lblNaturalGasLastBillTotalPayInfo.setStyleSheet(u"color: #f3f5f6;")
        self.lblNaturalGasLastBillTotalPay = QLabel(self.naturalGasLastBillTotalPay)
        self.lblNaturalGasLastBillTotalPay.setObjectName(u"lblNaturalGasLastBillTotalPay")
        self.lblNaturalGasLastBillTotalPay.setGeometry(QRect(90, 40, 191, 31))
        self.lblNaturalGasLastBillTotalPay.setFont(font7)
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
        self.lblNaturalGasLastBillPlotTitle.setFont(font6)
        self.lblNaturalGasLastBillPlotTitle.setStyleSheet(u"color: #f3f5f6;")
        self.donutNaturalGasLastBill = QWidget(self.naturalGasLastBill)
        self.donutNaturalGasLastBill.setObjectName(u"donutNaturalGasLastBill")
        self.donutNaturalGasLastBill.setGeometry(QRect(0, 40, 391, 271))
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
        self.lblNaturalAllBillsPlot.setFont(font6)
        self.lblNaturalAllBillsPlot.setStyleSheet(u"color: #f3f5f6;")
        self.lineNaturalGasAllBillsPlot = QWidget(self.naturalGasBillsCosts)
        self.lineNaturalGasAllBillsPlot.setObjectName(u"lineNaturalGasAllBillsPlot")
        self.lineNaturalGasAllBillsPlot.setGeometry(QRect(0, 40, 651, 271))
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
        self.lblInternetProviderSelection.setFont(font6)
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
        self.btnInternetProviderDisplay.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.lblInternetTVDirectory.setFont(font6)
        self.lblInternetTVDirectory.setStyleSheet(u"color: #f3f5f6;")
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
        self.lblInternetTVLastBillI.setFont(font6)
        self.lblInternetTVLastBillI.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetTVLastBillID = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillID.setObjectName(u"lblInternetTVLastBillID")
        self.lblInternetTVLastBillID.setGeometry(QRect(20, 40, 391, 31))
        self.lblInternetTVLastBillID.setFont(font7)
        self.lblInternetTVLastBillID.setStyleSheet(u"color: #EE4540;")
        self.lblInternetTVLastBillAddress = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillAddress.setObjectName(u"lblInternetTVLastBillAddress")
        self.lblInternetTVLastBillAddress.setGeometry(QRect(20, 100, 401, 51))
        self.lblInternetTVLastBillAddress.setFont(font8)
        self.lblInternetTVLastBillAddress.setStyleSheet(u"color: #EE4540;")
        self.lblInternetTVLastBilltipAddress = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBilltipAddress.setObjectName(u"lblInternetTVLastBilltipAddress")
        self.lblInternetTVLastBilltipAddress.setGeometry(QRect(20, 140, 166, 16))
        self.lblInternetTVLastBilltipAddress.setFont(font3)
        self.lblInternetTVLastBilltipAddress.setStyleSheet(u"color: #6c6e71;")
        self.lblInternetTVLastBillIssueDate = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillIssueDate.setObjectName(u"lblInternetTVLastBillIssueDate")
        self.lblInternetTVLastBillIssueDate.setGeometry(QRect(20, 170, 301, 31))
        self.lblInternetTVLastBillIssueDate.setFont(font7)
        self.lblInternetTVLastBillIssueDate.setStyleSheet(u"color: #EE4540;")
        self.lblInternetTVLastBilltipIssueDate = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBilltipIssueDate.setObjectName(u"lblInternetTVLastBilltipIssueDate")
        self.lblInternetTVLastBilltipIssueDate.setGeometry(QRect(20, 200, 166, 16))
        self.lblInternetTVLastBilltipIssueDate.setFont(font3)
        self.lblInternetTVLastBilltipIssueDate.setStyleSheet(u"color: #6c6e71;")
        self.lblInternetTVLastBillDueDate = QLabel(self.internetTVLastBillData)
        self.lblInternetTVLastBillDueDate.setObjectName(u"lblInternetTVLastBillDueDate")
        self.lblInternetTVLastBillDueDate.setGeometry(QRect(20, 230, 301, 31))
        self.lblInternetTVLastBillDueDate.setFont(font7)
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
        self.lblInternetTVLastBillTotalPayInfo.setFont(font6)
        self.lblInternetTVLastBillTotalPayInfo.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetTVLastBillTotalPay = QLabel(self.internetTVLastBillTotalPay)
        self.lblInternetTVLastBillTotalPay.setObjectName(u"lblInternetTVLastBillTotalPay")
        self.lblInternetTVLastBillTotalPay.setGeometry(QRect(90, 40, 191, 31))
        self.lblInternetTVLastBillTotalPay.setFont(font7)
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
        self.lblInternetTVLastBillPlotTitle.setFont(font6)
        self.lblInternetTVLastBillPlotTitle.setStyleSheet(u"color: #f3f5f6;")
        self.donutInternetTVLastBill = QWidget(self.internetTVLastBill)
        self.donutInternetTVLastBill.setObjectName(u"donutInternetTVLastBill")
        self.donutInternetTVLastBill.setGeometry(QRect(0, 40, 391, 271))
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
        self.lblTestInternetSpeed.setFont(font6)
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
        self.lblTestInternetPing.setFont(font6)
        self.lblTestInternetPing.setStyleSheet(u"color: #C72C41;")
        self.lblTestInternetDownload = QLabel(self.internetSpeedtest)
        self.lblTestInternetDownload.setObjectName(u"lblTestInternetDownload")
        self.lblTestInternetDownload.setGeometry(QRect(70, 130, 101, 23))
        self.lblTestInternetDownload.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetDownload.setFont(font6)
        self.lblTestInternetDownload.setStyleSheet(u"color: #C72C41;")
        self.lblTestInternetUpload = QLabel(self.internetSpeedtest)
        self.lblTestInternetUpload.setObjectName(u"lblTestInternetUpload")
        self.lblTestInternetUpload.setGeometry(QRect(70, 185, 71, 23))
        self.lblTestInternetUpload.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetUpload.setFont(font6)
        self.lblTestInternetUpload.setStyleSheet(u"color: #C72C41;")
        self.lblTestInternetPingData = QLabel(self.internetSpeedtest)
        self.lblTestInternetPingData.setObjectName(u"lblTestInternetPingData")
        self.lblTestInternetPingData.setGeometry(QRect(125, 75, 181, 23))
        self.lblTestInternetPingData.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetPingData.setFont(font6)
        self.lblTestInternetPingData.setStyleSheet(u"color: #f3f5f6;")
        self.lblTestInternetDownloadData = QLabel(self.internetSpeedtest)
        self.lblTestInternetDownloadData.setObjectName(u"lblTestInternetDownloadData")
        self.lblTestInternetDownloadData.setGeometry(QRect(175, 130, 151, 23))
        self.lblTestInternetDownloadData.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetDownloadData.setFont(font6)
        self.lblTestInternetDownloadData.setStyleSheet(u"color: #f3f5f6;")
        self.lblTestInternetUploadData = QLabel(self.internetSpeedtest)
        self.lblTestInternetUploadData.setObjectName(u"lblTestInternetUploadData")
        self.lblTestInternetUploadData.setGeometry(QRect(150, 185, 181, 23))
        self.lblTestInternetUploadData.setMaximumSize(QSize(500, 16777215))
        self.lblTestInternetUploadData.setFont(font6)
        self.lblTestInternetUploadData.setStyleSheet(u"color: #f3f5f6;")
        self.lblInternetSpeedAdditionalInfo = QLabel(self.internetSpeedtest)
        self.lblInternetSpeedAdditionalInfo.setObjectName(u"lblInternetSpeedAdditionalInfo")
        self.lblInternetSpeedAdditionalInfo.setGeometry(QRect(20, 37, 291, 16))
        self.lblInternetSpeedAdditionalInfo.setFont(font3)
        self.lblInternetSpeedAdditionalInfo.setStyleSheet(u"color: #6c6e71;")
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
        self.txtUsername.setFont(font8)
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
        self.txtEarnings.setFont(font8)
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
        self.stackedWidget.addWidget(self.pageProfile)

        self.verticalLayout_2.addWidget(self.frameContentArea)


        self.horizontalLayout.addWidget(self.frameMainContentArea)

        BillyAppMain.setCentralWidget(self.mainCentralWidget)

        self.retranslateUi(BillyAppMain)

        self.btnDashboard.setDefault(False)
        self.electricityLegendIssueColor.setDefault(False)
        self.electricityLegendDueColor.setDefault(False)
        self.naturalGasLegendIssueColor.setDefault(False)
        self.naturalGasLegendDueColor.setDefault(False)
        self.internetTVLegendIssueColor.setDefault(False)
        self.internetTVLegendDueColor.setDefault(False)
        self.btnElectricitySupplierDisplay.setDefault(False)
        self.btnAddElectricityBill.setDefault(False)
        self.btnNaturalGasSupplierDisplay.setDefault(False)
        self.btnAddNaturalGasBill.setDefault(False)
        self.btnInternetProviderDisplay.setDefault(False)
        self.btnAddInternetTVBill.setDefault(False)
        self.btnTestInternetSpeed.setDefault(False)
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
        self.lblCalendarTitle.setText(QCoreApplication.translate("BillyAppMain", u"Calendar", None))
        self.electricityLegendIssueColor.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Issue Day", None))
        self.electricityLegendDueColor.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Due Day", None))
        self.naturalGasLegendIssueColor.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas Issue Day", None))
        self.naturalGasLegendDueColor.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas Due Day", None))
        self.internetTVLegendIssueColor.setText(QCoreApplication.translate("BillyAppMain", u"Internet TV Issue Day", None))
        self.internetTVLegendDueColor.setText(QCoreApplication.translate("BillyAppMain", u"Internet TV Due Day", None))
        self.lblElectricityTitle.setText(QCoreApplication.translate("BillyAppMain", u"Electricity", None))
        self.lblElectricitySupplierSelection.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Supplier", None))
        self.lblElectricitySupplierSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Selected electricity supplier", None))
        self.btnElectricitySupplierDisplay.setText("")
        self.lblElectricityDirectoryInfo.setText(QCoreApplication.translate("BillyAppMain", u"Management of added electricity bills", None))
        self.btnAddElectricityBill.setText(QCoreApplication.translate("BillyAppMain", u"Add", None))
        self.lblElectricityDirectory.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Bills", None))
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
        self.lblNaturalGasTitle.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas", None))
        self.lblNaturalGasSupplierSelection.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas Supplier", None))
        self.lblNaturalGasSupplierSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Selected natural gas supplier", None))
        self.btnNaturalGasSupplierDisplay.setText("")
        self.lblNaturalGasDirectoryInfo.setText(QCoreApplication.translate("BillyAppMain", u"Management of added electricity bills", None))
        self.btnAddNaturalGasBill.setText(QCoreApplication.translate("BillyAppMain", u"Add", None))
        self.lblNaturalGasDirectory.setText(QCoreApplication.translate("BillyAppMain", u"Electricity Bills", None))
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
        self.lblInternetTVTitle.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV", None))
        self.lblInternetProviderSelection.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV Provider", None))
        self.lblInternetProviderSelectionInfo.setText(QCoreApplication.translate("BillyAppMain", u"Selected internet & TV provider", None))
        self.btnInternetProviderDisplay.setText("")
        self.lblInternetTVDirectoryInfo.setText(QCoreApplication.translate("BillyAppMain", u"Management of added internet & TV bills", None))
        self.btnAddInternetTVBill.setText(QCoreApplication.translate("BillyAppMain", u"Add", None))
        self.lblInternetTVDirectory.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV Bills", None))
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
        self.btnVodafoneSelection.setText("")
    # retranslateUi

