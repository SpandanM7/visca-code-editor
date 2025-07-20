from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ExplorerPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Explorer Page: Project/File Tree"))
