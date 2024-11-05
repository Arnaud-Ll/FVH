import pandas as pd

products = {
    'Fruits': {
        'Apple': (101, 1.54), 'Banana': (102, 1.25), 'Orange': (103, 1.58), 'Pear': (104, 1.98),
        'Strawberry': (105, 2.25), 'Apricot': (106, 2.41), 'Cherry': (107, 5.46), 'Grape': (108, 2.12),
        'Pineapple': (109, 1.78), 'Peach': (110, 2.12), 'Mango': (111, 3.41), 'Papaya': (112, 3.89),
        'Lychee': (113, 4.26), 'Lemon': (114, 1.50), 'Kiwi': (115, 2.01), 'Raspberry': (116, 4.05),
        'Blueberry': (117, 3.91), 'Pomegranate': (118, 3.05), 'Melon': (119, 1.45), 'Watermelon': (120, 1.02)
    },
    'Vegetables': {
        'Carrot': (201, 1.02), 'Tomato': (202, 1.99), 'Cucumber': (203, 1.50), 'Bell Pepper': (204, 2.09),
        'Zucchini': (205, 1.45), 'Spinach': (206, 2.12), 'Lettuce': (207, 1.00), 'Broccoli': (208, 2.10),
        'Cabbage': (209, 0.69), 'Eggplant': (210, 1.82), 'Potato': (211, 0.89), 'Onion': (212, 1.11),
        'Garlic': (213, 2.72), 'Beet': (214, 1.09), 'Radish': (215, 1.51), 'Turnip': (216, 0.72),
        'Squash': (217, 0.83), 'Fennel': (218, 1.54), 'Green Bean': (219, 2.21), 'Corn': (220, 1.49)
    },
    'Herbs': {
        'Basil': (301, 16.32), 'Thyme': (302, 11.45), 'Rosemary': (303, 10.21), 'Mint': (304, 14.35),
        'Dill': (305, 12.16), 'Parsley': (306, 7.85), 'Cilantro': (307, 16.54), 'Chive': (308, 10.21),
        'Tarragon': (309, 17.19), 'Oregano': (310, 11.95)
    }
}

data = []

for category, items in products.items():
    for product_name, (product_id, base_price) in items.items():
        data.append({"Product ID": product_id, "Product Name": product_name, "Category": category})

df_products = pd.DataFrame(data)

df_products.to_csv('Products_database_en.csv', index=False, encoding='utf-8-sig')