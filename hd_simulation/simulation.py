from hd_models_lvlup import Sensor,Gateway,Silos,Site
from json import loads
import os,time
from threading import Thread


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
                sensortmp = Sensor(
                    site["Id"] + gateway["Id"] + sensor["Silos"]["Id"] + sensor["Id"],
                    sensor["Params"][0],
                    sensor["Params"][1],
                    sensor["Params"][2],
                    sensor["Params"][3],
                    sensor["Params"][4]
                )

                silostmp = Silos(
                    site["Id"] + gateway["Id"] + sensor["Silos"]["Id"],
                    sensor["Silos"]["Params"][0],
                    sensor["Silos"]["Params"][1],
                    sensor["Silos"]["Params"][2],
                    sensor["Silos"]["Params"][3],
                    sensor["Silos"]["Params"][4],
                    sensor["Silos"]["Params"][5],
                    sensor["Silos"]["Params"][6]
                )

                sensortmp.assigned_silos = silostmp
                sitetmp.siloses.append(silostmp)
                siloses.append(silostmp)
                sitetmp.sensors.append(sensortmp)
                sensors.append(sensortmp)
                gatewaytmp.sensors.append(sensortmp)
            sitetmp.gateways.append(gatewaytmp)
            gateways.append(gatewaytmp)
        sites.append(sitetmp)

def exec_tasks_on_insts():
    while True:
        for silos in siloses:
            Thread(target=silos.run()).run()
        for sensor in sensors:
            Thread(target=sensor.run()).start()
        for gateway in gateways:
            gateway.get_data_from_sensors()
        time.sleep(1.0)
                
def run():
    create_instances()
    exec_tasks_on_insts()


if __name__ == "__main__":
    run()
