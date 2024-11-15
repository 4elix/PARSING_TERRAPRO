import re
import json


def write_json(name, obj):
    with open(f'{name}.json', mode='w', encoding='utf-8') as file:
        json.dump(obj, file, indent=4, ensure_ascii=False)


def read_json(name):
    with open(f'{name}.json', mode='r', encoding='utf-8') as file_1:
        return json.load(file_1)


def change_link_for_photo(url):
    test = re.sub(' ', '%20', url)
    return test


def change_price(old_price):
    step_first = old_price.replace('\xa0', '')
    step_second = step_first.replace(' UZS', '')
    return step_second


def start_func(obj_cat, class_product):
    lis = []
    for item in obj_cat:
        main_index = item['main_index']
        for sub_cat in item['sub_data']:
            sub_index = sub_cat['sub_index']
            sub_link = sub_cat['sub_link']
            data = class_product.get_data_product(f'https://terrapro.uz{sub_link}', main_index, sub_index)
            lis += data
    return lis
