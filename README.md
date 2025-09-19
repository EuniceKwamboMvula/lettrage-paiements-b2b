# Projet : Système de lettrage automatique des paiement 

## objectif
ce projet simule le travail d'un Agent de lettrage des paiements :
-Comparer les factures émises aux paiements reçus.
-Identifier les factures payées, partiellement payées ou impayées.
-Générer un rapport `balance_clients.csv`.

## Structure du projet

Projet-lettrage/
|
|--- data/
|  |---features.csv
|  |----paiements.csv
|
|--- output/
|   |--- balance_clients.csv
|
|
|--- lettrage.py
|
|--- README.md

## Lancer le projet
1. cloner le dépôt Github
2. Installer pandas :
   ``` bash
   pip install pandas

3. Exécuter le script :
   ``` bash
   python lettrage.py
4. Le resultat se trouve dans :
output/balance_clients.csv

## Améliorations possibles
- gestion des paiements en trop ou non identifiés (paiements sans facture correspondante).
- Ajout d'un tableau de bord (ex. Power BI, Streamlit).
- Automatisation des justificatifs (via google Drive API).
- Création d'une API pour intégrer le lettrage dans une application Web.

## Auteur
Projet réalisé par Eunice Kwambo Mvula, inspiré des missions d'agent de lettrage des paiements.
