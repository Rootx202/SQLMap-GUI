from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QSpinBox, QCheckBox, QPushButton, QGroupBox, QFileDialog
)

from .base_tab import BaseTab


class GeneralTab(BaseTab):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        session_group = QGroupBox("Session Management")
        session_layout = QFormLayout(session_group)
        self.batch = QCheckBox("--batch (No user input)")
        self.batch.setChecked(True)
        session_layout.addRow("Automation:", self.batch)
        self.flush = QCheckBox("--flush-session")
        session_layout.addRow("Clear:", self.flush)
        self.fresh = QCheckBox("--fresh-queries")
        session_layout.addRow("Fresh:", self.fresh)
        self.session_file = QLineEdit()
        session_browse = QPushButton("Browse")
        session_browse.setMaximumWidth(70)
        session_browse.clicked.connect(self.browse_session)
        session_row = QHBoxLayout()
        session_row.addWidget(self.session_file)
        session_row.addWidget(session_browse)
        session_layout.addRow("Session File:", session_row)
        self._layout.addWidget(session_group)

        output_group = QGroupBox("Output Configuration")
        output_layout = QFormLayout(output_group)
        self.verbose = QSpinBox()
        self.verbose.setRange(0, 6)
        self.verbose.setValue(1)
        output_layout.addRow("Verbosity (0-6):", self.verbose)
        self.output_dir = QLineEdit()
        output_browse = QPushButton("Browse")
        output_browse.setMaximumWidth(70)
        output_browse.clicked.connect(self.browse_output)
        output_row = QHBoxLayout()
        output_row.addWidget(self.output_dir)
        output_row.addWidget(output_browse)
        output_layout.addRow("Output Dir:", output_row)
        self.save_config_cb = QCheckBox("--save")
        output_layout.addRow("Save Config:", self.save_config_cb)
        self._layout.addWidget(output_group)

        perf_group = QGroupBox("Performance")
        perf_layout = QFormLayout(perf_group)
        self.keep_alive = QCheckBox("--keep-alive")
        perf_layout.addRow("Connection:", self.keep_alive)
        self.null_conn = QCheckBox("--null-connection")
        perf_layout.addRow("Null:", self.null_conn)
        self.text_only = QCheckBox("--text-only")
        perf_layout.addRow("Response:", self.text_only)
        self.titles = QCheckBox("--titles")
        perf_layout.addRow("Titles:", self.titles)
        self.str_input = QLineEdit()
        self.str_input.setPlaceholderText("Welcome")
        perf_layout.addRow("--string:", self.str_input)
        self.not_str = QLineEdit()
        self.not_str.setPlaceholderText("Error")
        perf_layout.addRow("--not-string:", self.not_str)
        self.code_input = QSpinBox()
        self.code_input.setRange(0, 999)
        self.code_input.setSpecialValueText("Any")
        perf_layout.addRow("--code:", self.code_input)
        self._layout.addWidget(perf_group)

    def browse_session(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Session File")
        if file:
            self.session_file.setText(file)

    def browse_output(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if directory:
            self.output_dir.setText(directory)

    def get_options(self):
        options = []
        if self.batch.isChecked(): options.append("--batch")
        if self.flush.isChecked(): options.append("--flush-session")
        if self.fresh.isChecked(): options.append("--fresh-queries")
        if self.session_file.text().strip():
            options.extend(["--session-file", self.session_file.text().strip()])
        if self.verbose.value() != 1:
            options.extend(["-v", str(self.verbose.value())])
        if self.output_dir.text().strip():
            options.extend(["--output-dir", self.output_dir.text().strip()])
        if self.save_config_cb.isChecked(): options.append("--save")
        if self.keep_alive.isChecked(): options.append("--keep-alive")
        if self.null_conn.isChecked(): options.append("--null-connection")
        if self.text_only.isChecked(): options.append("--text-only")
        if self.titles.isChecked(): options.append("--titles")
        if self.str_input.text().strip():
            options.extend(["--string", self.str_input.text().strip()])
        if self.not_str.text().strip():
            options.extend(["--not-string", self.not_str.text().strip()])
        if self.code_input.value() > 0:
            options.extend(["--code", str(self.code_input.value())])
        return options
