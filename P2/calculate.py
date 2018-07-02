#calculate clustering coefficient, # of 3-cycles
__author__ = 'HP'
import networkx as nx
import operator

import csv
fe=open('anonymized_edge_list.csv','rb')

reader=csv.reader(fe)
G=nx.Graph()
#edge_list=[]
for x in reader:
    #edge_list.append(x)
    print x
    G.add_edge(x[0],x[1])


print nx.average_clustering(G)
print nx.transitivity(G)
print sum(list(nx.triangles(G).values()))/3.0  # the number of 3-cycles