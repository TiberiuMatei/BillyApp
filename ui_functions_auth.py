# GUI File
from main import *

# GLOBALS

GLOBAL_STATE = 0

class UIFunctionsAuth(MainWindowAuth): 

    #  UI DEFINITIONS
    def uiDefinitionsAuth(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #####################
        # APP TOOLTIP SECTION
        #####################

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.mainAuthWidget.setGraphicsEffect(self.shadow)

        # MINIMIZE
        self.ui.btnMinimizeAuth.clicked.connect(lambda: self.showMinimized())
        self.ui.btnMinimizeAuth.setToolTip("Minimize")

        # CLOSE
        self.ui.btnCloseAuth.clicked.connect(lambda: self.close())
        self.ui.btnCloseAuth.setToolTip("Close")