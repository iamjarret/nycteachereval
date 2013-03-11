'''
This code runs off the configuration file in the same folder and 


'''
import requests
import ConfigParser
import sys
sys.path.append("/home/jarret/nycteacher/nycteacher/")
from teachers.models import Teachers, School


cfg = ConfigParser.ConfigParser()
cfg.read(['socrata.cfg', expanduser('~/.socrata.cfg')])




payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)

http://data.cityofnewyork.us/resource/nurr-mhyi.json