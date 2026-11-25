= Stop it :
Arrêt de développement du projet. Mais au cas où je voudrais le reprendre, voici ce qu'il reste à faire :

# ROADMAP de la ZTVS

## Service votant
- Implémentation du système d'authentification par OTP
- Réparation du système de vérification de l'adresse email : seules les personnes dont l'email est présent dans la base de données sont autorisées à voter
- Génération côté serveur d'un couple de clés public/privé (chercher un algorithme efficace et irréversible en un temps fini sans connaître la clé) => envoi de la clé public côté client pour chiffrer le ciphertext de la réponse avant sauvegarde dans la base de données
- Envoi API POST (/api/saveanswer) du ciphertext chiffré et enregistrement dans la base de données
- Gérer le timestamp de fin d'élection
- Connecter la base de données au projet (Supabase) et au serveur SMTP (Resend)

## Assurement de l'intégrité du vote
- Envoi de l'identifiant unique de connexion email mélangé au timestamp de la connexion et ajouté à un sel puis chiffré avec une fonction de hashage avec code d'erreur (si bien qu'une modification de cette valeur prouve la modification du ballot) ; la fonction de hashage est donc associée à une fonction de vérification d'intégrité QUI DOIT RESTER CÔTÉ SERVEUR
    - P.S. : Ne pas enregistrer l'identifiant unique : faire un envoi direct en base de données !!!
- Chaque vote est associé à cet identifiant.
- Après enregistrement, bloquer la modification unique du ballot sans modifier la valeur du hash d'intégrité => lancer une erreur

## Erreurs en base de données
- Email non listé
- Vote déjà enregistré (un seul vote permis par personne)
- Élection terminée
- Modification unique interdite (détection d'une tentative de compromission)

## Début de l'élection
- Implémenter les routes POST /api/post_timestamp et GET /api/get_public_key, ainsi que le GitHub Actions pour lancer une élection à partir de la modification du fichier ``votedata.json``
- Lancer les envois de mail automatiques à partir de la liste d'emails enregistrés dans Supabase (en passant par Resend stp)
- Le serveur doit être en mesure de conserver sa clé privée tout au long de l'élection SANS JAMAIS LA COMMUNIQUER (Supabase Secrets ?)

## Fin de l'élection
- Implémenter la fonction de fermeture des votes et de fin d'élection
- Ajout de la route /api/get_results
- La logique de comptage :
    - Pour chaque vote enregistré, vérifier l'intégrité du vote avec la fonction de vérification du hash; si mauvais => vote nul
    - Décryptage du vote avec la clé privée puis la fonction de chiffrement réversible
    - Comptage du vote => Y : Oui ; N : Non ; W : Blanc ; Autre (on sait pas trop pourquoi) : Nul
    - Tout ça se fait côté serveur
    - Chiffrement avec clé privée des résultats puis envoi sur la route API GET
- Décryptage avec la clé publique côté client : si le truc reçu n'est pas qqch de chiffré avec la clé privée, rejet car intégrité des résultats perdue
- Gestion de l'affichage des résultats (éventuellement, envoi des résultats par mail DEPUIS LE SERVEUR)

## Si tu as la flemme
=> Helios Voting
