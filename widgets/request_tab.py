from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QComboBox, QTextEdit,
    QCheckBox, QSpinBox, QGroupBox, QFileDialog
)

from .base_tab import BaseTab


class RequestTab(BaseTab):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        headers_group = QGroupBox("HTTP Headers")
        headers_layout = QFormLayout(headers_group)
        self.cookie_input = QLineEdit()
        self.cookie_input.setPlaceholderText("PHPSESSID=a8d127e...")
        headers_layout.addRow("Cookie:", self.cookie_input)
        self.ua_input = QLineEdit()
        self.ua_input.setPlaceholderText("Mozilla/5.0...")
        headers_layout.addRow("User-Agent:", self.ua_input)
        self.referer_input = QLineEdit()
        self.referer_input.setPlaceholderText("http://referer.com")
        headers_layout.addRow("Referer:", self.referer_input)
        self.host_input = QLineEdit()
        headers_layout.addRow("Host:", self.host_input)
        self.headers_input = QTextEdit()
        self.headers_input.setPlaceholderText("X-Custom-Header: value")
        self.headers_input.setMaximumHeight(60)
        headers_layout.addRow("Custom:", self.headers_input)
        self._layout.addWidget(headers_group)

        auth_group = QGroupBox("Authentication")
        auth_layout = QFormLayout(auth_group)
        self.auth_type = QComboBox()
        self.auth_type.addItems(["None", "Basic", "Digest", "NTLM", "Bearer"])
        auth_layout.addRow("Auth Type:", self.auth_type)
        self.auth_cred = QLineEdit()
        self.auth_cred.setPlaceholderText("user:pass")
        auth_layout.addRow("Credentials:", self.auth_cred)
        self.auth_file = QLineEdit()
        auth_file_btn = QPushButton("Browse")
        auth_file_btn.setMaximumWidth(70)
        auth_file_btn.clicked.connect(self.browse_auth_file)
        auth_file_row = QHBoxLayout()
        auth_file_row.addWidget(self.auth_file)
        auth_file_row.addWidget(auth_file_btn)
        auth_layout.addRow("Auth File:", auth_file_row)
        self._layout.addWidget(auth_group)

        network_group = QGroupBox("Network & Proxy")
        network_layout = QFormLayout(network_group)
        self.proxy_input = QLineEdit()
        self.proxy_input.setPlaceholderText("http://127.0.0.1:8080")
        network_layout.addRow("Proxy:", self.proxy_input)
        self.proxy_file = QLineEdit()
        proxy_file_btn = QPushButton("Browse")
        proxy_file_btn.setMaximumWidth(70)
        proxy_file_btn.clicked.connect(self.browse_proxy_file)
        proxy_file_row = QHBoxLayout()
        proxy_file_row.addWidget(self.proxy_file)
        proxy_file_row.addWidget(proxy_file_btn)
        network_layout.addRow("Proxy File:", proxy_file_row)
        self.tor_check = QCheckBox("Use Tor")
        self.check_tor = QCheckBox("Verify Tor")
        tor_row = QHBoxLayout()
        tor_row.addWidget(self.tor_check)
        tor_row.addWidget(self.check_tor)
        tor_row.addStretch()
        network_layout.addRow("Tor:", tor_row)
        self.delay_spin = QSpinBox()
        self.delay_spin.setRange(0, 60)
        self.delay_spin.setSuffix(" sec")
        network_layout.addRow("Delay:", self.delay_spin)
        self.timeout_spin = QSpinBox()
        self.timeout_spin.setRange(1, 300)
        self.timeout_spin.setValue(30)
        self.timeout_spin.setSuffix(" sec")
        network_layout.addRow("Timeout:", self.timeout_spin)
        self.retries_spin = QSpinBox()
        self.retries_spin.setRange(0, 10)
        self.retries_spin.setValue(3)
        network_layout.addRow("Retries:", self.retries_spin)
        self._layout.addWidget(network_group)

    def browse_auth_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Auth File")
        if file:
            self.auth_file.setText(file)

    def browse_proxy_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Proxy File")
        if file:
            self.proxy_file.setText(file)

    def get_options(self):
        options = []
        if self.cookie_input.text().strip():
            options.extend(["--cookie", self.cookie_input.text().strip()])
        if self.ua_input.text().strip():
            options.extend(["--user-agent", self.ua_input.text().strip()])
        else:
            options.append("--random-agent")
        if self.referer_input.text().strip():
            options.extend(["--referer", self.referer_input.text().strip()])
        if self.host_input.text().strip():
            options.extend(["--host", self.host_input.text().strip()])
        if self.headers_input.toPlainText().strip():
            for line in self.headers_input.toPlainText().strip().split('\n'):
                if line.strip():
                    options.extend(["--headers", line.strip()])
        if self.auth_type.currentText() != "None":
            options.extend(["--auth-type", self.auth_type.currentText().lower()])
        if self.auth_cred.text().strip():
            options.extend(["--auth-cred", self.auth_cred.text().strip()])
        if self.auth_file.text().strip():
            options.extend(["--auth-file", self.auth_file.text().strip()])
        if self.proxy_input.text().strip():
            options.extend(["--proxy", self.proxy_input.text().strip()])
        if self.proxy_file.text().strip():
            options.extend(["--proxy-file", self.proxy_file.text().strip()])
        if self.tor_check.isChecked():
            options.append("--tor")
        if self.check_tor.isChecked():
            options.append("--check-tor")
        if self.delay_spin.value() > 0:
            options.extend(["--delay", str(self.delay_spin.value())])
        if self.timeout_spin.value() != 30:
            options.extend(["--timeout", str(self.timeout_spin.value())])
        if self.retries_spin.value() != 3:
            options.extend(["--retries", str(self.retries_spin.value())])
        return options
