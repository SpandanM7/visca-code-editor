from PyQt5.QtWidgets import (
    QMainWindow, QAction, QSplitter, QWidget, QVBoxLayout, QStackedWidget
)
from PyQt5.QtCore import Qt
from editor.editor_widget import CodeEditor
from editor.output_console import OutputConsole
from editor.file_manager import open_file, save_file
from editor.sidebar import Sidebar
from editor.explorer_page import ExplorerPage
from editor.settings_page import SettingsPage
import subprocess
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cool PyQt5 Code Editor")
        self.setGeometry(200, 100, 900, 650)
        self.sidebar = Sidebar()

        # Initialize content pages
        self.editor = CodeEditor()
        self.terminal = OutputConsole()
        self.explorer_page = ExplorerPage()
        self.settings_page = SettingsPage()

        # Stacked widget for main pages
        self.stacked_widget = QStackedWidget()
        self.editor_page = QWidget()
        editor_layout = QVBoxLayout()
        editor_layout.addWidget(self.editor)
        editor_layout.addWidget(self.terminal)
        self.editor_page.setLayout(editor_layout)

        self.stacked_widget.addWidget(self.editor_page)     # Index 0: Editor + Terminal
        self.stacked_widget.addWidget(self.explorer_page)   # Index 1: Explorer
        self.stacked_widget.addWidget(self.settings_page)   # Index 2: Settings

        self.init_ui()
        self.connect_sidebar()

    def init_ui(self):
        # Horizontal splitter: Sidebar | Main Pages
        splitter_main = QSplitter(Qt.Horizontal)
        splitter_main.addWidget(self.sidebar)
        splitter_main.addWidget(self.stacked_widget)
        splitter_main.setSizes([120, 780])

        # Main layout
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(splitter_main)
        self.setCentralWidget(container)

        # Menubar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        run_action = QAction("Run", self)

        open_action.triggered.connect(lambda: open_file(self, self.editor))
        save_action.triggered.connect(lambda: save_file(self, self.editor))
        run_action.triggered.connect(self.run_code)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(run_action)

    def connect_sidebar(self):
        # Button signals switch visible page in stacked widget
        self.sidebar.explorer_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.sidebar.settings_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        # You can add more handler/buttons similarly
        # To return to the editor/terminal page:
        # e.g. add a button or connect double click / menu action for: self.stacked_widget.setCurrentIndex(0)

    def run_code(self):
        code = self.editor.toPlainText()
        temp_file = "temp_code.py"
        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write(code)
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=10
            )
            output = result.stdout
            error = result.stderr
            self.terminal.console.clear()
            self.terminal.append_text(">> Output:\n" + output)
            if error:
                self.terminal.append_text(">> Errors:\n" + error)
        except Exception as e:
            self.terminal.append_text(f"Exception: {e}")
        finally:
            try:
                os.remove(temp_file)
            except Exception:
                pass
