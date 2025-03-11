import mysql.connector


conn = mysql.connector.connect(
    host="localhost",      
    user="root",  
    password="gina0900",  
    database="LaPlateforme"  
)

cursor = conn.cursor()

query = "SELECT * FROM etudiant;"
cursor.execute(query)

etudiants = cursor.fetchall()
for etudiant in etudiants:
    print(etudiant)


cursor.close()
conn.close()
