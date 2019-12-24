from py2neo import Node, Graph, Relationship, NodeMatcher, Subgraph
import pandas as pd
import numpy as np

test_graph = Graph(
    "http://localhost:7474",
    username="earphone",
    password="000000"
)
def writeneo4j(entity1, entity2, relation):
    matcher = NodeMatcher(test_graph)
    if len(list(matcher.match("earphone").where(f"_.name = '{entity1}'"))) == 0:
        a = Node("earphone", name=entity1)
        test_graph.create(a)
    else:
        a = list(matcher.match("earphone").where(f"_.name = '{entity1}'"))[0]

    if len(list(matcher.match("earphone").where(f"_.name = '{entity2}'"))) == 0:
        b = Node("earphone", name=entity2)
        test_graph.create(b)
    else:
        b= list(matcher.match("earphone").where(f"_.name = '{entity2}'"))[0]

    r = Relationship(a, relation, b)
    test_graph.create(r)

if __name__ == "__main__":
    writeneo4j("a", "b", "is better than")