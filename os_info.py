import platform
import sys
import datetime

class OSInfo:
    def __init__(self):
        # Initialisiere die Attribute mit Systeminformationen
        self.platform_info = platform.platform()
        self.python_version = sys.version
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_platform_info(self):
        # Gibt die Plattforminformationen zurück
        return self.platform_info

    def get_python_version(self):
        # Gibt die Python-Version zurück
        return self.python_version

    def get_platform_machine(self):
        # Gibt die Maschinenarchitektur zurück
        return platform.machine()

    def get_timestamp(self):
        # Gibt den aktuellen Zeitstempel zurück
        return self.timestamp
