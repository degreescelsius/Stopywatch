import subprocess
import os
import sys

def install_packages(package):
    if os.name == 'nt':
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    else:
        subprocess.check_call([sys.executable, "-m", "pip3", "install", package, "--break-system-packages"])

required_packages = ["pyqt5"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"installing required package {package}...")
        install_packages(package)

from PyQt6 import uic
from PyQt6 import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
