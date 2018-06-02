from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return "hello world"

@app.route("/tmp1")
def tmp1():
	return "TMP"

@app.route("/tmp/<string:name>/")
def template(name):
	return render_template('template2.html',name=name)

if __name__ == "__main__":
	app.run()
