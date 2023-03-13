#!/usr/bin/python3

import json
import sys

if len(sys.argv) != 3:
    print('Uso: python i18n/get_missing_translations.py <file_es.json> <file_en.json>')
    exit(1)

json_file_es = sys.argv[1]
json_file_en = sys.argv[2]

with open(json_file_es, 'r') as f:
    es_translations = json.load(f)

with open(json_file_en, 'r') as f:
    en_translations = json.load(f)

# Llaves faltantes en el archivo en.json
missing_in_en = set(es_translations.keys()) - set(en_translations.keys())
print(f'Llaves faltantes en el archivo {json_file_en}:')
print(missing_in_en)

# Llaves faltantes en el archivo es.json
missing_in_es = set(en_translations.keys()) - set(es_translations.keys())
print(f'Llaves faltantes en el archivo {json_file_es}:')
print(missing_in_es)
