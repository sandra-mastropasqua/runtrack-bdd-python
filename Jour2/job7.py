import mysql.connector

class Employe:
    def __init__(self, id=None, nom=None, prenom=None, salaire=None, id_service=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    def connect(self):
        """Connect to the database."""
        return mysql.connector.connect(
            host="localhost", 
            user="root",  
            password="gina0900",  
            database="employe_db"
        )

    def create(self):
        """Create a new employee."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)",
                       (self.nom, self.prenom, self.salaire, self.id_service))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def read_all():
        conn = Employe.connect(None)
        cursor = conn.cursor()
        cursor.execute("SELECT e.nom, e.prenom, e.salaire, s.nom AS service FROM employe e JOIN service s ON e.id_service = s.id")
        for row in cursor.fetchall():
            print(f"{row[0]} {row[1]}, Salaire: {row[2]} €, Service: {row[3]}")
        cursor.close()
        conn.close()

    @staticmethod
    def read_high_salary(min_salary=3000):
        conn = Employe.connect(None)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employe WHERE salaire > %s", (min_salary,))
        for row in cursor.fetchall():
            print(f"ID: {row[0]}, Nom: {row[1]}, Prénom: {row[2]}, Salaire: {row[3]} €")
        cursor.close()
        conn.close()

    def update(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE employe SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s",
                       (self.nom, self.prenom, self.salaire, self.id_service, self.id))
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employe WHERE id=%s", (self.id,))
        conn.commit()
        cursor.close()
        conn.close()


employe1 = Employe(nom="Leclerc", prenom="Amandine", salaire=3200, id_service=1)
employe1.create()

print("\nListe des employés avec leur service :")
Employe.read_all()


print("\nEmployés avec un salaire supérieur à 3000 € :")
Employe.read_high_salary()


employe1.nom = "Leclerc-Morel"
employe1.update()


