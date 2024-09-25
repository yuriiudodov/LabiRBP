# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_add.ui'
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
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

from settings import DB_PATH


class Ui_Form(object):
    def add_customer_to_db(self):
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        vet_query_str = (f'INSERT INTO customers (name, property_type, address, phone) VALUES '
                         f"('{self.nameLineEdit.text()}','{self.propertyLineEdit.text()}','{self.addressLineEdit.text()}', '{self.addressLineEdit.text()}')")
        VetTableQuery.prepare(vet_query_str)
        #VetTableQuery.bindValue(":name", self.nameLineEdit.text())
        #VetTableQuery.bindValue(":property_type", self.propertyLineEdit.text())
        #VetTableQuery.bindValue(":address",self.addressLineEdit.text())
        #VetTableQuery.bindValue(":phone", self.phoneLineEdit.text())
        print(vet_query_str)
        uspeh = VetTableQuery.exec()
        VetDbConnnection.close()
        print("uspeh& customer", uspeh)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(622, 469)
        self.confirmPushButton = QPushButton(Form, clicked = lambda :self.add_customer_to_db())
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setGeometry(QRect(10, 420, 141, 41))
        self.cancelPushButton = QPushButton(Form)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(470, 420, 141, 41))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 251, 61))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 140, 49, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 170, 111, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 200, 111, 16))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 230, 111, 16))
        self.nameLineEdit = QLineEdit(Form)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(150, 140, 113, 21))
        self.propertyLineEdit = QLineEdit(Form)
        self.propertyLineEdit.setObjectName(u"propertyLineEdit")
        self.propertyLineEdit.setGeometry(QRect(180, 170, 113, 21))
        self.addressLineEdit = QLineEdit(Form)
        self.addressLineEdit.setObjectName(u"addressLineEdit")
        self.addressLineEdit.setGeometry(QRect(150, 200, 113, 21))
        self.phoneLineEdit = QLineEdit(Form)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        self.phoneLineEdit.setGeometry(QRect(140, 230, 113, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0438\u043b\u0435\u043d\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0434\u0440\u0435\u0441\u0441", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
    # retranslateUi

