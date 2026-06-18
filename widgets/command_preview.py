from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPlainTextEdit, QPushButton, QProgressBar, QFileDialog, QApplication, QLabel
)


class CommandPreview(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        cmd_row = QHBoxLayout()
        cmd_label = QLabel("Command:")
        cmd_label.setFixedWidth(70)
        self.command_edit = QPlainTextEdit()
        self.command_edit.setPlaceholderText("Command will appear here...")
        self.command_edit.setMaximumHeight(60)
        self.command_edit.setReadOnly(True)
        cmd_row.addWidget(cmd_label)
        cmd_row.addWidget(self.command_edit, stretch=1)
        layout.addLayout(cmd_row)

        btn_row = QHBoxLayout()
        self.copy_btn = QPushButton("Copy")
        self.save_btn = QPushButton("Save")
        self.run_btn = QPushButton("Run sqlmap")
        self.run_btn.setStyleSheet("""
            QPushButton {
                background-color: #00d4aa;
                color: #1a1a2e;
                font-weight: 700;
            }
            QPushButton:hover { background-color: #00b894; }
        """)
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.setEnabled(False)
        self.wizard_btn = QPushButton("Wizard")

        self.copy_btn.clicked.connect(self.copy_command)
        self.save_btn.clicked.connect(self.save_command)

        btn_row.addWidget(self.copy_btn)
        btn_row.addWidget(self.save_btn)
        btn_row.addStretch()
        btn_row.addWidget(self.run_btn)
        btn_row.addWidget(self.stop_btn)
        btn_row.addWidget(self.wizard_btn)
        layout.addLayout(btn_row)

        self.progress = QProgressBar()
        self.progress.setTextVisible(True)
        self.progress.setFormat("%p%")
        self.progress.setMaximumHeight(16)
        layout.addWidget(self.progress)

    def update_command(self, command):
        self.command_edit.setPlainText(" ".join(command))

    def copy_command(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.command_edit.toPlainText())

    def save_command(self):
        file, _ = QFileDialog.getSaveFileName(
            self, "Save Command", "sqlmap_command.sh", "Shell Script (*.sh);;All Files (*)"
        )
        if file:
            with open(file, 'w') as f:
                f.write("#!/bin/bash\n")
                f.write(self.command_edit.toPlainText())
