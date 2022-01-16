import os
import subprocess as sp
import time

import psutil
from directory import Directory

class Operations(object):
    def __init__(self) -> None:
        super().__init__()
        self.app_dir = Directory().get_app_paths()
        
    
    def open_app(self, app_name:str) -> None:
        """
        Opens an application based on given app name
        """
        for i in range(len(self.app_dir)):
            if app_name in self.app_dir[i]:
                sp.call(self.app_dir[i][app_name])
                break
        else:
            print(f"{app_name} not found")
    

    def close_app(self, app_name:str) -> None:
        """
        Closes an application based on given app name
        """
        try:
            for process in (process for process in psutil.process_iter() if process.name()==app_name):
                process.kill()
        except:
            print(f"{app_name} process not open")

