# -*- coding: utf-8 -*-
import pandas as pd
################################################################################
## Form generated from reading UI file 'investment_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
from sqlalchemy import create_engine,text

import settings
from settings import DB_PATH


class Ui_Form(object):

    def transfer_data(self,customer_pk,paper_pk,kotirovka,buy_date,sell_date, investment_pk):
        self.customer_pk=customer_pk
        self.paper_pk = paper_pk
        self.kotirovka=kotirovka

        self.buy_date=buy_date
        self.sell_date=sell_date
        self.investment_pk=investment_pk
    def write_investment_to_db(self):
        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        VetTableQuery.prepare("""
                          UPDATE investments SET paper_pk = :paper_pk,customer_pk=:customer_pk, kotirovka = :kotirovka,
                           buy_date=:buy_date, sell_date = :sell_date
                           WHERE pk=:investment_pk
                           
                          """)
        VetTableQuery.bindValue(":paper_pk", self.paperTableWidget.item(self.paperTableWidget.currentRow(),0).text())
        VetTableQuery.bindValue(":customer_pk", self.customerTableWidget.item(self.customerTableWidget.currentRow(),0).text())
        VetTableQuery.bindValue(":kotirovka", self.kotirovkaLineEdit.text())
        VetTableQuery.bindValue(":buy_date", self.buydateLineEdit.text())
        VetTableQuery.bindValue(":sell_date", self.selldateLineEdit.text())
        VetTableQuery.bindValue(":investment_pk", self.investment_pk)
        print("customer pk", self.customer_pk)

        uspeh=VetTableQuery.exec()
        print("is update uspeh",uspeh, VetTableQuery.lastQuery())
        VetDbConnnection.close()
    def fill_papers_table(self):
        TABLE_ROW_LIMIT = 10
        db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        data_for_table = pd.read_sql(text(f'SELECT * FROM papers'), db_connection).astype(str)
        self.paperTableWidget.setRowCount(len(data_for_table))
        self.paperTableWidget.setColumnCount(len(data_for_table.columns))
        print(data_for_table,len(data_for_table),(len(data_for_table.columns)))
        for col_num in range(len(data_for_table.columns)):
            for row_num in range(len(data_for_table)):
                self.paperTableWidget.setItem(row_num, col_num,
                                                 QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def fill_customers_table(self):
        TABLE_ROW_LIMIT = 10
        db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        data_for_table = pd.read_sql(text(f'SELECT * FROM customers'), db_connection).astype(str)
        self.customerTableWidget.setRowCount(len(data_for_table))
        self.customerTableWidget.setColumnCount(len(data_for_table.columns))
        print(data_for_table,len(data_for_table),(len(data_for_table.columns)))
        for col_num in range(len(data_for_table.columns)):
            for row_num in range(len(data_for_table)):
                self.customerTableWidget.setItem(row_num, col_num,
                                                 QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(910, 514)
        self.customerTableWidget = QTableWidget(Form)
        self.customerTableWidget.setObjectName(u"customerTableWidget")
        self.customerTableWidget.setGeometry(QRect(330, 100, 256, 351))
        self.paperTableWidget = QTableWidget(Form)
        self.paperTableWidget.setObjectName(u"paperTableWidget")
        self.paperTableWidget.setGeometry(QRect(630, 100, 256, 351))
        self.selldateLineEdit = QLineEdit(Form)
        self.selldateLineEdit.setObjectName(u"selldateLineEdit")
        self.selldateLineEdit.setGeometry(QRect(120, 230, 113, 21))
        self.selldateLineEdit.setText(self.sell_date)
        self.buydateLineEdit = QLineEdit(Form)
        self.buydateLineEdit.setObjectName(u"buydateLineEdit")
        self.buydateLineEdit.setGeometry(QRect(120, 190, 113, 21))
        self.buydateLineEdit.setText(self.buy_date)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 230, 91, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 190, 91, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 70, 101, 21))
        font = QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(630, 70, 131, 21))
        self.label_4.setFont(font)
        self.kotirovkaLineEdit = QLineEdit(Form)
        self.kotirovkaLineEdit.setObjectName(u"kotirovkaLineEdit")
        self.kotirovkaLineEdit.setGeometry(QRect(120, 160, 113, 21))
        self.kotirovkaLineEdit.setText(self.kotirovka)
        font1 = QFont()
        font1.setPointSize(9)
        self.kotirovkaLineEdit.setFont(font1)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 160, 91, 16))
        self.confirmPushButton = QPushButton(Form, clicked = lambda:self.write_investment_to_db())
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setGeometry(QRect(10, 443, 141, 61))
        self.cancelPushButton = QPushButton(Form, clicked = lambda:Form.close())
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(770, 460, 131, 51))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 321, 41))
        font2 = QFont()
        font2.setPointSize(17)
        self.label_6.setFont(font2)

        self.fill_papers_table()
        self.fill_customers_table()

        # ==========================selector customer==========================
        rowcount = self.customerTableWidget.rowCount()

        for i in range(0, rowcount):

            if (self.customerTableWidget.item(i, 0).text() == self.customer_pk):
                self.pidor = i
        self.customerTableWidget.selectRow(self.pidor)
        # ==========================selector customer==========================


        # ==========================selector paper==========================
        rowcount = self.paperTableWidget.rowCount()

        for i in range(0, rowcount):

            if (self.paperTableWidget.item(i, 0).text() == self.paper_pk):
                self.pidor = i
        self.paperTableWidget.selectRow(self.pidor)
        # ==========================selector paper==========================

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0411\u0443\u043c\u0430\u0433\u0430", None))
        self.kotirovkaLineEdit.setInputMask(QCoreApplication.translate("Form", u"999999999999", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u0438", None))
    # retranslateUi

