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
def hello():
	return jsonify({'name' : 'Jimit', 'address': 'India'})

	
app.run(debug = 1)