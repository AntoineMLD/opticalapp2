import scrapy
import re 
from opticalapp2.items import EngravingItem

class OpticalspiderSpider(scrapy.Spider):
    name = "opticalspider"
    allowed_domains = ["www.france-optique.com"]

    # Ajout des URLs de tous les fournisseurs
    start_urls = [
        "https://www.france-optique.com/gravures/fournisseur=2399",
        "https://www.france-optique.com/gravures/fournisseur=1344",
        "https://www.france-optique.com/gravures/fournisseur=70",
        "https://www.france-optique.com/gravures/fournisseur=521",
        "https://www.france-optique.com/gravures/fournisseur=1488",
        "https://www.france-optique.com/gravures/fournisseur=130",
        "https://www.france-optique.com/gravures/fournisseur=1958",
        "https://www.france-optique.com/gravures/fournisseur=2217",
        "https://www.france-optique.com/gravures/fournisseur=2532",
        "https://www.france-optique.com/gravures/fournisseur=644",
        "https://www.france-optique.com/gravures/fournisseur=1838",
        "https://www.france-optique.com/gravures/fournisseur=561",
        "https://www.france-optique.com/gravures/fournisseur=711",
        "https://www.france-optique.com/gravures/fournisseur=2395",
        "https://www.france-optique.com/gravures/fournisseur=127",
        "https://www.france-optique.com/gravures/fournisseur=659",
        "https://www.france-optique.com/gravures/fournisseur=789",
        "https://www.france-optique.com/gravures/fournisseur=2069",
        "https://www.france-optique.com/gravures/fournisseur=1407",
        "https://www.france-optique.com/gravures/fournisseur=2397",
        "https://www.france-optique.com/gravures/fournisseur=2644",
        "https://www.france-optique.com/gravures/fournisseur=2414",
    ]

    def parse(self, response):
        # Extract all categories and their engravings
        category_elements = response.xpath('//div[contains(@class, "group")]')

        category_elements = response.xpath('//div[@class="row tr group"]')
        
        for category in category_elements:
            category_name = category.xpath('./text()').get().strip()
        
        # Extract each engraving details within this category
            engraving_rows = category.xpath('./following-sibling::div[@class="row tr"]')

            for engraving_row in engraving_rows:
                item = EngravingItem()
                item['category'] = category_name

                # Extract engraving details
                item['nom_verre'] = engraving_row.xpath('.//div[contains(@class, "col s4 m4")]/p/text()').get()
                item['gravure_nasale'] = engraving_row.xpath('.//div[contains(@class, "col s1 m1")][2]/img/@src').get() or \
                                         engraving_row.xpath('.//div[contains(@class, "col s1 m1")][2]/p[@class="gravure_txt"]/b/text()').get()
                item['indice'] = engraving_row.xpath('.//div[contains(@class, "col s1 m1")][4]/p/text()').get()
                item['matiere'] = engraving_row.xpath('.//div[contains(@class, "col s1 m1")][5]/p/text()').get()
                
                # Extract fournisseur from URL
                item['fournisseur_id'] = re.search(r'fournisseur=(\d+)', response.url).group(1)

                yield item