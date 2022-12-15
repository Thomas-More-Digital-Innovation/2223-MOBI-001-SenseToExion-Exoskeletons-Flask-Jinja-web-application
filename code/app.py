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
    query_all_exoskeletons = "MATCH (e:Exo) RETURN e.exoNaam as Name, e.exoFabrikant as Manufacturer, e.exoBeschrijving as Description"
    all_exoskeletons = g.run(query_all_exoskeletons).data()
    query_all_aim_types = 'match (n)-[]-(p) call { with n, p with n, p where (n:Aim and n.aimIsSelectable="x") and (p:AimType and p.aimTypeIsSelectable="x") return p.aimTypeNameEn as name, n.aimId as id union with n, p with n, p where (n:StructureKinematicName and n.structureKinematicNameIsSelectable="x") and (p:StructureKinematicNameType and p.structureKinematicNameTypeIsSelectable="x") return p.structureKinematicNameTypeNameEn as name, n.structureKinematicNameId as id} return name,collect(id) as ids;'
    all_aim_types = g.run(query_all_aim_types).data()
    # sorted_exoskeletons = sorted(all_exoskeletons, key=lambda d: d["exoskeletons"]["exo_name"])
    print(all_exoskeletons)
    print(all_aim_types)
    return render_template("tool.html",  aim_types=all_aim_types, exoskeletons=all_exoskeletons)


@app.route("/tool/<exo_name>")
def tool_name(exo_name):
    exo_name = str(exo_name)
    return render_template("tool_details.html", exo_name=exo_name)


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/cases")
def cases():
    return render_template("cases.html")


@app.route("/links")
def links():
    links = [
        {
            "url": "https://www.ergonomiesite.be/",
            "title": "Ergonomie",
            "description": "Informatie en onderzoek over ergonomie"
        },
        {
            "url": "https://mobilabandcare.be/",
            "title": "Mobilab",
            "description": "Mobilab & care"
        },
        {
            "url": "https://mobilabandcare.be/sense-to-exion/",
            "title": "Sense2Exion",
            "description": "Sense2Exion website"
        },
        {
            "url": "https://www.verv.be",
            "title": "Beroepsvereniging",
            "description": "Beroepsvereniging voor Ergonomie website"
        },
        {
            "url": "https://exoskeletonreport.com/",
            "title": "Exoskeletten",
            "description": "Een uitgebreid overzicht van exoskeletten"
        },
        {
            "url": "https://www.vlaio.be",
            "title": "Vlaio",
            "description": "Vlaamse overheid"
        }

    ]

    return render_template("links.html", links=links)


if __name__ == '__main__':
    app.run(debug=True)
