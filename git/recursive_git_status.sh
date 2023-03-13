#!/bin/bash

# Verifica si se proporcionó un argumento
if [ $# -eq 0 ]
  then
    echo "Debe proporcionar un directorio como argumento"
    exit 1
fi

# Verifica si el directorio proporcionado es válido
if [ ! -d "$1" ]
  then
    echo "$1 no es un directorio válido"
    exit 1
fi

# Recorre el directorio de manera recursiva
for dir in $(find "$1" -type d -name ".git")
do
    # Obtiene el nombre del repositorio actual
    repo_dir=$(dirname "$dir")
    repo_name=$(basename "$repo_dir")

    # Obtiene la rama actual
    cd "$repo_dir"
    branch=$(git symbolic-ref --short HEAD)

    # Verifica si hay cambios pendientes de hacer commit
    if git status --porcelain | grep -q "^M\|^ M\|^A\|^D\|^R\|^C\|^U"; then
        changes="Sí"
    else
        changes="No"
    fi

    echo "$repo_name"
    echo "    Rama actual: $branch"
    echo "    Cambios pendientes de hacer commit: $changes"
    echo ""

    # Regresa al directorio raíz para continuar la búsqueda de repositorios
    cd - >/dev/null
done
