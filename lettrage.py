import pandas as pd

#charger les fichiers CSV
factures = pd.read_csv("data/factures.csv")
paiements = pd.read_csv("data/paiements.csv")

#Somme des paiements par client
paiements_groupes = paiements.groupby("client_id")["montant_paye"].sum().reset_index()
paiements_groupes.rename(columns={"montant_paye": "total_paye"}, inplace=True)

#Somme des factures par client
factures_groupes = factures.groupby("client_id")["montant_facture"].sum().reset_index()
factures_groupes.rename(columns={"montant_facture": "total_facture"}, inplace=True)

#fusionner les deux
balance = pd.merge(factures_groupes, paiements_groupes, on="client_id", how="left")
balance["total_paye"] = balance["total_paye"].fillna(0)

#calcul du solde restant
balance["solde_restant"] = balance["total_facture"] - balance["total_paye"]

#Ajouter statut
def definir_statut(row):
    if row["solde_restant"] == 0:
        return "Payé"
    elif row["solde_restant"] > 0 and row["total_paye"] > 0:
        return "Partiellement Payé"
    else:
        return "Impayé"

balance["statut"] = balance.apply(definir_statut, axis=1)

#Joindre avec le nom du client
clients = factures[["client_id", "client_nom"]].drop_duplicates()
balance = pd.merge(balance, clients, on="client_id", how="left")

#Sauvegarder dans un fichier csv
balance.to_csv("output/balance_client.csv", index=False)
print("Fichier 'balance_clients.csv' généré avec succès !")


