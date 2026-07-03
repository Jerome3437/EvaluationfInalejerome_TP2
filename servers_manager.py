#===========================#
#Chargement du fichier JSON#
#===========================#

import json

with open("servers.json", "r", encoding="utf-8") as fichier:
    serveurs = json.load(fichier)

print(serveurs)

#===========================#
# Afficher les 12 noms de serveurs et leurs status
#===========================#

for serveur in serveurs:
	print(serveur["name"])

#==========================#
# Afficher les serveurs dont le cpu_usage est supérieur à 80% 
#==========================#
print("Serveurs à surveiller (CPU > 80%) :\n")

for serveur in serveurs:
    if serveur["cpu_usage"] > 80:
        print(serveur['name'], "--", serveur['cpu_usage'],"%")

#=========================#
#Filter et afficher les serveurs dont le status est "down"
#=========================#

for serveur in serveurs:

	if serveur["status"] == "down":

		print(serveur["name"], "--", serveur["os"], "--", "statut du serveur :", serveur["status"])
#========================#
#Calculcer et afficher la moyenne d'utilisation CPU et RAM
#========================#

cpus=[serveur["cpu_usage"] for serveur in serveurs] 
mem=[serveur["ram_usage"] for serveur in serveurs]
print("moyenne cpu : ", sum(cpus)/len(cpus), "minimum cpu : ", min(cpus), "maximum cpu : ", max(cpus))
print("moyenne mémoire : ", sum(mem)/len(mem), "minimum memoire : ", min(mem), "maximum memoire : ", max(mem))

#====================#
#Ajoute nouveau serveur par l'utilsiateur~#
#====================#

import json

# Charger le fichier JSON
with open("servers.json", "r", encoding="utf-8") as fichier:
    serveurs = json.load(fichier)

# Nouveau serveur (codé en dur)
nouveau_serveur = {
    "name": "srv-web-03",
    "ip": "192.168.1.12",
    "os": "Ubuntu 22.04",
    "region": "eu-west-1",
    "status": "up",
    "cpu_usage": 30,
    "ram_usage": 40
}

# Ajouter à la liste
serveurs.append(nouveau_serveur)

# Sauvegarder dans le fichier JSON
with open("servers.json", "w", encoding="utf-8") as fichier:
    json.dump(serveurs, fichier, indent=4)

print("Serveur ajouté et fichier mis à jour.")

#======================#
#Génération du rapport
#======================#

import json

# Charger les serveurs
with open("servers.json", "r", encoding="utf-8") as fichier:
    serveurs = json.load(fichier)

# Ouvrir le fichier de rapport en écriture
with open("report.txt", "w", encoding="utf-8") as report:
    report.write("=== SERVEURS CRITIQUES ===\n\n")

    for serveur in serveurs:
        raisons = []

        # Conditions critiques
        if serveur["status"] == "down":
            raisons.append("status DOWN")

        if serveur["cpu_usage"] > 80:
            raisons.append("CPU > 80%")

        if serveur["ram_usage"] > 80:
            raisons.append("RAM > 80%")

        # Si au moins une alerte
        if raisons:
            report.write(
                f"{serveur['name']} ({serveur['ip']}) -> {', '.join(raisons)}\n"
            )

print("Rapport généré : report.txt")
