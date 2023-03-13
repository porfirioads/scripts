import os.path
from googletrans import Translator
import json
import sys

if len(sys.argv) != 2:
    print('Uso: python i18n/get_missing_translations.py <file_es.json>')
    exit(1)

# Rutas de los archivos
json_file_es = sys.argv[1]
json_file_en = os.path.splitext(json_file_es)[0] + '_en.json'

if os.path.isfile(json_file_en):
    with open(json_file_en, 'r', encoding='utf-8') as f:
        en_data = json.load(f)
else:
    en_data = {}

# Cargar archivo en español
with open(json_file_es, 'r', encoding='utf-8') as f:
    es_data = json.load(f)

# Inicializar el traductor
translator = Translator()
translator.raise_Exception = True

# Traducir las claves faltantes al inglés
for key in es_data.keys():
    try:
        # Comprobar si la clave ya existe en el archivo en inglés
        if key in en_data:
            continue

        # Traducir el valor de la clave al inglés
        translation = translator.translate(
            es_data[key], dest='en', src='es').text

        # Guardar la traducción en el archivo en inglés
        en_data[key] = translation
        with open(json_file_en, 'w', encoding='utf-8') as f:
            json.dump(en_data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f'Error al traducir clave {key}: {e}')
