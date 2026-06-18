from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QComboBox, QTextEdit, QGroupBox
)

from .base_tab import BaseTab


class TargetTab(BaseTab):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        url_group = QGroupBox("Target URL")
        url_layout = QVBoxLayout(url_group)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("http://www.site.com/vuln.php?id=1")
        url_layout.addWidget(self.url_input)

        presets_layout = QHBoxLayout()
        for preset in ["GET", "POST", "JSON", "XML"]:
            btn = QPushButton(preset)
            btn.setMaximumWidth(70)
            btn.clicked.connect(lambda checked, p=preset: self.apply_preset(p))
            presets_layout.addWidget(btn)
        presets_layout.addStretch()
        url_layout.addLayout(presets_layout)

        self._layout.addWidget(url_group)

        dork_group = QGroupBox("Google Dork")
        dork_layout = QVBoxLayout(dork_group)
        self.dork_input = QLineEdit()
        self.dork_input.setPlaceholderText("inurl:admin.php?id=")
        dork_layout.addWidget(self.dork_input)
        self._layout.addWidget(dork_group)

        method_group = QGroupBox("HTTP Method")
        method_layout = QHBoxLayout(method_group)
        self.method_combo = QComboBox()
        self.method_combo.addItems(["GET", "POST", "PUT", "DELETE", "PATCH"])
        method_layout.addWidget(self.method_combo)
        method_layout.addStretch()
        self._layout.addWidget(method_group)

        data_group = QGroupBox("POST Data")
        data_layout = QVBoxLayout(data_group)
        self.data_input = QTextEdit()
        self.data_input.setPlaceholderText("id=1&name=test")
        self.data_input.setMaximumHeight(60)
        data_layout.addWidget(self.data_input)
        self._layout.addWidget(data_group)

        adv_group = QGroupBox("Advanced Options")
        adv_layout = QFormLayout(adv_group)
        self.param_input = QLineEdit()
        self.param_input.setPlaceholderText("id,name,search")
        adv_layout.addRow("-p:", self.param_input)
        self.skip_input = QLineEdit()
        self.skip_input.setPlaceholderText("token,csrf")
        adv_layout.addRow("--skip:", self.skip_input)
        self.prefix_input = QLineEdit()
        self.prefix_input.setPlaceholderText("')")
        adv_layout.addRow("Prefix:", self.prefix_input)
        self.suffix_input = QLineEdit()
        self.suffix_input.setPlaceholderText("--")
        adv_layout.addRow("Suffix:", self.suffix_input)
        self._layout.addWidget(adv_group)

    def apply_preset(self, preset):
        if preset == "GET":
            self.method_combo.setCurrentText("GET")
            self.data_input.clear()
        elif preset == "POST":
            self.method_combo.setCurrentText("POST")
            self.data_input.setText("id=1")
        elif preset == "JSON":
            self.method_combo.setCurrentText("POST")
            self.data_input.setText('{"id": 1}')
        elif preset == "XML":
            self.method_combo.setCurrentText("POST")
            self.data_input.setText("<id>1</id>")

    def get_options(self):
        options = []
        if self.url_input.text().strip():
            options.extend(["-u", self.url_input.text().strip()])
        elif self.dork_input.text().strip():
            options.extend(["-g", self.dork_input.text().strip()])
        if self.method_combo.currentText() != "GET":
            options.extend(["--method", self.method_combo.currentText()])
        if self.data_input.toPlainText().strip():
            options.extend(["--data", self.data_input.toPlainText().strip()])
        if self.param_input.text().strip():
            options.extend(["-p", self.param_input.text().strip()])
        if self.skip_input.text().strip():
            options.extend(["--skip", self.skip_input.text().strip()])
        if self.prefix_input.text().strip():
            options.extend(["--prefix", self.prefix_input.text().strip()])
        if self.suffix_input.text().strip():
            options.extend(["--suffix", self.suffix_input.text().strip()])
        return options
