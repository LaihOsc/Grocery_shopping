import json

with open('data/categorized_database.txt', 'r') as data:
    y = json.load(data)


    def find_products(query):
        results = []
        for category in y.keys():
            for product in y[category]:
                if query.lower() in y[category][product]['title'].lower():
                    results.append(y[category][product])

        return results


    def get_product_object_by_ean(ean):
        for category in y.values():
            for product in category:
                if product == ean:
                    return category[product]


    def get_product_object_by_name(query):
        for category in y.keys():
            for product in y[category]:
                if query.lower() in y[category][product]['title'].lower():
                    return y[category][product]


    def get_coordinate_by_category(category):
        return category_coordinates[category]

category_coordinates = {
    'hedelmat-ja-vihannekset': 'b5',
    'juomat': 'h2',
    'kodinhoito-ja-taloustarvikkeet': 'g3',
    'kodintekstiilit-ja-sisustus': 'h3',
    'kosmetiikka-terveys-ja-hygienia': 'h3',
    'kuivat-elintarvikkeet-ja-leivonta': 'a6',
    'leivat-keksit-ja-leivonnaiset': 'd3',
    'liha-ja-kasviproteiinit': 'a4',
    'maito-juusto-munat-ja-rasvat': 'i3',
    'makeiset-ja-naposteltavat': 'j2',
    'pakasteet': 'j3',
    'sailykkeet-keitot-ja-ateria-ainekset': 'e2',
    'texmex-ja-maailman-maut': 'b6',
    'valmisruoka': 'b7',
}
