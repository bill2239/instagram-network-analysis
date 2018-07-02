import networkx as nx
import operator
import random
import csv
#remove the edges randomly and output the size of giant components
fe=open('anonymized_edge_list.csv','rb')
fw=open('size_giantcom.csv','wb')
writer=csv.writer(fw)
reader=csv.reader(fe)
G=nx.Graph()

edge_list=[]
reduced_list=[]
for x in reader:
    edge_list.append(x)
    G.add_edge(x[0],x[1])
    print x


for x in range(1,100):

    k=len(edge_list)*(x/100.0)
    print k
    for o in range(int(k)):
        index=random.randint(0,int(len(edge_list)-1))
        #print edge_list[index]
        if(edge_list[index]):
            reduced_list=edge_list.pop(index)
            print reduced_list
            if(G.has_edge(reduced_list[0],reduced_list[1])):
                G.remove_edge(reduced_list[0],reduced_list[1])
    Gcc=sorted((nx.connected_component_subgraphs(G)), key = len, reverse=True)
    s=0
    print Gcc
    print Gcc[0].size()


    writer.writerow([Gcc[0].size()])



fw.close()
fe.close()