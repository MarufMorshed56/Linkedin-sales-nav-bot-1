import datetime
from threading import Thread
from time import sleep
import var
import os
import sys
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import encodings.idna
from utils import update_config_json, export_data_to_csv
import scraper
from pyautogui import confirm

print("App started....")


class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)



class myMainClass():
    def __init__(self):
        GUI.lineEdit_email.setText(var.email)
        GUI.lineEdit_password.setText(var.password)
        GUI.lineEdit_filename.setText(var.filename)
        GUI.lineEdit_delay.setText(str(var.delay))
        GUI.lineEdit_page_number.setText(str(var.page_number))
        GUI.spinBox_speed.setValue(var.scrolling_step)
        GUI.spinBox_try_count.setValue(var.try_count)

        GUI.pushButton_login.clicked.connect(self.start)
        GUI.pushButton_export.clicked.connect(self.export)
        GUI.pushButton_start.clicked.connect(self.start_scrap)
        GUI.pushButton_close.clicked.connect(self.stop)

        GUI.spinBox_speed.valueChanged.connect(self.update_speed)
        GUI.spinBox_try_count.valueChanged.connect(self.update_try_count)
        GUI.checkBox_remember_me.stateChanged.connect(self.update_remember_me)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)

    def update_try_count(self):
        print("try count : {}".format(GUI.spinBox_try_count.value()))
        var.try_count = GUI.spinBox_try_count.value()

    def update_speed(self):
        print("speed : {}".format(GUI.spinBox_speed.value()))
        var.scrolling_step = GUI.spinBox_speed.value()

    def update_label(self):
        text = "Remaining: {} | Profile: {} | Total Profile: {}".format(
            var.remaining_page, var.profile_count, len(var.scrap_data))
        GUI.label_status.setText(text)

    def start(self):
        self.validation()
        update_config_json()
        if not var.status:
            var.status = True
            var.stop = False
            Thread(target=scraper.run, daemon=True).start()

    def start_scrap(self):
        self.validation()
        update_config_json()

        if var.status == True and var.scarp_start == False:
            if len(var.scrap_data)>0:
                confirm_return = confirm(text='Do you want to keep data\'s from previous scrap?',
                        title='Confirm', buttons=['yes', 'no'])

                if confirm_return == "yes":
                    pass
                else:
                    var.scrap_data = []

            var.scarp_start = True

    def stop(self):
        var.stop = True

    def export(self):

        dialog = QFileDialog()
        dialog.setDirectory(var.directory)
        # print(var.filename)
        # dialog.selectFile(var.filename)
        # dialog.selectUrl(csvPath)
        csvPath = dialog.getExistingDirectory(None,"File saving window")
        if csvPath:
            print(csvPath)
            var.directory = csvPath
            self.validation()
            update_config_json()
            print("Total Data : {}".format(len(var.scrap_data)))
            Thread(target=export_data_to_csv, daemon=True).start()
        else:
            print("Exporting Cancelled")


    def update_remember_me(self, checked):
        if checked:
            var.remember_me = True
        else:
            var.remember_me = False
        print("Remember me : {}".format(var.remember_me))

    def validation(self):
        if GUI.lineEdit_email.text():
            var.email = GUI.lineEdit_email.text()
        else:
            GUI.lineEdit_email.setText(var.email)

        if GUI.lineEdit_password.text():
            var.password = GUI.lineEdit_password.text()
        else:
            GUI.lineEdit_password.setText(var.password)

        if GUI.lineEdit_delay.text() and GUI.lineEdit_delay.text().isnumeric():
            var.delay = int(GUI.lineEdit_delay.text())
        else:
            GUI.lineEdit_delay.setText(str(var.delay))

        if GUI.lineEdit_page_number.text() and GUI.lineEdit_page_number.text().isnumeric():
            var.page_number = int(GUI.lineEdit_page_number.text())
        else:
            GUI.lineEdit_page_number.setText(str(var.page_number))

        if GUI.lineEdit_filename.text():
            var.filename = GUI.lineEdit_filename.text()
        else:
            GUI.lineEdit_filename.setText(var.filename)

        # print("Config {0} {1} {2} {3} {4}".format(
        #     var.email, var.password, var.delay, var.page_number, var.filename))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    # try:
    #     def resource_path(relative_path):
    #         if hasattr(sys, '_MEIPASS'):
    #             return os.path.join(sys._MEIPASS, relative_path)
    #         return os.path.join(os.path.abspath("."), relative_path)

    #     p = resource_path('icons/settings_applications-24px.svg')
    #     mainWindow.setWindowIcon(QtGui.QIcon(p))
    # except Exception as e:
    #     print(e)

    mainWindow.setWindowFlags(mainWindow.windowFlags(
    ) | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowSystemMenuHint)

    GUI = MyGui(mainWindow)
    # mainWindow.showMaximized()
    mainWindow.show()

    myMC = myMainClass()

    app.exec_()
    print("Exit")
    sys.exit()
