#TODO: Create function to return all app paths into dictionary structure
import os

COMMAND = ["/usr/bin/open", "-n", "-a"]

class Directory(object):
    def __init__(self) -> None:
        super().__init__()
        self.app_paths = []
        self.initialize()

  
    
    def parse_app_name(self, app_name:str) -> str:
        """
        Parses app name to .app from end of string
        """
        return app_name[:-4]
        
    def add_app_path(self, app_name:str, app_path:list) -> None:
        """
        Adds app path to dictionary
        """
        self.app_paths.append({app_name: app_path})
    
    def initialize(self) -> None:
        dir = "/Applications/"
        for path in os.listdir(dir):
            full_path = os.path.join(dir, path)
            temp = COMMAND + [full_path]
            self.add_app_path(self.parse_app_name(path), temp)
        #print(self.app_paths)

    
    def get_app_paths(self) -> list:
        """
        Returns all app paths
        """
        return self.app_paths


# TESTING PURPOSES
#print(Directory().get_app_paths())