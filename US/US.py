from flask import Flask,  request, Response
import json

app = Flask(__name__)


@app.route('/')
def Welcome():
    return 'Hello!Welcome to User Server!'


@app.route('/fibonacci')
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = int(request.args.get('number'))
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    if (hostname == '' or fs_port == '' or number == '' or as_ip == '' or as_port == ''):
        return Response("Bad request", status=400)
    else:
        response = {
            "hostname": hostname,
            "fs_port": fs_port,
            "number": number,
            "as_ip": as_ip,
            "as_port": as_port,
            "HTTP_code": 200
        }
        return Response(response=json.dumps(response), status=200, mimetype='application/json')


app.run(host='0.0.0.0', port=8080, debug=True)
##US does not know the IP address of the given hostname and therefore needs to query its authoritative DNS server

