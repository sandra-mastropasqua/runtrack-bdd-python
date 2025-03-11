SELECT * FROM etudiant
    -> WHERE nom = 'Dupuis' AND prenom = 'Gertrude';

INSERT INTO etudiant (nom, prenom, age, email)
    -> VALUES ('Dupuis', 'Martin', 18, 'martindupuis@laplateforme.io');

SELECT * FROM etudiant
    -> WHERE nom = 'Dupuis';
