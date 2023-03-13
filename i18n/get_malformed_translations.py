#!/usr/bin/python3

import json
import sys

if len(sys.argv) != 2:
    print('Uso: python i18n/get_malformed_translations.py <file.json>')
    exit(1)

json_file = sys.argv[1]

with open(json_file, 'r') as f:
    data = json.load(f)

for key in data.keys():
    if key.count('.') >= 3:
        print(key)