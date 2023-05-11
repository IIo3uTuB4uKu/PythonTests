import socket
from Funcs import getTests, reSaveTests, getInfoTests

def main(command):
    with open("settings.txt") as  f:
        settings = eval(f.read())

    PORT = settings["port"]
    IP = settings["ip"]
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP, PORT))
            s.send(str(command).encode('utf-8'))
            data = s.recv(16384)

        if command["command"] == "give info":
            if len(getTests()) != len(eval(data)) or getInfoTests() != eval(data):
                reSaveTests(eval(data))

                settings["UpDateTests"] = True
                with open("settings.txt", 'w') as f:
                    f.write(str(settings))

        s.close()
        return eval(data.decode())
    except:
        s.close()
        return None

if __name__ == "__main__":
    main({"command": "give info"})