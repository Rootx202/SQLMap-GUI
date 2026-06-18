DARK = """
QMainWindow {
    background-color: #1a1a2e;
}
QWidget {
    background-color: #1a1a2e;
    color: #eaeaea;
    font-family: 'Segoe UI', 'SF Pro Display', sans-serif;
    font-size: 13px;
}
QGroupBox {
    border: 1px solid #16213e;
    border-radius: 8px;
    margin-top: 12px;
    padding-top: 10px;
    font-weight: 600;
    color: #00d4aa;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 8px;
}
QLineEdit, QComboBox, QSpinBox, QTextEdit, QPlainTextEdit {
    background-color: #16213e;
    border: 1px solid #0f3460;
    border-radius: 6px;
    padding: 8px;
    color: #eaeaea;
    selection-background-color: #00d4aa;
}
QLineEdit:focus, QComboBox:focus, QTextEdit:focus {
    border: 1px solid #00d4aa;
}
QPushButton {
    background-color: #0f3460;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    color: white;
    font-weight: 600;
}
QPushButton:hover {
    background-color: #00d4aa;
    color: #1a1a2e;
}
QPushButton:pressed {
    background-color: #00b894;
}
QPushButton:disabled {
    background-color: #333;
    color: #666;
}
QTabWidget::pane {
    border: 1px solid #16213e;
    border-radius: 8px;
    background-color: #16213e;
}
QTabBar::tab {
    background-color: #1a1a2e;
    border: 1px solid #16213e;
    border-bottom: none;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    padding: 10px 20px;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background-color: #16213e;
    border-bottom: 2px solid #00d4aa;
    color: #00d4aa;
}
QTabBar::tab:hover:!selected {
    background-color: #0f3460;
}
QProgressBar {
    border: 1px solid #0f3460;
    border-radius: 4px;
    text-align: center;
    color: white;
}
QProgressBar::chunk {
    background-color: #00d4aa;
    border-radius: 4px;
}
QCheckBox {
    spacing: 8px;
}
QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border-radius: 4px;
    border: 1px solid #0f3460;
}
QCheckBox::indicator:checked {
    background-color: #00d4aa;
    border: 1px solid #00d4aa;
}
QMenuBar {
    background-color: #1a1a2e;
    border-bottom: 1px solid #16213e;
}
QMenuBar::item:selected {
    background-color: #0f3460;
}
QMenu {
    background-color: #16213e;
    border: 1px solid #0f3460;
}
QMenu::item:selected {
    background-color: #00d4aa;
    color: #1a1a2e;
}
QStatusBar {
    background-color: #16213e;
    border-top: 1px solid #0f3460;
}
QScrollBar:vertical {
    background-color: #1a1a2e;
    width: 12px;
    border-radius: 6px;
}
QScrollBar::handle:vertical {
    background-color: #0f3460;
    border-radius: 6px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover {
    background-color: #00d4aa;
}
QLabel#title {
    font-size: 24px;
    font-weight: 700;
    color: #00d4aa;
}
QLabel#subtitle {
    font-size: 14px;
    color: #888;
}
"""
