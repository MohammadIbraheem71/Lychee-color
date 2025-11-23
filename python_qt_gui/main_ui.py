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
        self.selectinputimage = QPushButton(Form)
        self.selectinputimage.setObjectName(u"selectinputimage")
        self.selectinputimage.setGeometry(QRect(240, 20, 681, 24))
        self.downloadimagebutton = QPushButton(Form)
        self.downloadimagebutton.setObjectName(u"downloadimagebutton")
        self.downloadimagebutton.setGeometry(QRect(250, 540, 731, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 100, 181, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(540, 100, 131, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(930, 100, 141, 20))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 160, 1201, 302))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.inputimagelabel = QLabel(self.widget)
        self.inputimagelabel.setObjectName(u"inputimagelabel")
        self.inputimagelabel.setMinimumSize(QSize(300, 300))
        self.inputimagelabel.setMaximumSize(QSize(512, 512))
        self.inputimagelabel.setScaledContents(False)

        self.horizontalLayout.addWidget(self.inputimagelabel)

        self.outputimagelabel = QLabel(self.widget)
        self.outputimagelabel.setObjectName(u"outputimagelabel")
        self.outputimagelabel.setMinimumSize(QSize(300, 300))
        self.outputimagelabel.setMaximumSize(QSize(1024, 1024))
        self.outputimagelabel.setScaledContents(False)

        self.horizontalLayout.addWidget(self.outputimagelabel)

        self.enhancedimage = QLabel(self.widget)
        self.enhancedimage.setObjectName(u"enhancedimage")
        self.enhancedimage.setMinimumSize(QSize(300, 300))
        self.enhancedimage.setMaximumSize(QSize(512, 512))
        self.enhancedimage.setScaledContents(False)

        self.horizontalLayout.addWidget(self.enhancedimage)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.selectinputimage.setText(QCoreApplication.translate("Form", u"Select Input Image", None))
        self.downloadimagebutton.setText(QCoreApplication.translate("Form", u"Download Output", None))
        self.label.setText(QCoreApplication.translate("Form", u"INPUT IMAGE", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"BASIC COLOR", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"POST PROCCESSING", None))
        self.inputimagelabel.setText(QCoreApplication.translate("Form", u"input image", None))
        self.outputimagelabel.setText(QCoreApplication.translate("Form", u"output image", None))
        self.enhancedimage.setText(QCoreApplication.translate("Form", u"enhanced image", None))
    # retranslateUi

