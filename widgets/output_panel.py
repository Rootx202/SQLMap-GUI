from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QPlainTextEdit, QLabel, QFileDialog
)
from PyQt6.QtGui import QFont

from datetime import datetime


class OutputPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        toolbar = QHBoxLayout()
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.clicked.connect(self.clear_output)
        self.save_btn = QPushButton("Save Output")
        self.save_btn.clicked.connect(self.save_output)
        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("Filter output...")
        self.filter_input.setMaximumWidth(200)
        toolbar.addWidget(self.clear_btn)
        toolbar.addWidget(self.save_btn)
        toolbar.addStretch()
        toolbar.addWidget(self.filter_input)
        layout.addLayout(toolbar)

        self.output_text = QPlainTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("Output will appear here...")
        font = QFont("Consolas", 11)
        font.setStyleHint(QFont.StyleHint.Monospace)
        self.output_text.setFont(font)
        layout.addWidget(self.output_text)

        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)

    def append_output(self, text):
        self.output_text.appendPlainText(text)
        scrollbar = self.output_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def clear_output(self):
        self.output_text.clear()

    def save_output(self):
        file, _ = QFileDialog.getSaveFileName(
            self, "Save Output",
            f"sqlmap_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            "Text Files (*.txt);;All Files (*)"
        )
        if file:
            with open(file, 'w') as f:
                f.write(self.output_text.toPlainText())

    def set_status(self, text):
        self.status_label.setText(text)
