from parser import CategoryManager, website_html, ProductManager
from support import start_func, write_json

if __name__ == '__main__':
    print('start')
    category_manager = CategoryManager(website_html)
    product_manager = ProductManager()

    data_categories = category_manager.get_data_categories()
    category_manager.write_category('categories', data_categories)

    data_products = start_func(data_categories, product_manager)
    write_json('p', data_products)
