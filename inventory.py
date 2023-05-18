shelves = {
    'b' : {
        'b1': ['salad'],
        'b2': ['basil'],
        'b3': ['banana'],
        'b4': ['spaghetti_and_meatballs'],
        'b5': ['banana'],
        'b6': ['nachos'],
        'b7': ['nuggets'],
        'b8': ['special'],
        'b9': ['pepper']
    },

    'a' : {
        'a1': ['chicken'],
        'a2': ['berliinimunkki'],
        'a3': ['sprinkles'],
        'a4': ['salmon'],
        'a5': ['bread'],
        'a6': ['canned_tuna'],
        'a7': ['sausage'],
        'a8': ['pepporoni'],
        'a9': ['ham']
    },

    'c' : {
        'c1': [],
        'c2': ['oats'],
        'c3': ['spaghetti', 'rice'],
        'c4': ['butter']
    },''

    'd' : {
        'd1': ['fortune_cookie'],
        'd2': ['coffee'],
        'd3': ['cookies'],
        'd4': []
    },

    'e' : {
        'e1': [],
        'e2': [],
        'e3': [],
        'e4': ['oil'],
    },

    'f' : {
        'f1': [],
        'f2': ['beer'],
        'f3': ['redbull'],
        'f4': []
    },

    'g' : {
        'g1': [],
        'g2': ['dogfood'],
        'g3': ['paper_plate'],
        'g4': ['juice'],
    },

    'h' : {
        'h1': [],
        'h2': ['sprite'],
        'h3': ['condom', 'shampoo',],
        'h4': [],
    },

    'i' : {
        'i1': [],
        'i2': ['whey'],
        'i3': ['milk'],
        'i4': ['yoghurt']
    },

    'j' : {
        'j1': ['brunberg'],
        'j2': ['candy'],
        'j3': ['frozen_fries'],
        'j4': ['nail_clippers']
    },
}

shop = {
    'a': [item for item in shelves['a'].values()],
    'b': [item for item in shelves['b'].values()],
    'c': [item for item in shelves['c'].values()],
    'd': [item for item in shelves['d'].values()],
    'e': [item for item in shelves['e'].values()],
    'f': [item for item in shelves['f'].values()],
    'g': [item for item in shelves['g'].values()],
    'h': [item for item in shelves['h'].values()],
    'i': [item for item in shelves['i'].values()],
    'j': [item for item in shelves['j'].values()],

}

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

G.add_edge("start", "b1", weight=1)
G.add_edge("start", "b2", weight=1)
G.add_edge("start", "b3", weight=1)

G.add_edge("end", "f1", weight=1)
G.add_edge("end", "h1", weight=2)


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
G.add_edge("d4", "d2", weight=1)
G.add_edge("d4", "d3", weight=1)

#c
G.add_edge("c1", "c2", weight=1)
G.add_edge("c1", "c3", weight=1)
G.add_edge("c2", "c3", weight=1)
G.add_edge("c1", "c4", weight=2)
G.add_edge("c4", "c2", weight=1)
G.add_edge("c4", "c3", weight=1)

#f
G.add_edge("f1", "f2", weight=1)
G.add_edge("f1", "f3", weight=1)
G.add_edge("f2", "f3", weight=1)
G.add_edge("f1", "f4", weight=2)
G.add_edge("f4", "f2", weight=1)
G.add_edge("f4", "f3", weight=1)

#e
G.add_edge("e1", "e2", weight=1)
G.add_edge("e1", "e3", weight=1)
G.add_edge("e2", "e3", weight=1)
G.add_edge("e1", "e4", weight=2)
G.add_edge("e4", "e2", weight=1)
G.add_edge("e4", "e3", weight=1)

#h
G.add_edge("h1", "h2", weight=1)
G.add_edge("h1", "h3", weight=1)
G.add_edge("h2", "h3", weight=1)
G.add_edge("h1", "h4", weight=2)
G.add_edge("h4", "h2", weight=1)
G.add_edge("h4", "h3", weight=1)

#g
G.add_edge("g1", "g2", weight=1)
G.add_edge("g1", "g3", weight=1)
G.add_edge("g2", "g3", weight=1)
G.add_edge("g1", "g4", weight=2)
G.add_edge("g4", "g2", weight=1)
G.add_edge("g4", "g3", weight=1)

#j
G.add_edge("j1", "j2", weight=1)
G.add_edge("j1", "j3", weight=1)
G.add_edge("j2", "j3", weight=1)
G.add_edge("j1", "j4", weight=2)
G.add_edge("j4", "j2", weight=1)
G.add_edge("j4", "j3", weight=1)

#i
G.add_edge("i1", "i2", weight=1)
G.add_edge("i1", "i3", weight=1)
G.add_edge("i2", "i3", weight=1)
G.add_edge("i1", "i4", weight=2)
G.add_edge("i4", "i2", weight=1)
G.add_edge("i4", "i3", weight=1)


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
G.add_edge("a3", "d4", weight=2)

#cd
G.add_edge("c1", "d4", weight=1)

#ce
G.add_edge("c1", "e1", weight=1)
G.add_edge("c4", "e4", weight=1)

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
