# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from MyQtClasses import MyFrame, MyButton, MyTextBrowser
from colors import colors
from mysettings import getinfo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        colors_num = getinfo()[0]
        test = MainWindow.test


        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        #menu
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(50, 0))
        self.frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame.setStyleSheet(f"background-color: {colors[colors_num][5]};")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(10)
        self.pushButton = MyButton(QtGui.QColor(*colors[colors_num][0]), QtGui.QColor(*colors[colors_num][1]), "border: 0px; border-radius: 5px;", self.frame)
        self.pushButton.setIcon(QtGui.QIcon(f"pics\\info{colors[colors_num][7]}.png"))
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = MyButton(QtGui.QColor(*colors[colors_num][0]), QtGui.QColor(*colors[colors_num][1]), "border: 0px; border-radius: 5px;", self.frame)
        self.pushButton_2.setIcon(QtGui.QIcon(f"pics\\testsintestpic{colors[colors_num][7]}.png"))
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = MyButton(QtGui.QColor(*colors[colors_num][0]), QtGui.QColor(*colors[colors_num][1]), "border: 0px; border-radius: 5px;", self.frame)
        self.pushButton_3.setIcon(QtGui.QIcon(f"pics\\random{colors[colors_num][7]}.png"))
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_info = MyButton(QtGui.QColor(*colors[colors_num][1]), QtGui.QColor(*colors[colors_num][1]), "border: 0px; border-radius: 5px;", self.frame)
        self.pushButton_info.setIcon(QtGui.QIcon(f"pics\\settingtest{colors[colors_num][7]}.png"))
        self.pushButton_info.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_info.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_info.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_info.setText("")
        self.pushButton_info.setObjectName("pushButton_info")
        self.verticalLayout.addWidget(self.pushButton_info)
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.pushButton_delite = MyButton(QtGui.QColor(*colors[colors_num][0]), QtGui.QColor(*colors[colors_num][1]), "border: 0px; border-radius: 5px;", self.frame)
        self.pushButton_delite.setIcon(QtGui.QIcon(f"pics\\delite{colors[colors_num][7]}.png"))
        self.pushButton_delite.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_delite.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_delite.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_delite.setStyleSheet(f"background-color: {colors[colors_num][2]};\n"
"border: 0px; border-radius: 5px")
        self.pushButton_delite.setText("")
        self.pushButton_delite.setObjectName("pushButton_delite")
        self.verticalLayout.addWidget(self.pushButton_delite)
        
        self.pushButton_back = MyButton(QtGui.QColor(*colors[colors_num][0]), QtGui.QColor(*colors[colors_num][1]), "border: 0px; border-radius: 5px;", self.frame)
        self.pushButton_back.setIcon(QtGui.QIcon(f"pics\\returnpic{colors[colors_num][7]}.png"))
        self.pushButton_back.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_back.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_back.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_back.setStyleSheet(f"background-color: {colors[colors_num][2]};\n"
"border: 0px; border-radius: 5px")
        self.pushButton_back.setText("")
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayout.addWidget(self.pushButton_back)

        self.horizontalLayout.addWidget(self.frame)


        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setStyleSheet(f"background-color: {colors[colors_num][3]};")
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.gridFrame)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(400, 0))
        self.horizontalFrame.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setSpacing(0)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalFrame)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setChecked(test["settings"][0])
        self.checkBox.setStyleSheet(f"color:{colors[colors_num][6]}")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalFrame)
        self.lineEdit.setEnabled(test["settings"][0])
        self.lineEdit.setPlaceholderText("Имя Функции")
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit.setStyleSheet("color: #000;\n"
"background: #fff;\n"
"border:0px;\n"
"border-radius: 2px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addWidget(self.horizontalFrame, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.horizontalFrame1 = QtWidgets.QFrame(self.gridFrame)
        self.horizontalFrame1.setMinimumSize(QtCore.QSize(400, 0))
        self.horizontalFrame1.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalFrame1)
        self.checkBox_2.setStyleSheet(f"color:{colors[colors_num][6]}")
        self.checkBox_2.setChecked(test["settings"][1])
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.pushButton_5 = MyButton(QtGui.QColor(*colors[colors_num][0]), QtGui.QColor(*colors[colors_num][1]), "border: 0px; border-radius: 5px;", self.horizontalFrame1)
        self.pushButton_5.setEnabled(test["settings"][1])
        self.pushButton_5.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setIcon(QtGui.QIcon(f"pics\\download{colors[colors_num][7]}.png"))
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.gridLayout.addWidget(self.horizontalFrame1, 1, 1, 1, 1)

        self.horizontalFrame2 = QtWidgets.QFrame(self.gridFrame)
        self.horizontalFrame2.setMinimumSize(QtCore.QSize(400, 0))
        self.horizontalFrame2.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame2.setObjectName("horizontalFrame2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_3")
        self.Labelpic = QtWidgets.QLabel(self.horizontalFrame1)
        self.Labelpic.setStyleSheet(f"color:{colors[colors_num][6]}")
        self.Labelpic.setText("Поставить иконку")
        self.Labelpic.setObjectName("checkBox_2")
        self.horizontalLayout_6.addWidget(self.Labelpic)
        self.pushButton_pic = MyButton(QtGui.QColor(*colors[colors_num][0]), QtGui.QColor(*colors[colors_num][1]), "border: 0px; border-radius: 5px;", self.horizontalFrame1)
        self.pushButton_pic.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_pic.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_pic.setIcon(QtGui.QIcon(f"pics\\pic{colors[colors_num][7]}.png"))
        self.pushButton_pic.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_pic.setText("")
        self.pushButton_pic.setObjectName("pushButton_pic")
        self.horizontalLayout_6.addWidget(self.pushButton_pic)
        self.gridLayout.addWidget(self.horizontalFrame2, 2, 1, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.pushButton_save = MyButton(QtGui.QColor(*colors[colors_num][0]), QtGui.QColor(*colors[colors_num][1]), f"border: 0px; border-radius: 5px;color:{colors[colors_num][6]};", self.gridFrame)
        self.pushButton_save.setMinimumSize(QtCore.QSize(70, 20))
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_2.addWidget(self.pushButton_save)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.gridFrame)

        self.horizontalLayout.addWidget(self.gridFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        return self

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Проверять в Функции"))
        self.pushButton_save.setText("Сохранить")
        self.checkBox_2.setText(_translate("MainWindow", "Авторское решение"))
