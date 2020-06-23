from datetime import datetime


class SensorData:
    def __init__(self):
        self.SilosCode:str = None
        self.SilosDataTime:datetime = None
        self.SilosValue:float = None
        self.ErrorCodes = None
