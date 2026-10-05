---
description: >-
  Toutes les commandes du chat et les interfaces en jeu.
icon: terminal
---

# Commandes et interfaces

Toutes les commandes s'écrivent dans le chat et commencent par `!`. Elles ne sont jamais affichées aux autres joueurs.

## Commandes de tous les joueurs

| Commande | Effet |
| --- | --- |
| `!help` | Affiche la liste des commandes |
| `!role` | Réaffiche la description de son rôle et les pseudos qu'il connaît |
| `!compo` | Affiche la composition de la partie, par camp (les rôles morts en sont retirés) |
| `!effects` | Affiche ses pourcentages de Force, Résistance, Vitesse et sa Régénération |
| `!alters` | Affiche la liste et les effets des alters éparpillés |
| `!marqueur` ou `!mark` | Ouvre le menu des marqueurs personnels |
| `!claim` | Récupère les objets mis de côté quand l'inventaire était plein |
| `!lag` | Affiche les performances du serveur (TPS et nombre d'entités) |
| `!tp <pseudo>` | Spectateurs uniquement, pendant la partie : se téléporte sur un joueur |

## Commandes de rôle et de camp

| Commande | Réservée à | Effet |
| --- | --- | --- |
| `!qg` | Préceptes | Téléporte au cœur du QG quand il est actif |
| `!manip` | Overhaul | Active ou désactive la Manipulation (1x/partie) |
| `!brainless` | All For One et Brainless, une fois le lien établi | Active ou désactive la création d'un nouveau Brainless (1x/partie) |
| `!missions` | Black Mist | Affiche l'avancement des trois missions |
| `!cleartp` | Black Mist | Supprime tous ses portails |
| `!fire` | Dabi | Active ou désactive les Flammes bleues |
| `!balises` | Denki | Affiche les joueurs balisés |
| `!jump` | Lady Nagant | Active ou désactive le double saut |
| `!snipe` | Lady Nagant | Active ou désactive la flèche téléguidée |
| `!patinoire` | Shoto | Active ou désactive Patinoire |
| `!flamme` | Shoto | Active ou désactive Flamme |
| `!tempset <0-100>` | Shoto en duo | Règle sa température |
| `!gs` | Stain | Affiche le groupe sanguin des joueurs à moins de 20 blocs (1x/3min) |

## Commandes du staff

| Commande | Effet |
| --- | --- |
| `!setcompo` | Ouvre le menu de composition |
| `!setinv` puis `confirm` | Définit l'inventaire de départ |
| `!start` | Lance la partie |
| `!grp <nombre>` | Définit la taille des groupes |
| `!title <texte>` | Change le titre du tableau de bord |
| `!alert <message>` | Envoie une annonce de l'hôte |
| `!fh` | Final Heal : soigne tous les joueurs |
| `!givestar <nom>` | Se donne une étoile du Nether portant ce nom |
| `!lobby` | Construit le lobby |
| `!lobby arena` | Reconstruit seulement l'arène du lobby |
| `!lag` | Version détaillée : TPS sur 5 secondes, joueurs, objets au sol, nettoyage |

## Interfaces en jeu

**Tableau de bord** (affiché en permanence sur le côté de l'écran) :

- Titre de la partie et date du jour.
- Temps écoulé.
- Cycle en cours (Jour ou Nuit) et temps avant le prochain changement.
- Taille de la carte.
- Kills du joueur.
- Taille des groupes.
- Nombre de joueurs en vie.
- Nom du serveur, NEXORA, en dégradé animé.

**Barre d'action** (au-dessus de la barre d'objets) : état et temps de recharge du pouvoir tenu en main, jauges de rôle (sueur, température, ombre, batterie, etc.), progression d'une extraction d'alter, d'une fouille de bureau ou de la capture du QG.

**Messages du chat** : les messages du jeu sont préfixés par `[MHA]`. Les messages du chat des Préceptes sont préfixés par `[Préceptes]`. Les annonces de l'hôte sont préfixées par `HOST`.

**Menus** : la composition, les marqueurs, le calcul d'extraction d'un alter et certains pouvoirs à cible (Effacement, Ciment, Attaque Surprise, Vol d'Alter) s'ouvrent sous forme de formulaires.
