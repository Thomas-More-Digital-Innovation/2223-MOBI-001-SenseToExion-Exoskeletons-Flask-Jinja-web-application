from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/msa")
def msa():
    return render_template("msa.html")


@app.route("/risks")
def risks():
    return render_template("risks.html")


@app.route("/exoskeletons")
def exoskeletons():
    return render_template("exoskeletons.html")


@app.route("/sensors")
def sensors():
    return render_template("sensors.html")


@app.route("/tool")
def tool():
    return render_template("tool.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/cases")
def cases():
    return render_template("cases.html")


@app.route("/links")
def links():
    return render_template("links.html")


if __name__ == '__main__':
    app.run(debug=True)
