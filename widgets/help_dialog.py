from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QSplitter,
    QTreeWidget, QTreeWidgetItem, QTextBrowser,
    QLineEdit, QPushButton, QLabel, QWidget
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

from resources.help_content import HELP_DATA


ITEM_STYLE = """
<style>
body { color: #eaeaea; font-family: 'Segoe UI', sans-serif; font-size: 13px; padding: 10px 16px; }
h1 { color: #00d4aa; font-size: 22px; border-bottom: 1px solid #0f3460; padding-bottom: 8px; margin-bottom: 16px; }
h2 { color: #00d4aa; font-size: 17px; margin: 4px 0 12px 0; }
.opt { color: #ffd54f; font-size: 15px; font-weight: 700; font-family: 'Consolas', monospace; }
.meta { color: #888; font-size: 12px; margin-bottom: 12px; }
.desc { color: #ccc; font-size: 13px; line-height: 1.6; margin: 8px 0; }
.example { color: #81c784; font-family: 'Consolas', monospace; font-size: 12px; background: #16213e; padding: 8px 12px; border-radius: 4px; display: block; margin: 8px 0; border-left: 3px solid #00d4aa; }
.note { color: #ff8a65; font-size: 12px; margin: 4px 0; }
.hint { color: #4fc3f7; font-size: 12px; margin: 16px 0; text-align: center; }
</style>
"""


class SearchableTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderHidden(True)
        self.setIndentation(16)
        self._all_items = []

    def set_all_items(self, items):
        self._all_items = items

    def filter(self, text):
        lower = text.lower()
        has_results = False
        for item in self._all_items:
            if isinstance(item, QTreeWidgetItem):
                if item.parent():
                    title = item.text(0).lower()
                    matches = lower in title if lower else True
                    item.setHidden(not matches)
                    if matches:
                        item.parent().setHidden(False)
                        has_results = True
                else:
                    has_visible = False
                    for j in range(item.childCount()):
                        child = item.child(j)
                        child_title = child.text(0).lower()
                        child_matches = (lower in child_title) if lower else True
                        child.setHidden(not child_matches)
                        if child_matches:
                            has_visible = True
                    if lower and not has_visible:
                        item.setHidden(True)
                    else:
                        item.setHidden(False)
        return has_results


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("SQLMap Pro GUI — Help & Documentation")
        self.setMinimumSize(750, 500)
        self.resize(1000, 750)

        self._items_map = {}

        self.setup_ui()
        self.populate_tree()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        header = QWidget()
        header.setStyleSheet("background-color: #16213e; border-bottom: 1px solid #0f3460;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(12, 8, 12, 8)

        icon_label = QLabel("Help & Documentation")
        icon_label.setStyleSheet("color: #00d4aa; font-size: 15px; font-weight: 700;")
        header_layout.addWidget(icon_label)
        header_layout.addStretch()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search commands...")
        self.search_input.setClearButtonEnabled(True)
        self.search_input.setMaximumWidth(300)
        self.search_input.setMinimumHeight(30)
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a2e;
                border: 1px solid #0f3460;
                border-radius: 15px;
                padding: 5px 12px;
                color: #eaeaea;
            }
            QLineEdit:focus { border: 1px solid #00d4aa; }
        """)
        self.search_input.textChanged.connect(self.on_search)
        header_layout.addWidget(self.search_input)

        self.match_label = QLabel("")
        self.match_label.setStyleSheet("color: #888; font-size: 12px; padding: 0 8px;")
        header_layout.addWidget(self.match_label)

        layout.addWidget(header)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(1)

        self.tree = SearchableTree()
        self.tree.setMinimumWidth(200)
        self.tree.setStyleSheet("""
            QTreeWidget {
                background-color: #16213e;
                border: none;
                color: #eaeaea;
                font-size: 13px;
            }
            QTreeWidget::item {
                padding: 4px 8px;
                border-radius: 4px;
            }
            QTreeWidget::item:selected {
                background-color: #0f3460;
                color: #00d4aa;
            }
            QTreeWidget::item:hover:!selected {
                background-color: #0a1628;
            }
        """)
        self.tree.itemClicked.connect(self.on_item_clicked)
        splitter.addWidget(self.tree)

        self.browser = QTextBrowser()
        self.browser.setOpenExternalLinks(True)
        self.browser.setFrameShape(QTextBrowser.Shape.NoFrame)
        self.browser.setStyleSheet("""
            QTextBrowser {
                background-color: #1a1a2e;
                border: none;
                color: #eaeaea;
            }
        """)
        splitter.addWidget(self.browser)

        splitter.setSizes([280, 720])
        layout.addWidget(splitter, stretch=1)

        footer = QWidget()
        footer.setStyleSheet("background-color: #16213e; border-top: 1px solid #0f3460;")
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(12, 6, 12, 6)

        count = sum(len(cat["items"]) for cat in HELP_DATA)
        footer_label = QLabel(f"{len(HELP_DATA)} categories, {count} commands")
        footer_label.setStyleSheet("color: #888; font-size: 11px;")
        footer_layout.addWidget(footer_label)
        footer_layout.addStretch()

        close_btn = QPushButton("Close")
        close_btn.setFixedWidth(100)
        close_btn.clicked.connect(self.close)
        footer_layout.addWidget(close_btn)

        layout.addWidget(footer)

    def populate_tree(self):
        font = QFont("Consolas", 12)
        self.tree.clear()
        self._items_map.clear()
        all_items = []

        for category in HELP_DATA:
            top = QTreeWidgetItem([category["category"]])
            top.setExpanded(True)
            top_font = top.font(0)
            top_font.setBold(True)
            top.setFont(0, top_font)
            top.setForeground(0, Qt.GlobalColor.cyan)
            self.tree.addTopLevelItem(top)
            all_items.append(top)

            for item in category["items"]:
                child = QTreeWidgetItem([f"  {item['cmd']}  —  {item['title']}"])
                child.setFont(0, font)
                child.setForeground(0, Qt.GlobalColor.white)
                top.addChild(child)
                all_items.append(child)
                self._items_map[id(child)] = item

        self.tree.set_all_items(all_items)

    def on_search(self, text):
        self.tree.filter(text)
        visible = 0
        for item in self.tree._all_items:
            if isinstance(item, QTreeWidgetItem) and item.parent() and not item.isHidden():
                visible += 1
        if text:
            self.match_label.setText(f"{visible} matches" if visible else "No matches")
        else:
            self.match_label.setText("")

    def on_item_clicked(self, item, column):
        data = self._items_map.get(id(item))
        if not data:
            return

        html = ITEM_STYLE
        html += f"<h1>{data['cmd']}</h1>"
        html += f"<h2>{data['title']}</h2>"
        html += f"<div class='meta'>sqlmap command-line option</div>"
        html += f"<div class='desc'>{data['desc']}</div>"

        if data.get("example"):
            html += f"<div class='example'>{data['example']}</div>"

        self.browser.setHtml(html)
