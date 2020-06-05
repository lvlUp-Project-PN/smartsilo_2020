import json, os
from datetime import datetime
from dbconnection.data import SensorDataRepository
from dbconnection.services import SensorsDataServices
from dbconnection.models import Sensor
from dbconnection.configuration import Configuration


service = SensorsDataServices(SensorDataRepository(Configuration(),"SensorTemp"))

# for m in range(1,10):
#   for n in range(10):
#     sensore = Sensor()
#     sensore.SilosCode = "00000000000" + str(m)
#     sensore.SilosDataTime = datetime.now()
#     sensore.SilosValue = float(n)
#     service.insert(sensore)

for item in service.get_all_data():
  p = setattr(item,"SilosCode",)
  print()

# for item in service.get_data_from_id("000000000006"):
#   print(item)