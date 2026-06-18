from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QCheckBox, QComboBox, QGroupBox
)

from .base_tab import BaseTab


class OSTab(BaseTab):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        subtitle = QLabel("Requires privileged database access")
        subtitle.setObjectName("subtitle")
        self._layout.addWidget(subtitle)

        shell_group = QGroupBox("Interactive Shell Access")
        shell_layout = QVBoxLayout(shell_group)
        self.os_shell = QCheckBox("--os-shell (Interactive OS Shell)")
        self.os_pwn = QCheckBox("--os-pwn (OOB Shell/Meterpreter/VNC)")
        shell_layout.addWidget(self.os_shell)
        shell_layout.addWidget(self.os_pwn)
        self._layout.addWidget(shell_group)

        file_group = QGroupBox("File System Operations")
        file_layout = QFormLayout(file_group)
        self.os_read = QLineEdit()
        self.os_read.setPlaceholderText("/etc/passwd")
        file_layout.addRow("--read-file:", self.os_read)
        self.os_write = QLineEdit()
        self.os_write.setPlaceholderText("/var/www/html/shell.php")
        file_layout.addRow("--write-file:", self.os_write)
        self.os_dest = QLineEdit()
        self.os_dest.setPlaceholderText("C:/windows/temp/file.txt")
        file_layout.addRow("--dest:", self.os_dest)
        self._layout.addWidget(file_group)

        reg_group = QGroupBox("Windows Registry")
        reg_layout = QFormLayout(reg_group)
        self.reg_read = QCheckBox("--reg-read")
        self.reg_add = QCheckBox("--reg-add")
        self.reg_del = QCheckBox("--reg-del")
        reg_row = QHBoxLayout()
        for cb in [self.reg_read, self.reg_add, self.reg_del]:
            reg_row.addWidget(cb)
        reg_row.addStretch()
        reg_layout.addRow("Operations:", reg_row)
        self.reg_key = QLineEdit()
        self.reg_key.setPlaceholderText(r"HKEY_LOCAL_MACHINE\SOFTWARE\...")
        reg_layout.addRow("Registry Key:", self.reg_key)
        self.reg_value = QLineEdit()
        reg_layout.addRow("Value:", self.reg_value)
        self.reg_data = QLineEdit()
        reg_layout.addRow("Data:", self.reg_data)
        self.reg_type = QComboBox()
        self.reg_type.addItems(["REG_SZ", "REG_DWORD", "REG_BINARY"])
        reg_layout.addRow("Type:", self.reg_type)
        self._layout.addWidget(reg_group)

    def get_options(self):
        options = []
        if self.os_shell.isChecked(): options.append("--os-shell")
        if self.os_pwn.isChecked(): options.append("--os-pwn")
        if self.os_read.text().strip():
            options.extend(["--read-file", self.os_read.text().strip()])
        if self.os_write.text().strip():
            options.extend(["--write-file", self.os_write.text().strip()])
        if self.os_dest.text().strip():
            options.extend(["--dest", self.os_dest.text().strip()])
        if self.reg_read.isChecked(): options.append("--reg-read")
        if self.reg_add.isChecked(): options.append("--reg-add")
        if self.reg_del.isChecked(): options.append("--reg-del")
        if self.reg_key.text().strip():
            options.extend(["--reg-key", self.reg_key.text().strip()])
        if self.reg_value.text().strip():
            options.extend(["--reg-value", self.reg_value.text().strip()])
        if self.reg_data.text().strip():
            options.extend(["--reg-data", self.reg_data.text().strip()])
        if self.reg_type.currentText():
            options.extend(["--reg-type", self.reg_type.currentText()])
        return options
