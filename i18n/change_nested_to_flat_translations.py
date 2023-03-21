#!/usr/bin/python3

import json
import sys

if len(sys.argv) != 2:
    print('Uso: python i18n/change_flat_to_nested_translations.py <file.json>')
    exit(1)

json_file = sys.argv[1]

with open(json_file, 'r') as f:
    data = json.load(f)

flat_dict = {}


def flatten_dict(d, parent_key=""):
    for key, value in d.items():
        new_key = parent_key + "." + key if parent_key else key
        if isinstance(value, dict):
            flatten_dict(value, new_key)
        else:
            flat_dict[new_key] = value


flatten_dict(data)
print(json.dumps(flat_dict, indent=4))
