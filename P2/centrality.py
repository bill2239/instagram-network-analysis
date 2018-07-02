
import networkx as nx
import operator
import numpy
import csv

fpr=open('pagerank.csv','wb')
fce=open('eigenvector.csv','wb')
cewriter=csv.writer(fce)
prwriter=csv.writer(fpr)
__author__ = 'HP'
fe=open('anonymized_edge_list.csv','rb')
reader=csv.reader(fe)
G=nx.DiGraph()
edge_list=[]

for x in reader:
    edge_list.append(x)
    print x
    G.add_edge(x[0],x[1])
list1=[]
pr=nx.pagerank(G,alpha=0.9)
for key, value in sorted(pr.items(), key=operator.itemgetter(1),reverse=True):
    list1=[key,value]
    prwriter.writerow(list1)
def eigenvector_centrality(G, max_iter=100, tol=1.0e-6, nstart=None,
                           weight='weight'):
    """Compute the eigenvector centrality for the graph G.

    Uses the power method to find the eigenvector for the
    largest eigenvalue of the adjacency matrix of G.

    Parameters
    ----------
    G : graph
      A networkx graph

    max_iter : interger, optional
      Maximum number of iterations in power method.

    tol : float, optional
      Error tolerance used to check convergence in power method iteration.

    nstart : dictionary, optional
      Starting value of eigenvector iteration for each node.

    weight : None or string, optional
      If None, all edge weights are considered equal.
      Otherwise holds the name of the edge attribute used as weight.

    Returns
    -------
    nodes : dictionary
       Dictionary of nodes with eigenvector centrality as the value.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> centrality = nx.eigenvector_centrality(G)
    >>> print(['%s %0.2f'%(node,centrality[node]) for node in centrality])
    ['0 0.37', '1 0.60', '2 0.60', '3 0.37']

    Notes
    ------
    The eigenvector calculation is done by the power iteration method
    and has no guarantee of convergence.  The iteration will stop
    after max_iter iterations or an error tolerance of
    number_of_nodes(G)*tol has been reached.

    For directed graphs this is "left" eigevector centrality which corresponds
    to the in-edges in the graph.  For out-edges eigenvector centrality
    first reverse the graph with G.reverse().

    See Also
    --------
    eigenvector_centrality_numpy
    pagerank
    hits
    """
    from math import sqrt
    if type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph:
        raise nx.NetworkXException("Not defined for multigraphs.")

    if len(G) == 0:
        raise nx.NetworkXException("Empty graph.")

    if nstart is None:
        # choose starting vector with entries of 1/len(G)
        x = dict([(n,1.0/len(G)) for n in G])
    else:
        x = nstart
    # normalize starting vector
    s = 1.0/sum(x.values())
    for k in x:
        x[k] *= s
    nnodes = G.number_of_nodes()
    # make up to max_iter iterations
    for i in range(max_iter):
        xlast = x
        x = dict.fromkeys(xlast, 0)
        # do the multiplication y^T = x^T A
        for n in x:
            for nbr in G[n]:
                x[nbr] += xlast[n] * G[n][nbr].get(weight, 1)
        # normalize vector
        try:
            s = 1.0/sqrt(sum(v**2 for v in x.values()))
        # this should never be zero?
        except ZeroDivisionError:
            s = 1.0
        for n in x:
            x[n] *= s
        # check convergence
        err = sum([abs(x[n]-xlast[n]) for n in x])
        if err < nnodes*tol:
            return x

    raise nx.NetworkXError("""eigenvector_centrality():
power iteration failed to converge in %d iterations."%(i+1))""")

centrality = eigenvector_centrality(G)
for key, value in sorted(centrality.items(), key=operator.itemgetter(1)):
    print key,value
    cewriter.writerow([key,value])
#print sorted(pr)
#print(['%s %0.2f'%(node,centrality[node]) for node in sorted(centrality)])


'''fw2=open('in_deg_cen.csv','wb')
dcwriter=csv.writer(fw2)
dict=nx.in_degree_centrality(G)
for key, value in sorted(dict.items(), key=operator.itemgetter(1),reverse=True):
    print (['%s %f'%(key,value)])
    dcwriter.writerow([key,value])
fw2.close()'''





fce.close()
fpr.close()


