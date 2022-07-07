from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections
import os
from dotenv import load_dotenv
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Разворачивает wine при запуске'
    )
    parser.add_argument(
        '-e',
        '--env_path',
        help='Укажите путь к файлу конфигурации',
        default='.env'
    )
    env_path = parser.parse_args()
    load_dotenv(env_path.env_path)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('base.html')
    excel_data_df = pandas.read_excel(
        os.getenv('FILE_PATH'), 
        sheet_name=os.getenv('SHEET_NAME'), 
        keep_default_na=False
    )
    wine_dict = excel_data_df.to_dict(orient='index')
    vine_list = [wine_dict[dic] for dic in wine_dict]
    grouped_vines = collections.defaultdict(list)
    [grouped_vines[vine['Категория']].append(vine) for vine in vine_list]

    rendered_page = template.render(
        age=datetime.date.today().year - int(os.getenv('WORKING_SINCE')),
        vines=grouped_vines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
