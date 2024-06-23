import sys
import csv
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QFileDialog, QDialog
from PyQt5.QtCore import Qt


# Ипортируем библиотеки, которые нам понадобятся (следующий коментарий на 11 строке)
# Импортируем дизайн из QtDesinger (следующий коментарий на 646 строке)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 327)
        MainWindow.setMinimumSize(QtCore.QSize(381, 327))
        MainWindow.setMaximumSize(QtCore.QSize(381, 327))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 200, 231, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    border-radius:  10px;\n"
                                      "    background-color:  rgb(8,166,82);\n"
                                      "    color:  rgb(255, 255, 255);\n"
                                      "    font-size:  23px; \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:  rgb(85, 170, 127);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 47, 13))
        self.label.setObjectName("label")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(60, 70, 231, 41))
        self.plainTextEdit_2.setTabChangesFocus(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(60, 140, 231, 41))
        self.plainTextEdit_3.setTabChangesFocus(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 47, 13))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Продолжить"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(410, 466)
        MainWindow.setMinimumSize(QtCore.QSize(410, 466))
        MainWindow.setMaximumSize(QtCore.QSize(410, 466))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 261, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 261, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 261, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 240, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 41, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-ciuB2466tm.png"))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 350, 71, 71))
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 320, 71, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-srTp7BtlCizS0A.png"))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 350, 71, 71))
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 330, 71, 121))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-65jVjSgWaVGU9qLr.png"))
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 350, 71, 71))
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 330, 71, 121))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-znPhiYz0mY.png"))
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(-1)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    border-radius:  10px;\n"
                                        "    background-color:  rgb(8,166,82);\n"
                                        "    color:  rgb(255, 255, 255);\n"
                                        "    font-size:  13px; \n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:  rgb(85, 170, 127);\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; "
                                                    "color:#313131;\">Добрый день,<br/></span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; "
                                                      "color:#313131;\">Name!<br/></span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#747474;\">Кошелек "
                                                      "</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; "
                                                      "font-weight:600; "
                                                      "color:#020202;\">9999$</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Выйти "))


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 466)
        MainWindow.setMinimumSize(QtCore.QSize(410, 466))
        MainWindow.setMaximumSize(QtCore.QSize(410, 466))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 371, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 150, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-110, 180, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 160, 221, 21))
        self.plainTextEdit.setTabChangesFocus(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(130, 190, 221, 21))
        self.plainTextEdit_2.setTabChangesFocus(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 320, 71, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-srTp7BtlCizS0A.png"))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 330, 71, 121))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-znPhiYz0mY.png"))
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 350, 71, 71))
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 350, 71, 71))
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 330, 71, 121))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-65jVjSgWaVGU9qLr.png"))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 350, 71, 71))
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 230, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(-1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    border-radius:  10px;\n"
                                        "    background-color:  rgb(8,166,82);\n"
                                        "    color:  rgb(255, 255, 255);\n"
                                        "    font-size:  13px; \n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:  rgb(85, 170, 127);\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.plainTextEdit.raise_()
        self.plainTextEdit_2.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:26pt; "
                                        "color:#313131;\">Отправить деньги<br/></span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" "
                                        "color:#747474;\">Кому:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" "
                                        "color:#747474;\">Сколько:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Перевести"))


class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 466)
        MainWindow.setMinimumSize(QtCore.QSize(410, 466))
        MainWindow.setMaximumSize(QtCore.QSize(410, 466))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 391, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 361, 101))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 330, 71, 121))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-65jVjSgWaVGU9qLr.png"))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 320, 71, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-srTp7BtlCizS0A.png"))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 330, 71, 121))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-znPhiYz0mY.png"))
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 350, 71, 71))
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 350, 71, 71))
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 350, 71, 71))
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Все ваши транзакции:</p></body></html>"))


class Ui_MainWindow5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 466)
        MainWindow.setMinimumSize(QtCore.QSize(410, 466))
        MainWindow.setMaximumSize(QtCore.QSize(410, 466))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 261, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 361, 171))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 351, 121))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 211, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    border-radius:  10px;\n"
                                      "    background-color:  rgb(8,166,82);\n"
                                      "    color:  rgb(255, 255, 255);\n"
                                      "    font-size:  17px; \n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color:  rgb(85, 170, 127);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(-1)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    border-radius:  10px;\n"
                                        "    background-color:  rgb(8,166,82);\n"
                                        "    color:  rgb(255, 255, 255);\n"
                                        "    font-size:  13px; \n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:  rgb(85, 170, 127);\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 390, 331, 21))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    border-radius:  10px;\n"
                                        "    background-color:  rgb(85, 170, 127);\n"
                                        "    color:  rgb(255, 255, 255);\n"
                                        "    font-size:  11px; \n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color:  rgb(85, 150, 127);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 340, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 330, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:26pt; color:#313131;\">Добрый "
                                      "день,<br/></span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#313131;\">Уважаемый "
                                        "администратор!</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; "
                                        "color:#747474;\">Редактор пользователей:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Добавить пользователей"))
        self.pushButton_5.setText(_translate("MainWindow", "Выйти "))
        self.pushButton_2.setText(_translate("MainWindow", "Инструкция по добавлению пользователей"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; "
                                        "color:#ff0000;\">Уважаемый администратор!</span></p><p "
                                        "align=\"center\"><span style=\" font-size:8pt; color:#ff0000;\">Просьба "
                                        "перед добавлением пользователей прочитать "
                                        "инструкцию!</span></p></body></html>"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 701)
        Dialog.setMinimumSize(QtCore.QSize(400, 701))
        Dialog.setMaximumSize(QtCore.QSize(400, 701))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 90, 331, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-xNpqMCTS6WqoPdA.jpg"))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 250, 271, 91))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-ciZHKj42Ue.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 350, 381, 131))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(90, 490, 261, 91))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("tXEtufZUOss.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(-30, 600, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(290, 600, 81, 71))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("imgonline-com-ua-Resize-Cp0x2xZ6TaQawJ1.png"))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:8pt; color:#313131;\">Подробная инструкция по добавлению "
                                                  "нового пользователя.</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:11pt;\">1. Жмем на кнопку &quot;Добавить "
                                                  "пользователя&quot;</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:9pt;\">2. Выбираем нужный файл, </span><span style=\" "
                                                  "font-size:9pt; color:#ff000d;\">ОБЯЗАТЕЛЬНО</span><span style=\" "
                                                  "font-size:9pt;\"> формата : *.csv</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:9pt;\">3. Файл обязательно должен содержать: "
                                                  "</span></p><p align=\"center\"><span style=\" "
                                                  "font-size:9pt;\">Одного или нескольких пользователей. "
                                                  "</span></p><p align=\"center\"><span style=\" "
                                                  "font-size:9pt;\">Каждый пользователь - строка таблицы, "
                                                  "столбцы </span></p><p align=\"center\"><span style=\" "
                                                  "font-size:9pt;\">которой - login, password, money (если их нет - "
                                                  "пишите 0).</span></p><p align=\"center\"><span style=\" "
                                                  "font-size:9pt; color:#ff0000;\">Если не понятно, посмотрите "
                                                  "картинку ниже!</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:9pt;\">4. Радуемся, что у нас все "
                                                  "получилось!</span></p></body></html>"))


class Registration(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("bank_db.db")
        self.login = ''
        self.pushButton.clicked.connect(self.login_system)
        self.glavnotprilojenie = HomeWindow(self)
        self.adminokno = AdminWindow()
        self.setWindowTitle('Авторизация')
        # Инициализируем класс регистрационного окна, так же, создаем обьекты класса(следующий коментарий на 653 строке)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.login_system()
        # При нажатии клавиши Enter произойдет тоже самое, что и при нажатии кнопки pushbutton
        # (следующий коментарий на 680 строке)

    def login_system(self):
        cur = self.connection.cursor()
        login = self.plainTextEdit_2.toPlainText()
        password = self.plainTextEdit_3.toPlainText()
        try:
            spisokloginov = [i[0] for i in cur.execute("""SELECT login FROM polzovateli""").fetchall()]
            if login in spisokloginov:
                pravilniypass = cur.execute(f"""SELECT password FROM polzovateli
                                            WHERE login = '{login}'""").fetchall()[0][0]
                if login == 'admin' and password == pravilniypass:
                    self.adminokno.show()
                    self.hide()
                else:
                    if password == pravilniypass:
                        self.glavnotprilojenie.show()
                        self.hide()
                        self.login = login
                        self.glavnotprilojenie.zamena()
                    else:
                        raise ValueError("В пароле допущена ошибка.")
            else:
                raise ValueError("Указанного пользователя не существует.")
        except ValueError as e:
            self.statusbar.showMessage(str(e))
            # Функция выше отвечает за вход в систему. Проверку пароля, логина, открытие следующего окна
            # (следующий коментарий на 699 строке)


class HomeWindow(QMainWindow, Ui_MainWindow2):
    def __init__(self, parent):
        super().__init__()
        self.connection = sqlite3.connect("bank_db.db")
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.parent = parent
        self.login = parent.login
        self.coords = (self.x(), self.y())
        self.perevodokno = PerevodWindow(self)
        self.tranzactionokno = TranzactionWindow(self)
        self.ui.pushButton_2.clicked.connect(self.perevod)
        self.ui.pushButton_3.clicked.connect(self.tranzaction)
        self.ui.pushButton_5.clicked.connect(self.vihod)
        self.setWindowTitle('Главная страница')
        # Инициализируем главное окно и его дизайн, подключаем кнопки, создаем обьекты классов всех вкладок
        # (следующий коментарий на 706 строке)

    def zamena(self):
        self.ui.label_4.setText(str(self.connection.cursor().execute(f"""SELECT money FROM polzovateli
                                             WHERE login = '{self.parent.login}'""").fetchone()[0]) + ' ₽')
        self.ui.label_2.setText(self.parent.login)
        # Функция выше отвечает за количество денег, которые отображаются на главной странице
        # (следующий коментарий на 717 строке)

    def perevod(self):
        self.login = self.parent.login
        self.perevodokno.move(self.x(), self.y())
        self.perevodokno.show()
        self.perevodokno.ui.statusbar.clearMessage()
        self.perevodokno.ui.plainTextEdit.setPlainText('')
        self.perevodokno.ui.plainTextEdit_2.setPlainText('')
        self.hide()
        # Функция выше отвечает за открытие вкладки перевода, так-же, переходя на эту вкладку, мы очищаем все, что там
        # уже написано, и если текущее окно передвинуто, передвигаем окно с переводом на текущие координаты
        # (следующий коментарий на 727 строке)

    def tranzaction(self):
        self.login = self.parent.login
        self.tranzactionokno.move(self.x(), self.y())
        self.tranzactionokno.update_tables()
        self.tranzactionokno.show()
        self.hide()
        # Функция выше отвечает за открытие вкладки с транзакциями, переходя на эту вкладку,
        # мы вызываем функцию update_tables которое отвечает за обновление данных в таблице с транзакциями
        # (следующий коментарий на 734 строке)

    def vihod(self):
        Registration().show()
        self.hide()
        # Функция выше отвечает за кнопку выхода (следующий коментарий на 749 строке)


class PerevodWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, parent):
        super().__init__()
        self.connection = sqlite3.connect("bank_db.db")
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.login = parent.login
        self.parent = parent
        self.ui.pushButton.clicked.connect(self.home)
        self.ui.pushButton_3.clicked.connect(self.tranzaction)
        self.ui.pushButton_4.clicked.connect(self.perevesti)
        self.setWindowTitle('Перевод')
        # Инициализируем класс окна для переводов, подключаем кнопки (следующий коментарий на 754 строке)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.perevesti()
        # При нажатии клавиши Enter произойдет тоже самое, что и при нажатии кнопки pushbutton_4
        # (следующий коментарий на 761 строке)

    def home(self):
        self.parent.move(self.x(), self.y())
        self.parent.show()
        self.hide()
        # Функция выше отвечает за открытие вкладки главного окна (следующий коментарий на 768 строке)

    def tranzaction(self):
        self.parent.tranzactionokno.move(self.x(), self.y())
        self.parent.tranzactionokno.show()
        self.parent.tranzactionokno.update_tables()
        self.hide()
        # Функция выше отвечает за открытие вкладки с транзакциями (Следующий коментарий на 819 строке)

    def perevesti(self):
        try:
            cur = self.connection.cursor()
            komy = self.ui.plainTextEdit.toPlainText()
            skolko = self.ui.plainTextEdit_2.toPlainText()
            logini = [i[0] for i in cur.execute(f"""SELECT login FROM polzovateli""").fetchall()]
            if komy == 'admin':
                raise SystemError
            if float(skolko) <= 0:
                raise PermissionError
            if komy == self.parent.login:
                raise TypeError
            if komy not in logini:
                raise NameError
            polz1 = float(cur.execute(f"""SELECT money FROM polzovateli
                                          WHERE login = '{self.parent.login}'""").fetchall()[0][0]) - float(skolko)
            if polz1 < 0:
                raise AttributeError
            polz2 = float(cur.execute(f"""SELECT money
                                        FROM polzovateli
                                        WHERE login = '{komy}'""").fetchall()[0][0]) + float(skolko)
            cur.execute(f"""UPDATE polzovateli
                            SET money = {polz2}
                            WHERE login = '{komy}'""")
            cur.execute(f"""UPDATE polzovateli
                            SET money = {polz1}
                            WHERE login = '{self.parent.login}'""")
            tox = cur.execute(f"""SELECT id
                                  FROM polzovateli
                                  WHERE login = '{komy}'""").fetchall()[0][0]
            fromx = cur.execute(f"""SELECT id
                                    FROM polzovateli
                                    WHERE login = '{self.parent.login}'""").fetchall()[0][0]
            cur.execute(f"""INSERT INTO tranzaction(fromx, tox, summa) VALUES({fromx}, {tox}, {skolko})""")
            self.connection.commit()
            self.parent.zamena()
            self.ui.statusbar.showMessage('Транзакция прошла успешна!')
        except ValueError:
            self.ui.statusbar.showMessage('Ошибка в строке суммы перевода.')
        except NameError:
            self.ui.statusbar.showMessage('Указанного логина человека не существует.')
        except PermissionError:
            self.ui.statusbar.showMessage('Вы ввели недопустимую. сумму или сумма равна нулю.')
        except TypeError:
            self.ui.statusbar.showMessage('Вы пытаетесь перевести самому себе.')
        except AttributeError:
            self.ui.statusbar.showMessage('У вас нехватает денег!')
        except SystemError:
            self.ui.statusbar.showMessage('Администратору нельзя пересети средства.')
    # Функция выше отвечает за перевод одному пользователю от другого, с большим количеством исключений,
    # а также работой с БД (Следующий коментарий на 836 строке)


class TranzactionWindow(QMainWindow, Ui_MainWindow4):
    def __init__(self, parent):
        super().__init__()
        self.connection = sqlite3.connect("bank_db.db")
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)
        self.login = parent.login
        self.parent = parent
        self.update_tables()
        self.ui.pushButton.clicked.connect(self.home)
        self.ui.pushButton_2.clicked.connect(self.perevod)
        self.setWindowTitle('Транзакции')

    # Инициализируем класс окна для транзакций, подключаем кнопки, вызываем функцию обновления TableWidget
    # (следующий коментарий на 843 строке)

    def home(self):
        self.parent.move(self.x(), self.y())
        self.parent.show()
        self.hide()
    # Функция выше отвечает за открытие вкладки главного окна (следующий коментарий на 852 строке)

    def perevod(self):
        self.parent.perevodokno.move(self.x(), self.y())
        self.parent.perevodokno.show()
        self.parent.perevodokno.ui.statusbar.clearMessage()
        self.parent.perevodokno.ui.plainTextEdit.setPlainText('')
        self.parent.perevodokno.ui.plainTextEdit_2.setPlainText('')
        self.hide()
    # Функция выше отвечает за открытие вкладки окна с переводом (следующий коментарий на 875 строке)

    def update_tables(self):
        cur = self.connection.cursor()
        self.login = self.parent.login
        if self.login:
            idlogin = cur.execute(f"""SELECT id FROM polzovateli
                                WHERE login = '{self.login}'""").fetchone()[0]
            result = cur.execute(f"""SELECT t.id, u.login, u1.login, t.summa
                                FROM polzovateli as u, tranzaction as t,  polzovateli as u1
                                WHERE (t.fromx = u.id and t.tox = u1.id) and (u.id = {idlogin} 
                                or u1.id = {idlogin})""").fetchall()
            if result:
                self.ui.tableWidget.setRowCount(len(result))
                self.ui.tableWidget.setColumnCount(len(result[0]))
            else:
                self.ui.tableWidget.setRowCount(len(result))
                self.ui.tableWidget.setColumnCount(len(result))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID Транзакции', 'От кого', 'Кому',
                                                           'Сколько'])
    # Функция выше отвечает за обновления таблицы с транзакциями, меняя id пользователей на логины
    # (следующий коментарий на 890 строке)


class AdminWindow(QMainWindow, Ui_MainWindow5):
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect("bank_db.db")
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.vihod)
        self.ui.pushButton.clicked.connect(self.noviy_polzovatel)
        self.ui.pushButton_2.clicked.connect(self.instruction)
        self.setWindowTitle('Главная страница администраторов')

    # Инициализируем класс главного окна администрации, подключаем кнопки (следующий коментарий на 896 строке)

    def vihod(self):
        Registration().show()
        self.hide()

    # Функция выше отвечает за кнопку выхода (следующий коментарий на 908 строке)

    def noviy_polzovatel(self):
        cur = self.connection.cursor()
        try:
            fname = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',
                'Текстовый файл (*.csv)')[0]
            if fname == '':
                raise ValueError
        except ValueError:
            return
        # Функция, чтоб если диалоговое окно было аварийно закрыто, наше приложение не крашилось
        # (следующий коментарий на 934 строке)
        idx = int(cur.execute("SELECT id FROM polzovateli").fetchall()[-1][-1])
        spisokloginov = [i[0] for i in cur.execute("SELECT login FROM polzovateli").fetchall()]
        counter = 0
        with open(fname, encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            unpack = [*reader]
            for index, row in enumerate(unpack):
                try:
                    login = str(row[0])
                    password = str(row[1])
                    money = int(row[2])
                    if (login and password and str(money)) and login not in spisokloginov:
                        cur.execute(
                            "INSERT or IGNORE INTO polzovateli (id, login, password, money) VALUES (?, ?, ?, ?)",
                            (idx + counter + 1, login, password, money))
                        counter += 1
                        spisokloginov.append(login)
                    else:
                        raise LookupError
                except LookupError:
                    pass
            self.connection.commit()
            self.ui.statusbar.showMessage(f'Успешно добавлено {counter} из {len(unpack)} пользователей')

    # Функция выше отвечает добавление новых пользователей в БД с помощью csv таблиц(следующий коментарий на 939 строке)

    def instruction(self):
        dlg = DialogWidget()
        dlg.exec()
    # Функция выше отвечает за открытие диалогового окна с инструкцией (следующий коментарий на 948 строке)


class DialogWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Инструкция')
    # Инициализируем класс диалогового окна инструкции.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registration()
    ex.show()
    sys.exit(app.exec())
