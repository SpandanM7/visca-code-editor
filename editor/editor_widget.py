from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QFont

class CodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Consolas", 12))
        self.setPlaceholderText("Write your code here...")
