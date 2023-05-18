import turtle
import math
from inventory import shelves, shop
from coordinates import area_list, areas
shopping_list = [
    'oats', 'salmon', 'banana', 'coffee', 'canned_tuna', 'fortune_cookie', 'redbull', 'spaghetti_and_meatballs', 'dogfood'
]


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
    try:
        categorized_shopping_list[get_category(item)].append(item)
        if get_category(item) in poi:
            continue
        else:
            poi.append(get_category(item))
    except KeyError:
        print(f'{item} does not exist in the dataset. sorry')
        if len(shopping_list) == 1:
            print('yeet')



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
tr.speed(100)
tr.setpos(-450, -570)

#
# for area in route:
#     if area == 'j':
#
#         continue
#     if area[0] == 'b':
#
#         for product in categorized_shopping_list[area]:
#             print(get_shelf(product))
#             tr.setpos(areas[get_shelf(product)])
#             tr.color('blue')
#             tr.dot(20)
#             tr.color('black')
#             tr.write(product)
#             print(product)
#
#
#     elif area[0] == 'a':
#         smallest = 2000
#         for i in range(1,4):
#             if tr.distance(areas[f'{area}{i}']) < smallest:
#                 smallest = i
#         tr.setpos(areas[f'a{smallest}'])
#
#         for product in categorized_shopping_list[area]:
#             print(get_shelf(product))
#             tr.setpos(areas[get_shelf(product)])
#
#             tr.color('blue')
#             tr.dot(20)
#             tr.color('black')
#             print(product)
#
#
#     else:
#         if tr.distance(areas[f'{area}1']) < tr.distance(areas[f'{area}4']):
#             smallest = 1
#         else:
#             smallest = 4
#         tr.setpos(areas[f'{area}{smallest}'])
#         for product in categorized_shopping_list[area]:
#             print(get_shelf(product))
#             tr.setpos(areas[get_shelf(product)])
#             tr.write(product)
#             tr.color('blue')
#             tr.dot(20)
#             tr.color('black')
#             print(product)
#
#
# tr.setpos(areas['h1'])
# tr.setpos(50, -320)



# doing visible



tr.speed(3)
tr.setpos(-450, -570)
tr.down()
tr.showturtle()

print(route)


def get_shortest_distance(points1, endpoint):
    shortest = (3000, 3000)
    for point in points1:
        if math.dist(point, endpoint) < math.dist(shortest, endpoint):
            shortest = point
    return shortest
for area in route:
    if area[0] == 'b':

        for product in categorized_shopping_list[area]:
            tr.setpos(areas[get_shelf(product)])
            print('going b')
            tr.dot(20)




    elif area[0] == 'a':
        smallest = 2000
        for i in range(1,4):
            if tr.distance(areas[f'{area}{i}']) < smallest:
                smallest = i
        tr.setpos(areas[f'a{smallest}'])
        print('going a first ')

        for product in categorized_shopping_list[area]:
            tr.setpos(areas[get_shelf(product)])
            print('going a seconds')
            tr.dot(20)

    else:
        if tr.distance(areas[f'{area}1']) < tr.distance(areas[f'{area}4']):
            smallest = 1
        else:
            smallest = 4



        points = [point for point in area_list[route[route.index(area) - 1]].values()]
        endpoint = areas[f'{area}{smallest}']

        tr.setpos(get_shortest_distance(points, endpoint))
        print('going other first ')

        tr.setpos(areas[f'{area}{smallest}'])
        print('going other 2nd')
        for product in categorized_shopping_list[area]:
            print(product)
            tr.setpos(areas[get_shelf(product)])
            print('going other 3rd?')
            tr.dot(20)
            last_product = areas[get_shelf(product)]

tr.setpos(get_shortest_distance([areas[f'j{i}'] for i in range(1,5)],areas['h1']))
tr.setpos(areas['h1'])
tr.setpos(50, -320)






wn.mainloop()