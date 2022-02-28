import requests
import json


def registration():
    url = 'http://192.168.1.206:9090/register'
    values = {'hostname': 'fibonacci.com',
              'ip': '0.0.0.0',
              'as_ip': '172.18.0.1',
              'as_port': '30001'}
    headers = {"Content-Type": "application/json"}
    values = json.dumps(values)
    r = requests.put(url, data=values, headers=headers)
    return r

registration()