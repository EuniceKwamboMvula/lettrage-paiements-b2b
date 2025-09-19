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