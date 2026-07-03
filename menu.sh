#!/bin/bash

choix=0

while [ "$choix" -ne 4 ]
do
    echo "===================="
    echo "        MENU"
    echo "===================="
    echo "1. Afficher la date et l'heure"
    echo "2. Afficher les utilisateurs connectés"
    echo "3. Afficher l'espace disque disponible"
    echo "4. Quitter"
    echo "===================="
    echo -n "Votre choix : "
    read choix

    case $choix in
        1)
            date
            ;;
        2)
            who
            ;;
        3)
            df -h
            ;;
        4)
            echo "Fin du programme."
            ;;
        *)
            echo "Choix invalide."
            ;;
    esac

    echo ""
done
