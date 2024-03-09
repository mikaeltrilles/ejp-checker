# README.md

## EJP Checker

This script retrieves and displays the off-peak electricity days ("Jours EJP") from EDF's API. It also provides a notification if there is a change in the upcoming off-peak day.

### Utilisation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Téléchargez le script `ejp_checker.py`.
3. Installez les dépendances en exécutant la commande suivante dans le terminal :

```shell
pip install requests
```

4. Exécutez le script en utilisant la commande suivante :

```Shell
python3 ejp_checker.py
```


### Fonctionnement

Le script utilise la bibliothèque `requests` pour interroger l'API d'EDF et récupérer les informations sur les jours EJP. Les données sont ensuite traitées et affichées de manière lisible.

Le tableau des jours EJP est trié par date, les doublons sont supprimés, et seules les dates après le 1er novembre de l'année en cours moins un an sont conservées. Ensuite, le script affiche les jours EJP restants avant le 31 mars de l'année en cours.

Le dernier jour EJP est sauvegardé dans un fichier, et si ce dernier diffère du jour précédemment enregistré, une notification est affichée.

### Exemple d'utilisation

```bash
$ python ejp_checker.py
````

Liste des jours EJP depuis le 01/11/YYYY jusqu'au 31/03/YYYY :

05/12/YYYY : Jour EJP
...

Il reste X jours EJP avant le 31/03/YYYY
Dernier jour EJP : 05/12/YYYY
Prochain jour : 10/01/YYYY

## Remarques

Assurez-vous d'avoir les autorisations nécessaires pour afficher des notifications sur votre système d'exploitation.
Le script crée et utilise un fichier (lastEJP.txt) pour stocker la dernière date EJP afin de détecter les changements.
N'hésitez pas à contribuer ou à signaler des problèmes en ouvrant une issue.
