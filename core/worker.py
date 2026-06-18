import subprocess

from PyQt6.QtCore import QThread, pyqtSignal


class SqlmapWorker(QThread):
    output_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(int, str)

    def __init__(self, command, cwd=None):
        super().__init__()
        self.command = command
        self.cwd = cwd
        self.process = None

    def run(self):
        try:
            self.process = subprocess.Popen(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=self.cwd,
                bufsize=1
            )
            for line in iter(self.process.stdout.readline, ''):
                if line:
                    self.output_signal.emit(line.rstrip())
            self.process.wait()
            self.finished_signal.emit(
                self.process.returncode,
                "Completed" if self.process.returncode == 0 else f"Exit code: {self.process.returncode}"
            )
        except Exception as e:
            self.finished_signal.emit(-1, str(e))

    def stop(self):
        if self.process:
            self.process.terminate()
