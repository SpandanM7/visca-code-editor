from PyQt5.QtWidgets import QFileDialog

def open_file(parent, editor):
    fname, _ = QFileDialog.getOpenFileName(parent, "Open File", "", "Python Files (*.py);;All Files (*)")
    if fname:
        with open(fname, "r", encoding="utf-8") as f:
            editor.setPlainText(f.read())

def save_file(parent, editor):
    fname, _ = QFileDialog.getSaveFileName(parent, "Save File", "", "Python Files (*.py);;All Files (*)")
    if fname:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(editor.toPlainText())
