 INSERT INTO etage (nom, numero, superficie) VALUES
    -> ('RDC', 0, 500 ),
    -> ('R+1', 1, 500);

 SELECT * FROM etage;
+----+-----+--------+------------+
| id | nom | numero | superficie |
+----+-----+--------+------------+
|  1 | RDC |      0 |        500 |
|  2 | R+1 |      1 |        500 |
+----+-----+--------+------------+
2 rows in set (0.00 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite) VALUES
    -> ('Lounge', 1,100),
    -> ('Studio Son', 1, 5),
    -> ('Broadcasting', 2, 50),
    -> ('Bocal Peda', 2, 4),
    -> ('Coworking', 2, 80),
    -> ('Studio Video', 2, 5);

 SELECT * FROM salle;
+----+--------------+----------+----------+
| id | nom          | id_etage | capacite |
+----+--------------+----------+----------+
|  1 | Lounge       |        1 |      100 |
|  2 | Studio Son   |        1 |        5 |
|  3 | Broadcasting |        2 |       50 |
|  4 | Bocal Peda   |        2 |        4 |
|  5 | Coworking    |        2 |       80 |
|  6 | Studio Video |        2 |        5 |
+----+--------------+----------+----------+

