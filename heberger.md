# Héberger une partie

Toute la configuration se fait en jeu par l'hôte, c'est-à-dire un joueur qui possède le grade staff. Il n'y a pas de fichier de configuration à modifier.

## Menu de composition (`!setcompo`)

| Entrée du menu | Rôle |
| --- | --- |
| Camps (Héros, Vilains, Préceptes, Solitaire) | Ouvre la liste des rôles du camp, chacun avec un interrupteur actif / inactif, et une action rapide « tout activer » ou « tout désactiver » |
| Tout activer / Tout désactiver | Agit sur les 31 rôles d'un coup |
| Presets | Sauvegarde la composition actuelle sous un nom, puis permet de la charger, l'écraser ou la supprimer |
| Aperçu et annonce | Affiche la composition par camp et permet de l'annoncer dans le chat |
| Joueurs simulés | Ajoute de 0 à 30 faux joueurs immobiles qui reçoivent un rôle, pour tester seul |
| Générer la map | Lance la génération de la carte personnalisée |
| Attribuer les rôles | En mode test uniquement : choisit à la main le rôle de chaque joueur |

Le menu affiche en permanence le nombre de rôles actifs et le nombre de joueurs, et prévient s'il manque des rôles. La composition est conservée d'une partie à l'autre. Un nouveau rôle est actif par défaut.

## Réglages de la carte personnalisée

| Réglage | Choix | Valeur par défaut |
| --- | --- | --- |
| Densité de la forêt | Clairsemée, Normale, Dense, Très dense | Dense |
| Relief | Presque plat, Plaine vallonnée, Collines | Plaine vallonnée |
| Clairières | Aucune, Rares, Normales, Nombreuses | Normales |
| Petits lacs | 0 à 30 | 12 |
| Mares d'eau | 0 à 60 | 26 |
| Mares de lave | 0 à 20 | 7 |
| Champignons géants | Oui ou non | Oui |

La génération remplace tout le terrain de la zone au-dessus de la couche 48, sans retour possible, et prend plusieurs minutes.

## Inventaire de départ (`!setinv`)

L'hôte compose l'inventaire et l'armure dans son propre inventaire, puis écrit `confirm` dans le chat pour l'enregistrer. Tous les joueurs reçoivent cet inventaire au lancement. Le contenu exact dépend donc de l'hôte et n'est pas fixé par le mode.

## Réglages en cours de partie

- `!grp <nombre>` : force la taille des groupes.
- `!title <texte>` : change le titre affiché sur le tableau de bord.
- `!alert <message>` : envoie une annonce de l'hôte à tous.
- `!fh` : Final Heal, soigne entièrement tous les joueurs.

## Bot Discord

Un bot Discord accompagne le serveur pour organiser les parties.

| Commande | Rôle |
| --- | --- |
| `/link <gamertag>` | Lie un gamertag Xbox à son compte Discord (3 maximum) |
| `/unlink` | Affiche ses gamertags liés et permet d'en retirer un |
| `/profil [membre]` | Affiche les gamertags liés à un compte Discord |
| `/host <heure> <mode> <slots>` | Annonce une partie avec son heure, son mode et son nombre de places |
| `/cancelhost` | Annule la partie prévue |
| `/confighost [salon]` | Choisit le salon où sont envoyées les annonces |
| `/panel` | Panneau de contrôle du serveur, réservé aux administrateurs |

La liste blanche du serveur est synchronisée automatiquement avec les gamertags des joueurs inscrits à la partie annoncée. Un joueur doit donc lier son gamertag puis s'inscrire au host pour pouvoir se connecter.
