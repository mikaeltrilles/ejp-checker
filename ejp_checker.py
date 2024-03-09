import requests
from datetime import datetime

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "particulier.edf.fr",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"
}

response = requests.get("https://particulier.edf.fr/services/rest/referentiel/historicEJPStore?searchType=ejp", headers=headers)
data = response.json()
print("Liste des jours EJP depuis le 01/11/" + str(datetime.now().year - 1) + " jusqu'au 31/03/" + str(datetime.now().year) + " :")
print("")

# Je boucle sur le tableau et recrée un tableau avec les données que je veux : un tableau associatif avec la date et le statut
tab = []
for i in data['listeEjp']:
    tab.append({'date': i['dateApplication'], 'statut': i['statut']})

# Je trie le tableau par date
tab.sort(key=lambda x: x['date'])

# Je supprime les doublons
tab = [i for n, i in enumerate(tab) if i not in tab[n + 1:]]

# Je convertis le timestamp en date et j'affiche le jour devant la date
for i in tab:
    i['date'] = datetime.fromtimestamp(int(i['date']) / 1000).strftime("%d/%m/%Y")


# Je supprime les dates antérieures au 01 novembre de l'année en cours moins 1
tab = [i for i in tab if datetime.strptime(i['date'], "%d/%m/%Y") >= datetime.strptime("01/11/" + str(datetime.now().year - 1), "%d/%m/%Y")]

# Je boucle sur le tableau et j'affiche les données, la dernière ligne est en rouge et je supprime les doublons
for i in tab:
    if i == tab[-1]:
        print("\033[91m" + i['date'] + " : " + i['statut'] + "\033[0m")
    else:
        print(i['date'] + " : " + i['statut'])

# Je saute une ligne
print("")

# J'indique le nombre de jours EJP restant avant le 31 mars, sachant que le total est de 22 jours entre le 1er novembre et le 31 mars
print("Il reste " + str(22 - len(tab)) + " jours EJP avant le 31/03/" + str(datetime.now().year))

# Je récupère le dernier jour EJP du tableau et le sauvegarde dans un fichier
lastEJP = tab[-1]['date']
# with open('/Users/mikaeltrilles/Documents/lastEJP.txt', 'w') as f:
#     f.write(lastEJP)

# Je récupère le dernier jour EJP du fichier
with open('/Users/mikaeltrilles/Documents/lastEJP.txt', 'r') as f:
    lastEJPFile = f.read()

# Je compare le dernier jour EJP du fichier avec le dernier jour EJP du tableau
print("Dernier jour EJP : " + lastEJPFile)
print("Prochain jour : " + lastEJP)
print("")

if lastEJP != lastEJPFile:
    # S'il y a un changement, j'affiche une popup pendant 20 secondes sur le système d'exploitation
    import os
    os.system("osascript -e 'display notification \"🔴 Demain est un jour rouge : " + lastEJP + "\" with title \"EJP\"'")

    # Je sauvegarde le dernier jour EJP dans le fichier
    with open('/Users/mikaeltrilles/Documents/lastEJP.txt', 'w') as f:
        f.write(lastEJP)

# Je contrôle l'API tous les jours à 17h00 pour voir s'il y a des changements.
# Si