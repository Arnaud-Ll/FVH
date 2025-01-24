import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

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

buyers = {
    'Île-de-France': [
        ('IDF008', 10.4), ('IDF021', 3), ('IDF002', 2.9), ('IDF014', 6.1),
        ('IDF010', 14.4), ('IDF015', 3.7), ('IDF003', 6.5),
        ('IDF019', 19.3), ('IDF006', 1.1), ('IDF005', 0.8),
        ('IDF013', 3.3), ('IDF009', 6.9), ('IDF004', 12.1), ('IDF012', 9.5)
    ],
    'Auvergne-Rhône-Alpes': [
        ('ARA001', 20.5), ('ARA012', 19.5), ('ARA005', 60)
    ],
    'Bourgogne-Franche-Comté': [
        ('BFC007', 32.6), ('BFC002', 33.8), ('BFC009', 33.6)
    ],
    'Bretagne': [
        ('BRE015', 25.5), ('BRE003', 15.8), ('BRE006', 10.4),
        ('BRE010', 14.3), ('BRE012', 34)
    ],
    'Centre-Val de Loire': [
        ('CVL008', 49.5), ('CVL004', 50.5)
    ],
    'Grand Est': [
        ('GE007', 8.1), ('GE001', 3.2), ('GE010', 84.6), ('GE012', 4.1)
    ],
    'Hauts-de-France': [
        ('HDF005', 24.6), ('HDF007', 4.9), ('HDF013', 29.1),
        ('HDF002', 22.5), ('HDF011', 10.2), ('HDF003', 8.7)
    ],
    'Normandie': [
        ('NOR001', 74.9), ('NOR006', 25.1)
    ],
    'Nouvelle-Aquitaine': [
        ('NAQ009', 12.3), ('NAQ005', 19.5), ('NAQ013', 50.2), ('NAQ002', 18)
    ],
    'Occitanie': [
        ('OCC006', 12.4), ('OCC012', 6.8), ('OCC001', 14.2),
        ('OCC003', 9.8), ('OCC014', 13.3), ('OCC008', 11.5),
        ('OCC011', 14.9), ('OCC015', 5.6), ('OCC005', 11.5)
    ],
    'Pays de la Loire': [
        ('PDL003', 21.4), ('PDL008', 62.1), ('PDL015', 16.5)
    ],
    'Provence-Alpes-Côte d\'Azur': [
        ('PAC011', 11.8), ('PAC001', 13), ('PAC007', 14.1),
        ('PAC003', 19.3), ('PAC004', 2.4), ('PAC009', 24.6),
        ('PAC013', 14.8)
    ],
    'Corse': [
        ('COR002', 100)
    ]
}

annual_sales_quantities = {
    101: 6323909, 102: 3135204, 103: 2752526, 104: 709854,
    105: 400941, 106: 220285, 107: 201301, 108: 983508,
    109: 483707, 110: 659604, 111: 329439, 112: 144753,
    113: 88256, 114: 497282, 115: 191300, 116: 102764,
    117: 48594, 118: 164788, 119: 1523708, 120: 1439424,
    201: 2836862, 202: 3983359, 203: 506715, 204: 483480,
    205: 832106, 206: 170600, 207: 1639488, 208: 560875,
    209: 655277, 210: 365930, 211: 122080381, 212: 3029459,
    213: 173294, 214: 199799, 215: 165221, 216: 100739,
    217: 204507, 218: 69984, 219: 552997, 220: 477759,
    301: 294968, 302: 137966, 303: 183934, 304: 209246,
    305: 130072, 306: 799989, 307: 215094, 308: 124287,
    309: 80075, 310: 149989
}

region_distribution = {
    'Auvergne-Rhône-Alpes': 0.12, 'Bourgogne-Franche-Comté': 0.04, 'Bretagne': 0.05,
    'Centre-Val de Loire': 0.04, 'Corse': 0.01, 'Grand Est': 0.08, 'Hauts-de-France': 0.09,
    'Île-de-France': 0.2, 'Normandie': 0.05, 'Nouvelle-Aquitaine': 0.09, 
    'Occitanie': 0.09, 'Pays de la Loire': 0.06, 'Provence-Alpes-Côte d\'Azur': 0.08
}

seasonal_factors = {
    'Apple': [8.1, 6.5, 5.9, 4.7, 5.0, 4.8, 6.9, 7.8, 10.3, 14.6, 13.8, 11.6],
    'Banana': [7.9, 8.3, 7.8, 7.6, 8.1, 9.1, 9.3, 9.1, 7.9, 8.6, 8.3, 8.0],
    'Orange': [12.2, 11.6, 11.0, 9.0, 7.4, 8.0, 6.1, 6.4, 5.9, 6.9, 5.2, 10.3],
    'Pear': [5.1, 5.5, 6.2, 6.5, 7.1, 7.3, 7.0, 14.6, 13.6, 10.4, 10.2, 6.5],
    'Strawberry': [0.6, 1.1, 2.2, 12.1, 21.4, 20.3, 19.5, 13.3, 6.5, 1.1, 1.5, 0.4],
    'Apricot': [0.5, 0.9, 1.1, 1.1, 6.4, 19.2, 21.4, 26.4, 13.3, 5.6, 3.2, 0.9],
    'Grape': [1.5, 1.5, 1.0, 1.1, 2.6, 5.2, 9.8, 25.2, 23.8, 17.1, 10.2, 1.0],
    'Pineapple': [8.1, 7.4, 6.5, 8.2, 6.4, 9.9, 10.1, 10.2, 8.1, 9.2, 8.2, 7.7],
    'Peach': [0.5, 1.1, 1.5, 3.2, 7.4, 15.3, 25.1, 23.2, 14.8, 5.8, 2.0, 0.1],
    'Mango': [1.1, 1.0, 2.3, 4.3, 7.5, 14.9, 20.2, 29.9, 10.7, 4.1, 3.0, 1.0],
    'Papaya': [1.2, 1.6, 2.2, 4.5, 7.3, 10.1, 15.2, 24.5, 19.1, 9.5, 4.1, 0.7],
    'Litchi': [11.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.9, 5.5, 81.1],
    'Lemon': [5.2, 5.0, 6.0, 5.8, 8.1, 10.3, 12.2, 11.9, 10.7, 7.1, 6.2, 11.5],
    'Kiwi': [4.1, 4.7, 5.3, 5.5, 8.9, 9.9, 12.1, 15.5, 13.5, 10.2, 6.3, 4.0],
    'Raspberry': [0.6, 0.9, 2.0, 8.3, 15.1, 24.5, 19.9, 15.6, 7.1, 3.5, 2.1, 0.4],
    'Blueberry': [0.5, 0.8, 2.1, 7.5, 11.3, 25.0, 20.5, 15.9, 9.5, 5.1, 1.8, 0.0],
    'Pomegranate': [3.1, 3.6, 4.0, 5.1, 7.2, 9.8, 15.0, 20.1, 12.9, 10.1, 4.0, 5.1],
    'Melon': [1.1, 1.6, 3.3, 10.0, 19.9, 25.1, 19.8, 14.0, 6.2, 0.0, 0.0, 0.0],
    'Watermelon': [1.0, 1.3, 1.6, 3.1, 7.1, 26.0, 26.5, 22.3, 11.1, 0.0, 0.0, 0.0],
    'Carrot': [8.9, 8.9, 9.2, 8.1, 7.9, 6.8, 7.4, 7.4, 7.4, 9.1, 9.3, 9.6],
    'Tomato': [3.6, 4.1, 5.9, 9.9, 11.2, 13.5, 15.3, 12.6, 9.9, 7.6, 4.5, 1.9],
    'Cucumber': [2.1, 3.2, 4.3, 7.8, 15.2, 19.2, 18.9, 12.1, 9.1, 4.3, 1.6, 2.2],
    'Pepper': [1.3, 2.1, 3.4, 7.5, 16.4, 26.2, 22.4, 15.4, 4.1, 1.2, 0.0, 0.0],
    'Courgette': [2.3, 2.4, 5.1, 9.7, 13.3, 15.5, 13.1, 14.2, 6.9, 9.9, 5.3, 2.3],
    'Eggplant': [1.2, 1.8, 2.7, 5.4, 10.2, 20.6, 24.5, 18.5, 8.4, 5.0, 1.4, 0.3],
    'Spinach': [7.4, 4.3, 3.1, 2.2, 5.1, 8.1, 11.3, 14.5, 12.8, 11.2, 10.5, 9.5], 
    'Lettuce': [2.0, 2.5, 4.5, 8.0, 14.2, 15.8, 12.7, 12.5, 9.7, 8.5, 8.1, 1.5],
    'Broccoli': [6.2, 7.2, 7.5, 7.5, 8.7, 10.9, 9.8, 8.5, 7.2, 8.1, 9.6, 8.8],
    'Cabbage': [9.9, 8.8, 9.3, 6.4, 7.2, 9.1, 7.2, 6.1, 7.0, 8.4, 9.1, 11.5],
    'Potato': [8.5, 8.2, 9.0, 10.6, 9.0, 9.1, 8.3, 7.9, 8.2, 7.8, 6.0, 7.4],
    'Onion': [6.4, 5.5, 7.1, 8.6, 8.2, 12.2, 13.9, 10.8, 8.0, 6.9, 6.4, 5.9],
    'Garlic': [1.2, 1.4, 1.5, 1.3, 1.6, 1.8, 2.2, 3.0, 4.4, 5.1, 7.4, 9.1],
    'Beetroot': [9.8, 10.1, 7.5, 5.9, 4.5, 2.5, 4.2, 6.1, 7.3, 15.6, 14.5, 12.0],
    'Radish': [1.4, 2.5, 3.8, 5.1, 8.6, 9.9, 13.5, 15.5, 14.4, 13.2, 7.0, 5.1],
    'Turnip': [15.9, 16.5, 12.3, 9.0, 7.2, 5.1, 3.1, 2.0, 1.6, 4.9, 9.6, 12.8],
    'Squash': [10.9, 11.9, 10.2, 8.9, 7.3, 5.0, 2.6, 1.2, 3.2, 16.1, 10.3, 12.4],
    'Fennel': [5.8, 4.3, 5.8, 5.3, 9.9, 12.2, 12.8, 12.9, 13.1, 8.9, 5.1, 3.9],
    'Green Bean': [8.9, 7.3, 6.8, 8.0, 5.7, 7.3, 9.6, 12.3, 10.5, 7.9, 8.1, 7.6],
    'Corn': [3.3, 6.1, 4.5, 6.5, 8.1, 8.4, 9.3, 13.0, 12.1, 13.1, 9.3, 6.3],
    'Basil': [3.3, 5.1, 4.2, 4.6, 7.0, 13.6, 14.6, 19.4, 12.1, 8.8, 4.4, 2.9],
    'Thyme': [7.8, 8.3, 9.1, 5.7, 5.4, 6.6, 6.0, 7.4, 9.3, 7.9, 13.9, 12.6],
    'Rosemary': [1.8, 2.2, 3.0, 4.2, 4.2, 8.2, 12.4, 16.6, 18.0, 16.4, 8.8, 4.2],
    'Mint': [1.8, 2.4, 3.6, 4.8, 6.2, 8.2, 12.4, 19.2, 16.4, 11.6, 9.6, 3.8],
    'Dill': [1.2, 1.8, 3.0, 4.2, 6.2, 8.2, 9.0, 13.4, 19.4, 17.6, 8.4, 7.6],
    'Parsley': [1.4, 2.2, 3.0, 4.2, 5.8, 7.6, 11.6, 11.8, 16.2, 15.6, 12.2, 8.4],
    'Coriander': [1.8, 2.6, 3.8, 4.6, 6.0, 7.4, 11.4, 15.2, 16.2, 15.4, 11.0, 4.6],
    'Chives': [1.5, 2.5, 2.9, 4.6, 5.4, 7.6, 10.2, 15.2, 20.2, 14.6, 11.2, 4.1],
    'Tarragon': [3.5, 5.2, 4.1, 4.2, 5.9, 8.4, 9.6, 12.6, 16.9, 12.6, 9.4, 7.6],
    'Oregano': [1.3, 1.8, 3.4, 4.9, 6.8, 10.1, 14.1, 12.1, 19.8, 11.3, 9.5, 4.9]
 }

# Buyer selection function
def select_buyer(region):
    clients, weights = zip(*buyers[region])
    return random.choices(clients, weights=weights, k=1)[0]

# Database generation
def generate_database(start_date, end_date):
    data = []
    current_date = start_date
    last_month = start_date.month  # Track the initial month

    while current_date <= end_date:
        # Check for new month and adjust prices
        if current_date.month != last_month:
            last_month = current_date.month  # Update the month tracker
            for category, items in products.items():
                for product_name, (product_id, base_price) in items.items():
                    # Price modulation each month
                    increment_percentage = np.random.choice([random.uniform(0.995, 1.0075),random.uniform(0.985, 1.0175),random.uniform(0.955, 1.0625),random.uniform(0.92, 1.085)],p=[0.65, 0.20, 0.10, 0.05])
                    actualized_price = round(base_price * increment_percentage, 2)
                    products[category][product_name] = (product_id, actualized_price)

        if current_date.weekday() == 6:  # Chill on sunday no work :)
            current_date += timedelta(days=1)
            continue

        for category, items in products.items():
            for product_name, (product_id, actualized_price) in items.items():
                if random.random() > 0.75:
                    continue

                purchase_price = float(round(actualized_price * np.random.choice([random.uniform(0.84, 1.08),random.uniform(0.80, 1.16),random.uniform(0.76, 1.22),random.uniform(0.50, 1.50)],p=[0.50, 0.30, 0.15, 0.05]), 2))

                # Define sale_price with margin based on category
                if category == 'Fruits':
                    sale_price = float(round(purchase_price * np.random.choice(
                        [random.uniform(0.95, 1.50), random.uniform(0.95, 1.85), random.uniform(2.00, 3.00), random.uniform(0.5, 1)],
                        p=[0.50, 0.35, 0.10, 0.05]
                    ), 2))
                elif category == 'Vegetables':
                    sale_price = float(round(purchase_price * np.random.choice(
                        [random.uniform(0.98, 1.45), random.uniform(0.96, 1.75), random.uniform(1.75, 2.75), random.uniform(0.8, 1.00)],
                        p=[0.50, 0.35, 0.10, 0.05]
                    ), 2))
                elif category == 'Herbs':
                    sale_price = float(round(purchase_price * np.random.choice(
                        [random.uniform(1.50, 2.00), random.uniform(2.00, 7.00), random.uniform(3.00, 15.00), random.uniform(0.75, 1.25)],
                        p=[0.50, 0.30, 0.15, 0.05]
                    ), 2))
                
                # Calculate the seasonal factor for the product and month
                month_index = current_date.month - 1  # 0 for January, 11 for December
                seasonal_factor = seasonal_factors.get(product_name, [1] * 12)[month_index] / 100

                # Adjust daily sales quantity using seasonal factor and days in the month
                days_in_month = (current_date.replace(day=28) + timedelta(days=4)).day  # Finds last day of the month
                daily_sales_quantity = round(annual_sales_quantities[product_id] * seasonal_factor / days_in_month * np.random.choice([random.uniform(0.75, 1.25), random.uniform(0.75, 2), random.uniform(1.5, 3), random.uniform(2, 10)], p=[0.35, 0.35, 0.25, 0.05]), 2)

                for region, region_percentage in region_distribution.items():
                    region_quantity = daily_sales_quantity * region_percentage

                    for buyer, buyer_percentage in buyers[region]:
                        quantity_purchased = int(region_quantity * (buyer_percentage / 100) / 30)
                        quantity_sold = int(round(quantity_purchased * np.random.choice([random.uniform(0.99, 1),random.uniform(0.95, 0.99),random.uniform(0.90, 0.95),random.uniform(0.5, 0.9)],p=[0.5, 0.4, 0.09, 0.01]), 0))
                        

                        data.append({
                            "Purchase Date": current_date.strftime('%Y-%m-%d'), "Product ID": product_id,
                            "Quantity Purchased (kg)": quantity_purchased, "Purchase Price": purchase_price,
                            "Quantity Sold (kg)": quantity_sold, "Sale Price": sale_price,
                            "Buyer ID": buyer
                        })

        current_date += timedelta(days=1)

    df = pd.DataFrame(data)

    df = df[df["Quantity Purchased (kg)"] > 0]

    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], format='%Y-%m-%d')

    return df


# Dates selection
start_date = datetime(2000, 1, 1)
end_date = datetime(2024, 12, 31)

df_database = generate_database(start_date, end_date)

df_database.to_csv('Sales_database_2000_2024.csv', index=False, encoding='utf-8-sig')