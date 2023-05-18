import turtle

shopping_list = [
    'coke', 'chicken', 'rice', 'banana',
]

shop = {
    '1': ['bread', 'chicken', 'red_meat'],
    '2': ['banana', 'salad', 'tomato', 'potato'],
    '3': ['oatmeal', 'cereal', 'noodles', 'rice'],
    '4': ['cookies', 'tea', 'coffee'],
    '5': ['dogfood', 'detergent'],
    '6': ['ipa', 'redbull', 'sandels'],
    '7': ['charcoal'],
    '8': ['coke', 'sprite', 'pepsi'],
    '9': ['whey', 'eggs', 'milk'],
  #  '10': ['chocolate', 'tuttifrutti', 'tictac']
}

categories = shop.keys()


def category(item):
    for cat in categories:
        if item in shop[cat]:
            return cat



categorized_shopping_list = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
  #  '10': []
}

routes = ['2468', '213468', '243579', '213568', '21356879', '21346578', '21347679']

poi = []

for item in shopping_list:
    categorized_shopping_list[category(item)].append(item)
    if category(item) in poi:
        continue
    else:
        poi.append(category(item))

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
            return route

route = router(poi)

print('The route:')

for i in route:
    for ing in categorized_shopping_list[i]:
        print(ing)


#Converts x,y coordinates from Photoshop into Turtles coordinates (Like coordinate system in math)
def converter(x, y):
    result = (x-600, 600-y)
    return result
coordinates = {
    '1': {'x': 214, 'y': 280},
    '2': {'x': 214, 'y': 653},
    '3': {'x': 466, 'y': 280},
    '4': {'x': 466, 'y': 653},
    '5': {'x': 657, 'y': 280},
    '6': {'x': 657, 'y': 653},
    '7': {'x': 844, 'y': 280},
    '8': {'x': 844, 'y': 653},
    '9': {'x': 1029, 'y': 280},
    '10': {'x': 1029, 'y': 653},

}

tr = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width=1200, height=1200)
wn.bgpic("kylis.png")

tr.up()
tr.setpos(-400, -550)
tr.down()

for coord in route:
    tr.setpos(converter(coordinates[coord]['x'], coordinates[coord]['y']))

tr.setpos(converter(940, 1015))



wn.mainloop()