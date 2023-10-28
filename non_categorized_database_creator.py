import json

from bs4 import BeautifulSoup

final_product = {}

files = ['hedelmat-ja-vihannekset',
         'juomat',
         'kodinhoito-ja-taloustarvikkeet',
         'kodintekstiilit-ja-sisustus',
         'kosmetiikka-terveys-ja-hygienia',
         'kuivat-elintarvikkeet-ja-leivonta',
         'leivat-keksit-ja-leivonnaiset',
         'liha-ja-kasviproteiinit',
         'maito-juusto-munat-ja-rasvat',
         'makeiset-ja-naposteltavat',
         'pakasteet',
         'sailykkeet-keitot-ja-ateria-ainekset',
         'texmex-ja-maailman-maut',
         'valmisruoka'
         ]

for filename in files:

    with open(f'data/{filename}.txt', 'r') as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')

        category_object = {}

        for product in soup.find_all('a'):

            title = product['title']

            href = product['href']

            ean = href[len(href) - 13:]

        # Object representation
            # product_object = {
            #     'ean': ean,
            #     'title': title,
            #     'href': href,
            #     'category': filename
            # }

            final_product[title] = ean


with open('data/non_categorized_database.txt', 'w') as html_doc:

    html_doc.write(json.dumps(final_product))
