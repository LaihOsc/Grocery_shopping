import turtle
from inventory import shelves, shop, G
from coordinates import area_list, areas
import networkx as nx
import matplotlib.pyplot as plt
from yeet import get_product_object_by_ean, get_coordinate_by_category, get_product_object_by_name
def show_map(shopping_list):
    # shopping_list = input("What would you like to buy? (e.g.: milk, sprite, rice...):  ")
    #
    # shopping_list = shopping_list.replace(' ', '').split(',')
    #
    # for index, word in enumerate(shopping_list):
    #     if 'ä' in word:
    #         shopping_list[index] = word.replace('ä', 'Ã¤').replace('ö', 'Ã¶')
    #
    # print(shopping_list)

    #'paper_plate', 'cookies', 'rice', 'salad', 'nachos', 'fortune_cookie', 'frozen_fries'



    def get_category(item):
        for cat in shop.keys():
            for get_shelf in shop[cat]:
                if item in get_shelf:
                    return cat

    def get_shelf(item):

        cat = get_category(item)

        for s in shelves[cat].keys():
            for product in shelves[cat][s]:
                if item in product:
                    return s


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

    poi = []



    for item in shopping_list:
        print(item)
        # try:
        product_object = get_product_object_by_ean(item)

        categorized_shopping_list[get_coordinate_by_category(product_object['category'])[0]].append(item)

        if get_coordinate_by_category(product_object['category'])[0] in poi:
            continue
        else:
            poi.append(get_coordinate_by_category(product_object['category'])[0])
        # except KeyError:
        #     print(f'{item} does not exist in the dataset. sorry')
        #     if len(shopping_list) == 1:
        #         print('yeet')



    def check_route(items, route):
        for item in items:
            if item not in route:
                return False
            else:
                continue
        return True


    def router(poi):
        for route in routes:
            if check_route(poi, route) == True:
                print('route', route)
                return route

    route = router(poi)

    print('The route:')



    #Converts x,y coordinates from Photoshop into Turtles coordinates (Like coordinate system in math)
    def converter(x, y):
        result = (x-0, 0-y)
        return result

    print(route)

    #Initializing turtle
    tr = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width=1200, height=1200)
    wn.bgpic("kylis.png")
    tr.shape('circle')
    tr.color('black')
    tr.pensize(3)


    #Hiding turtle
    tr.up()
    tr.hideturtle()
    tr.speed(3)
    tr.setpos(-450, -570)

    tr.showturtle()
    tr.down()


    graph = nx.Graph()


    items = []
    for yeet in route:
        for product in categorized_shopping_list[yeet]:
            product_object = get_product_object_by_ean(product)
            items.append(get_coordinate_by_category(product_object['category']))

    print(items)
    prev = 'start'
    for item in items:
        for dot in nx.shortest_path(G, prev, item):
            tr.setpos(areas[dot])
        tr.dot(20)
        prev = item


    #Going to checkout
    for dot in nx.shortest_path(G, prev, 'end'):
        tr.setpos(areas[dot])


    #items = ['b2' ,'a4', 'c3', 'd2', 'g2', 'j3']

    # weights = []
    #
    # def myFunc(e):
    #     return e['weight']
    #
    # for item in items:
    #     weights.append({"name": item, "weight": nx.shortest_path_length(G, 'b1', item)})
    #
    # print(weights)
    #
    # weights.sort(key=myFunc)
    #
    # print(weights)
    #
    # prev = 'b1'
    #
    # print('c1', 'e1' ,nx.shortest_path_length(G, 'c1', 'e1'))
    #
    # for i, product in enumerate(weights):
    #
    #     for coordinate in nx.shortest_path(G, prev ,product['name']):
    #         tr.setpos(areas[coordinate])
    #         tr.write(coordinate)
    #         print(prev, product['name'], nx.shortest_path_length(G, prev ,product['name']))
    #     prev = product['name']

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






    wn.mainloop()