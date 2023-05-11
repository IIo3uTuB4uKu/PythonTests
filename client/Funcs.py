import pathlib
import os
import shutil
from PIL import Image


def save(test):
    tests = getTests()
    namefile = "test" + str(len(tests))
    with open("tests/" + namefile + ".txt", "w") as f:
        f.write(str(test))

def getTests():
    tests = []
    for test in pathlib.Path("tests").iterdir():
        if "test" in test.name:
            tests.append(test.name)

    tests_new = []
    for i in range(len(tests)):
        tests_new.append(f"test{i}.txt")

    return tests_new

def getInfoTests():
    tests = getTests()
    InfoTests = []
    for i in tests:
        with open(f"tests/{i}") as f:
            InfoTests.append(eval(f.read()))

    return InfoTests

def change(test, num):
    namefile = "test" + num
    with open("tests/" + namefile + ".txt", "w") as f:
        f.write(str(test))

def deliteTest(num):
    tests = getTests()
    tests_date = []

    for i in tests:
        with open("tests/" + i) as f:
            tests_date.append(f.read())

    dir = 'tests'
    shutil.rmtree(dir)
    os.mkdir("tests")

    tests_date.pop(int(num))

    for test in tests_date:
        save(test)

def change_image(dir):
    img = Image.open(dir)

    name = ""
    for i in dir[::-1]:
        if i != "/":
            name += i
        else:
            break
    
    name = name[::-1]

    print(name)

    new_image = img.resize((100, 100))
    new_image.save(f'testsimgs/{name}')

    return name.replace(".png", "")


def connected(test):
    with open("connections.txt") as f:
        all_connected = eval(f.read())
    
    connections = []
    for i in all_connected:
        if i["test_number"] == test["test_number"]:
            connections.append(i)

    return connections

def reSaveTests(tests):
    dir = 'tests'
    shutil.rmtree(dir)
    os.mkdir("tests")

    for test in tests:
        save(test)

def CheckStandartFiles():
    all_files = os.listdir(".")
    dirs = list(os.walk('.'))[0][1]
    
    if "tests" not in dirs:
        os.mkdir("tests")
    
    if "testsimgs" not in dirs:
        os.mkdir("tests")

    if "log.txt" not in all_files:
        with open("log.txt", 'w') as f:
            f.write("")

    if "settings.txt" not in all_files:
        with open("settings.txt", 'w') as f:
            f.write("{'theme': '0', 'ip': '127.0.0.1', 'port': 5337, 'UpDateTests': False, 'theme_editor': '0'}")

if __name__ == "__main__":
    print(getTests())