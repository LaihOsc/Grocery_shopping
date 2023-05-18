import PySimpleGUI as sg
import os
from yeet import find_products
from yeet2 import get_ean_by_name
import urllib.request
from PIL import Image
def get_list():
    query = ''

    current = []

    sg.theme('DarkAmber')

    file_list_column = [
        [
            sg.Text('Product name'),
            sg.In(size=(25, 1), enable_events=True, key='-query-'),
            sg.Button('Search' ,key='-update-')
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key='-product_list-'
            )
        ]
    ]

    image_column =[
        [sg.Text(size=(40, 1), key="-product_name")],
        [sg.Image(key='-image-', size=(10, 10))],
        [sg.Button('Add to basket' ,key='-add_to_cart-')]
    ]

    shopping_cart_column = [
        [sg.Text('Shopping Basket'), sg.Button('Remove from basket', key='-remove-')],
        [sg.Listbox(values=[], enable_events=True, size=(40, 20), key='-basket-')],
        [sg.Button('Show map', key='-show_map-')]
    ]

    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_column),
            sg.VSeperator(),
            sg.Column(shopping_cart_column),
        ]
    ]

    window = sg.Window('picture', layout)
    while True:
        event, values = window.read()
        print(event, values)

        if event == '-query-':
            query = values['-query-']
            print(query)

        if event == '-update-':
            product_names = [product['title'] for product in find_products(values['-query-'])]
            window['-product_list-'].update(values=product_names)

        if event == '-product_list-':
            name = values['-product_list-'][0]
            urllib.request.urlretrieve(
                f'https://public.keskofiles.com/f/k-ruoka/product/{get_ean_by_name(name)}',
                "pic.png")
            pic = Image.open("pic.png")

            newsize = (300, 300)
            pic = pic.resize(newsize)
            pic = pic.save("pic.png")
            window['-image-'].update(filename="pic.png")

        if event == '-add_to_cart-':

            current.append(values['-product_list-'][0])
            print('yeet', current)

            window['-basket-'].update(values=current)

        if event == '-remove-':
            current.remove(values['-basket-'][0])
            window['-basket-'].update(values=current)

        if event == '-show_map-':
            return [get_ean_by_name(item) for item in current]
            break


        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
    window.close()
