#!/bin/bash

# Obtiene las opciones del menú del archivo package.json
options=($(jq -r '.dependencies | keys[]' package.json | grep '^@trackchain'))

# Si no se encontraron opciones, muestra un mensaje y sale
if [ ${#options[@]} -eq 0 ]; then
    echo "No se encontraron dependencias de @trackchain en el archivo package.json"
    exit 1
fi

# Agrega la opción "Salir"
options+=("Salir")

# Define la función para mostrar el menú y recibir la selección del usuario
function show_menu {
    tput civis # Oculta el cursor
    clear # Limpia la pantalla
    echo "Selecciona una opción:"
    for i in "${!options[@]}"; do
        if [ $i -eq $(( $selection - 1 )) ]; then
            echo -e "\033[32m>>> $((i+1))) ${options[$i]}\033[0m"
        else
            echo "    $((i+1))) ${options[$i]}"
        fi
    done
}

# Inicializa la selección del usuario
selection=1

# Muestra el menú por primera vez
show_menu

# Loop principal
while true; do
    # Espera la entrada del usuario y guarda el código ASCII de la tecla presionada
    read -s -n 1 key
    case $key in
        A) # Flecha arriba
            ((selection--))
            if [ $selection -lt 1 ]; then
                selection=${#options[@]}
            fi
            show_menu
            ;;
        B) # Flecha abajo
            ((selection++))
            if [ $selection -eq $(( ${#options[@]} + 1 )) ]; then
                selection=1
            fi
            show_menu
            ;;
        "") # Enter
            if [ $selection -eq ${#options[@]} ]; then
                tput cnorm # Muestra el cursor
                clear # Limpia la pantalla antes de salir
                exit 0 # Salir del script
            else
                echo "Seleccionaste la opción ${options[$((selection-1))]}"
                # Agrega el código para realizar la acción correspondiente a la opción seleccionada
                # ...
                # ...
                echo "Presiona cualquier tecla para continuar..."
                read -n 1 -s # Espera a que el usuario presione cualquier tecla para continuar
                show_menu # Vuelve a mostrar el menú
            fi
            ;;
        *) # Cualquier otra tecla
            ;;
    esac
done
