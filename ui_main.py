# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billy_uizBBqFm.ui'
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
    def setupUi(self, BillyAppMain):
        if not BillyAppMain.objectName():
            BillyAppMain.setObjectName(u"BillyAppMain")
        BillyAppMain.resize(1200, 800)
        BillyAppMain.setMinimumSize(QSize(1200, 800))
        self.mainCentralWidget = QWidget(BillyAppMain)
        self.mainCentralWidget.setObjectName(u"mainCentralWidget")
        self.mainCentralWidget.setStyleSheet(u"background-color: rgb(45, 20, 44);")
        self.horizontalLayout = QHBoxLayout(self.mainCentralWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameLeftMenu = QFrame(self.mainCentralWidget)
        self.frameLeftMenu.setObjectName(u"frameLeftMenu")
        self.frameLeftMenu.setMaximumSize(QSize(200, 16777215))
        self.frameLeftMenu.setStyleSheet(u"QFrame{\n"
"   background-color: rgb(39, 43, 47);\n"
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
        self.frameLogo.setMaximumSize(QSize(16777215, 120))
        self.frameLogo.setStyleSheet(u"image: url(:/images/Resources/billy_logo.png);")
        self.frameLogo.setFrameShape(QFrame.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Raised)
        self.frameLogo.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.frameLogo)


        self.verticalLayout.addWidget(self.frameTitleLogo)

        self.frameUsername = QFrame(self.frameLeftMenu)
        self.frameUsername.setObjectName(u"frameUsername")
        self.frameUsername.setMaximumSize(QSize(200, 80))
        self.frameUsername.setFrameShape(QFrame.StyledPanel)
        self.frameUsername.setFrameShadow(QFrame.Raised)
        self.frameUsername.setLineWidth(0)

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
        self.btnDashboard.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"SF UI Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnDashboard.setFont(font)
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
        self.btnCalendar.setMaximumSize(QSize(16777215, 50))
        self.btnCalendar.setFont(font)
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
        self.btnElectricity.setMaximumSize(QSize(16777215, 50))
        self.btnElectricity.setFont(font)
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
        self.btnNaturalGas.setMaximumSize(QSize(16777215, 50))
        self.btnNaturalGas.setFont(font)
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
        self.btnInternetTV.setMaximumSize(QSize(16777215, 50))
        self.btnInternetTV.setFont(font)
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
        self.btnSubscriptions.setMaximumSize(QSize(16777215, 50))
        self.btnSubscriptions.setFont(font)
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
        self.btnProfile = QPushButton(self.frameTitle)
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
        self.btnProfile.setFlat(True)
        self.lblSetProfileName = QLabel(self.frameTitle)
        self.lblSetProfileName.setObjectName(u"lblSetProfileName")
        self.lblSetProfileName.setGeometry(QRect(40, 0, 400, 40))
        font1 = QFont()
        font1.setFamily(u"SF UI Display")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.lblSetProfileName.setFont(font1)
        self.lblSetProfileName.setCursor(QCursor(Qt.ArrowCursor))
        self.lblSetProfileName.setStyleSheet(u"color: #d0cfd0;\n"
"padding-left: 5px; \n"
"background-color:#202528;  ")

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
        font2 = QFont()
        font2.setKerning(False)
        self.btnMinimize.setFont(font2)
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
        self.stackedWidget.setGeometry(QRect(0, 0, 991, 751))
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"   background-color: rgb(32, 37, 40);\n"
"}")
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName(u"pageDashboard")
        self.lblDashTitle = QLabel(self.pageDashboard)
        self.lblDashTitle.setObjectName(u"lblDashTitle")
        self.lblDashTitle.setGeometry(QRect(30, 10, 281, 41))
        font3 = QFont()
        font3.setFamily(u"SF UI Display")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.lblDashTitle.setFont(font3)
        self.lblDashTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblDashTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageDashboard)
        self.pageCalendar = QWidget()
        self.pageCalendar.setObjectName(u"pageCalendar")
        self.lblCalendarTitle = QLabel(self.pageCalendar)
        self.lblCalendarTitle.setObjectName(u"lblCalendarTitle")
        self.lblCalendarTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblCalendarTitle.setFont(font3)
        self.lblCalendarTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblCalendarTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageCalendar)
        self.pageElectricity = QWidget()
        self.pageElectricity.setObjectName(u"pageElectricity")
        self.lblElectricityTitle = QLabel(self.pageElectricity)
        self.lblElectricityTitle.setObjectName(u"lblElectricityTitle")
        self.lblElectricityTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblElectricityTitle.setFont(font3)
        self.lblElectricityTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblElectricityTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageElectricity)
        self.pageNaturalGas = QWidget()
        self.pageNaturalGas.setObjectName(u"pageNaturalGas")
        self.lblNaturalGasTitle = QLabel(self.pageNaturalGas)
        self.lblNaturalGasTitle.setObjectName(u"lblNaturalGasTitle")
        self.lblNaturalGasTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblNaturalGasTitle.setFont(font3)
        self.lblNaturalGasTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblNaturalGasTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageNaturalGas)
        self.pageInternetTV = QWidget()
        self.pageInternetTV.setObjectName(u"pageInternetTV")
        self.lblInternetTVTitle = QLabel(self.pageInternetTV)
        self.lblInternetTVTitle.setObjectName(u"lblInternetTVTitle")
        self.lblInternetTVTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblInternetTVTitle.setFont(font3)
        self.lblInternetTVTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblInternetTVTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageInternetTV)
        self.pageSubscriptions = QWidget()
        self.pageSubscriptions.setObjectName(u"pageSubscriptions")
        self.lblSubscriptionsTitle = QLabel(self.pageSubscriptions)
        self.lblSubscriptionsTitle.setObjectName(u"lblSubscriptionsTitle")
        self.lblSubscriptionsTitle.setGeometry(QRect(30, 10, 281, 41))
        self.lblSubscriptionsTitle.setFont(font3)
        self.lblSubscriptionsTitle.setStyleSheet(u"color: #6c6e71;")
        self.lblSubscriptionsTitle.setTextFormat(Qt.MarkdownText)
        self.stackedWidget.addWidget(self.pageSubscriptions)
        self.pageProfile = QWidget()
        self.pageProfile.setObjectName(u"pageProfile")
        self.lblProfile = QLabel(self.pageProfile)
        self.lblProfile.setObjectName(u"lblProfile")
        self.lblProfile.setGeometry(QRect(30, 10, 281, 41))
        self.lblProfile.setFont(font3)
        self.lblProfile.setStyleSheet(u"color: #6c6e71;")
        self.lblProfile.setTextFormat(Qt.MarkdownText)
        self.profileName = QFrame(self.pageProfile)
        self.profileName.setObjectName(u"profileName")
        self.profileName.setGeometry(QRect(30, 80, 401, 121))
        self.profileName.setCursor(QCursor(Qt.ArrowCursor))
        self.profileName.setStyleSheet(u"QFrame{\n"
"   border-radius: 10px;    \n"
"   background-color: #2a2e32;\n"
"}")
        self.profileName.setFrameShape(QFrame.NoFrame)
        self.profileName.setFrameShadow(QFrame.Raised)
        self.lblProfileName = QLabel(self.profileName)
        self.lblProfileName.setObjectName(u"lblProfileName")
        self.lblProfileName.setGeometry(QRect(20, 10, 121, 21))
        font4 = QFont()
        font4.setFamily(u"SF UI Display")
        font4.setPointSize(14)
        self.lblProfileName.setFont(font4)
        self.lblProfileName.setStyleSheet(u"color: #d0cfd0;")
        self.txtUsername = QLineEdit(self.profileName)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setGeometry(QRect(20, 50, 280, 50))
        font5 = QFont()
        font5.setFamily(u"SF UI Display")
        font5.setPointSize(12)
        self.txtUsername.setFont(font5)
        self.txtUsername.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 60px; \n"
"   background-color:#202528;   \n"
"   background-image: url(:/images/Resources/username.png);\n"
"   background-repeat: none;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #C72C41;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.btnSetProfileName = QPushButton(self.profileName)
        self.btnSetProfileName.setObjectName(u"btnSetProfileName")
        self.btnSetProfileName.setGeometry(QRect(310, 50, 75, 50))
        self.btnSetProfileName.setFont(font)
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
        self.btnSetProfileName.setFlat(True)
        self.stackedWidget.addWidget(self.pageProfile)

        self.verticalLayout_2.addWidget(self.frameContentArea)


        self.horizontalLayout.addWidget(self.frameMainContentArea)

        BillyAppMain.setCentralWidget(self.mainCentralWidget)

        self.retranslateUi(BillyAppMain)

        QMetaObject.connectSlotsByName(BillyAppMain)
    # setupUi

    def retranslateUi(self, BillyAppMain):
        BillyAppMain.setWindowTitle(QCoreApplication.translate("BillyAppMain", u"Billy", None))
        self.btnDashboard.setText(QCoreApplication.translate("BillyAppMain", u"Dashboard", None))
        self.btnCalendar.setText(QCoreApplication.translate("BillyAppMain", u"Calendar", None))
        self.btnElectricity.setText(QCoreApplication.translate("BillyAppMain", u"Electricity", None))
        self.btnNaturalGas.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas", None))
        self.btnInternetTV.setText(QCoreApplication.translate("BillyAppMain", u"Internet && TV", None))
        self.btnSubscriptions.setText(QCoreApplication.translate("BillyAppMain", u"Subscriptions", None))
        self.btnProfile.setText("")
        self.lblSetProfileName.setText("")
        self.btnMinimize.setText("")
        self.btnMaximizeRestore.setText("")
        self.btnClose.setText("")
        self.lblDashTitle.setText(QCoreApplication.translate("BillyAppMain", u"Dashboard", None))
        self.lblCalendarTitle.setText(QCoreApplication.translate("BillyAppMain", u"Calendar", None))
        self.lblElectricityTitle.setText(QCoreApplication.translate("BillyAppMain", u"Electricity", None))
        self.lblNaturalGasTitle.setText(QCoreApplication.translate("BillyAppMain", u"Natural Gas", None))
        self.lblInternetTVTitle.setText(QCoreApplication.translate("BillyAppMain", u"Internet & TV", None))
        self.lblSubscriptionsTitle.setText(QCoreApplication.translate("BillyAppMain", u"Subscriptions", None))
        self.lblProfile.setText(QCoreApplication.translate("BillyAppMain", u"Profile", None))
        self.lblProfileName.setText(QCoreApplication.translate("BillyAppMain", u"Account user", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("BillyAppMain", u"Username", None))
        self.btnSetProfileName.setText(QCoreApplication.translate("BillyAppMain", u"Set", None))
    # retranslateUi

