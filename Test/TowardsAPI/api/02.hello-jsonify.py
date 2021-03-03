from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/<int:number>/', methods = ['GET'])
def increment(number):
	return "Increment number is "+str(number+1)

@app.route('/<string:name>/', methods = ['GET'])
def hello(name):
	return f"Hello {name}"

@app.route('/person/')
def jsonTest():
	return jsonify({'name' : 'Jimit', 'address': 'India'})

@app.route('/numbers/')
def print_list():
	return jsonify(list(range(5)))

app.run(debug = 1)