import csv
import json

def convert_to_number(number):
    number = number.strip()
    return int(number) if number else 0

def convert_to_json():
    item_data = {}
    mat_data = {}

    with open('./data/items.csv', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['Item']
            item = {
                "Type" : rows['Type'],
                "Bmats" : convert_to_number(rows['BMats']),
                "Rmats" : convert_to_number(rows['RMats']),
                "Emats" : convert_to_number(rows['EMats']),
                "HEmats" : convert_to_number(rows['HEMats']),
                "Per Crate" : convert_to_number(rows['Per Crate'])
            }
            item_data[key] = item
    
    with open('./data/items.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(item_data, indent=4))

    with open('./data/materials.csv', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['Material']
            item = {
                "aka" : rows['aka'],
                "Resource" : rows['Raw Resource'],
                "Per Stack" : convert_to_number(rows['Per Stack']),
                "Per Crate" : convert_to_number(rows['Per Crate']),
                "Conversion Rate" : convert_to_number(rows['Conversion Rate'])
            }
            mat_data[key] = item
    
    with open('./data/materials.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(mat_data, indent=4))

if __name__ == '__main__':
    convert_to_json()