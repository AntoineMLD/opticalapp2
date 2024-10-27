import scrapy

class EngravingItem(scrapy.Item):
    # Champs à extraire pour chaque gravure

    # Indice du verre
    indice = scrapy.Field()

    # Matière du verre
    matiere = scrapy.Field()

    # Hauteur de montage du verre
    haut_de_montage = scrapy.Field()

    # Fournisseur du verre
    fournisseur_id = scrapy.Field()

    # Groupe/Catégorie du verre
    category = scrapy.Field()

    # Nom du verre
    nom_verre = scrapy.Field()

    # Gravure nasale
    gravure_nasale = scrapy.Field() 
