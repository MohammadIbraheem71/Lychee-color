# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1212, 594)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 160, 1201, 302))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.inputimagelabel = QLabel(self.layoutWidget)
        self.inputimagelabel.setObjectName(u"inputimagelabel")
        self.inputimagelabel.setMinimumSize(QSize(300, 300))
        self.inputimagelabel.setMaximumSize(QSize(512, 512))
        self.inputimagelabel.setScaledContents(False)

        self.horizontalLayout.addWidget(self.inputimagelabel)

        self.outputimagelabel = QLabel(self.layoutWidget)
        self.outputimagelabel.setObjectName(u"outputimagelabel")
        self.outputimagelabel.setMinimumSize(QSize(300, 300))
        self.outputimagelabel.setMaximumSize(QSize(1024, 1024))
        self.outputimagelabel.setScaledContents(False)

        self.horizontalLayout.addWidget(self.outputimagelabel)

        self.enhancedimage = QLabel(self.layoutWidget)
        self.enhancedimage.setObjectName(u"enhancedimage")
        self.enhancedimage.setMinimumSize(QSize(300, 300))
        self.enhancedimage.setMaximumSize(QSize(512, 512))
        self.enhancedimage.setScaledContents(False)

        self.horizontalLayout.addWidget(self.enhancedimage)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 50, 1131, 103))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Segoe Print\";\n"
"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(401, 521, 441, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.selectinputimage = QPushButton(self.widget)
        self.selectinputimage.setObjectName(u"selectinputimage")

        self.horizontalLayout_3.addWidget(self.selectinputimage)

        self.downloadimagebutton = QPushButton(self.widget)
        self.downloadimagebutton.setObjectName(u"downloadimagebutton")

        self.horizontalLayout_3.addWidget(self.downloadimagebutton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.inputimagelabel.setText("")
        self.outputimagelabel.setText("")
        self.enhancedimage.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">INPUT IMAGE</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">BASIC COLOR</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">POST PROCCESSING</span></p></body></html>", None))
        self.selectinputimage.setText(QCoreApplication.translate("Form", u"SELECT IMAGE", None))
        self.downloadimagebutton.setText(QCoreApplication.translate("Form", u"SAVE OUTPUT", None))
    # retranslateUi

