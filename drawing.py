import turtle
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

for coord in ['2', '1', '3', '4', '6', '5', '7', '8', '10']:
    tr.setpos(converter(coordinates[coord]['x'], coordinates[coord]['y']))

tr.setpos(converter(940, 1015))



wn.mainloop()