#!/bin/bash

# Función recursiva para eliminar dist
function eliminar_dist {
    local dir="$1"

    # Verificar si el directorio existe
    if [ -d "$dir" ]; then
        echo "Eliminando dist en: $dir"
        find "$dir" -type d -name "dist" -exec sudo rm -rf {} +
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
eliminar_dist "$1"
