from flask import Flask,render_template

app = Flask("app_Name")

@app.route("/")
def Bienvenida():
    return render_template("index.html")

@app.route("/about")
def Sobre():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
