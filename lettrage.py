import os
import pandas as pd

# Créer les dossiers si nécessaire
os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)

# --- Générer les fichiers CSV ---

# factures.csv
factures_data = {
    "client_nom": ["Entreprise Alpha", "Entreprise Alpha", "Entreprise Beta", "Entreprise Gamma"],
    "feature_id": ["F001", "F002", "F003", "F004"],
    "montant_factture": [1000, 500, 2000, 1500]
}
factures_df = pd.DataFrame(factures_data)
factures_df.to_csv("data/factures.csv", sep='\t', index=False)

# paiements.csv
paiements_data = {
    "paiement_id": ["P001", "P002", "P003", "P004"],
    "client_id": ["Entreprise Alpha", "Entreprise Alpha", "Entreprise Beta", "Entreprise Gamma"],
    "montant_paye": [1000, 200, 1500, 1500]
}
paiements_df = pd.DataFrame(paiements_data)
paiements_df.to_csv("data/paiements.csv", sep=';', index=False)

# --- Lecture des fichiers CSV ---

factures = pd.read_csv("data/factures.csv", sep='\t')
paiements = pd.read_csv("data/paiements.csv", sep=';')

# Nettoyer les colonnes
factures.columns = factures.columns.str.strip()
paiements.columns = paiements.columns.str.strip()

# --- Calcul des totaux ---

# Somme des paiements par client
paiements_groupes = paiements.groupby("client_id")["montant_paye"].sum().reset_index()
paiements_groupes.rename(columns={"montant_paye": "total_paye"}, inplace=True)

# Somme des factures par client (par nom du client)
factures_groupes = factures.groupby("client_nom")["montant_factture"].sum().reset_index()
factures_groupes.rename(columns={"montant_factture": "total_facture"}, inplace=True)

# --- Fusionner les deux ---
balance = pd.merge(factures_groupes, paiements_groupes, left_on="client_nom", right_on="client_id", how="left")
balance["total_paye"] = balance["total_paye"].fillna(0)

# Calcul du solde restant
balance["solde_restant"] = balance["total_facture"] - balance["total_paye"]

# Ajouter statut
def definir_statut(row):
    if row["solde_restant"] == 0:
        return "Payé"
    elif row["solde_restant"] > 0 and row["total_paye"] > 0:
        return "Partiellement Payé"
    else:
        return "Impayé"

balance["statut"] = balance.apply(definir_statut, axis=1)

# Sauvegarder le fichier final
balance.to_csv("output/balance_client.csv", index=False)

print("✅ Fichier 'output/balance_client.csv' généré avec succès !")
print(balance)
