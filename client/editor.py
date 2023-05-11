from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.Qsci import * 


import keyword
import pkgutil
from pathlib import Path
from lexer import PyCustomLexer
from autcompleter import AutoCompleter
from typing import TYPE_CHECKING
from colors import colors, colors_editor
from mysettings import getinfo

if TYPE_CHECKING:
    from main import MainWindow

import resources

class Editor(QsciScintilla):
    
    def __init__(self, main_window, parent=None,):
        super(Editor, self).__init__(parent)

        self.colors_num = getinfo()[0]
        self.colors_num_editor = getinfo()[3]

        self.main_window: MainWindow = main_window
        
        # EDITOR
        self.cursorPositionChanged.connect(self._cusorPositionChanged)        

        # encoding
        self.setUtf8(True)
        # Font
        self.window_font = QFont("Fire Code") # font needs to be installed in your computer if its not use something else
        self.window_font.setPointSize(12)
        self.setFont(self.window_font)

        # brace matching
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # indentation
        self.setIndentationGuides(True)
        self.setTabWidth(4)
        self.setIndentationsUseTabs(False)
        self.setAutoIndent(True)

        # autocomplete
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.setAutoCompletionThreshold(1) 
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionUseSingle(QsciScintilla.AcusNever)


        # caret
        self.setCaretForegroundColor(QColor(colors_editor[self.colors_num_editor][2]))
        self.setCaretLineVisible(True)
        self.setCaretWidth(2)
        self.setCaretLineBackgroundColor(QColor(colors_editor[self.colors_num_editor][3]))
        
        self.setStyleSheet(f"""background-color: {colors[self.colors_num][5]};
    color: #fff;
    border-radius: 3px;
    font-size: 12px;
    border:0px""")


        # EOL
        self.setEolMode(QsciScintilla.EolWindows)
        self.setEolVisibility(False)


   
            # lexer for syntax highlighting
        self.pylexer = PyCustomLexer(self) 
        self.pylexer.setDefaultFont(self.window_font)

        self.__api = QsciAPIs(self.pylexer)

        self.auto_completer = AutoCompleter("test.py", self.__api)
        self.auto_completer.finished.connect(self.loaded_autocomplete) # you can use this callback to do something 

        self.setLexer(self.pylexer)



        # line numbers
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, "000")
        self.setMarginsForegroundColor(QColor("#ff888888"))
        self.setMarginsBackgroundColor(QColor(colors_editor[self.colors_num_editor][0]))
        self.setMarginsFont(self.window_font)

        # key press
        # self.keyPressEvent = self.handle_editor_press

    def toggle_comment(self, text: str):
        lines = text.split('\n')
        toggled_lines = []
        for line in lines:
            if line.startswith('#'):
                toggled_lines.append(line[1:].lstrip())
            else:
                toggled_lines.append("# " + line)
        
        return '\n'.join(toggled_lines)

    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_Space:
            pos = self.getCursorPosition()
            self.auto_completer.get_completions(pos[0]+1, pos[1], self.text())
            self.autoCompleteFromAPIs()
            return

        if e.modifiers() == Qt.ControlModifier and e.key() == Qt.Key_X: # CUT SHORTCUT
            if not self.hasSelectedText():
                line, index = self.getCursorPosition()
                self.setSelection(line, 0, line, self.lineLength(line))
                self.cut()
                return
            
        if e.modifiers() == Qt.ControlModifier and e.text() == "/": # COMMENT SHORTCUT
            if self.hasSelectedText():
                start, srow, end, erow = self.getSelection()
                self.setSelection(start, 0, end, self.lineLength(end)-1)
                self.replaceSelectedText(self.toggle_comment(self.selectedText()))
                self.setSelection(start, srow, end, erow)
            else:
                line, _ = self.getCursorPosition()
                self.setSelection(line, 0, line, self.lineLength(line)-1)
                self.replaceSelectedText(self.toggle_comment(self.selectedText()))
                self.setSelection(-1, -1, -1, -1) # reset selection
            return

        return super().keyPressEvent(e)
    
    def _cusorPositionChanged(self, line: int, index: int) -> None:
        self.auto_completer.get_completions(line+1, index, self.text())

    def loaded_autocomplete(self):
        pass
