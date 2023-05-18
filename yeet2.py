import json

with open('data/database2.txt', 'r') as data2:
    y2 = json.load(data2)
    def get_ean_by_name(ean):

        return y2[ean]

