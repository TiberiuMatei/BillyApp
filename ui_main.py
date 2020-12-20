# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billy_uiOhuXKT.ui'
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
        self.frameLeftMenu.setFrameShape(QFrame.NoFrame)
        self.frameLeftMenu.setFrameShadow(QFrame.Raised)
        self.frameLeftMenu.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frameLeftMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameTitleLogo = QFrame(self.frameLeftMenu)
        self.frameTitleLogo.setObjectName(u"frameTitleLogo")
        self.frameTitleLogo.setMaximumSize(QSize(200, 16777215))
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
        self.frameLogo.setStyleSheet(u"image: url(:/images/Resources/billy_logo.png);")
        self.frameLogo.setFrameShape(QFrame.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Raised)
        self.frameLogo.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.frameLogo)


        self.verticalLayout.addWidget(self.frameTitleLogo)

        self.frameUsername = QFrame(self.frameLeftMenu)
        self.frameUsername.setObjectName(u"frameUsername")
        self.frameUsername.setMaximumSize(QSize(200, 16777215))
        self.frameUsername.setFrameShape(QFrame.StyledPanel)
        self.frameUsername.setFrameShadow(QFrame.Raised)
        self.frameUsername.setLineWidth(0)

        self.verticalLayout.addWidget(self.frameUsername)

        self.frameMenuContent = QFrame(self.frameLeftMenu)
        self.frameMenuContent.setObjectName(u"frameMenuContent")
        self.frameMenuContent.setMaximumSize(QSize(200, 16777215))
        self.frameMenuContent.setFrameShape(QFrame.StyledPanel)
        self.frameMenuContent.setFrameShadow(QFrame.Raised)
        self.frameMenuContent.setLineWidth(0)

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
        self.frameTitle.setFrameShape(QFrame.StyledPanel)
        self.frameTitle.setFrameShadow(QFrame.Raised)
        self.frameTitle.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.frameTitle)

        self.frameControlButtons = QFrame(self.frameHeader)
        self.frameControlButtons.setObjectName(u"frameControlButtons")
        self.frameControlButtons.setMaximumSize(QSize(120, 16777215))
        self.frameControlButtons.setFrameShape(QFrame.StyledPanel)
        self.frameControlButtons.setFrameShadow(QFrame.Raised)
        self.frameControlButtons.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frameControlButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnMinimize = QPushButton(self.frameControlButtons)
        self.btnMinimize.setObjectName(u"btnMinimize")
        font = QFont()
        font.setKerning(False)
        self.btnMinimize.setFont(font)
        self.btnMinimize.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:#510A32;\n"
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
"}\n"
"QPushButton:hover{\n"
"   background-color:#510A32;\n"
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
        self.btnMinimize.setText("")
        self.btnMaximizeRestore.setText("")
        self.btnClose.setText("")
    # retranslateUi

