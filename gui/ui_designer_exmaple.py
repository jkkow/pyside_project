# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer_exmapleaflRdO.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(448, 146)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(600, 300))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 20))
        font = QFont()
        font.setFamilies([u"D2CodingLigature Nerd Font"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 30))
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 20))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 30))
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.frame)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(600, 30))
        font1 = QFont()
        font1.setFamilies([u"D2CodingLigature Nerd Font"])
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color:green;")

        self.verticalLayout_4.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

