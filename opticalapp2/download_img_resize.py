import csv
import os
import requests
from PIL import Image
from io import BytesIO

# Crée un dossier pour enregistrer les images si le dossier n'existe pas encore
output_dir = "downloaded_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Chemin vers le fichier CSV
input_csv = 'test2_mapped_cleaned.csv'

# Télécharge les images, les redimensionne et les enregistre avec le nom de la gravure
with open(input_csv, mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        gravure_nasale = row['gravure_nasale']
        nom_verre = row['nom_verre']

        # Vérifie si la donnée de gravure_nasale est un lien valide
        if gravure_nasale.startswith("http"):
            try:
                response = requests.get(gravure_nasale)
                response.raise_for_status()

                # Ouvre l'image à partir de la réponse HTTP
                img = Image.open(BytesIO(response.content))

                # Redimensionne l'image à 640x640 pixels
                img = img.resize((640, 640), Image.LANCZOS)

                # Enregistre l'image dans le dossier de sortie avec le nom de la gravure
                image_path = os.path.join(output_dir, f"{nom_verre}.jpg")
                img.save(image_path)
                print(f"Image téléchargée et enregistrée pour {nom_verre}")

            except requests.exceptions.RequestException as e:
                print(f"Erreur lors du téléchargement de l'image pour {nom_verre}: {e}")

            except Exception as e:
                print(f"Erreur lors de l'enregistrement de l'image pour {nom_verre}: {e}")

        else:
            print(f"Pas de lien valide pour {nom_verre}, image ignorée")
