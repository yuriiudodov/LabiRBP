# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QWidget, QDialog)
from ui_compiled import spravochnik_choose_ui, graph_builder_ui


class Ui_MainWindow(object):
    def open_graphic_builder(self):
        self.window = QDialog()
        self.ui = graph_builder_ui.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_spravochniki_choose(self):  # opens hyety nesysvetnyu
        self.window = QDialog()
        self.ui = spravochnik_choose_ui.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.middlePushButton = QPushButton(self.centralwidget, clicked = lambda:self.open_spravochniki_choose())##spravichniki
        self.middlePushButton.setObjectName(u"middlePushButton")

        self.gridLayout.addWidget(self.middlePushButton, 2, 1, 1, 1)

        self.lowerPushButton = QPushButton(self.centralwidget)
        self.lowerPushButton.setObjectName(u"lowerPushButton")

        self.gridLayout.addWidget(self.lowerPushButton, 3, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.upperPushButton = QPushButton(self.centralwidget,clicked = lambda:self.open_graphic_builder())
        self.upperPushButton.setObjectName(u"upperPushButton")

        self.gridLayout.addWidget(self.upperPushButton, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.middlePushButton.setText("Справочники")
        self.lowerPushButton.setText(QCoreApplication.translate("MainWindow", u"\u043b\u0430\u0431\u0430 1488", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.upperPushButton.setText("Построить график")
    # retranslateUi

