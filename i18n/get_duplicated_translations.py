#!/usr/bin/python3

import json
import sys

if len(sys.argv) != 2:
    print('Uso: python i18n/get_duplicated_translations.py <file.json>')
    exit(1)

json_file = sys.argv[1]

with open(json_file, 'r') as f:
    data = json.load(f)

values = {}
duplicates = {}

for key, value in data.items():
    if value in values:
        if value in duplicates:
            duplicates[value].append(key)
        else:
            duplicates[value] = [values[value], key]
    else:
        values[value] = key

if duplicates:
    print("Traducciones duplicadas encontradas:\n")
    for value, keys in duplicates.items():
        print(f"{value}: {json.dumps(keys, indent=4)}\n")
else:
    print("No se encontraron traducciones duplicadas.")
