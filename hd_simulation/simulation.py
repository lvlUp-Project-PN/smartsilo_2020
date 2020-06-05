from hd_models_lvlup import Sensor,Gateway,Silos,Site
from json import loads
import os


siloses:list = []
sensors:list = []
gateways:list = []
sites:list = []

def readconfig(path):
    with open(path) as file:
        return loads(file.read())

def create_instances():
    json = readconfig(os.path.join(os.getcwd(),"config","simconfig.json"))

    for site in json["sites"]:
        sitetmp = Site()
        sitetmp.site_id = site["Id"]
        for gateway in site["Gateways"]:
            gatewaytmp = Gateway()
            gatewaytmp.gateway_id = site["Id"] + gateway["Id"]
            for sensor in gateway["Sensors"]:
                sensortmp = Sensor()
                sensortmp.sensor_id = site["Id"] + gateway["Id"] + sensor["Silos"]["Id"] + sensor["Id"]
                silostmp = Silos(
                    site["Id"] + gateway["Id"] + sensor["Silos"]["Id"],
                    sensor["Silos"]["Params"][0],
                    sensor["Silos"]["Params"][1],
                    sensor["Silos"]["Params"][2],
                    sensor["Silos"]["Params"][3],
                    sensor["Silos"]["Params"][4],
                    sensor["Silos"]["Params"][5]
                )
                sensortmp.assigned_silos = silostmp
                sitetmp.siloses.append(silostmp)
                siloses.append(silostmp)
                sitetmp.sensors.append(sensortmp)
                sensors.append(sensortmp)
            sitetmp.gateways.append(gatewaytmp)
            gateways.append(gatewaytmp)
        sites.append(sitetmp)

def exec_tasks_on_insts():
    while True:
        for site in sites:
            for gateway in gateways:
                for sensor in sensors:
                    sensor.assignedSilos.update_content_level()

def run():
    create_instances()
    exec_tasks_on_insts()


if __name__ == "__main__":
    run()
