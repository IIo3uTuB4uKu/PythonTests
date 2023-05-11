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
    try:
        with open("connections.txt") as f:
            all_connected = eval(f.read())
    except:
        all_connected = []
    
    connections = []
    for i in all_connected:
        if i["test_number"] == test["test_number"]:
            connections.append(i)

    return connections

def getInfoTests():
    tests = getTests()
    InfoTests = []
    for i in tests:
        with open(f"tests/{i}") as f:
            InfoTests.append(eval(f.read()))

    return InfoTests

def UpDateFiles():
    with open("connections.txt", 'w') as f:
        f.close()

    with open("downloadtest.txt", 'w') as f:
        f.write("[]")

def saveUserInfo(info):
    tests = getTests()
    with open(f"tests/{tests[info['test_number']]}") as f:
        test = eval(f.read())
        test_name = test["Name"].replace('\n', '')
    if not os.path.exists(f"solutions/{test_name}"):
        os.mkdir(f"solutions/{test_name}")
    if not os.path.exists(f"solutions/{test_name}/{info['class']}"):
        os.mkdir(f"solutions/{test_name}/{info['class']}")
    with open(f"solutions/{test_name}/{info['class']}/{info['first_name']} {info['second_name']}.txt", 'w') as f:
        f.write(str(info))


def getUsers(test_name):
    users = dict()
    with open(f"tests/{test_name}") as f:
        test = eval(f.read())
        test_name = test["Name"].replace('\n', '')
    try:
        for class_ in pathlib.Path(f"solutions/{test_name}").iterdir():
            users[class_.name] = []
            for name_ in pathlib.Path(f"solutions/{test_name}/{class_.name}").iterdir():
                users[class_.name].append(name_.name)
    except:
        pass

    return users

def CheckStandartFiles():
    all_files = os.listdir(".")
    dirs = list(os.walk('.'))[0][1]

    if "solutions" not in dirs:
        os.mkdir("solutions")
    
    if "tests" not in dirs:
        os.mkdir("tests")
    
    if "testsimgs" not in dirs:
        os.mkdir("testsimgs")
    
    if "connections.txt" not in all_files:
        with open("connections.txt", 'w') as f:
            f.write("")
    
    if "downloadtest.txt" not in all_files:
        with open("downloadtest.txt", 'w') as f:
            f.write("[]")
    
    if "log.txt" not in all_files:
        with open("log.txt", 'w') as f:
            f.write("")

    if "settings.txt" not in all_files:
        with open("settings.txt", 'w') as f:
            f.write("{'theme': '0', 'ip': '', 'port': 5337, 'server_enable': False, 'theme_editor': '0'}")

if __name__ == "__main__":
    saveUserInfo({'first_name': 'Максим', 'second_name': 'Шишкин', 'class': '8А', 'done': True, 'test_number': 1})