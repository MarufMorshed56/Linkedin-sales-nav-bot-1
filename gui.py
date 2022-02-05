# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 476)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(225, 225, 225);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_filename = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_filename.sizePolicy().hasHeightForWidth())
        self.lineEdit_filename.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_filename.setFont(font)
        self.lineEdit_filename.setAutoFillBackground(False)
        self.lineEdit_filename.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_filename.setMaxLength(500)
        self.lineEdit_filename.setFrame(False)
        self.lineEdit_filename.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_filename.setClearButtonEnabled(True)
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.gridLayout.addWidget(self.lineEdit_filename, 34, 2, 1, 2)
        self.lineEdit_page_number = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_page_number.sizePolicy().hasHeightForWidth())
        self.lineEdit_page_number.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_page_number.setFont(font)
        self.lineEdit_page_number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_page_number.setMaxLength(3)
        self.lineEdit_page_number.setFrame(False)
        self.lineEdit_page_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_page_number.setClearButtonEnabled(True)
        self.lineEdit_page_number.setObjectName("lineEdit_page_number")
        self.gridLayout.addWidget(self.lineEdit_page_number, 31, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 33, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_export = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_export.sizePolicy().hasHeightForWidth())
        self.pushButton_export.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_export.setFont(font)
        self.pushButton_export.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_export.setFlat(False)
        self.pushButton_export.setObjectName("pushButton_export")
        self.gridLayout.addWidget(self.pushButton_export, 36, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 32, 0, 1, 4)
        self.checkBox_remember_me = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_remember_me.sizePolicy().hasHeightForWidth())
        self.checkBox_remember_me.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.checkBox_remember_me.setFont(font)
        self.checkBox_remember_me.setChecked(False)
        self.checkBox_remember_me.setObjectName("checkBox_remember_me")
        self.gridLayout.addWidget(self.checkBox_remember_me, 3, 2, 1, 1)
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_login.setObjectName("pushButton_login")
        self.gridLayout.addWidget(self.pushButton_login, 3, 3, 1, 1, QtCore.Qt.AlignRight)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 11, 3, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_password.setMaxLength(500)
        self.lineEdit_password.setFrame(False)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setClearButtonEnabled(True)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 4)
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_email.setMaxLength(500)
        self.lineEdit_email.setFrame(False)
        self.lineEdit_email.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_email.setClearButtonEnabled(True)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout.addWidget(self.lineEdit_email, 0, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 34, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 31, 3, 1, 1)
        self.lineEdit_delay = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_delay.sizePolicy().hasHeightForWidth())
        self.lineEdit_delay.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lineEdit_delay.setFont(font)
        self.lineEdit_delay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_delay.setMaxLength(2)
        self.lineEdit_delay.setFrame(False)
        self.lineEdit_delay.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_delay.setClearButtonEnabled(True)
        self.lineEdit_delay.setObjectName("lineEdit_delay")
        self.gridLayout.addWidget(self.lineEdit_delay, 11, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 31, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.spinBox_speed = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_speed.sizePolicy().hasHeightForWidth())
        self.spinBox_speed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.spinBox_speed.setFont(font)
        self.spinBox_speed.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_speed.setWrapping(False)
        self.spinBox_speed.setFrame(False)
        self.spinBox_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_speed.setMinimum(-150)
        self.spinBox_speed.setMaximum(6000)
        self.spinBox_speed.setSingleStep(25)
        self.spinBox_speed.setObjectName("spinBox_speed")
        self.gridLayout.addWidget(self.spinBox_speed, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.spinBox_try_count = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_try_count.sizePolicy().hasHeightForWidth())
        self.spinBox_try_count.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.spinBox_try_count.setFont(font)
        self.spinBox_try_count.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_try_count.setFrame(False)
        self.spinBox_try_count.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_try_count.setMinimum(2)
        self.spinBox_try_count.setMaximum(50)
        self.spinBox_try_count.setObjectName("spinBox_try_count")
        self.gridLayout.addWidget(self.spinBox_try_count, 6, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linkedin Bot"))
        self.lineEdit_page_number.setText(_translate("MainWindow", "30"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton_export.setText(_translate("MainWindow", "Export"))
        self.label_status.setText(_translate("MainWindow", "Remaining: 0 | Profile: 0 | Total Profile: 0"))
        self.checkBox_remember_me.setText(_translate("MainWindow", "Remember me"))
        self.pushButton_login.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "Delay"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Filename"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.lineEdit_delay.setText(_translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "Pages Number"))
        self.label_6.setText(_translate("MainWindow", "Speed"))
        self.label_7.setText(_translate("MainWindow", "Try Count"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
