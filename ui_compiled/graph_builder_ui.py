# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph_builder.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import numpy as np
import matplotlib.pyplot as plt
import os

from PySide6 import QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):


    def plot_function(self,func_str, num_points, begin, end):
        # Create the directory for saving the graph if it doesn't exist
        os.makedirs('graphs', exist_ok=True)

        # Create a range of x values from -100 to 100
        x = np.linspace(begin, end, num_points)

        # Use eval to compute y values from the function string
        try:
            y = eval(func_str)
        except Exception as e:
            print(f"Error evaluating the function: {e}")
            return

        # Plotting the function
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=func_str)
        plt.title(f'Graph of {func_str}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.axhline(0, color='black', linewidth=0.5, ls='--')
        plt.axvline(0, color='black', linewidth=0.5, ls='--')
        plt.grid()
        plt.legend()

        # Save the plot as graph.png in the graphs folder
        plt.savefig(r'C:\Users\Kingfish\PycharmProjects\LabiRBP\RBP\graph')
        plt.close()


        pixmap = QtGui.QPixmap(r'C:\Users\Kingfish\PycharmProjects\LabiRBP\RBP\graph.png')
        self.graphLabel.setPixmap(pixmap)

        print("Graph saved as")
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(749, 479)
        self.confirmPushButton = QPushButton(Form, clicked=lambda:self.plot_function(self.lineEdit.text(),int(self.pointsLineEdit.text()),int(self.otLineEdit.text()),int(self.doLineEdit.text())))
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setGeometry(QRect(620, 410, 101, 61))
        self.graphLabel = QLabel(Form)
        self.graphLabel.setObjectName(u"graphLabel")
        self.graphLabel.setGeometry(QRect(60, 70, 531, 321))
        self.graphLabel.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 271, 31))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 440, 531, 21))
        self.lineEdit.setText("np.sqrt(x*x + 5) - 10 * np.sin(x - 1)*np.sin(x - 1)")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 440, 49, 16))
        self.pointsLineEdit = QLineEdit(Form)
        self.pointsLineEdit.setObjectName(u"pointsLineEdit")
        self.pointsLineEdit.setGeometry(QRect(440, 410, 161, 21))
        self.pointsLineEdit.setText("100")

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 410, 49, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 410, 49, 16))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 410, 49, 16))
        self.otLineEdit = QLineEdit(Form)
        self.otLineEdit.setObjectName(u"otLineEdit")
        self.otLineEdit.setGeometry(QRect(60, 410, 113, 21))
        self.otLineEdit.setText("2")

        self.doLineEdit = QLineEdit(Form)
        self.doLineEdit.setObjectName(u"doLineEdit")
        self.doLineEdit.setGeometry(QRect(230, 410, 113, 21))
        self.doLineEdit.setText("10")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.graphLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0442\u043e\u0447\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u043e\u0442", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0434\u043e", None))
    # retranslateUi

