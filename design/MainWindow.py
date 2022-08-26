# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\KLSH_Sender\design/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.choose_html_file_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choose_html_file_btn.setFont(font)
        self.choose_html_file_btn.setObjectName("choose_html_file_btn")
        self.gridLayout.addWidget(self.choose_html_file_btn, 3, 2, 1, 1)
        self.choose_file_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choose_file_btn.setFont(font)
        self.choose_file_btn.setObjectName("choose_file_btn")
        self.gridLayout.addWidget(self.choose_file_btn, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.excel_filename_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.excel_filename_label.setFont(font)
        self.excel_filename_label.setObjectName("excel_filename_label")
        self.gridLayout.addWidget(self.excel_filename_label, 2, 1, 1, 1)
        self.txt_filename_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txt_filename_label.setFont(font)
        self.txt_filename_label.setObjectName("txt_filename_label")
        self.gridLayout.addWidget(self.txt_filename_label, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.html_filename_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.html_filename_label.setFont(font)
        self.html_filename_label.setObjectName("html_filename_label")
        self.gridLayout.addWidget(self.html_filename_label, 3, 1, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 1)
        self.choose_txt_file_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choose_txt_file_btn.setFont(font)
        self.choose_txt_file_btn.setObjectName("choose_txt_file_btn")
        self.gridLayout.addWidget(self.choose_txt_file_btn, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 3)
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setObjectName("send")
        self.gridLayout.addWidget(self.send, 7, 0, 1, 3)
        self.login_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login_input.setFont(font)
        self.login_input.setObjectName("login_input")
        self.gridLayout.addWidget(self.login_input, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.message_subject = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message_subject.setFont(font)
        self.message_subject.setObjectName("message_subject")
        self.gridLayout.addWidget(self.message_subject, 6, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_about = QtWidgets.QAction(MainWindow)
        self.open_about.setObjectName("open_about")
        self.menu.addAction(self.open_about)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choose_html_file_btn.setText(_translate("MainWindow", "Выбрать файл"))
        self.choose_file_btn.setText(_translate("MainWindow", "Выбрать файл"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.excel_filename_label.setText(_translate("MainWindow", "Выберите файл ->"))
        self.txt_filename_label.setText(_translate("MainWindow", "Выберите файл ->"))
        self.label_4.setText(_translate("MainWindow", "Путь до HTML файла с содержимым письма:"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_3.setText(_translate("MainWindow", "Путь до XLSX файла со списком школьников:"))
        self.html_filename_label.setText(_translate("MainWindow", "Выберите файл ->"))
        self.choose_txt_file_btn.setText(_translate("MainWindow", "Выбрать файл"))
        self.send.setText(_translate("MainWindow", "Разослать письма"))
        self.label_5.setText(_translate("MainWindow", "Путь до текстового файла для альт. письма:"))
        self.message_subject.setPlaceholderText(_translate("MainWindow", "Введите тему письма"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.open_about.setText(_translate("MainWindow", "Открыть справку"))
