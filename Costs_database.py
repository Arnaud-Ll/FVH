import pandas as pd

regions = [
    "Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Bretagne", "Centre-Val de Loire", 
    "Corse", "Grand Est", "Hauts-de-France", "Île-de-France", "Normandie", 
    "Nouvelle-Aquitaine", "Occitanie", "Pays de la Loire", "Provence-Alpes-Côte d'Azur"
]

fixed_cost = [1000] * len(regions)
variable_cost_per_region = [
    "7.1%", "8.3%", "9.4%", "6.1%", "14.8%", "9.4%", "8.1%", "5.7%", "8.9%", 
    "8.5%", "10.2%", "8.4%", "12.8%"
]
variable_cost_herbs = ["12.43%"] * len(regions)
variable_cost_fruits = ["10.85%"] * len(regions)
variable_cost_vegetables = ["8.13%"] * len(regions)

data = {
    "Region": regions,
    "Fixed cost": fixed_cost,
    "Variable cost per region": variable_cost_per_region,
    "Variable cost - Herbs": variable_cost_herbs,
    "Variable cost - Fruits": variable_cost_fruits,
    "Variable cost - Vegetables": variable_cost_vegetables
}

df = pd.DataFrame(data)

df.to_csv('Costs_database.csv', index=False, encoding='utf-8-sig')