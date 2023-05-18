import PySimpleGUI as psg

layout = [[psg.Text('Your moms a hoe')]]

window = psg.Window('window', layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])