#!/usr/bin/python3

import json
import sys

if len(sys.argv) != 2:
    print('Uso: python i18n/change_flat_to_nested_translations.py <file.json>')
    exit(1)

json_file = sys.argv[1]

with open(json_file, 'r') as f:
    data = json.load(f)


def add_to_nested_dict(nested_dict, keys, value):
    key = keys.pop(0)
    if not keys:
        nested_dict[key] = value
    else:
        nested_dict[key] = add_to_nested_dict(
            nested_dict.get(key, {}), keys, value)
    return nested_dict


nested_dict = {}
for key, value in data.items():
    keys = key.split(".")
    add_to_nested_dict(nested_dict, keys, value)

print(json.dumps(nested_dict, indent=4))
