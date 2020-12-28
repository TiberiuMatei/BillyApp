# GUI File
from main import *

# GLOBALS

GLOBAL_STATE = 0

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

    # RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE