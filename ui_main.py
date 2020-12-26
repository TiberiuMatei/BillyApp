# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billy_uiBmqimj.ui'
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
        self.frameLogo.setMaximumSize(QSize(16777215, 140))
        self.frameLogo.setStyleSheet(u"image: url(:/images/Resources/billy_logo.png);")
        self.frameLogo.setFrameShape(QFrame.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Raised)
        self.frameLogo.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.frameLogo)


        self.verticalLayout.addWidget(self.frameTitleLogo)

        self.frameUsername = QFrame(self.frameLeftMenu)
        self.frameUsername.setObjectName(u"frameUsername")
        self.frameUsername.setMaximumSize(QSize(200, 60))
        self.frameUsername.setFrameShape(QFrame.StyledPanel)
        self.frameUsername.setFrameShadow(QFrame.Raised)
        self.frameUsername.setLineWidth(0)

        self.verticalLayout.addWidget(self.frameUsername)

        self.frameMenuContent = QFrame(self.frameLeftMenu)
        self.frameMenuContent.setObjectName(u"frameMenuContent")
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
        self.frameMenuContent.setFrameShadow(QFrame.Raised)
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
        font.setFamily(u"SF Pro Display")
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
        self.frameTitle.setStyleSheet(u"QFrame{\n"
"   background-color: rgb(32, 37, 40);\n"
"}")
        self.frameTitle.setFrameShape(QFrame.NoFrame)
        self.frameTitle.setFrameShadow(QFrame.Raised)
        self.frameTitle.setLineWidth(0)

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
        font1 = QFont()
        font1.setKerning(False)
        self.btnMinimize.setFont(font1)
        self.btnMinimize.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: rgb(32, 37, 40);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:#2a2e32;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/Resources/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMinimize.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u":/images/Resources/maximize_restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMaximizeRestore.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/images/Resources/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClose.setIcon(icon2)
        self.btnClose.setIconSize(QSize(40, 40))
        self.btnClose.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnClose)


        self.horizontalLayout_2.addWidget(self.frameControlButtons)


        self.verticalLayout_2.addWidget(self.frameHeader)

        self.frameContentArea = QFrame(self.frameMainContentArea)
        self.frameContentArea.setObjectName(u"frameContentArea")
        self.frameContentArea.setStyleSheet(u"QFrame{\n"
"   background-color: rgb(32, 37, 40);\n"
"}")
        self.frameContentArea.setFrameShape(QFrame.StyledPanel)
        self.frameContentArea.setFrameShadow(QFrame.Raised)
        self.frameContentArea.setLineWidth(0)

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
        self.btnMinimize.setText("")
        self.btnMaximizeRestore.setText("")
        self.btnClose.setText("")
    # retranslateUi

