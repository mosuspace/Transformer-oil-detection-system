from PyQt5.QtCore import QRect, QSize, Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QGraphicsView, QLineEdit, QSpacerItem, QSizePolicy, \
    QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(701, 440)
        font = QFont()
        font.setFamily(u"AcadEref")
        font.setPointSize(12)
        Form.setFont(font)
        self.layoutWidget_4 = QWidget(Form)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 20, 221, 33))
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
        self.graphicsView.setGeometry(QRect(90, 70, 521, 361))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(360, 20, 301, 34))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(113, 16777215))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u88ab\u6d4b\u6cb9\u6ce2\u5f62", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u53c2\u8003\u7269\u8d28</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u539f\u6cb9", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u7535\u6027\u6545\u969c\u6cb9", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u53d7\u6f6e\u6cb9A\u578b", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\u53d7\u6f6e\u6cb9B\u578b", None))

        self.label.setText(QCoreApplication.translate("Form", u"\u5e8f\u53f7", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u7ed8\u5236\u6ce2\u5f62", None))
    # retranslateUi
