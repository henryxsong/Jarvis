import os
import subprocess as sp
from directory import app_paths

class Operations(object):
    def __init__(self) -> None:
        super().__init__()
    
    @staticmethod
    def open_app(app_name:str) -> None:
        """
        Opens an application based on given app name
        """
        for app in app_paths:
            if app_name in app:
                os.startfile(app_paths[app])
                break
        else:
            print(f"{app_name} not found")

if __name__ == "__main__":
    Operations.open_app("Discord")
