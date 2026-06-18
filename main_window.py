import json

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QSplitter,
    QTabWidget, QPushButton, QStatusBar, QToolBar, QMessageBox,
    QFileDialog, QDialog, QLabel
)
from PyQt6.QtCore import Qt, QSettings, QSize, QUrl
from PyQt6.QtGui import QDesktopServices, QFont

from core.worker import SqlmapWorker
from resources.style import DARK
from widgets.target_tab import TargetTab
from widgets.request_tab import RequestTab
from widgets.injection_tab import InjectionTab
from widgets.enumeration_tab import EnumerationTab
from widgets.os_tab import OSTab
from widgets.general_tab import GeneralTab
from widgets.command_preview import CommandPreview
from widgets.output_panel import OutputPanel
from widgets.help_dialog import HelpDialog


class SqlmapGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SQLMap Pro GUI")

        self.worker = None
        self.settings = QSettings("SQLMapPro", "GUI")

        self.setup_ui()
        self.setup_menu()
        self.setup_toolbar()
        self.apply_theme()
        self.load_settings()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        layout.setSpacing(10)

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        self.tabs = QTabWidget()
        self.target_tab = TargetTab()
        self.request_tab = RequestTab()
        self.injection_tab = InjectionTab()
        self.enum_tab = EnumerationTab()
        self.os_tab = OSTab()
        self.general_tab = GeneralTab()

        self.tabs.addTab(self.target_tab, "Target")
        self.tabs.addTab(self.request_tab, "Request")
        self.tabs.addTab(self.injection_tab, "Injection")
        self.tabs.addTab(self.enum_tab, "Enumeration")
        self.tabs.addTab(self.os_tab, "OS Access")
        self.tabs.addTab(self.general_tab, "General")

        left_layout.addWidget(self.tabs, stretch=1)

        self.command_preview = CommandPreview()
        self.command_preview.run_btn.clicked.connect(self.run_sqlmap)
        self.command_preview.stop_btn.clicked.connect(self.stop_sqlmap)
        self.command_preview.wizard_btn.clicked.connect(self.run_wizard)
        left_layout.addWidget(self.command_preview, stretch=0)

        self.generate_btn = QPushButton("Generate Command")
        self.generate_btn.setMinimumHeight(40)
        self.generate_btn.clicked.connect(self.generate_command)
        left_layout.addWidget(self.generate_btn, stretch=0)

        self.output_panel = OutputPanel()

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(self.output_panel)
        splitter.setSizes([500, 500])
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        splitter.setHandleWidth(2)

        layout.addWidget(splitter)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

    def setup_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction("New Session", self.new_session)
        file_menu.addAction("Load Config", self.load_config)
        file_menu.addAction("Save Config", self.save_config)
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)

        tools_menu = menubar.addMenu("Tools")
        tools_menu.addAction("Update sqlmap", self.update_sqlmap)
        tools_menu.addAction("Check Version", self.check_version)

        help_menu = menubar.addMenu("Help")
        help_menu.addAction("GUI Help", self.open_help)
        help_menu.addAction("Documentation", self.open_docs)
        help_menu.addAction("About", self.show_about)

    def setup_toolbar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        toolbar.addAction("Target", lambda: self.tabs.setCurrentIndex(0))
        toolbar.addAction("Request", lambda: self.tabs.setCurrentIndex(1))
        toolbar.addAction("Injection", lambda: self.tabs.setCurrentIndex(2))
        toolbar.addSeparator()
        toolbar.addAction("Run", self.run_sqlmap)
        toolbar.addAction("Stop", self.stop_sqlmap)
        toolbar.addSeparator()
        toolbar.addAction("Help", self.open_help)

    def apply_theme(self):
        self.setStyleSheet(DARK)

    def load_settings(self):
        saved = self.settings.value("window/size")
        if saved and saved.isValid():
            self.resize(saved)

    def save_settings(self):
        self.settings.setValue("window/size", self.size())

    def generate_command(self):
        command = ["sqlmap"]
        command.extend(self.target_tab.get_options())
        command.extend(self.request_tab.get_options())
        command.extend(self.injection_tab.get_options())
        command.extend(self.enum_tab.get_options())
        command.extend(self.os_tab.get_options())
        command.extend(self.general_tab.get_options())
        self.command_preview.update_command(command)
        return command

    def run_sqlmap(self):
        command = self.generate_command()
        if len(command) <= 1:
            QMessageBox.warning(self, "Warning", "Please configure at least a target URL!")
            return

        self.output_panel.clear_output()
        self.output_panel.set_status("Running...")
        self.command_preview.run_btn.setEnabled(False)
        self.command_preview.stop_btn.setEnabled(True)
        self.command_preview.progress.setRange(0, 0)

        self.worker = SqlmapWorker(command)
        self.worker.output_signal.connect(self.output_panel.append_output)
        self.worker.finished_signal.connect(self.on_finished)
        self.worker.start()

    def stop_sqlmap(self):
        if self.worker:
            self.worker.stop()
            self.output_panel.append_output("\n[STOPPED] Process terminated by user")

    def on_finished(self, code, message):
        self.command_preview.run_btn.setEnabled(True)
        self.command_preview.stop_btn.setEnabled(False)
        self.command_preview.progress.setRange(0, 100)
        self.command_preview.progress.setValue(100)
        self.output_panel.set_status(f"Finished: {message}")
        self.status_bar.showMessage(f"Exit code: {code} | {message}")

    def run_wizard(self):
        self.worker = SqlmapWorker(["sqlmap", "--wizard"])
        self.worker.output_signal.connect(self.output_panel.append_output)
        self.worker.start()

    def new_session(self):
        self.output_panel.clear_output()

    def load_config(self):
        file, _ = QFileDialog.getOpenFileName(self, "Load Config", "", "JSON (*.json)")
        if file:
            with open(file) as f:
                json.load(f)

    def save_config(self):
        file, _ = QFileDialog.getSaveFileName(self, "Save Config", "", "JSON (*.json)")
        if file:
            config = {"command": self.command_preview.command_edit.toPlainText()}
            with open(file, 'w') as f:
                json.dump(config, f, indent=2)

    def update_sqlmap(self):
        self.worker = SqlmapWorker(["sqlmap", "--update"])
        self.worker.output_signal.connect(self.output_panel.append_output)
        self.worker.start()

    def check_version(self):
        self.worker = SqlmapWorker(["sqlmap", "--version"])
        self.worker.output_signal.connect(self.output_panel.append_output)
        self.worker.start()

    def open_help(self):
        dialog = HelpDialog(self)
        dialog.exec()

    def open_docs(self):
        QDesktopServices.openUrl(QUrl("https://sqlmap.org"))

    def show_about(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("About")
        dialog.setFixedSize(400, 280)
        layout = QVBoxLayout(dialog)
        layout.setSpacing(8)

        title = QLabel("SQLMap Pro GUI")
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        title.setStyleSheet("color: #00d4aa;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        for text in ["Professional GUI for sqlmap", "Built with PyQt6", ""]:
            label = QLabel(text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)

        links = [
            ("Developer: RootX", ""),
            ("Telegram: @rootx.202", "https://t.me/rootx.202"),
            ("GitHub: Rootx202/SQLMap-GUI", "https://github.com/Rootx202/SQLMap-GUI"),
        ]
        for text, url in links:
            label = QLabel(f'<a href="{url}" style="color: #4fc3f7; text-decoration: none;">{text}</a>' if url else text)
            label.setOpenExternalLinks(True)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)

        layout.addStretch()
        note = QLabel("For authorized security testing only")
        note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        note.setStyleSheet("color: #888; font-size: 12px;")
        layout.addWidget(note)

        btn = QPushButton("Close")
        btn.clicked.connect(dialog.accept)
        btn.setFixedWidth(100)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn)
        layout.addLayout(btn_layout)

        dialog.exec()

    def closeEvent(self, event):
        self.save_settings()
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.wait(2000)
        event.accept()
