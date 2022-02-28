from flask import Flask, request, Response
import requests
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello!Welcome to Fibonacci Server!'


def caluculate_fibonacci(number):
    if number < 0:
        print("Please enter a positive integer")
    elif number == 0:
        return 0
    elif number <= 2:
        return 1
    else:
        return caluculate_fibonacci(number - 1) + caluculate_fibonacci(number - 2)


@app.route('/fibonacci')
def fibonacci():
    number = request.args.get('number')
    if not number:
        return Response(status=400)
    if not isinstance(number, int):
        return Response(status=400)
    result = caluculate_fibonacci(int(number))
    return Response("the fibonacci for "+str(number)+" is: "+str(result), status = 200)



@app.route('/register')
def register():
    hostname = request.args.get('hostname')
    ip = '0.0.0.0'
    dict = {}
    dict['name'] = hostname
    dict['address'] = ip
    r = requests.post('http://0.0.0.0:53533', data=dict)
    return r.text

#  as_ip = request.args.get('as_ip')
# as_port = request.args.get('as_port')
#  data = {
#          "NAME": hostname,
#          "VALUE": ip,
#          "TYPE": "A",
#          "TTL": 10
#    }
#  data = json.dumps(data)
#  print("data: ", data)
#  try:
#     socketget = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     socketget.sendto(data.encode(), (as_ip, as_port))
#  except socket.error as e:
#      print(e)
#      return Response(status=400)
#  response = {
#      "status_code": 201,
#      "hostname": hostname,
#      "ip": ip,
#      "as_ip": as_ip,
#      "as_port": as_port
#      }
#  return Response(response=json.dumps(response), status=200)


app.run(host='0.0.0.0', port=9090, debug=True)