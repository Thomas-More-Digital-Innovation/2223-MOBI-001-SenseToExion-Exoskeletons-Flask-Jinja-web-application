import os

from flask import Flask, render_template
from py2neo import Graph
from py2neo import NodeMatcher, RelationshipMatcher

# Credentials from Environment
NEO4J_CONNECTION_URI = os.environ.get("NEO4J_CONNECTION_URI")
NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD")
print(NEO4J_CONNECTION_URI)

# Neo4j Sense2Exion Database
Graph = Graph(NEO4J_CONNECTION_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
g = Graph
node_matcher = NodeMatcher(g)
relationship_matcher = RelationshipMatcher(g)

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
