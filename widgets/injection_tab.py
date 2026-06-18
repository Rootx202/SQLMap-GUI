from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QLineEdit, QComboBox, QSpinBox, QCheckBox,
    QListWidget, QGroupBox
)

from .base_tab import BaseTab


class InjectionTab(BaseTab):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        dbms_group = QGroupBox("Database Management System")
        dbms_layout = QVBoxLayout(dbms_group)
        self.dbms_combo = QComboBox()
        self.dbms_combo.addItems([
            "Auto-detect", "MySQL", "Oracle", "PostgreSQL",
            "Microsoft SQL Server", "SQLite", "IBM DB2",
            "Firebird", "Sybase", "SAP MaxDB", "HSQLDB",
            "H2", "Informix", "MariaDB", "MemSQL",
            "MonetDB", "CrateDB", "Presto", "Altibase",
            "Mckoi", "FrontBase", "Virtuoso", "Amazon Redshift"
        ])
        dbms_layout.addWidget(self.dbms_combo)
        self._layout.addWidget(dbms_group)

        detect_group = QGroupBox("Detection Settings")
        detect_layout = QFormLayout(detect_group)
        self.level_spin = QSpinBox()
        self.level_spin.setRange(1, 5)
        self.level_spin.setValue(1)
        detect_layout.addRow("Level (1-5):", self.level_spin)
        self.risk_spin = QSpinBox()
        self.risk_spin.setRange(1, 3)
        self.risk_spin.setValue(1)
        detect_layout.addRow("Risk (1-3):", self.risk_spin)
        self.threads_spin = QSpinBox()
        self.threads_spin.setRange(1, 10)
        self.threads_spin.setValue(1)
        detect_layout.addRow("Threads:", self.threads_spin)
        self._layout.addWidget(detect_group)

        tech_group = QGroupBox("SQL Injection Techniques")
        tech_layout = QVBoxLayout(tech_group)
        self.tech_all = QCheckBox("All Techniques")
        self.tech_all.setChecked(True)
        tech_layout.addWidget(self.tech_all)
        tech_grid = QGridLayout()
        self.tech_b = QCheckBox("B - Boolean")
        self.tech_e = QCheckBox("E - Error")
        self.tech_u = QCheckBox("U - UNION")
        self.tech_s = QCheckBox("S - Stacked")
        self.tech_t = QCheckBox("T - Time")
        self.tech_q = QCheckBox("Q - Inline")
        for i, tech in enumerate([self.tech_b, self.tech_e, self.tech_u, self.tech_s, self.tech_t, self.tech_q]):
            tech_grid.addWidget(tech, i // 3, i % 3)
            tech.setEnabled(False)
        tech_layout.addLayout(tech_grid)
        self.tech_all.stateChanged.connect(self.toggle_techniques)
        self._layout.addWidget(tech_group)

        tamper_group = QGroupBox("Tamper Scripts")
        tamper_layout = QVBoxLayout(tamper_group)
        self.tamper_list = QListWidget()
        self.tamper_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.tamper_list.addItems([
            "apostrophemask", "apostrophenullencode", "appendnullbyte",
            "base64encode", "between", "bluecoat", "chardoubleencode",
            "charencode", "charunicodeencode", "concat2concatws",
            "equaltolike", "escapequotes", "greatest", "halfversionedmorekeywords",
            "ifnull2ifisnull", "modsecurityversioned", "modsecurityzeroversioned",
            "multiplespaces", "nonrecursivereplacement", "percentage",
            "randomcase", "randomcomments", "securesphere", "space2comment",
            "space2dash", "space2hash", "space2morehash", "space2mssqlblank",
            "space2mssqlhash", "space2mysqlblank", "space2mysqldash",
            "space2plus", "space2randomblank", "sp_password", "unionalltounion",
            "unmagicquotes", "varnish", "versionedkeywords", "versionedmorekeywords",
            "xforwardedfor"
        ])
        tamper_layout.addWidget(self.tamper_list)
        self._layout.addWidget(tamper_group)

        adv_group = QGroupBox("Advanced Options")
        adv_layout = QFormLayout(adv_group)
        self.os_input = QLineEdit()
        self.os_input.setPlaceholderText("Linux / Windows")
        adv_layout.addRow("OS:", self.os_input)
        self.invalid_input = QLineEdit()
        self.invalid_input.setPlaceholderText("9999")
        adv_layout.addRow("Bignum:", self.invalid_input)
        self.no_cast = QCheckBox("No Cast")
        self.no_escape = QCheckBox("No Escape")
        self.hex_convert = QCheckBox("Hex Convert")
        checks = QHBoxLayout()
        checks.addWidget(self.no_cast)
        checks.addWidget(self.no_escape)
        checks.addWidget(self.hex_convert)
        checks.addStretch()
        adv_layout.addRow("Options:", checks)
        self._layout.addWidget(adv_group)

    def toggle_techniques(self, state):
        enabled = not self.tech_all.isChecked()
        for tech in [self.tech_b, self.tech_e, self.tech_u, self.tech_s, self.tech_t, self.tech_q]:
            tech.setEnabled(enabled)

    def get_options(self):
        options = []
        if self.dbms_combo.currentText() != "Auto-detect":
            options.extend(["--dbms", self.dbms_combo.currentText()])
        if self.level_spin.value() != 1:
            options.extend(["--level", str(self.level_spin.value())])
        if self.risk_spin.value() != 1:
            options.extend(["--risk", str(self.risk_spin.value())])
        if self.threads_spin.value() > 1:
            options.extend(["--threads", str(self.threads_spin.value())])
        if not self.tech_all.isChecked():
            techs = ""
            if self.tech_b.isChecked(): techs += "B"
            if self.tech_e.isChecked(): techs += "E"
            if self.tech_u.isChecked(): techs += "U"
            if self.tech_s.isChecked(): techs += "S"
            if self.tech_t.isChecked(): techs += "T"
            if self.tech_q.isChecked(): techs += "Q"
            if techs:
                options.extend(["--technique", techs])
        selected = [self.tamper_list.item(i).text()
                   for i in range(self.tamper_list.count())
                   if self.tamper_list.item(i).isSelected()]
        if selected:
            options.extend(["--tamper", ",".join(selected)])
        if self.os_input.text().strip():
            options.extend(["--os", self.os_input.text().strip()])
        if self.invalid_input.text().strip():
            options.extend(["--invalid-bignum", self.invalid_input.text().strip()])
        if self.no_cast.isChecked():
            options.append("--no-cast")
        if self.no_escape.isChecked():
            options.append("--no-escape")
        if self.hex_convert.isChecked():
            options.append("--hex")
        return options
