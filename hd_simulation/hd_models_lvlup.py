import json, os, math
from datetime import datetime
from dbconnection.data import SensorDataRepository
from dbconnection.services import SensorsDataServices
from dbconnection.models import SensorData
from dbconnection.configuration import Configuration


class Site:
    def __init__(self):
        self.site_id:str = None
        self.gateways:list = []
        self.siloses:list = []
        self.sensors:list = []


class Gateway:
    def __init__(self):
        self.gateway_id:str = None
        self.sensors:list = []
        self.out:list = []

    def get_data_from_sensors(self):
        while True:
            for sensor in self.sensors:
                self.out.append(sensor.output)


class Silos:
    def __init__(self,silos_id,d1,d2,d3,d4,d5,liq_density):
        """
        d1: raggio del silos \n
        d2: raggio minore rastremazione silos \n
        d3: altezza rastremazione silos \n
        d4: altezza parte cilindrica silos \n
        d5: altezza calotta sferica
        """
        self.silos_id = silos_id
        self._d1:float = d1
        self._d2:float = d2
        self._d3:float = d3
        self._d4:float = d4
        self._d5:float = d5

        self.content:float = 0.0
        self.max_content:float = sum([
            (((math.pi*((self._d1/2)**2)) + (math.pi*((self._d2/2)**2)) + math.sqrt((math.pi*((self._d1/2)**2)) * (math.pi*((self._d2/2)**2))))*self._d3)/3,
            (math.pi*((self._d1/2)**2))*self._d4,
            math.pi*self._d5*(((((self._d1/2)**2) + self._d5**2)/2*self._d5)-self._d5/3)
        ])
        self.liquid_density:float = 0.0
        self.silos_temperature:float = 0.0
    
    def update_content_level(self):
        pass
        

class Sensor:
    def __init__(self):
        self.sensor_id = None
        self.output:float = 4.0
        self.fondo_scala:float = 20.0
        self.assigned_silos = None

    def silos_listener(self):
        """
        silos: Instance of silos class
        """
        self.silos.content


class Gateway:
    def __init__(self):
        self.gateway_id:str = None
        self.sensors:list = []

    def get_data_from_sensors(self):
        while True:
            for sensor in self.sensors:
                self.out.append((sensor.sensor_id,sensor.output))

    def send_data_to_db(self,silos_id, silos_value):
        service = SensorsDataServices(SensorDataRepository(Configuration(),"SensorTemp"))
        data = SensorData()
        data.SilosCode = silos_id
        data.SilosDataTime = datetime.now()
        data.SilosValue = silos_value
        data.CodiciErrore = None
        service.insert(data)
    






        