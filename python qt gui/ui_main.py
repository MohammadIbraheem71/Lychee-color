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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(762, 535)
        self.selectinputimage = QPushButton(Form)
        self.selectinputimage.setObjectName(u"selectinputimage")
        self.selectinputimage.setGeometry(QRect(220, 10, 301, 24))
        self.inputimagelabel = QLabel(Form)
        self.inputimagelabel.setObjectName(u"inputimagelabel")
        self.inputimagelabel.setGeometry(QRect(60, 110, 271, 291))
        self.inputimagelabel.setMaximumSize(QSize(300, 300))
        self.outputimagelabel = QLabel(Form)
        self.outputimagelabel.setObjectName(u"outputimagelabel")
        self.outputimagelabel.setGeometry(QRect(420, 100, 281, 300))
        self.outputimagelabel.setMinimumSize(QSize(161, 161))
        self.outputimagelabel.setMaximumSize(QSize(300, 300))
        self.downloadimagebutton = QPushButton(Form)
        self.downloadimagebutton.setObjectName(u"downloadimagebutton")
        self.downloadimagebutton.setGeometry(QRect(200, 470, 361, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.selectinputimage.setText(QCoreApplication.translate("Form", u"select input image", None))
        self.inputimagelabel.setText(QCoreApplication.translate("Form", u"input image", None))
        self.outputimagelabel.setText(QCoreApplication.translate("Form", u"output image", None))
        self.downloadimagebutton.setText(QCoreApplication.translate("Form", u"download output", None))
    # retranslateUi

