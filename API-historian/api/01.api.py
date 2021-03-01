import flask

app = flask.Flask(__name__)

app.config["DEBUG"]=1


@app.route('/', methods=['GET'])
def home():
	return f"<h1>Distant reading archive</h1><p> Apit prototype for distant reading </p>"

app.run()