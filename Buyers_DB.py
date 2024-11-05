import pandas as pd

buyers_data = {
    'Île-de-France': [
        ('Transit MKT', 'IDF008'), ('Jordans', 'IDF021'), ('Demba LLC', 'IDF002'), ('Garnashy Solutions', 'IDF014'),
        ('Velkt Inc', 'IDF010'), ('MLTP', 'IDF015'), ('Portal Services', 'IDF003'), ('OMGG Group', 'IDF019'),
        ('PLH', 'IDF006'), ('Veentures', 'IDF005'), ('Dumont Gros', 'IDF013'), ('Mu-u', 'IDF009'),
        ('Nuyh', 'IDF004'), ('Toureifels', 'IDF012')
    ],
    'Auvergne-Rhône-Alpes': [
        ('Vortex', 'ARA001'), ('Mondaur', 'ARA012'), ('Clearmount', 'ARA005')
    ],
    'Bourgogne-Franche-Comté': [
        ('RedWine SLA', 'BFC007'), ('Deejoon', 'BFC002'), ('Aruit SSC', 'BFC009')
    ],
    'Bretagne': [
        ('Kreps', 'BRE015'), ('BRST', 'BRE003'), ('GGT Solutions', 'BRE006'), 
        ('BRZ HL', 'BRE010'), ('MLE', 'BRE012')
    ],
    'Centre-Val de Loire': [
        ('Loire Trans', 'CVL008'), ('NeTech', 'CVL004')
    ],
    'Grand Est': [
        ('Aptions', 'GE007'), ('Koya LTD', 'GE001'), ('Applepears', 'GE010'), ('SUES', 'GE012')
    ],
    'Hauts-de-France': [
        ('SHTI', 'HDF005'), ('LOK', 'HDF007'), ('Aurora', 'HDF013'), 
        ('Elemental Services', 'HDF002'), ('Geny', 'HDF011'), ('Stratosphere Solutions', 'HDF003')
    ],
    'Normandie': [
        ('Horizon', 'NOR001'), ('WINN', 'NOR006')
    ],
    'Nouvelle-Aquitaine': [
        ('Burdo', 'NAQ009'), ('AKKITn', 'NAQ005'), ('QuantumL', 'NAQ013'), ('RdTS', 'NAQ002')
    ],
    'Occitanie': [
        ('Phoenix', 'OCC006'), ('Matrix', 'OCC012'), ('TrT', 'OCC001'), 
        ('Unity Group', 'OCC003'), ('Nimbus', 'OCC014'), ('Equinox', 'OCC008'), 
        ('Oldingz', 'OCC011'), ('TerNova', 'OCC015'), ('Elemics', 'OCC005')
    ],
    'Pays de la Loire': [
        ('BlueSky', 'PDL003'), ('Oakwood PRT', 'PDL008'), ('Tranquil Solutions', 'PDL015')
    ],
    'Provence-Alpes-Côte d\'Azur': [
        ('RSPP', 'PAC011'), ('Cuiklers', 'PAC001'), ('EM EMT', 'PAC007'), 
        ('SuMM', 'PAC003'), ('Silverline', 'PAC004'), ('Zons', 'PAC009'), 
        ('Mitchells', 'PAC013')
    ],
    'Corse': [
        ('Island Frets', 'COR002')
    ]
}

data = []
for region, buyers in buyers_data.items():
    for buyer, buyer_id in buyers:
        data.append({"Buyer ID": buyer_id, "Buyer": buyer, "Region": region})

df_buyers = pd.DataFrame(data)

df_buyers.to_csv('Buyers_database.csv', index=False, encoding='utf-8-sig')
