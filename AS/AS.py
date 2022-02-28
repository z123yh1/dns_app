import os

from flask import Flask, request, Response
import json
app = Flask(__name__)
@app.route('/home')
def welcome():
    return 'Hello!Welcome to Authoritative Server!'

@app.route('/', methods = ['GET', 'POST'])
def initial():
    file = 'address_map.json'
    if not os.path.exists(file):
        os.system(r'touch address_map.json')
        file = 'address_map.json'
    if request.method == 'GET':
        name = request.args.get('name')
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            if name not in data:
                return Response("hostname not found", status=404)
            else:
                address = data.get(name)
                return Response(address, status=200)
    else:
        data_get = request.form
        hostname = data_get['name']
        ip_address =data_get['address']
        dict = {}
        dict[hostname] = ip_address
        with open(file, 'w') as json_file:
            json.dump(dict, json_file)
        return Response("successfully registered", status=200)


app.run(host='0.0.0.0',
        port=53533,
        debug=True)


