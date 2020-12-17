# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billy_uiTwBbes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import billy_app_rc

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
        self.verticalLayout = QVBoxLayout(self.frameLeftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameLogo = QFrame(self.frameLeftMenu)
        self.frameLogo.setObjectName(u"frameLogo")
        self.frameLogo.setMaximumSize(QSize(200, 16777215))
        self.frameLogo.setStyleSheet(u"image: url(:/images/Resources/billy_logo.png);")
        self.frameLogo.setFrameShape(QFrame.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frameLogo)

        self.frameUsername = QFrame(self.frameLeftMenu)
        self.frameUsername.setObjectName(u"frameUsername")
        self.frameUsername.setMaximumSize(QSize(200, 16777215))
        self.frameUsername.setFrameShape(QFrame.StyledPanel)
        self.frameUsername.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frameUsername)

        self.frameMenuContent = QFrame(self.frameLeftMenu)
        self.frameMenuContent.setObjectName(u"frameMenuContent")
        self.frameMenuContent.setMaximumSize(QSize(200, 16777215))
        self.frameMenuContent.setFrameShape(QFrame.StyledPanel)
        self.frameMenuContent.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frameMenuContent)


        self.horizontalLayout.addWidget(self.frameLeftMenu)

        self.frameMainContentArea = QFrame(self.mainCentralWidget)
        self.frameMainContentArea.setObjectName(u"frameMainContentArea")
        self.frameMainContentArea.setFrameShape(QFrame.NoFrame)
        self.frameMainContentArea.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frameMainContentArea)

        BillyAppMain.setCentralWidget(self.mainCentralWidget)

        self.retranslateUi(BillyAppMain)

        QMetaObject.connectSlotsByName(BillyAppMain)
    # setupUi

    def retranslateUi(self, BillyAppMain):
        BillyAppMain.setWindowTitle(QCoreApplication.translate("BillyAppMain", u"Billy", None))
    # retranslateUi

