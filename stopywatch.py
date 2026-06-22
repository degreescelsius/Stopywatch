required_packages = ["pyqt5"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"installing required package {package}...")
        install_packages(package)

from PyQt5 import uic
from PyQ
