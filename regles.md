---
description: >-
  Du lobby à la victoire : lancement, chronologie, mort et conditions de victoire.
icon: list-check
---

# Déroulement d'une partie

Une partie va du lobby à la victoire d'un seul camp : l'hôte règle la composition, lance la partie, chaque joueur reçoit un rôle secret, puis les camps s'affrontent jusqu'à ce qu'il n'en reste qu'un.

## Avant la partie

1. Les joueurs qui se connectent arrivent dans le lobby, une île flottante protégée (ni dégâts, ni casse, ni pose de blocs).
2. L'hôte (joueur avec le grade staff) choisit les rôles actifs avec `!setcompo`, et peut y générer la carte personnalisée.
3. L'hôte définit l'inventaire de départ commun à tous avec `!setinv`.
4. Tout joueur peut consulter la composition avec `!compo`.

## Lancement (`!start`)

1. Les rôles actifs sont mélangés et distribués au hasard, un par joueur. S'il y a plus de joueurs que de rôles, les joueurs en trop jouent sans rôle.
2. Chaque joueur reçoit l'inventaire de départ, 10 cœurs, et le message qui décrit son rôle.
3. Les joueurs sont dispersés dans un rayon de 140 blocs autour du centre de la carte (0, 0).
4. Le serveur se ferme : un joueur qui n'était pas présent au lancement est expulsé s'il tente de rejoindre.
5. Le chat public est coupé pour toute la partie. Seules les commandes en `!` fonctionnent, ainsi que le chat privé du camp des Préceptes.

## Chronologie d'une partie normale

| Moment | Événement |
| --- | --- |
| 0 min | Début de partie, de jour. PvP désactivé. |
| 45 s | Un Héros au hasard est désigné Symbole de la paix. |
| 5 min | Première apparition de Yuei (4 min). La nuit tombe. |
| 7 min | Premier alter éparpillé. |
| 10 min | Le jour se lève. |
| 12 min | PvP activé. |
| 15 min | Deuxième alter éparpillé et deuxième apparition de Yuei. |
| 25 min | Troisième alter et troisième apparition de Yuei. |
| 35 min | Quatrième alter. |
| 40 min | Dernière apparition de Yuei. |
| 45 min | Cinquième et dernier alter. |

{% hint style="info" %}
Le cycle jour/nuit alterne toutes les 5 minutes pendant toute la partie, en commençant par le jour. Plusieurs rôles ont des effets qui dépendent du jour ou de la nuit.
{% endhint %}

## Règles permanentes

- La carte fait 900 × 900 blocs. Une bordure à 450 blocs du centre repousse les joueurs vers l'intérieur.
- Taille maximale des groupes : 4 joueurs, puis 3 dès qu'il reste moins de 19 joueurs en vie. Le changement est annoncé dans le chat.
- Pas de dégâts de chute ni de noyade. Les dégâts de lave et de feu sont fortement réduits.
- Vision nocturne permanente et aucune faim.
- Les pseudos au-dessus des têtes et les messages de mort vanilla sont masqués.
- Objets interdits, supprimés en permanence : champignons bruns et rouges, graines de blé, coquelicots.
- Les objets, orbes d'expérience et flèches restés 1 minute au sol sont supprimés, sauf les pommes dorées.

## Mort d'un joueur

1. Le joueur passe en spectateur à l'endroit de sa mort.
2. Son équipement tombe au sol, avec 3 pommes dorées bonus. Les objets de pouvoir ne tombent pas.
3. Sa mort est annoncée à tous avec son rôle, écrit dans la couleur de son camp.
4. Son rôle est retiré de la composition affichée par `!compo`.
5. Le tueur gagne 1 kill, affiché sur son tableau de bord.

{% hint style="info" %}
Certains rôles peuvent annuler une mort (résurrection) ou la mettre en attente (voir Eri et le QG des Préceptes). Un spectateur peut se téléporter sur un joueur avec `!tp pseudo`.
{% endhint %}

## Conditions de victoire

| Situation | Vainqueur |
| --- | --- |
| Il ne reste en vie que des joueurs d'un même camp (Héros, Vilains, Préceptes ou Duo Todoroki) et aucun Solitaire | Ce camp, y compris ses membres morts |
| Il ne reste en vie qu'un seul Solitaire et personne d'autre | Ce Solitaire uniquement |

{% hint style="success" %}
La victoire est annoncée 6 secondes après la dernière mort, avec le classement des kills des gagnants et le top 5 des autres joueurs. Si le lobby est construit, une cérémonie de 15 secondes a lieu dans son arène : les 3 meilleurs tueurs montent sur le podium et les autres joueurs sont assis dans les gradins.
{% endhint %}
