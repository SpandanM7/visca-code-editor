from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSignal

class Sidebar(QWidget):
    explorer_clicked = pyqtSignal()
    settings_clicked = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.explorer_btn = QPushButton("Explorer")
        self.settings_btn = QPushButton("Settings")
        layout.addWidget(self.explorer_btn)
        layout.addWidget(self.settings_btn)
        layout.addStretch(1)

        self.explorer_btn.clicked.connect(self.explorer_clicked.emit)
        self.settings_btn.clicked.connect(self.settings_clicked.emit)
