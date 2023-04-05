import platform
import configparser
from time import strftime
import os
from pathlib import Path
import sys

class Preprocessor:
    def __init__(self):
        if(sys.argv[0] == "__main__.py"):
            self.data_path = os.path.abspath(os.path.join(os.getcwd(),r'Data'))
        else:
            self.data_path = os.path.abspath(os.path.join(os.getcwd(),sys.argv[0],r'Data'))
        print(self.data_path)
        return

    # def setFileLoc(self,)