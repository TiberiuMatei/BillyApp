# -*- coding: utf-8 -*-

############################
## Main app auth page design
############################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import billy_app_qrc

class Ui_BillyAuth(object):
    def setupUi(self, BillyAuth):
        if not BillyAuth.objectName():
            BillyAuth.setObjectName(u"BillyAuth")
        BillyAuth.resize(531, 800)
        self.mainAuthWidget = QWidget(BillyAuth)
        self.mainAuthWidget.setObjectName(u"mainAuthWidget")
        self.mainAuthWidget.setStyleSheet(u"background-color: rgb(32, 37, 40);\n"
"outline: none;")
        self.verticalLayout = QVBoxLayout(self.mainAuthWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.authHeader = QFrame(self.mainAuthWidget)
        self.authHeader.setObjectName(u"authHeader")
        self.authHeader.setMaximumSize(QSize(16777215, 300))
        self.authHeader.setFrameShape(QFrame.NoFrame)
        self.authHeader.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.authHeader)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.authControl = QFrame(self.authHeader)
        self.authControl.setObjectName(u"authControl")
        self.authControl.setMinimumSize(QSize(0, 0))
        self.authControl.setMaximumSize(QSize(16777215, 40))
        self.authControl.setFrameShape(QFrame.StyledPanel)
        self.authControl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.authControl)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.authDrag = QFrame(self.authControl)
        self.authDrag.setObjectName(u"authDrag")
        self.authDrag.setMaximumSize(QSize(16777215, 40))
        self.authDrag.setFrameShape(QFrame.StyledPanel)
        self.authDrag.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.authDrag)

        self.authControlButtons = QFrame(self.authControl)
        self.authControlButtons.setObjectName(u"authControlButtons")
        self.authControlButtons.setMaximumSize(QSize(80, 40))
        self.authControlButtons.setFrameShape(QFrame.StyledPanel)
        self.authControlButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.authControlButtons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnMinimizeAuth = QPushButton(self.authControlButtons)
        self.btnMinimizeAuth.setObjectName(u"btnMinimizeAuth")
        font = QFont()
        font.setKerning(False)
        self.btnMinimizeAuth.setFont(font)
        self.btnMinimizeAuth.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: rgb(32, 37, 40);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:#2a2e32;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/Resources/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMinimizeAuth.setIcon(icon)
        self.btnMinimizeAuth.setIconSize(QSize(40, 40))
        self.btnMinimizeAuth.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnMinimizeAuth)

        self.btnCloseAuth = QPushButton(self.authControlButtons)
        self.btnCloseAuth.setObjectName(u"btnCloseAuth")
        self.btnCloseAuth.setStyleSheet(u"QPushButton{\n"
"   border: none;\n"
"   background-color: rgb(32, 37, 40);\n"
"}\n"
"QPushButton:hover{\n"
"   background-color:#C72C41;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/Resources/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCloseAuth.setIcon(icon1)
        self.btnCloseAuth.setIconSize(QSize(40, 40))
        self.btnCloseAuth.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnCloseAuth)


        self.horizontalLayout.addWidget(self.authControlButtons)


        self.verticalLayout_2.addWidget(self.authControl)

        self.authLogo = QFrame(self.authHeader)
        self.authLogo.setObjectName(u"authLogo")
        self.authLogo.setMaximumSize(QSize(16777215, 260))
        self.authLogo.setStyleSheet(u"background-image: url(:/images/Resources/billy_full_logo_auth.png);\n"
"background-repeat: none;\n"
"background-position: center;")
        self.authLogo.setFrameShape(QFrame.StyledPanel)
        self.authLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.authLogo)


        self.verticalLayout.addWidget(self.authHeader)

        self.authButtons = QFrame(self.mainAuthWidget)
        self.authButtons.setObjectName(u"authButtons")
        self.authButtons.setMaximumSize(QSize(16777215, 100))
        self.authButtons.setFrameShape(QFrame.StyledPanel)
        self.authButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.authButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnSignInSelection = QPushButton(self.authButtons)
        self.btnSignInSelection.setObjectName(u"btnSignInSelection")
        self.btnSignInSelection.setMaximumSize(QSize(100, 50))
        font1 = QFont()
        font1.setFamily(u"SF UI Display")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnSignInSelection.setFont(font1)
        self.btnSignInSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSignInSelection.setStyleSheet(u"QPushButton{\n"
"   background-image: url(:/images/Resources/sign_in.png);\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:checked\n"
"{  \n"
"   background-image: url(:/images/Resources/sign_in_selected.png);\n"
"}")
        self.btnSignInSelection.setCheckable(True)
        self.btnSignInSelection.setChecked(True)
        self.btnSignInSelection.setAutoDefault(True)
        self.btnSignInSelection.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnSignInSelection)

        self.btnSignUpSelection = QPushButton(self.authButtons)
        self.btnSignUpSelection.setObjectName(u"btnSignUpSelection")
        self.btnSignUpSelection.setMaximumSize(QSize(100, 50))
        self.btnSignUpSelection.setFont(font1)
        self.btnSignUpSelection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSignUpSelection.setStyleSheet(u"QPushButton{\n"
"   background-image: url(:/images/Resources/sign_up.png);\n"
"   border-radius: 5px;\n"
"}\n"
"QPushButton:checked\n"
"{  \n"
"   background-image: url(:/images/Resources/sign_up_selected.png);\n"
"}")
        self.btnSignUpSelection.setCheckable(True)
        self.btnSignUpSelection.setAutoDefault(True)
        self.btnSignUpSelection.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btnSignUpSelection)


        self.verticalLayout.addWidget(self.authButtons)

        self.authFields = QFrame(self.mainAuthWidget)
        self.authFields.setObjectName(u"authFields")
        self.authFields.setFrameShape(QFrame.StyledPanel)
        self.authFields.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.authFields)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, -1, 511, 331))
        self.signInPage = QWidget()
        self.signInPage.setObjectName(u"signInPage")
        self.txtSignInUsername = QLineEdit(self.signInPage)
        self.txtSignInUsername.setObjectName(u"txtSignInUsername")
        self.txtSignInUsername.setGeometry(QRect(110, 60, 300, 50))
        font2 = QFont()
        font2.setFamily(u"SF UI Display")
        font2.setPointSize(12)
        self.txtSignInUsername.setFont(font2)
        self.txtSignInUsername.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 70px; \n"
"   background-color:#202528;   \n"
"   background-image: url(:/images/Resources/username.png);\n"
"   background-repeat: none;\n"
"   background-position: center;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.txtSignInPassword = QLineEdit(self.signInPage)
        self.txtSignInPassword.setObjectName(u"txtSignInPassword")
        self.txtSignInPassword.setGeometry(QRect(110, 150, 300, 50))
        self.txtSignInPassword.setFont(font2)
        self.txtSignInPassword.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 70px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/password.png);\n"
"   background-repeat: none;\n"
"   background-position: center;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.txtSignInPassword.setEchoMode(QLineEdit.Password)
        self.btnSignIn = QPushButton(self.signInPage)
        self.btnSignIn.setObjectName(u"btnSignIn")
        self.btnSignIn.setGeometry(QRect(110, 240, 300, 50))
        self.btnSignIn.setFont(font1)
        self.btnSignIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSignIn.setStyleSheet(u"QPushButton{\n"
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
        self.btnSignIn.setAutoDefault(True)
        self.btnSignIn.setFlat(True)
        self.stackedWidget.addWidget(self.signInPage)
        self.signUpPage = QWidget()
        self.signUpPage.setObjectName(u"signUpPage")
        self.txtSignUpEmail = QLineEdit(self.signUpPage)
        self.txtSignUpEmail.setObjectName(u"txtSignUpEmail")
        self.txtSignUpEmail.setGeometry(QRect(110, 30, 300, 50))
        self.txtSignUpEmail.setFont(font2)
        self.txtSignUpEmail.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 70px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/email.png);\n"
"   background-repeat: none;\n"
"   background-position: center;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.txtSignUpUsername = QLineEdit(self.signUpPage)
        self.txtSignUpUsername.setObjectName(u"txtSignUpUsername")
        self.txtSignUpUsername.setGeometry(QRect(110, 110, 300, 50))
        self.txtSignUpUsername.setFont(font2)
        self.txtSignUpUsername.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 70px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/username.png);\n"
"   background-repeat: none;\n"
"   background-position: center;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.txtSignUpPassword = QLineEdit(self.signUpPage)
        self.txtSignUpPassword.setObjectName(u"txtSignUpPassword")
        self.txtSignUpPassword.setGeometry(QRect(110, 190, 300, 50))
        self.txtSignUpPassword.setFont(font2)
        self.txtSignUpPassword.setStyleSheet(u"QLineEdit{\n"
"   border: 2px solid #272b2f;\n"
"   border-radius: 5px;\n"
"   color: #d0cfd0;\n"
"   padding-left: 70px; \n"
"   background-color:#202528;\n"
"   background-image: url(:/images/Resources/password.png);\n"
"   background-repeat: none;\n"
"   background-position: center;\n"
"}\n"
"QLineEdit:hover{\n"
"   border: 2px solid #EE4540;\n"
"}\n"
"QLineEdit:focus{\n"
"   border: 2px solid #EE4540;\n"
"}")
        self.txtSignUpPassword.setEchoMode(QLineEdit.Password)
        self.btnSignUp = QPushButton(self.signUpPage)
        self.btnSignUp.setObjectName(u"btnSignUp")
        self.btnSignUp.setGeometry(QRect(110, 270, 300, 50))
        self.btnSignUp.setFont(font1)
        self.btnSignUp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSignUp.setStyleSheet(u"QPushButton{\n"
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
        self.btnSignUp.setAutoDefault(True)
        self.btnSignUp.setFlat(True)
        self.stackedWidget.addWidget(self.signUpPage)

        self.verticalLayout.addWidget(self.authFields)

        self.authInfo = QFrame(self.mainAuthWidget)
        self.authInfo.setObjectName(u"authInfo")
        self.authInfo.setMaximumSize(QSize(16777215, 60))
        self.authInfo.setFrameShape(QFrame.StyledPanel)
        self.authInfo.setFrameShadow(QFrame.Raised)
        self.lblAppVersion = QLabel(self.authInfo)
        self.lblAppVersion.setObjectName(u"lblAppVersion")
        self.lblAppVersion.setGeometry(QRect(150, 20, 231, 21))
        font3 = QFont()
        font3.setFamily(u"SF UI Display")
        font3.setPointSize(10)
        self.lblAppVersion.setFont(font3)
        self.lblAppVersion.setStyleSheet(u"color: #6c6e71;")
        self.lblAppVersion.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.authInfo)

        BillyAuth.setCentralWidget(self.mainAuthWidget)

        self.retranslateUi(BillyAuth)

        self.btnSignInSelection.setDefault(False)
        self.btnSignUpSelection.setDefault(False)
        self.btnSignIn.setDefault(False)
        self.btnSignUp.setDefault(False)


        QMetaObject.connectSlotsByName(BillyAuth)
    # setupUi

    def retranslateUi(self, BillyAuth):
        BillyAuth.setWindowTitle(QCoreApplication.translate("BillyAuth", u"MainWindow", None))
        self.btnMinimizeAuth.setText("")
        self.btnCloseAuth.setText("")
        self.btnSignInSelection.setText("")
        self.btnSignUpSelection.setText("")
        self.txtSignInUsername.setPlaceholderText(QCoreApplication.translate("BillyAuth", u"Username", None))
        self.txtSignInPassword.setPlaceholderText(QCoreApplication.translate("BillyAuth", u"Password", None))
        self.btnSignIn.setText(QCoreApplication.translate("BillyAuth", u"Sign In", None))
        self.txtSignUpEmail.setPlaceholderText(QCoreApplication.translate("BillyAuth", u"Email", None))
        self.txtSignUpUsername.setPlaceholderText(QCoreApplication.translate("BillyAuth", u"Username", None))
        self.txtSignUpPassword.setPlaceholderText(QCoreApplication.translate("BillyAuth", u"Password", None))
        self.btnSignUp.setText(QCoreApplication.translate("BillyAuth", u"Sign Up", None))
        self.lblAppVersion.setText(QCoreApplication.translate("BillyAuth", u"v1.0", None))
    # retranslateUi

