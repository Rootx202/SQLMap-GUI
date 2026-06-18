from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QLabel, QLineEdit, QSpinBox, QCheckBox, QGroupBox
)

from .base_tab import BaseTab


class EnumerationTab(BaseTab):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        quick_group = QGroupBox("Quick Actions")
        quick_layout = QGridLayout(quick_group)
        self.all_check = QCheckBox("--all")
        self.banner_check = QCheckBox("--banner")
        self.current_user = QCheckBox("--current-user")
        self.current_db = QCheckBox("--current-db")
        self.is_dba = QCheckBox("--is-dba")
        self.hostname = QCheckBox("--hostname")
        for i, cb in enumerate([self.all_check, self.banner_check, self.current_user,
                                self.current_db, self.is_dba, self.hostname]):
            quick_layout.addWidget(cb, i // 3, i % 3)
        self._layout.addWidget(quick_group)

        users_group = QGroupBox("Users & Passwords")
        users_layout = QGridLayout(users_group)
        self.users_check = QCheckBox("--users")
        self.passwords_check = QCheckBox("--passwords")
        self.privileges_check = QCheckBox("--privileges")
        self.roles_check = QCheckBox("--roles")
        for i, cb in enumerate([self.users_check, self.passwords_check, self.privileges_check, self.roles_check]):
            users_layout.addWidget(cb, i // 2, i % 2)
        self._layout.addWidget(users_group)

        structure_group = QGroupBox("Database Structure")
        structure_layout = QVBoxLayout(structure_group)
        struct_grid = QGridLayout()
        self.dbs_check = QCheckBox("--dbs")
        self.tables_check = QCheckBox("--tables")
        self.columns_check = QCheckBox("--columns")
        self.schema_check = QCheckBox("--schema")
        for i, cb in enumerate([self.dbs_check, self.tables_check, self.columns_check, self.schema_check]):
            struct_grid.addWidget(cb, i // 2, i % 2)
        structure_layout.addLayout(struct_grid)
        specific = QFormLayout()
        self.db_input = QLineEdit()
        self.db_input.setPlaceholderText("database_name")
        specific.addRow("-D:", self.db_input)
        self.table_input = QLineEdit()
        self.table_input.setPlaceholderText("table_name")
        specific.addRow("-T:", self.table_input)
        self.column_input = QLineEdit()
        self.column_input.setPlaceholderText("col1,col2,col3")
        specific.addRow("-C:", self.column_input)
        structure_layout.addLayout(specific)
        self._layout.addWidget(structure_group)

        dump_group = QGroupBox("Data Dumping")
        dump_layout = QVBoxLayout(dump_group)
        dump_row = QHBoxLayout()
        self.dump_check = QCheckBox("--dump")
        self.dump_all = QCheckBox("--dump-all")
        self.search_check = QCheckBox("--search")
        for cb in [self.dump_check, self.dump_all, self.search_check]:
            dump_row.addWidget(cb)
        dump_row.addStretch()
        dump_layout.addLayout(dump_row)
        range_row = QHBoxLayout()
        self.start_row = QSpinBox()
        self.start_row.setRange(0, 999999)
        self.start_row.setSpecialValueText("Start")
        self.stop_row = QSpinBox()
        self.stop_row.setRange(0, 999999)
        self.stop_row.setSpecialValueText("Stop")
        range_row.addWidget(QLabel("Start:"))
        range_row.addWidget(self.start_row)
        range_row.addWidget(QLabel("Stop:"))
        range_row.addWidget(self.stop_row)
        range_row.addStretch()
        dump_layout.addLayout(range_row)
        self._layout.addWidget(dump_group)

        fmt_group = QGroupBox("Output Format")
        fmt_layout = QHBoxLayout(fmt_group)
        self.csv_check = QCheckBox("CSV")
        self.json_check = QCheckBox("JSON")
        fmt_check = QCheckBox("XML")
        self.xml_check = fmt_check
        for cb in [self.csv_check, self.json_check, fmt_check]:
            fmt_layout.addWidget(cb)
        fmt_layout.addStretch()
        self._layout.addWidget(fmt_group)

    def get_options(self):
        options = []
        if self.all_check.isChecked(): options.append("--all")
        if self.banner_check.isChecked(): options.append("--banner")
        if self.current_user.isChecked(): options.append("--current-user")
        if self.current_db.isChecked(): options.append("--current-db")
        if self.is_dba.isChecked(): options.append("--is-dba")
        if self.hostname.isChecked(): options.append("--hostname")
        if self.users_check.isChecked(): options.append("--users")
        if self.passwords_check.isChecked(): options.append("--passwords")
        if self.privileges_check.isChecked(): options.append("--privileges")
        if self.roles_check.isChecked(): options.append("--roles")
        if self.dbs_check.isChecked(): options.append("--dbs")
        if self.tables_check.isChecked(): options.append("--tables")
        if self.columns_check.isChecked(): options.append("--columns")
        if self.schema_check.isChecked(): options.append("--schema")
        if self.db_input.text().strip():
            options.extend(["-D", self.db_input.text().strip()])
        if self.table_input.text().strip():
            options.extend(["-T", self.table_input.text().strip()])
        if self.column_input.text().strip():
            options.extend(["-C", self.column_input.text().strip()])
        if self.dump_check.isChecked(): options.append("--dump")
        if self.dump_all.isChecked(): options.append("--dump-all")
        if self.search_check.isChecked(): options.append("--search")
        if self.start_row.value() > 0:
            options.extend(["--start", str(self.start_row.value())])
        if self.stop_row.value() > 0:
            options.extend(["--stop", str(self.stop_row.value())])
        if self.csv_check.isChecked(): options.append("--csv-del=,")
        if self.json_check.isChecked(): options.append("--json")
        if self.xml_check.isChecked(): options.append("--xml")
        return options
