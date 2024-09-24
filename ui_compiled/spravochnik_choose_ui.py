# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spravochnik_choose.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget, QDialog)

from ui_compiled import spravochnik_customers_ui, spravochnik_papers_ui, spravochnik_investments_ui


class Ui_Form(object):
    def open_papers(self):  # opens hyety nesysvetnyu
        self.window = QDialog()
        self.ui = spravochnik_papers_ui.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_investments(self):  # opens hyety nesysvetnyu
        self.window = QDialog()
        self.ui = spravochnik_investments_ui.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_customers(self):  # opens hyety nesysvetnyu
        self.window = QDialog()
        self.ui = spravochnik_customers_ui.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(346, 388)
        self.clientsPushButton = QPushButton(Form, clicked= lambda:self.open_customers())
        self.clientsPushButton.setObjectName(u"clientsPushButton")
        self.clientsPushButton.setGeometry(QRect(124, 110, 141, 24))
        self.papersPushButton = QPushButton(Form, clicked= lambda:self.open_papers())
        self.papersPushButton.setObjectName(u"papersPushButton")
        self.papersPushButton.setGeometry(QRect(120, 150, 151, 24))
        self.investmentPushButton = QPushButton(Form, clicked= lambda:self.open_investments())
        self.investmentPushButton.setObjectName(u"investmentPushButton")
        self.investmentPushButton.setGeometry(QRect(130, 190, 151, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.clientsPushButton.setText(QCoreApplication.translate("Form", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.papersPushButton.setText(QCoreApplication.translate("Form", u"\u0411\u0443\u043c\u0430\u0433\u0438 ", None))
        self.investmentPushButton.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u0438", None))
    # retranslateUi

