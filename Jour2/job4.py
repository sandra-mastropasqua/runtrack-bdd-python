import mysql.connector

# Connexion à la base de données
try:
    conn = mysql.connector.connect(
        host="localhost",        
        user="root",  
        password="gina0900",  
        database="LaPlateforme"  
    )

    cursor = conn.cursor()


    query = "SELECT nom, capacite FROM salle"
    cursor.execute(query)

   
    print(" Liste des salles et leur capacité :")
    for nom, capacite in cursor.fetchall():
        print(f" Salle : {nom}, Capacité : {capacite}")

except mysql.connector.Error as err:
    print(f" Erreur MySQL : {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
