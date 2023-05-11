def getinfo():
    with open("settings.txt", "r") as file:
        settings = eval(file.read())

    colornum = settings["theme"]
    ip = settings["ip"]
    port = settings["port"]
    colornumeditor = settings["theme_editor"]

    return (colornum, ip, port, colornumeditor)