import csv
from jinja2 import Template
from dataclasses import dataclass

@dataclass
class Musette(dict):
    team: str
    year: str
    category: str
    picture_front: str
    picture_back: str
    difference: str
    kevin: str
    special: str
    url_front: str
    url_back: str


class InventoryGenerator:
    def __init__(self):
        self.file_name = "inventory.csv"
        self.musettes_list = []

    def import_csv(self):
        with open(self.file_name, newline='') as csvfile:
            musettes_list = csv.reader(csvfile, delimiter=';', quotechar='|')
            for team, year, category, picture_front, picture_back, difference, kevin, special, url_front, url_back in musettes_list:
                mus = Musette(team, year, category, picture_front, picture_back, difference, kevin, special, url_front, url_back)
                self.musettes_list.append(mus)

    def generate_website(self):
        with open("website_template.html.j2", newline='') as jinja_template:
            website_template = jinja_template.read()
            website_html = Template(source=website_template).render(musette_list=self.musettes_list)
            print(website_html)
        with open("index.html", "w") as text_file:
            text_file.write(website_html)



if __name__ == '__main__':
    generator = InventoryGenerator()
    generator.import_csv()
    generator.generate_website()