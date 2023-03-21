import os.path
from googletrans import Translator
import json
import sys

if len(sys.argv) != 2:
    print('Uso: python i18n/get_missing_translations.py <file_es.json>')
    exit(1)

# Rutas del archivo
json_file_es = sys.argv[1]

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

    except Exception as e:
        print(f'Error al traducir clave {key}: {e}')

print(json.dumps(en_data, ensure_ascii=False, indent=4))
