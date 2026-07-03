#!/bin/bash

# Tableau de ports
ports=(22 25 80 443 3306 8080)

# Parcours du tableau
for port in "${ports[@]}"
do
    case $port in
        22)
            echo "$port -> SSH"
            ;;
        80)
            echo "$port -> HTTP"
            ;;
        443)
            echo "$port -> HTTPS"
            ;;
        3306)
            echo "$port -> MySQL"
            ;;
        *)
            echo "$port -> Port inconnu"
            ;;
    esac
done
