import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
#b
G.add_edge("b1", "b2", weight=1)
G.add_edge("b2", "b3", weight=1)
G.add_edge("b1", "b4", weight=1)
G.add_edge("b3", "b6", weight=1)
G.add_edge("b4", "b5", weight=1)
G.add_edge("b5", "b6", weight=1)
G.add_edge("b4", "b7", weight=1)
G.add_edge("b6", "b9", weight=1)
G.add_edge("b7", "b8", weight=1)
G.add_edge("b8", "b9", weight=1)




#a
G.add_edge("a1", "a2", weight=1)
G.add_edge("a2", "a3", weight=1)
G.add_edge("a1", "a4", weight=1)
G.add_edge("a3", "a6", weight=1)
G.add_edge("a4", "a5", weight=1)
G.add_edge("a5", "a6", weight=1)
G.add_edge("a4", "a7", weight=1)
G.add_edge("a6", "a9", weight=1)
G.add_edge("a7", "a8", weight=1)
G.add_edge("a8", "a9", weight=1)

#d
G.add_edge("d1", "d2", weight=1)
G.add_edge("d1", "d3", weight=1)
G.add_edge("d2", "d3", weight=1)
G.add_edge("d1", "d4", weight=2)

#c
G.add_edge("c1", "c2", weight=1)
G.add_edge("c1", "c3", weight=1)
G.add_edge("c2", "c3", weight=1)
G.add_edge("c1", "c4", weight=2)

#f
G.add_edge("f1", "f2", weight=1)
G.add_edge("f1", "f3", weight=1)
G.add_edge("f2", "f3", weight=1)
G.add_edge("f1", "f4", weight=2)

#e
G.add_edge("e1", "e2", weight=1)
G.add_edge("e1", "e3", weight=1)
G.add_edge("e2", "e3", weight=1)
G.add_edge("e1", "e4", weight=2)

#h
G.add_edge("h1", "h2", weight=1)
G.add_edge("h1", "h3", weight=1)
G.add_edge("h2", "h3", weight=1)
G.add_edge("h1", "h4", weight=2)

#g
G.add_edge("g1", "g2", weight=1)
G.add_edge("g1", "g3", weight=1)
G.add_edge("g2", "g3", weight=1)
G.add_edge("g1", "g4", weight=2)

#j
G.add_edge("j1", "j2", weight=1)
G.add_edge("j1", "j3", weight=1)
G.add_edge("j2", "j3", weight=1)
G.add_edge("j1", "j4", weight=2)

#i
G.add_edge("i1", "i2", weight=1)
G.add_edge("i1", "i3", weight=1)
G.add_edge("i2", "i3", weight=1)
G.add_edge("i1", "i4", weight=2)


# ba
G.add_edge("b7", "a1", weight=1)
G.add_edge("b8", "a2", weight=1)
G.add_edge("b9", "a3", weight=1)

# bd
G.add_edge("b3", "d1", weight=1)
G.add_edge("b9", "d4", weight=1)

# bc
G.add_edge("b9", "c1", weight=2)

# ac
G.add_edge("a3", "c1", weight=1)
G.add_edge("a9", "c4", weight=1)

# ad
G.add_edge("a3", "d4", weight=1)

#cd
G.add_edge("c1", "d4", weight=1)

#ce
G.add_edge("c1", "d1", weight=1)
G.add_edge("c4", "d4", weight=1)

#cf
G.add_edge("c1", "f4", weight=2)

#df
G.add_edge("d1", "f1", weight=1)
G.add_edge("d4", "f4", weight=1)

#de
G.add_edge("d4", "e1", weight=2)

#eg
G.add_edge("e1", "g1", weight=1)
G.add_edge("e4", "g4", weight=1)

#ef
G.add_edge("e1", "f4", weight=1)

#eh
G.add_edge("e1", "h4", weight=2)

#fh
G.add_edge("f1", "h1", weight=1)
G.add_edge("f4", "h4", weight=1)

#fg
G.add_edge("f4", "g1", weight=2)

#gi
G.add_edge("g1", "i1", weight=1)
G.add_edge("g4", "i4", weight=1)

#gh
G.add_edge("g1", "h4", weight=1)

#gj
G.add_edge("g1", "j4", weight=2)

#hj
G.add_edge("h1", "j1", weight=1)
G.add_edge("h4", "j4", weight=1)

#hi
G.add_edge("h4", "i1", weight=2)

#ij
G.add_edge("i1", "j4", weight=1)



print(nx.shortest_path(G, 'b1', 'i4'))
print(nx.shortest_path_length(G, 'b1', 'i4'))

print(nx.shortest_path(G, 'b2', 'a4'))
print(nx.shortest_path_length(G, 'b1', 'i4'))

graph = nx.Graph()

def path(x1, x2):
    weight = nx.shortest_path_length(G, x1, x2)
    graph.add_edge(x1, x2, weight=weight)

items = ['b2' ,'a4', 'c3', 'd2', 'g2', 'j3']

weights = []

def myFunc(e):
    return e['weight']

for item in items:
    weights.append({"name": item, "weight": nx.shortest_path_length(G, 'b1', item), "path": nx.shortest_path(G, 'b1', item)})

print(weights)

weights.sort(key=myFunc)

print(weights)


# for item1 in items:
#     for item2 in items:
#         if item1 == item2:
#             continue
#         else:
#             path(item1, item2)
#
# pos = nx.circular_layout(graph)
# nx.draw(graph, with_labels=True)
# edge_weight = nx.get_edge_attributes(graph,'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
#
# print(nx.single_source_dijkstra_path(graph, 'b2'))
# print(nx.all_pairs_dijkstra_path_length(graph))


plt.show()