import shutil
import sys 
import os
import typing
from multiprocessing import Process
from threading import Thread

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from colors import colors, colors_editor
from Funcs import getTests, reSaveTests, CheckStandartFiles
from complitecode import Log
import mysettings
import complitecode
import client

import mainpage
import ShowSolution
import TestsDone
import myInfo
import TestMain
import settings


class Solution(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

    def gomain(self, solution):
        self.gui = ShowSolution.Ui_MainWindow().setupUi(self, solution)
        self.connectButtons()

    def connectButtons(self):
        self.gui.pushButton.clicked.connect(self.close)


class ResultTests(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
    
    def gomain(self, info, mainwin):
        self.gui = TestsDone.Ui_MainWindow().setupUi(self, info)
        with open(f"tests/{mainwin.test}") as f:
            self.test = eval(f.read())
        self.ConnectButtons()
    
    def ConnectButtons(self):
        self.gui.pushButton.clicked.connect(self.close)
        if self.gui.add_solution:
            self.gui.pushButton_solution.clicked.connect(self.showSolution)
    
    def showSolution(self):
        self.solution = Solution()
        self.solution.gomain(self.test["settingsValue"][1])
        self.solution.show()

class InfoAboutMe(QtWidgets.QMainWindow):
    def __init__(self, main, ) -> None:
        super().__init__()
        self.main = main
    
    def gomain(self, testnum, info):
        self.testnum = testnum
        self.info = info
        self.gui = myInfo.Ui_MainWindow().setupUi(self, self.info)

        self.connectButtons()
    
    def connectButtons(self):
        self.gui.pushButton.clicked.connect(self.saveInfo)

    def saveInfo(self):
        self.info["first_name"] = self.gui.lineEdit.text()
        self.info["second_name"] = self.gui.lineEdit_2.text()
        self.info["class"] = self.gui.lineEdit_3.text()
        self.info["test_number"] = self.testnum
        self.close()
        self.main.gotest()

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ResultTest = ResultTests()
        self.MenuInfo = InfoAboutMe(self)
        self.TimerUpdate = QtCore.QTimer()
        self.TimerUpdate.timeout.connect(self.CheckServer)
        self.myInfo = {"first_name": "", "second_name": "", "class": "", "done": False, "test_number": 0}

        self.gomain()

    def gomain(self):
        self.TimerUpdate.start(1000)
        self.nowWindow = "main"
        self.gui = mainpage.Ui_MainWindow().setupUi(self)
        self.ConnectTests()
        self.ConnectUpDate()
        self.ConnectMenu()

    def gotest(self):
        self.myInfo["done"] = False
        self.TimerUpdate.stop()
        self.nowWindow = "test"
        self.myInfo = self.MenuInfo.info
        p1 = Thread(target=client.main, args=({"command": "connectTest", "args": self.myInfo}, ))
        p1.start()
        self.gui = TestMain.Ui_MainWindow().setupUi(self, self.test)
        self.connectTestMenu()
        self.connectCompliteCode()

    def gosettings(self):
        self.TimerUpdate.stop()
        self.nowWindow = "settings"
        self.gui = settings.Ui_MainWindow().setupUi(self)
        self.ConnectMenu()
        self.ConnectSaveSettings()

    def ConnectTests(self):
        for i, test in enumerate(self.gui.Tests):
            test.connect(self.test_4, f"{i}")

    def connectCompliteCode(self):
        self.gui.pushButton_2.clicked.connect(self.complitecode)
    
    def ConnectUpDate(self):
        self.gui.pushButton_update.clicked.connect(self.CheckServer)

    def ConnectMenu(self):
        self.gui.pushButton.clicked.connect(self.gomain)
        self.gui.pushButton_3.clicked.connect(self.gosettings)

    def connectTestMenu(self):
        self.gui.pushButton_back.clicked.connect(self.gomain)

    def ConnectSaveSettings(self):
        self.gui.pushButtonDone.clicked.connect(self.SaveSettings)
    
    def SaveSettings(self):
        settings__ = {"theme": "0", "ip": "", "port": 0, "UpDateTests": False, "theme_editor": "0"}
        
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
        
        settings__["ip"] = self.gui.lineEdit.text()
        settings__["port"] = int(self.gui.lineEdit_2.text())

        with open("settings.txt", "w") as file:
            file.write(str(settings__))

        self.gosettings()

    def CheckServer(self):
        p1 = Thread(target=client.main, args=({"command": "give info"}, ))
        p1.start()

        with open("settings.txt") as  f:
            settings = eval(f.read())
        if settings["UpDateTests"]:
            settings["UpDateTests"] = False
            with open("settings.txt", "w") as file:
                file.write(str(settings))

            self.gomain()


    def complitecode(self):
        open("log.txt", 'w').close()
        code = self.gui.textEdit.text()
        
        with open(f"tests/{self.test}") as f:
            test = eval(f.read())

        tests = test["Tests"]
        all_inputs = []
        all_outputs = []
        for i in tests:
            try:
                complitecode.check_code(code, eval("(" + i["input"] + ",)"))
                all_inputs.append(i["input"])
                all_outputs.append(i["output"])
            except:
                pass

        with open("log.txt") as f:
            logs = f.readlines()

        self.gui.textBrowser_2.setText("".join(str(x) for x in logs))

        
        rights = [False for x in range(len(tests))]
        try:    
            if len(logs) / len(tests) == len(eval("(" + tests[0]["input"] + ",)")):
                rights = [True for x in range(len(tests))]
                for i, j in enumerate(tests):
                    exit = []
                    for k in range(int(len(logs) / len(tests))):
                        exit.append(logs[k + i * int(len(logs) / len(tests))].replace("\n", ""))
                    output = eval("(" + j["output"].replace("\n", "") + ", )")

                    print(output[0])

                    for i1, i2 in list(zip(exit, output)):
                        if str(i1) != str(i2):
                            rights[i] = False

            else:
                self.gui.textBrowser_2.setText("Неверное количество выводов")
        except:
            pass
        randoms = True

        if int(test["RandomTestIter"]) > 0:
            randoms = True
            sys.stdout = Log()
            for i in range(int(test["RandomTestIter"])):
                with open("log.txt", 'w') as f:
                    f.write("")
                code_rand = test["RandomTestsCode"]
                code_rand += "\nprint(inputs)"
                code_rand += "\nprint(outputs)"
                exec(code_rand)

                with open("log.txt") as f:
                    logs = f.readlines()

                inputs = eval(logs[0][:-1:])
                outputs = eval(logs[1][:-1:])

                print(logs, "logs")

                open("log.txt", 'w').close()
                complitecode.check_code(self.gui.textEdit.text(), inputs)

                with open("log.txt") as f:
                    logs_code = f.readlines()

                exit_code = "".join(str(x) for x in logs_code).replace("\n", '')
                true_outputs = "".join(str(x) for x in outputs).replace("\n", '')

                self.gui.textBrowser_2.append(exit_code)
                
                
                if exit_code != true_outputs:
                    randoms = False
                    break

        try: 
            if not False in rights and randoms:
                self.myInfo["done"] = True

                p1 = Thread(target=client.main, args=({"command": "UpdateInfo", "args": self.myInfo, "solution": code}, ))
                p1.start()

            print(rights)
            self.ResultTest.gomain((rights, all_inputs, all_outputs, randoms), self)
            self.ResultTest.show()
        except:
            pass

        

    def test_4(self, text):
        __tests = getTests()
        self.test = __tests[int(text)]

        with open(f"tests/{self.test}") as f:
            test = eval(f.read())

        self.MenuInfo.gomain(test["test_number"], self.myInfo)
        self.MenuInfo.show()



def main():
    CheckStandartFiles()
    dir = 'tests'
    shutil.rmtree(dir)
    os.mkdir("tests")
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.showMaximized()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()