import os, json


class Configuration:

    def __init__(self):
        self.conndict:dict = None
        path = os.path.join(os.getcwd(),"appconfig.json")
        with open(path) as file:
            self.conndict = json.loads(file.read())["ConnectionStrings"]