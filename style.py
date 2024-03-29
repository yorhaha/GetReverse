# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'style.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userid = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.userid.setFont(font)
        self.userid.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.userid.setObjectName("userid")
        self.horizontalLayout.addWidget(self.userid)
        self.inputUserid = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUserid.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.inputUserid.setMaxLength(10)
        self.inputUserid.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputUserid.setObjectName("inputUserid")
        self.horizontalLayout.addWidget(self.inputUserid)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.inputPassword.setMaxLength(40)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.horizontalLayout_2.addWidget(self.inputPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.inputBookId = QtWidgets.QLineEdit(self.centralwidget)
        self.inputBookId.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.inputBookId.setObjectName("inputBookId")
        self.horizontalLayout_3.addWidget(self.inputBookId)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.buttonGetInfo = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.buttonGetInfo.setFont(font)
        self.buttonGetInfo.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.buttonGetInfo.setAutoRepeat(False)
        self.buttonGetInfo.setFlat(False)
        self.buttonGetInfo.setObjectName("buttonGetInfo")
        self.horizontalLayout_10.addWidget(self.buttonGetInfo)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.labelBookInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.labelBookInfo.setMinimumSize(QtCore.QSize(300, 100))
        self.labelBookInfo.setMaximumSize(QtCore.QSize(300, 150))
        self.labelBookInfo.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.labelBookInfo.setAcceptRichText(False)
        self.labelBookInfo.setObjectName("labelBookInfo")
        self.horizontalLayout_9.addWidget(self.labelBookInfo)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.buttonDownload = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDownload.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.buttonDownload.setObjectName("buttonDownload")
        self.horizontalLayout_8.addWidget(self.buttonDownload)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.labelStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelStatus.setMinimumSize(QtCore.QSize(300, 50))
        self.labelStatus.setMaximumSize(QtCore.QSize(300, 50))
        self.labelStatus.setStyleSheet("font: 10pt \"微软雅黑\";\n"
"background: \"white\";")
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.horizontalLayout_7.addWidget(self.labelStatus)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(36, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 10pt \"微软雅黑\";\n"
"color: red;")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Downloader"))
        self.userid.setText(_translate("MainWindow", "学号   "))
        self.label_2.setText(_translate("MainWindow", "密码   "))
        self.label_3.setText(_translate("MainWindow", "书籍ID"))
        self.buttonGetInfo.setText(_translate("MainWindow", "获取书籍信息"))
        self.labelBookInfo.setPlaceholderText(_translate("MainWindow", "书籍信息"))
        self.buttonDownload.setText(_translate("MainWindow", "开始下载"))
        self.labelStatus.setText(_translate("MainWindow", "下载状态"))
        self.label.setText(_translate("MainWindow", "此程序仅作为学习交流使用，禁止作为商业用途。\n"
"短时间内大批量下载会浪费公共资源，并造成侵权！"))
