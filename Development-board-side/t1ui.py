# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'T1HmOcDY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 480)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(590, 361, 183, 101))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(91, 31))
        self.pushButton.setToolTipDuration(0)
        self.pushButton.setAutoRepeatDelay(297)
        self.pushButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.textEdit_2 = QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(181, 51))

        self.verticalLayout.addWidget(self.textEdit_2)

        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(590, 27, 183, 63))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(81, 31))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.textEdit = QTextEdit(self.layoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(181, 31))

        self.verticalLayout_3.addWidget(self.textEdit)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(560, 27, 20, 431))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.layoutWidget_3 = QWidget(Form)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(590, 177, 183, 91))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.layoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(121, 41))
        self.pushButton_2.setToolTipDuration(0)
        self.pushButton_2.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.textEdit_3 = QTextEdit(self.layoutWidget_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(181, 41))
        self.textEdit_3.setMaximumSize(QSize(181, 41))

        self.verticalLayout_2.addWidget(self.textEdit_3)

        self.layoutWidget_4 = QWidget(Form)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(50, 27, 221, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.layoutWidget_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(91, 31))

        self.horizontalLayout.addWidget(self.comboBox)

        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(30, 90, 521, 361))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate("Form", u"\u53d8\u538b\u5668\u6cb9\u68c0\u6d4b\u5206\u6790\u7cfb\u7edf", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.label_3.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:12pt;\">\u4e32\u53e3\u72b6\u6001</span></p></body></html>",
                                                        None))
        self.pushButton_2.setText(
            QCoreApplication.translate("Form", u"\u540c\u53c2\u8003\u7269\u8d28\u5bf9\u6bd4", None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"<html><head/><body><p><span style=\" font-size:12pt;\">\u53c2\u8003\u7269\u8d28</span></p></body></html>",
                                                        None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u539f\u6cb9", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u7535\u6027\u6545\u969c\u6cb9", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u53d7\u6f6e\u6cb9A\u578b", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\u53d7\u6f6e\u6cb9B\u578b", None))

    # retranslateUi
