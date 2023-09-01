from flask import Flask,render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def Redir():
    return redirect("/Home")

@app.route("/Login")
def Login():
    return render_template("login.html")

@app.route("/Register")
def Register():
    return render_template("register.html")

@app.route("/Home")
def Bienvenida():
    return render_template("index.html")

@app.route("/Greissy")
def Sobre():
    return render_template("greissy.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
