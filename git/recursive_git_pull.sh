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

    echo "Actualizando el repositorio de Git $repo_name en $repo_dir"
    
    # Verifica si la rama actual es development o develop antes de ejecutar git pull origin
    cd "$repo_dir"
    branch=$(git symbolic-ref --short HEAD)
    if [ "$branch" == "development" ] || [ "$branch" == "develop" ]
    then
        git pull origin $branch -v
    else
        echo "La rama actual en $repo_name no es development ni develop. Saltando la actualización."
    fi

    echo ""

    # Regresa al directorio raíz para continuar la búsqueda de repositorios
    cd - >/dev/null
done
