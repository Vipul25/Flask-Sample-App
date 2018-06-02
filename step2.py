from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world"

@app.route("/tmp")
def tmp():
	return "TMP"

if __name__ == "__main__":
	app.run()
