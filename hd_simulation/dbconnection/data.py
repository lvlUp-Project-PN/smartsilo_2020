from mysql.connector import connect
from dbconnection.models import SensorData
from dbconnection.configuration import Configuration
from datetime import datetime
import os


class SensorDataRepository:
  """
  params: config [Configuration], key [str]
  """
  def __init__(self,config:Configuration,key:str):
    self._conndata:dict = config.conndict[key]

  def get_all_data(self):
    conn = connect(**self._conndata)
    cursor = conn.cursor()
    query = ("SELECT * FROM realtime")
    try:
      cursor.execute(query)
      for item in cursor:
        s = SensorData()
        s.SilosCode = item[0]
        s.SilosDataTime = item[1]
        s.SilosValue = item[2]
        s.CodiciErrore = item[3]
        yield s
    except TypeError:
      print("Unable to find rows in table")
    finally:
      cursor.close()
      conn.close()
  
  def get_snsdata_from_id(self, silos_id:str):
    conn = connect(**self._conndata)
    cursor = conn.cursor()
    try:
      if silos_id.__contains__(';') or silos_id.__contains__('(') or silos_id.__contains__(')'):
        raise TypeError
      query = ("SELECT * FROM realtime WHERE SilosCode = %s" % (silos_id))
      cursor.execute(query)
      for item in cursor:
        s = SensorData()
        s.SilosCode = item[0]
        s.SilosDataTime = item[1]
        s.SilosValue = item[2]
        s.CodiciErrore = item[3]
        yield s
    except TypeError:
      print("Unable to find rows in table")
    finally:
      cursor.close()
      conn.close()
  
  def insert(self,item:SensorData):
    conn = connect(**self._conndata)
    cursor = conn.cursor()
    date = datetime.isoformat(
      item.SilosDataTime
    )
    query = "INSERT INTO silos_data_irt VALUES('%s','%s',%f,%s);" % (
      item.SilosCode,
      item.SilosDataTime,
      item.SilosValue,
      "NULL"
    )
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()