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
        # TODO: Add support for subdirectories (i.e. apps in /Applications/Utilities)
        dir = "/Applications/"

        for path in os.listdir(dir):
            if path.startswith("."):
                continue
            # #print(path)
            # if path[-4:] != ".app":
            #     for sub_path in os.listdir(dir + path):
            #         if sub_path.startswith("."):
            #             continue
            #         if sub_path[-4:] == ".app":
            #             self.add_app_path(self.parse_app_name(sub_path), COMMAND + [dir + path + "/" + sub_path])
            # else:
            full_path = os.path.join(dir, path)

            self.add_app_path(self.parse_app_name(path), COMMAND + [full_path])
        print(self.app_paths)

    
    def get_app_paths(self) -> list:
        """
        Returns all app paths
        """
        return self.app_paths


# TESTING PURPOSES
for app in Directory().get_app_paths():
    print(app)
print(len(Directory().get_app_paths()))
#Directory()