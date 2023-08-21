#!/bin/bash

# Función recursiva para eliminar angular
function eliminar_angular {
    local dir="$1"

    # Verificar si el directorio existe
    if [ -d "$dir" ]; then
        echo "Eliminando angular en: $dir"
        find "$dir" -type d -name "angular" -exec sudo rm -rf {} +
    else
        echo "Directorio no encontrado: $dir"
    fi
}

# Comprobar si se proporcionó un argumento
if [ $# -eq 0 ]; then
    echo "Uso: $0 directorio"
    exit 1
fi

# Llamar a la función con el directorio proporcionado como argumento
eliminar_angular "$1"
