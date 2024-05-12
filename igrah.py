import igraph as ig
g = ig.Graph()
g.add_vertices(3)
g.add_edges([(0,1), (1,2), (2,0)])
ig.plot(g)  