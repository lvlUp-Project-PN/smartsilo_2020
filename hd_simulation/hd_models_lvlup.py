import json, os, math, time, random, json
from datetime import datetime
from requests import post
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
        self._output_params:dict = dict()

    def get_data_from_sensors(self):
        for sensor in self.sensors:
            level = self._convert_into_quantity(sensor,sensor.assigned_silos)
            self.send_data_to_db(
                sensor.assigned_silos.silos_id,
                level
            )

    def _convert_into_quantity(self, sensor, silos):
        if silos.iscylindrical:
            pressure = ((sensor.output-sensor._min_output)/(sensor._full_scale-sensor._min_output))*sensor._max_pressure
            height = (pressure*100000)/(silos.p1*9.80665)
            return ((math.pi * pow((silos._d1/2.0),2.0))*height)*1000
        else:
            return

    def send_data_to_db(self,silos_id, silos_value):
        service = SensorsDataServices(SensorDataRepository(Configuration(),"SensorTemp"))
        data = SensorData()
        data.SilosCode = silos_id
        data.SilosDataTime = datetime.now()
        data.SilosValue = silos_value
        #post(url='http://52.49.107.35/post/SilosDataIrt/', json=json.dumps(data))
        service.insert(data)
        print(f'value inserted: {silos_id} {data.SilosDataTime} {data.SilosValue}')


class Silos:
    def __init__(self,silos_id,d1,d2,d3,d4,d5,liq_density,flow_per_sec):
        """
        d1: raggio del silos \n
        d2: raggio minore rastremazione silos \n
        d3: altezza rastremazione silos \n
        d4: altezza parte cilindrica silos \n
        d5: altezza calotta sferica \n
        p1: liquid_density \n
        p2: portata riempimento/svuotamento
        """
        self.silos_id = silos_id
        self._d1:float = d1
        self._d2:float = d2
        self._d3:float = d3
        self._d4:float = d4
        self._d5:float = d5
        self.iscylindrical = False
        self._is_in_loading = False
    
        self.p1:float = liq_density
        self._p2:float = flow_per_sec
        self._max_content:float
        
        def cal_max_content():
            if self._d1 == self._d2:
                self._max_content = sum([
                    (math.pi*((self._d1/2)**2))*(self._d3 + self._d4),
                    math.pi*pow(self._d5,2.0)*(((((self._d1/2)**2) + self._d5**2)/(2*self._d5))-(self._d5/3))
                ])
                self.iscylindrical = True
            else:
                lower_sect = (((math.pi*((self._d1/2)**2)) + (math.pi*((self._d2/2)**2)) + 
                math.sqrt((math.pi*((self._d1/2)**2)) * (math.pi*((self._d2/2)**2))))*self._d3)/3
                self._max_content = sum([
                    lower_sect,
                    (math.pi*((self._d1/2)**2))*self._d4,
                    math.pi*pow(self._d5,2.0)*(((((self._d1/2)**2) + self._d5**2)/(2*self._d5))-(self._d5/3))
                ])

        cal_max_content()
        self.content:float = [0.0,self._max_content][random.randint(0,1)]
        self._counter:int = random.randint(4,int(self._max_content/self._p2))
        self._stop_counter = random.randint(0,10)
        self._action = random.randint(0,1)

    def run(self):
        if self._counter > 0:
            if self._action == 0:
                if self._stop_counter == 0:
                    self._action = 1
                    self._stop_counter = random.randint(0,10)
                else:
                    self._stop_counter -= 1
            else:
                if self.content > self._max_content:
                    self._is_in_loading = False
                    self.content -= self.content-self._max_content
                    self._counter -= 1 
                    return
                elif self.content > 0:
                    if self._is_in_loading:
                        self.content += self._p2/(math.pi*((self._d1/2)**2))
                        self._counter -= 1
                        return
                    else:
                        self.content -= self._p2/(math.pi*((self._d1/2)**2))
                        self._counter -= 1
                        return
                else:
                    self._is_in_loading = True
                    self._counter = int(self._max_content/self._p2)
                    self.content += self._p2/(math.pi*((self._d1/2)**2))
                    self._counter -= 1
                    return
        else:
            self._counter = random.randint(1,int(self._max_content/self._p2))
            self._action = 0
            self.run()

        
class Sensor:
    def __init__(self, sensor_id, min_output, full_scale, max_pressure, break_coeff, detected_temp):
        """
        min_output [mA] 
        full_scale [mA]
        max_pressure [bar]
        break_coeff [max_pressure * x]
        detected_temp [°C]
        """
        self.sensor_id = sensor_id
        self._min_output:float = min_output
        self._full_scale:float = full_scale
        self._max_pressure:float = max_pressure
        self._full_silos_pressure:float = 0.0
        self._break_coeff:int = break_coeff
        self._break_pressure:float = self._max_pressure * self._break_coeff
        self.detected_temp:float = detected_temp
        self.assigned_silos = None
        self._k_temp = 0.0
        self._counter = random.randint(1,10) 
        self.output:float = 4.0

        self._set_temp_k()

    def _set_temp_k(self):
        temp = self.detected_temp
        if temp > -10.0 and temp < 4:
            self._k_temp = 1.1
        elif temp > 4 and temp < 35:
            self._k_temp = 0.7
        elif temp > 35 and temp < 50:
            self._k_temp = 1.1
    
    def _set_full_silos_pressure(self):
        if self.assigned_silos.iscylindrical:
            height = self.assigned_silos._max_content/(math.pi*pow((self.assigned_silos._d1/2.0),2.0))
            self._full_silos_pressure = (self.assigned_silos.p1 * height * 9.80665)*0.00001
        else:
            pass

    def run(self):
        if self._full_silos_pressure == 0.0:
            self._set_full_silos_pressure()
        if self.assigned_silos.iscylindrical:
            height = self.assigned_silos.content/(math.pi*pow((self.assigned_silos._d1/2.0),2.0))
            pressure = (self.assigned_silos.p1 * height * 9.80665)*0.00001
            times = (pressure/self._max_pressure)*100
            self.output = self._min_output * 1 + (((self._full_scale-self._min_output)/100)*times)
        else:
            pass