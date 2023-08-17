from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def Bienvenida():
    return render_template("index.html")

@app.route("/Greissy")
def Sobre():
    return render_template("greissy.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
