import pandas as pd

# Dictionnaire de mapping des fournisseurs avec leurs IDs
fournisseur_mapping = {
    2399: "ADN OPTIS",
    1344: "BBGR OPTIQUE",
    70: "DIVEL FRANCE",
    521: "ESSILOR FRANCE",
    1488: "HEPHILENS",
    130: "HOYA VISION CARE FRANCE",
    1958: "INDO OPTICAL FRANCE",
    2217: "K OPTICAL",
    2532: "LEICA EYECARE",
    644: "MEGA OPTIC",
    1838: "MONT ROYAL",
    561: "NIKON VERRES OPTIQUES",
    711: "NOVACEL",
    2395: "OPHTALMIC COMPAGNIE",
    127: "OPTIC 200",
    659: "OPTISWWIS FRANCE",
    789: "OPTOVISION GMBH",
    2069: "RODENSTOCK",
    1407: "SEIKO OPTICAL France",
    2397: "SHAMIR FRANCE",
    2644: "VERRES KODAK",
    2414: "ZEISS VISION CARE FRANCE"
}

# Charge le fichier CSV2
csv_path = "test2.csv"  
df = pd.read_csv(csv_path)

# Ajouter une colonne 'fournisseur_nom' en utilisant le mapping du dictionnaire
df["fournisseur_nom"] = df["fournisseur_id"].map(fournisseur_mapping)

# Sauvegarde le fichier CSV mis à jour
df.to_csv("test2_mapped.csv", index=False)

print("La colonne 'fournisseur_nom' a été ajoutée avec succès.")