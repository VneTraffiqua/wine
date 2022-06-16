from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('index.html')
excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1', keep_default_na=False)
dict = excel_data_df.to_dict(orient='index')
vine_list = [dict[dic] for dic in dict]
grouped_vines = collections.defaultdict(list)
[grouped_vines[vine['Категория']].append(vine) for vine in vine_list]

rendered_page = template.render(
    age=datetime.date.today().year - 1920,
    vines=grouped_vines
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()