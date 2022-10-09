from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def hello() :
    return render_template("index.html")

@app.route("/commands")
def command() : 
    return render_template("commands.html")

@app.route("/logs")
def logs() : 
    return render_template("logs.html")

@app.route("/dev")
def dev() : 
    return render_template("dev.html")

@app.route("/plans")
def plans() : 
    return render_template("plans.html")

if __name__ == "__main__" : 
    app.run(debug=True, port = 5333)