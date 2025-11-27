# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
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
import resources_rc

class Ui_WelcomeForm(object):
    def setupUi(self, WelcomeForm):
        if not WelcomeForm.objectName():
            WelcomeForm.setObjectName(u"WelcomeForm")
        WelcomeForm.resize(600, 400)
        WelcomeForm.setStyleSheet(u"")
        self.label = QLabel(WelcomeForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 601, 251))
        self.label.setStyleSheet(u"image: url(:/Downloads/logo.png);\n"
"")
        self.selectImageButton = QPushButton(WelcomeForm)
        self.selectImageButton.setObjectName(u"selectImageButton")
        self.selectImageButton.setGeometry(QRect(150, 290, 300, 60))
        self.selectImageButton.setMinimumSize(QSize(300, 60))
        font = QFont()
        font.setPointSize(12)
        self.selectImageButton.setFont(font)
        self.selectImageButton.setStyleSheet(u"")

        self.retranslateUi(WelcomeForm)

        QMetaObject.connectSlotsByName(WelcomeForm)
    # setupUi

    def retranslateUi(self, WelcomeForm):
        WelcomeForm.setWindowTitle(QCoreApplication.translate("WelcomeForm", u"Image Colorization - Welcome", None))
        self.label.setText("")
        self.selectImageButton.setText(QCoreApplication.translate("WelcomeForm", u"Select Image to Colorize", None))
    # retranslateUi

