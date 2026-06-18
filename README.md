<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=white" alt="PyQt6">
  <img src="https://img.shields.io/badge/sqlmap-FF6600?style=for-the-badge&logo=sqlite&logoColor=white" alt="sqlmap">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Version-2.0-00d4aa?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/PyPI-3775A9?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI">
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=SQLMap%20Pro%20GUI&fontSize=60&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Professional%20PyQt6%20Interface%20for%20sqlmap&descAlignY=55&descSize=18">
</p>

---

<p align="center">
  <b>Developer:</b> <a href="https://t.me/rootx.202">RootX</a> &nbsp;|&nbsp;
  <b>Telegram:</b> <a href="https://t.me/rootx.202">@rootx.202</a> &nbsp;|&nbsp;
  <b>GitHub:</b> <a href="https://github.com/Rootx202/SQLMap-GUI">Rootx202/SQLMap-GUI</a>
</p>

---

A professional, feature-rich graphical user interface built with **PyQt6** for [sqlmap](https://sqlmap.org) — the world's most popular open-source SQL injection detection and exploitation tool. Designed for penetration testers and security researchers who prefer a visual workflow over command-line operations.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **6 Organized Tabs** | Target, Request, Injection, Enumeration, OS Access, General |
| ⚡ **Full sqlmap Support** | Every command-line argument exposed through an intuitive GUI |
| 📝 **Live Command Preview** | See the generated sqlmap command in real-time before execution |
| 📊 **Real-time Output** | View scan results as they stream in from the background process |
| 📱 **Responsive Layout** | Adapts perfectly to any screen size — from laptops to ultrawide monitors |
| 📚 **Built-in Help** | Searchable, comprehensive documentation for every option |
| 🌙 **Dark Theme** | Modern, eye-friendly dark UI with teal accents |
| 🔍 **Smart Search** | Find any command instantly in the help dialog |
| 🧩 **Modular Architecture** | Clean, maintainable codebase split into logical modules |
| 🚀 **One-click Execution** | Generate, preview, and run sqlmap commands with a single click |

---

## 📋 Requirements

| Dependency | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.10+ | Runtime environment |
| **PyQt6** | Latest | GUI framework |
| **sqlmap** | Latest | SQL injection engine (must be in PATH) |

---

## 🚀 Installation

### Quick Install (via PyPI)

```bash
pip install sqlmap-pro-gui
sqlmap-gui
```

### Manual Install (from source)

```bash
# 1. Clone the repository
git clone https://github.com/Rootx202/SQLMap-GUI.git
cd SQLMap-GUI

# 2. Create virtual environment (recommended)
python3 -m venv venv

# 3. Activate the environment
source venv/bin/activate      # Linux / macOS
# or: venv\Scripts\activate   # Windows

# 4. Install the package
pip install .

# 5. Run the application
sqlmap-gui
```

> **Note:** Ensure `sqlmap` is installed and accessible from your terminal before running the GUI (`apt install sqlmap` on Debian/Kali or download from [sqlmap.org](https://sqlmap.org)).

---

## 🎮 Usage Guide

### Quick Start

| Step | Action | Tab |
|:----:|--------|:----:|
| 1 | Enter your target URL (e.g., `http://site.com/page.php?id=1`) | **Target** |
| 2 | Add cookies, headers, or proxy if needed | **Request** |
| 3 | Configure detection level, risk, and techniques | **Injection** |
| 4 | Choose what data to extract (banner, dbs, tables, etc.) | **Enumeration** |
| 5 | Enable OS shell or file operations if desired | **OS Access** |
| 6 | Set batch mode or verbosity level | **General** |
| 7 | Click **Generate Command** to preview | — |
| 8 | Click **Run sqlmap** to start the scan | — |

### Tips

- 💡 Use **Generate Command** first to verify your configuration before running
- 🔍 Press `Ctrl+F` in the **Help** dialog to search for any command
- ⚠️ Higher `--level` and `--risk` values mean more thorough (but slower) scans
- 🛡️ Enable **Tamper Scripts** in the Injection tab to bypass WAF/IDS filters

---

## 📁 Project Structure

```
SQLMap-GUI/
│
├── main.py                      # Application entry point
├── main_window.py               # Main window with tabs, toolbar, menus
│
├── core/
│   └── worker.py                # Background QThread for sqlmap execution
│
├── resources/
│   ├── style.py                 # Dark theme QSS stylesheet
│   └── help_content.py          # Structured help documentation data
│
├── widgets/
│   ├── base_tab.py              # Base scrollable tab widget
│   ├── target_tab.py            # Target configuration (URL, dork, method)
│   ├── request_tab.py           # HTTP request headers & authentication
│   ├── injection_tab.py         # DBMS, techniques, tamper scripts
│   ├── enumeration_tab.py       # Data extraction options
│   ├── os_tab.py                # OS shell & file system access
│   ├── general_tab.py           # Session, output & performance settings
│   ├── command_preview.py       # Command preview & execution controls
│   ├── output_panel.py          # Scan output display panel
│   └── help_dialog.py           # Searchable help & documentation dialog
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🖼️ Screenshots

> *Coming soon — screenshots will be added in a future update.*

---

## 🛠️ Architecture

The application follows a clean **modular architecture**:

- **`core/`** — Business logic layer (worker thread for non-blocking sqlmap execution)
- **`resources/`** — Static assets (stylesheets, documentation data)
- **`widgets/`** — UI components (each tab and panel is an independent, reusable widget)
- **`main_window.py`** — Orchestrator that wires everything together (tabs, toolbar, menus, splitter)

All tab widgets inherit from `BaseTab`, which provides automatic scroll functionality for small screens, ensuring a consistent and responsive experience across all tabs.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find any issues:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

This tool is intended for **authorized security testing and educational purposes only**. The developer assumes no responsibility for any misuse or damage caused by this program. Always ensure you have explicit permission before testing any system.

---

<p align="center">
  <b>Developed with ❤️ by <a href="https://t.me/rootx.202">RootX</a></b><br>
  <sub>For authorized security testing only. Use responsibly.</sub>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer">
</p>
