from base import base_config
from support import write_json, change_link_for_photo, change_price

website_html = base_config.base_connect()


class CategoryManager:
    def __init__(self, content):
        self.content = content

    def get_data_categories(self):
        categories = []
        main_index = 0
        list_category = self.content.find('div', class_='i-menu i-menu-catalog')
        items_list_category = list_category.find_all('div', class_='i-menu-item')
        for item in items_list_category:
            main_title = item.find('span', class_='t-menu').get_text(strip=True)
            sub_index = 0
            main_index += 1
            list_sub = []
            list_sub_category = item.find('ul').find_all('li')
            for item_sub in list_sub_category:
                sub_title = item_sub.find('a').get_text(strip=True)
                sub_link = item_sub.find('a')['href']
                sub_index += 1

                list_sub.append(
                    {
                        'sub_index': sub_index,
                        'sub_title': sub_title,
                        'sub_link': sub_link
                    }
                )
            categories.append({
                'main_title': main_title,
                'main_index': main_index,
                'sub_data': list_sub
            })
        return categories

    def write_category(self, name, category):
        write_json(name, category)


class ProductManager:
    def get_data_product(self, *args):
        data_products = []

        path, main_index, sub_index = args
        html_page = base_config.custom_connect(path)
        main_block = html_page.find('div', class_='i-grid')
        cards = main_block.find_all('div', class_='i-card-swiper')
        for card in cards:
            title = card.find('p', class_='i-card-name').find('a').get_text(strip=True)
            price = change_price(card.find('span', class_='i-card-price_current').get_text(strip=True))
            img = change_link_for_photo(
                'https://terrapro.uz' + card.find('a', class_='i-card-photo').find('img')['data-src'])
            size = ', '.join(
                [item.get_text(strip=True) for item in card.find('ul', class_='i-card-sizes').find_all('label')])
            data_products.append({
                'title': title,
                'price': price,
                'img': img,
                'size': size,
                'main_index': main_index,
                'sub_index': sub_index,
            })

        return data_products

