# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(315, 253)
        MainWindow.setWindowOpacity(0.6)
        MainWindow.setAutoFillBackground(True)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QPushButton(self.centralWidget)
        self.closeButton.setMinimumSize(QtCore.QSize(25, 25))
        self.closeButton.setMaximumSize(QtCore.QSize(25, 20))
        self.closeButton.setBaseSize(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closeButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        spacerItem = QtWidgets.QSpacerItem(237, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.moreButton = QtWidgets.QPushButton(self.centralWidget)
        self.moreButton.setMinimumSize(QtCore.QSize(22, 22))
        self.moreButton.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Shruti")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.moreButton.setFont(font)
        self.moreButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"}")
        self.moreButton.setObjectName("moreButton")
        self.horizontalLayout.addWidget(self.moreButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Failamp"))
        self.closeButton.setText(_translate("MainWindow", "×"))
        self.moreButton.setText(_translate("MainWindow", "＋"))

