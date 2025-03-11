import mysql.connector


try:
    conn = mysql.connector.connect(
        host="localhost",        
        user="root",  
        password="gina0900",  
        database="LaPlateforme"  
    )

    cursor = conn.cursor()

    query = "SELECT SUM(capacite) FROM salle"
    cursor.execute(query)

    
    capacite_totale = cursor.fetchone()[0]
    print(f"La capacité totale des salles est de {capacite_totale} personnes.")

except mysql.connector.Error as err:
    print(f" Erreur MySQL : {err}")

finally:
   
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
