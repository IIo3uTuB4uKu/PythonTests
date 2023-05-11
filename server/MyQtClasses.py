from PyQt5 import QtCore, QtGui, QtWidgets
import copy

class MyFrame(QtWidgets.QFrame):
    def __init__(self, color1, color2, qss, parent=None):
        super().__init__(parent)

        self.MouseInFrame = False
        self.function = False
        self.argsFunc = False
        self.setMinimumSize(0, 50)

        self.color1 = color1
        self.color2 = color2

        self.qss = qss

        self.enable_anim = True

        self.multies = [(self.color2.red() - self.color1.red()) / 100,
                        (self.color2.green() - self.color1.green()) / 100,
                        (self.color2.blue() - self.color1.blue()) / 100,
                        ]

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0,
            endValue=100,
            duration=200
        )

        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)

    def _animate(self, value):
        if self.enable_anim:
            color = (int(self.color1.red() + (value * self.multies[0])),
                     int(self.color1.green() + (value * self.multies[1])),
                     int(self.color1.blue() + (value * self.multies[2])))
            qss = copy.copy(self.qss)

            qss += f"background-color: rgb({color[0]}, {color[1]}, {color[2]})"
            self.setStyleSheet(qss)

            self.shadow = QtWidgets.QGraphicsDropShadowEffect(
                blurRadius=0.3 * value, xOffset=0, yOffset=0, color=QtGui.QColor(255, 255, 255))
            self.setGraphicsEffect(self.shadow)

    def connect(self, func, *args):
        self.function = func
        self.argsFunc = args

    def enterEvent(self, event):
        self.MouseInFrame = True
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def mousePressEvent(self, event):
        if self.function:
            self.function(*self.argsFunc)

    def leaveEvent(self, event):
        self.MouseInFrame = False
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)


class MyButton(QtWidgets.QPushButton):
    def __init__(self, color1, color2, qss, parent=None):
        super().__init__(parent)

        self.setMinimumSize(0, 50)

        self.color1 = color1
        self.color2 = color2

        self.qss = qss

        self.enable_anim = True

        self.multies = [(self.color2.red() - self.color1.red()) / 100,
                        (self.color2.green() - self.color1.green()) / 100,
                        (self.color2.blue() - self.color1.blue()) / 100,
                        ]

        self._animation = QtCore.QVariantAnimation(
            self,
            valueChanged=self._animate,
            startValue=0,
            endValue=100,
            duration=200
        )

        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)

    def _animate(self, value):
        if self.enable_anim:
            color = (int(self.color1.red() + (value * self.multies[0])),
                     int(self.color1.green() + (value * self.multies[1])),
                     int(self.color1.blue() + (value * self.multies[2])))
            qss = copy.copy(self.qss)

            qss += f"background-color: rgb({color[0]}, {color[1]}, {color[2]})"
            self.setStyleSheet(qss)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

class MyTextBrowser(QtWidgets.QTextBrowser):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def mousePressEvent(self, event):
        self.parent.mousePressEvent(event)