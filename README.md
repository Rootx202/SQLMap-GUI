# SQLMap Pro GUI

**Developer:** RootX  
**Telegram:** [@rootx.202](https://t.me/rootx.202)  
**GitHub:** [Rootx202/SQLMap-GUI](https://github.com/Rootx202/SQLMap-GUI)

A professional PyQt6 graphical interface for [sqlmap](https://sqlmap.org) — the popular open-source SQL injection detection and exploitation tool.

---

## Features

- **6 organized tabs**: Target, Request, Injection, Enumeration, OS Access, General
- **Full sqlmap option support** — every command-line argument exposed via GUI
- **Live command preview** — see the generated sqlmap command before running
- **Real-time output** — view scan results as they come in
- **Responsive layout** — adapts to any screen size
- **Built-in help** — searchable documentation for every option
- **Dark theme** — modern dark UI design

## Requirements

- Python 3.10+
- PyQt6
- sqlmap (installed and available in PATH)

## Installation

```bash
# Clone the repository
git clone https://github.com/Rootx202/SQLMap-GUI.git
cd SQLMap-GUI

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install PyQt6

# Run the application
python3 main.py
```

## Usage

1. Enter your target URL in the **Target** tab
2. Configure request headers, authentication, and proxy settings in the **Request** tab
3. Set injection parameters (DBMS, level, risk, techniques, tamper scripts) in the **Injection** tab
4. Choose what data to extract in the **Enumeration** tab
5. Enable OS-level features in the **OS Access** tab
6. Adjust general settings (batch mode, verbosity, performance) in the **General** tab
7. Click **Generate Command** to preview the full sqlmap command
8. Click **Run sqlmap** to execute

## Project Structure

```
SQLMap-GUI/
├── main.py                  # Entry point
├── main_window.py           # Main application window
├── core/
│   └── worker.py            # Background sqlmap worker thread
├── resources/
│   ├── style.py             # Dark theme stylesheet
│   └── help_content.py      # Help documentation data
└── widgets/
    ├── base_tab.py          # Base tab with scroll support
    ├── target_tab.py        # Target configuration
    ├── request_tab.py       # HTTP request configuration
    ├── injection_tab.py     # Injection configuration
    ├── enumeration_tab.py   # Enumeration & data extraction
    ├── os_tab.py            # OS access configuration
    ├── general_tab.py       # General options
    ├── command_preview.py   # Command preview & execution
    ├── output_panel.py      # Output display panel
    └── help_dialog.py       # Searchable help dialog
```

## License

For authorized security testing only. Use responsibly.
