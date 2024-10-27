import pandas as pd

# Charge le fichier CSV dans un DataFrame
csv_file_path = 'test2_mapped_cleaned.csv' 
df = pd.read_csv(csv_file_path)

# Filtre les lignes où 'gravure_nasale' ne contient pas de lien HTTP
non_http_entries = df[~df['gravure_nasale'].str.startswith('http', na=False)]

# Enregistre les noms des gravures nasales qui ne sont pas des liens dans un fichier texte
output_file_path = 'gravure_texte.txt'  
with open(output_file_path, 'w') as file:
    for entry in non_http_entries['gravure_nasale']:
        file.write(f"{entry}\n")

print("Extraction terminée. Fichier enregistré sous :", output_file_path)