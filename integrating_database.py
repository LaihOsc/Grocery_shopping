import turtle
from graph_creator import Graph
from coordinates import areas
import networkx as nx
import matplotlib.pyplot as plt
from categorized_database_methods import get_product_object_by_ean, get_coordinate_by_category


def show_map(shopping_list):
    categorized_shopping_list = {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': [],
        'h': [],
        'i': [],
        'j': [],
    }

    routes = ['bdfhj', 'bacdfhj', 'bdcegij', 'bacefij', 'bacefhgij', 'bacdfeghj', 'bacdgfhij']

    poi = []  # Points of interest

    for item in shopping_list:
        product_object = get_product_object_by_ean(item)

        categorized_shopping_list[get_coordinate_by_category(product_object['category'])[0]].append(item)

        if get_coordinate_by_category(product_object['category'])[0] in poi:
            continue
        else:
            poi.append(get_coordinate_by_category(product_object['category'])[0])

    def check_route(items_input, route_input):
        for item_input in items_input:
            if item_input not in route_input:
                return False
            else:
                continue
        return True

    def router(poi_input):
        for route in routes:
            if check_route(poi_input, route):
                print('route', route)
                return route

    route = router(poi)

    print(route)

    # Initializing turtle
    tr = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width=1200, height=1200)
    wn.bgpic("store.png")
    tr.shape('circle')
    tr.color('black')
    tr.pensize(3)

    # Hiding turtle
    tr.up()
    tr.hideturtle()
    tr.speed(3)
    tr.setpos(-450, -570)

    tr.showturtle()
    tr.down()

    items = []
    for yeet in route:
        for product in categorized_shopping_list[yeet]:
            product_object = get_product_object_by_ean(product)
            items.append(get_coordinate_by_category(product_object['category']))

    print(items)
    prev = 'start'
    for item in items:
        for dot in nx.shortest_path(Graph, prev, item):
            tr.setpos(areas[dot])
        tr.dot(20)
        tr.up()
        tr.pensize(20)
        tr.sety(tr.ycor() - 7)
        tr.color('red')
        tr.write('1', align='left')
        tr.color('black')
        tr.sety(tr.ycor() + 7)
        tr.pensize(3)
        tr.down()
        prev = item

    # Going to checkout
    for dot in nx.shortest_path(Graph, prev, 'end'):
        tr.setpos(areas[dot])

    plt.show()

    wn.mainloop()
