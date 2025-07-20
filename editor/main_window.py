from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog, QSplitter, QWidget, QVBoxLayout
from editor.editor_widget import CodeEditor
from editor.output_console import OutputConsole
from editor.file_manager import open_file, save_file
import subprocess, sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cool PyQt5 Code Editor")
        self.setGeometry(200, 100, 900, 650)

        # Central widgets
        self.editor = CodeEditor()
        self.terminal = OutputConsole()
        self.init_ui()

    def init_ui(self):
        # --- Layout: Code Editor & Terminal ---
        splitter = QSplitter()
        splitter.setOrientation(2)  # Vertical (Qt.Vertical)
        splitter.addWidget(self.editor)
        splitter.addWidget(self.terminal)
        splitter.setSizes([400, 150])
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(splitter)
        container.setLayout(layout)
        self.setCentralWidget(container)

        # --- Menubar ---
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

    def run_code(self):
        code = self.editor.toPlainText()
        temp_file = "temp_code.py"
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(code)
        try:
            result = subprocess.run([sys.executable, temp_file],
                                    capture_output=True, text=True, timeout=10)
            output = result.stdout
            error = result.stderr
            self.terminal.append_text(">> Output:\n" + output)
            if error:
                self.terminal.append_text(">> Errors:\n" + error)
        except Exception as e:
            self.terminal.append_text(f"Exception: {e}")
