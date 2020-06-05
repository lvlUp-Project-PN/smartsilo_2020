from dbconnection.data import SensorDataRepository
from dbconnection.models import SensorData

class SensorsDataServices:
    def __init__(self,repository:SensorDataRepository):
        self._repository = repository
    
    def get_all_data(self):
        return self._repository.get_all_data()
    
    def get_data_from_id(self, silos_id:str):
        return self._repository.get_snsdata_from_id(silos_id)
    
    def insert(self, item:SensorData):
        self._repository.insert(item)