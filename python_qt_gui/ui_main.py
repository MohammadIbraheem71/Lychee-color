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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1212, 594)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.selectinputimage = QPushButton(Form)
        self.selectinputimage.setObjectName(u"selectinputimage")

        self.verticalLayout.addWidget(self.selectinputimage)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputimagelabel = QLabel(Form)
        self.inputimagelabel.setObjectName(u"inputimagelabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputimagelabel.sizePolicy().hasHeightForWidth())
        self.inputimagelabel.setSizePolicy(sizePolicy)
        self.inputimagelabel.setMinimumSize(QSize(300, 300))
        self.inputimagelabel.setMaximumSize(QSize(512, 512))
        self.inputimagelabel.setScaledContents(False)

        self.horizontalLayout.addWidget(self.inputimagelabel)

        self.outputimagelabel = QLabel(Form)
        self.outputimagelabel.setObjectName(u"outputimagelabel")
        sizePolicy.setHeightForWidth(self.outputimagelabel.sizePolicy().hasHeightForWidth())
        self.outputimagelabel.setSizePolicy(sizePolicy)
        self.outputimagelabel.setMinimumSize(QSize(300, 300))
        self.outputimagelabel.setMaximumSize(QSize(1024, 1024))
        self.outputimagelabel.setScaledContents(False)

        self.horizontalLayout.addWidget(self.outputimagelabel)

        self.enhancedimage = QLabel(Form)
        self.enhancedimage.setObjectName(u"enhancedimage")
        sizePolicy.setHeightForWidth(self.enhancedimage.sizePolicy().hasHeightForWidth())
        self.enhancedimage.setSizePolicy(sizePolicy)
        self.enhancedimage.setMinimumSize(QSize(300, 300))
        self.enhancedimage.setMaximumSize(QSize(512, 512))
        self.enhancedimage.setScaledContents(False)

        self.horizontalLayout.addWidget(self.enhancedimage)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.downloadimagebutton = QPushButton(Form)
        self.downloadimagebutton.setObjectName(u"downloadimagebutton")

        self.verticalLayout.addWidget(self.downloadimagebutton)

        self.selectinputimage.raise_()
        self.downloadimagebutton.raise_()
        self.inputimagelabel.raise_()
        self.outputimagelabel.raise_()
        self.enhancedimage.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.selectinputimage.setText(QCoreApplication.translate("Form", u"select input image", None))
        self.inputimagelabel.setText(QCoreApplication.translate("Form", u"input image", None))
        self.outputimagelabel.setText(QCoreApplication.translate("Form", u"output image", None))
        self.enhancedimage.setText(QCoreApplication.translate("Form", u"enhanced image", None))
        self.downloadimagebutton.setText(QCoreApplication.translate("Form", u"download output", None))
    # retranslateUi

