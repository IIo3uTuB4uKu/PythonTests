import sys 
import os
import copy
import typing
from threading import Thread

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

import server
from colors import colors, colors_editor
from Funcs import save, getTests, change, deliteTest, change_image, UpDateFiles, getUsers, CheckStandartFiles

import MainTestCreate
import TestsCreate
import RandomTestCreate
import MenuDownloadTests
import InfoTest
import lookuser
import RandExit
import LookTest
import mainpage
import settings
import AddSolution


class MenuTests(QtWidgets.QMainWindow):
    def __init__(self, MainWindow) -> None:
        super().__init__()

    def gomain(self):
        self.gui = MenuDownloadTests.Ui_MainWindow().setupUi(self)
        self.ConnectButtons()

    def ConnectButtons(self):
        self.gui.pushButton.clicked.connect(self.SaveTests)

    def SaveTests(self):
        tests = getTests()
        dowloadtests = []
        for i, checkbox in enumerate(self.gui.checksboxes):
            if checkbox.isChecked():
                dowloadtests.append(i)
        
        with open("downloadtest.txt", 'w') as f:
            f.write(str(dowloadtests))

        self.close()

class MenuRandExit(QtWidgets.QMainWindow):
    def __init__(self, MainWindow) -> None:
        super().__init__()

    def gomain(self, info):
        self.gui = RandExit.Ui_MainWindow().setupUi(self, info)
        self.connectButtons()
    
    def connectButtons(self):
        self.gui.pushButton.clicked.connect(self.close)

class Log(object):
    def __init__(self):
        self.orgstdout = sys.stdout
        self.log = open("log.txt", "r")
        self.texts = self.log.read()

    def write(self, msg):
        self.log = open("log.txt", "r")
        self.texts = self.log.read()
        self.texts += msg
        self.orgstdout.write(msg)
        self.log = open("log.txt", "w")
        self.log.write(str(self.texts))
        self.log.close()


class AddSolutionMain(QtWidgets.QMainWindow):
    def __init__(self, MainWindow) -> None:
        super().__init__()
        self.solution = ""
        self.MainWindow = MainWindow
    
    def gomain(self):
        self.gui = AddSolution.Ui_MainWindow().setupUi(self)
        self.gui.textEdit.setText(self.MainWindow.test["settingsValue"][1])
        self.connectButtons()

    def connectButtons(self):
        self.gui.pushButton.clicked.connect(self.save)

    def save(self):
        self.solution = self.gui.textEdit.toPlainText()
        self.MainWindow.saveSolution()
        self.close()


class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        UpDateFiles()
        self.mychoice = ["0", "0"]
        self.menutest = MenuTests(self)
        self.solution = AddSolutionMain(self)
        self.randmenu = MenuRandExit(self)
        self.timermain = QtCore.QTimer()
        self.timerOn = False
        self.timermain.timeout.connect(self.UpdatePage)
        self.timertest = QtCore.QTimer()
        self.gomain()

    def gomain(self):
        self.timerOn = False
        self.timertest.stop()
        self.timerOn = False
        self.timermain.start(1000)
        self.nowWindow = "main"
        self.gui = mainpage.Ui_MainWindow().setupUi(self)
        self.ConnectTests()
        self.ConnectMenu()

    def gosettings(self):
        self.timermain.stop()
        self.nowWindow = "settings"
        self.gui = settings.Ui_MainWindow().setupUi(self)
        self.ConnectMenu()
        self.ConnectSaveSettings()

    def gocreatetestmain(self):
        self.saveTestInfo()
        self.nowWindow = "MainTestCreate"
        self.gui = MainTestCreate.Ui_MainWindow().setupUi(self, self.test)
        self.ConnectButtonsMainTest()
        self.ConnectMenuTest()

    def gotestscreate(self):
        self.saveTestInfo()
        
        self.nowWindow = "TestCreateInTest"
        self.gui = TestsCreate.Ui_MainWindow().setupUi(self, self.test, self.numTest)
        self.ConnectTestsInTest()
        self.ConnectMenuTest()

    def gorandomcreatetest(self):
        self.saveTestInfo()
        self.nowWindow = "RandomTestCreate"
        self.gui = RandomTestCreate.Ui_MainWindow().setupUi(self, self.test)
        self.ConnectMenuTest()
        self.ConnectRandomButton()

    def golookuser(self):
        self.timertest.stop()
        self.timerOn = False
        self.nowWindow = "LookUser"
        test = getTests()[int(self.test_number)]
        self.gui = lookuser.Ui_MainWindow().setupUi(self, test, self.mychoice)
        self.ConnectMenuLookTest()
        self.ConnectChangeMenu()

    def goInfoTest(self):
        self.saveTestInfo()
        self.nowWindow = "InfoTest"
        self.gui = InfoTest.Ui_MainWindow().setupUi(self)
        self.ConnectMenuTest()
        self.ConnectEnableCheckBox()
        self.ConnectOtherButtons()

    def gotestintest(self, i):
        self.saveTestInfo()
        self.numTest = i
        self.nowWindow = "oldTest"
        self.gotestscreate()

    def godownloadTests(self):
        self.menutest.gomain()
        self.menutest.show()

    def gochangetest(self):
        self.timerOn = False
        self.timertest.stop()
        self.numTest = 0
        self.changeTest = True
        self.gocreatetestmain()

    def ConnectTests(self):
        for i, test in enumerate(self.gui.Tests):
            if test != self.gui.Tests[-1]:
                test.connect(self.OpenTest, f"{i}")
            else:
                test.connect(self.AddNewTest, "AddNew")

    def ConnectTestsInTest(self):
        for i, button in enumerate(self.gui.TestButtons):
            button.clicked.connect(lambda checked, i=i: self.gotestintest(i))
        
        self.gui.pushButton_5.clicked.connect(self.AddNewTestToTest)
        self.gui.pushButton_6.clicked.connect(self.RemoveTestInTest)

    def ConnectChangeMenu(self):
        self.gui.comboBox.currentTextChanged.connect(lambda x: self.changeMyChoice(1))
        if self.mychoice[0] != "0":
            self.gui.comboBox_2.currentTextChanged.connect(lambda x: self.changeMyChoice(2))

    def ConnectMenu(self):
        self.gui.pushButton.clicked.connect(self.gomain)
        self.gui.pushButton_download.clicked.connect(self.godownloadTests)
        self.gui.pushButton_3.clicked.connect(self.gosettings)

    def ConnectRandomButton(self):
        self.gui.pushButton_4.clicked.connect(self.goInfoTest)
        self.gui.pushButton_5.clicked.connect(self.checkRandom)

    def ConnectEnableCheckBox(self):
        self.gui.checkBox.stateChanged.connect(lambda state=self.gui.checkBox.isChecked(): self.gui.lineEdit.setEnabled(state))
        self.gui.checkBox_2.stateChanged.connect(lambda state=self.gui.checkBox_2.isChecked(): self.gui.pushButton_5.setEnabled(state))

    def ConnectOtherButtons(self):
        self.gui.pushButton_5.clicked.connect(self.addAuthorSolution)
        self.gui.pushButton_pic.clicked.connect(self.addImage)
        self.gui.pushButton_save.clicked.connect(self.SaveTest)

    def ConnectMenuLookTest(self):
        self.gui.pushButton_back.clicked.connect(self.gomain)
        self.gui.pushButton.clicked.connect(lambda a, x=self.test_number: self.OpenTest(x))
        self.gui.pushButton_2.clicked.connect(self.gochangetest)
        self.gui.pushButton_3.clicked.connect(self.golookuser)

    def ConnectMenuTest(self):
        self.gui.pushButton.clicked.connect(self.gocreatetestmain)
        self.gui.pushButton_2.clicked.connect(self.gotestscreate)
        self.gui.pushButton_3.clicked.connect(self.gorandomcreatetest)
        self.gui.pushButton_info.clicked.connect(self.goInfoTest)
        self.gui.pushButton_delite.clicked.connect(self.DeliteTest)
        self.gui.pushButton_back.clicked.connect(self.gomain)

    def ConnectSaveSettings(self):
        self.gui.pushButtonDone.clicked.connect(self.SaveSettings)

    def ConnectButtonsMainTest(self):
        self.gui.pushButton_4.clicked.connect(self.gotestscreate)
    
    def SaveSettings(self):
        settings__ = {"theme": "0", "ip": "", "port": 0, "server_enable": False, "theme_editor": "0"}
        
        theme = self.gui.comboBox.currentText()
        for key, value in colors.items():
            if value[8] == theme:
                settings__["theme"] = str(key)
                break
        
        theme = self.gui.comboBox_editor.currentText()
        for key, value in colors_editor.items():
            if value[4] == theme:
                settings__["theme_editor"] = str(key)
                break

        settings__["port"] = int(self.gui.lineEdit_2.text())

        with open("settings.txt", "w") as file:
            file.write(str(settings__))

        self.gosettings()

    def saveSolution(self):
        self.test["settingsValue"][1] = self.solution.solution 

    def OpenTest(self, text):
        self.timermain.stop()
        if not self.timerOn:
            self.timerOn = True
            self.test_number = text
            self.timertest.timeout.connect(lambda x=text: self.OpenTest(x))
            self.timertest.start(1000)
        self.numberTest = text
        try:
            with open("tests/test" + text + ".txt", 'r') as f:
                self.test = eval(f.read())
        except:
            pass

        self.gui = LookTest.Ui_MainWindow().setupUi(self, self.test)
        self.ConnectMenuLookTest()
        

    def AddNewTestToTest(self):
        self.test["Tests"].append({"input": "", "output": ""})
        self.saveTestInfo()
        self.nowWindow = "oldTest"
        self.numTest += 1
        self.gotestscreate()
    
    def DeliteTest(self):
        if self.changeTest:
            deliteTest(self.numberTest)
        
        self.gomain()

    
    def SaveTest(self):
        self.saveTestInfo()
        if not self.changeTest:
            save(self.test)
        else:
            change(self.test, self.numberTest)
        self.gomain()

    def changeMyChoice(self, num_box):
        classes = ["Класс"]
        names = ["Имя Фамилия"]
        tests = getTests()
        for key, value in getUsers(tests[self.test["test_number"]]).items():
            print(key)
            classes.append(key)
            if num_box:
                for i in value:
                    names.append(i.replace(".txt", ''))
        
        print(names)

        if num_box == 2:
            self.mychoice[1] = str(names.index(self.gui.comboBox_2.currentText()))
        if self.mychoice[0] != str(classes.index(self.gui.comboBox.currentText())):
            self.mychoice[1] = "0"
        self.mychoice[0] = str(classes.index(self.gui.comboBox.currentText()))
        


        print(self.mychoice)

        self.golookuser()
        

    def addAuthorSolution(self):
        self.solution.gomain()
        self.solution.show()

    def addImage(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        name = change_image(file)
        self.test["iconame"] = name

    def saveTestInfo(self):
        if self.nowWindow == "MainTestCreate":
            self.test["Name"] = self.gui.textBrowser_2.toPlainText()
            self.test["Description"] = self.gui.textEdit.toPlainText()

        if self.nowWindow == "TestCreateInTest":
            self.test["Tests"][self.numTest]["input"] = self.gui.lineEdit.text()
            self.test["Tests"][self.numTest]["output"] = self.gui.lineEdit_2.text()
        
        if self.nowWindow == "InfoTest":
            self.test["settings"][0] = self.gui.checkBox.isChecked()
            self.test["settingsValue"][0] = self.gui.lineEdit.text()
            self.test["settings"][1] = self.gui.checkBox_2.isChecked()

        if self.nowWindow == "RandomTestCreate":
            self.test["RandomTestsCode"] = self.gui.textEdit.text()
            self.test["RandomTestIter"] = self.gui.lineEdit.text()        

    def RemoveTestInTest(self):
        self.test["Tests"].pop(self.numTest)
        self.numTest -= 1
        self.gotestscreate()

    def AddNewTest(self, text):
        self.timermain.stop()
        self.changeTest = False
        tests = getTests()
        self.test = {"Name": "", "Description": "", "Tests": [{"input": "", "output": ""},], "RandomTestsCode": "", "RandomTestIter": 0, "AuthorSolution": "", "settings": [False, False], "settingsValue": ["", ""], "iconame": "standartpic", "test_number": len(tests)}
        self.numTest = 0
        self.gocreatetestmain()

    def UpdatePage(self):
        if getTests() != self.gui.tests:
            self.gomain()

    def checkRandom(self):
        sys.stdout = Log()
        code_rand = self.gui.textEdit.text()
        inputs = [1]
        outputs = [1]

        with open("log.txt", 'w') as f:
            f.write("")

        code_rand += "\nprint(inputs)"
        code_rand += "\nprint(outputs)"
        exec(code_rand)

        with open("log.txt") as f:
            logs = f.readlines()

        inputs = eval(logs[0][:-1:])
        outputs = eval(logs[1][:-1:])
        
        self.randmenu.gomain((inputs, outputs))
        self.randmenu.show()
        

    def closeEvent(self, event):
        with open("settings.txt") as f:
            settings = eval(f.read())
        
        settings["server_enable"] = False

        with open("settings.txt", "w") as f:
            f.write(str(settings))


def main():
    CheckStandartFiles()
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.showMaximized()
    window.show()
    app.exec_()

if __name__ == '__main__':
    p1 = Thread(target=main)
    p2 = Thread(target=server.main)
    p2.start()
    p1.start()
    p1.join()