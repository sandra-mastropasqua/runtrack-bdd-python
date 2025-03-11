import mysql.connector
from datetime import date

class Zoo:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="gina0900",  
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    def add_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = """
            INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine)
            VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (nom, race, id_cage, date_naissance, pays_origine))
        self.conn.commit()

    def remove_animal(self, id_animal):
        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (id_animal,))
        self.conn.commit()

    def update_animal(self, id_animal, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        self.cursor.execute(query, (nom, race, id_cage, date_naissance, pays_origine, id_animal))
        self.conn.commit()

    def add_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        self.cursor.execute(query, (superficie, capacite_max))
        self.conn.commit()

    def remove_cage(self, id_cage):
        query = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(query, (id_cage,))
        self.conn.commit()

    def update_cage(self, id_cage, superficie=None, capacite_max=None):
        query = "UPDATE cage SET superficie = %s, capacite_max = %s WHERE id = %s"
        self.cursor.execute(query, (superficie, capacite_max, id_cage))
        self.conn.commit()

    def display_animals(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        animals = self.cursor.fetchall()
        for animal in animals:
            print(f"ID: {animal[0]}, Nom: {animal[1]}, Race: {animal[2]}, Cage ID: {animal[3]}, Date de naissance: {animal[4]}, Pays d'origine: {animal[5]}")

    def display_animals_in_cages(self):
        query = """
            SELECT a.nom, a.race, a.id_cage, c.superficie, c.capacite_max
            FROM animal a
            JOIN cage c ON a.id_cage = c.id
        """
        self.cursor.execute(query)
        animals_in_cages = self.cursor.fetchall()
        for animal in animals_in_cages:
            print(f"Nom: {animal[0]}, Race: {animal[1]}, Cage ID: {animal[2]}, Superficie de la cage: {animal[3]} m², Capacité max: {animal[4]}")

    def total_superficie_cages(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        total_superficie = self.cursor.fetchone()[0]
        print(f"La superficie totale des cages est de {total_superficie} m².")

    def close(self):
        self.cursor.close()
        self.conn.close()




zoo = Zoo()

zoo.add_cage(100, 10)
zoo.add_cage(200, 20)


zoo.add_animal("Lion", "Blanc", 1, date(2015, 6, 1), "Afrique")
# zoo.add_animal("Tigre", "Marron", 2, date(2017, 8, 10), "Asie")


# print("Tous les animaux dans le zoo:")
# zoo.display_animals()

# print("\nLes animaux présents dans les cages:")



zoo.remove_animal(2)


zoo.remove_cage(2)


zoo.close()
