import mysql.connector


try:
    conn = mysql.connector.connect(
        host="localhost",        
        user="root",  
        password="gina0900",  
        database="LaPlateforme"  
    )

    cursor = conn.cursor()

   
    query = "SELECT SUM(superficie) FROM etage"
    cursor.execute(query)

    
    superficie_totale = cursor.fetchone()[0]
    print(f"La superficie de La Plateforme est de {superficie_totale} m2")

except mysql.connector.Error as err:
    print(f" Erreur MySQL : {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
