import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# Charge le fichier CSV
csv_path = 'test2_mapped_cleaned.csv' 
df = pd.read_csv(csv_path)
# Créer un dossier pour stocker les images textuelles générées
output_folder = 'text_images'
os.makedirs(output_folder, exist_ok=True)

# Fonction pour vérifier si une valeur est un lien HTTP
def is_http_link(value):
    return isinstance(value, str) and value.startswith('http')

# Fonction pour créer une image à partir du texte
def create_text_image(text, output_path):
    img = Image.new('RGB', (640, 640), color=(255, 255, 255))  # Créer une image blanche
    draw = ImageDraw.Draw(img)
    
    # Charge une police plus grande pour le texte (par défaut de PIL)
    try:
        font = ImageFont.truetype("arial.ttf", 80)  # Utilise une police TrueType si disponible
    except IOError:
        font = ImageFont.load_default()  # Utilise la police par défaut si TrueType n'est pas disponible

    # Centre le texte sur l'image
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]  # Utilise textbbox pour mesurer le texte
    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 2

    draw.text((x, y), text, fill=(0, 0, 0), font=font)  # Dessine le texte au centre de l'image
    img.save(output_path)

# Parcour les lignes du CSV pour trouver les entrées non HTTP
for index, row in df.iterrows():
    gravure_nasale = row['gravure_nasale']
    nom_verre = row['nom_verre']

    # Vérifie si gravure_nasale n'est pas un lien HTTP et n'est pas NaN
    if not is_http_link(gravure_nasale) and pd.notna(gravure_nasale):
        # Converti en chaîne de caractères pour éviter les erreurs de type
        gravure_nasale = str(gravure_nasale)

        # Chemin de sortie basé sur le nom du verre déjà nettoyé
        output_path = os.path.join(output_folder, f"{nom_verre}.jpg")
        
        # Créer l'image textuelle avec une police plus grande
        create_text_image(gravure_nasale, output_path)
        print(f"Image créée : {output_path}")

print("Création des images textuelles terminée.")