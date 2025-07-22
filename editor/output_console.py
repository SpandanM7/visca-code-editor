from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class OutputConsole(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.console = QTextEdit(self)
        self.console.setReadOnly(True)
        self.console.setStyleSheet("background: #23272e; color: #9cdcfe; font-family: Consolas")
        self.layout.addWidget(self.console)

    def append_text(self, text):
        self.console.append(text)
