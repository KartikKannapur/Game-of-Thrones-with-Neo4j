__author__ = "Kartik Kannapur"

# #Python File Imports
import properties as prop

# #Python Library Imports
import py2neo as py2neo


def char_relationships():
    # #Authentication
    py2neo.authenticate("localhost:7474", "neo4j", "neo4j")

    # #Neo4j server connection must be started - './bin/neo4j start'
    # #Connection made to http://localhost:7474/db/data/
    graph_db = py2neo.Graph("http://localhost:7474/db/data/")
    # print graph_db

    # #CHARACTER DEFINITIONS
    char_eddard_stark = py2neo.Node.cast({"name" : "Eddard Stark"})
    char_catelyn_stark = py2neo.Node.cast({"name" : "Catelyn Stark"})

    # #RELATIONSHIP DEFINITIONS
    rel_eddard_stark_marriedTo_catelyn_stark = py2neo.Relationship(char_eddard_stark, "married", char_catelyn_stark)

    # #Create Graph
    graph_db.create(rel_eddard_stark_marriedTo_catelyn_stark)

    # #Tracker
    # #Number of Relationships


    
    print "Graph Created"
if __name__ == '__main__':
    char_relationships()