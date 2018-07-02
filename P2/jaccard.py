__author__ = 'HP'
import networkx as nx
import operator
# calculate jaccard coefficient
import csv
fe=open('anonymized_edge_list.csv','rb')

reader=csv.reader(fe)
#column=[]
#c_p=[]
G=nx.Graph()
edge_list=[]
for x in reader:
    edge_list.append(x)
    print x
    G.add_edge(x[0],x[1])


fja=open('jaccard.csv','wb')
writer=csv.writer(fja)

array=nx.jaccard_coefficient(G,edge_list)
for c,v,p in array:

    l=[c,v,p]
    writer.writerow(l)
#    column.append(l)



fja.close()
fe.close()