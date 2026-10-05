---
description: >-
  Le labyrinthe où se joue le sort d'Eri quand un Précepte la tue.
icon: dungeon
---

# QG des Préceptes

L'événement se déclenche quand un Précepte tue Eri. Sa mort est mise en attente pendant que les autres joueurs tentent de la sauver.

1. Le QG, un grand labyrinthe généré aléatoirement loin de la carte, s'active pendant 6 minutes.
2. Trois Portails Laser rouges apparaissent à moins de 150 blocs du centre. Leurs coordonnées sont envoyées à tous les joueurs qui ne sont pas Préceptes.
3. Les joueurs qui passent un portail arrivent à l'entrée du labyrinthe et doivent en atteindre le cœur. Les Préceptes s'y téléportent directement avec `!qg`.
4. Un joueur qui n'est pas Précepte doit rester 30 secondes dans la zone de capture du cœur (4 blocs de rayon). La capture est bloquée tant qu'un Précepte se trouve dans la zone, et repart de zéro si plus aucun attaquant n'y est.
5. Dans le QG, les téléportations sont bloquées et rien ne peut être cassé ni posé. On en sort par l'alcôve verte de l'entrée (retour au portail) ou par le portail vert du cœur (retour au hasard sur la carte).

| Issue | Conséquence |
| --- | --- |
| Zone capturée à temps | Eri ressuscite et le QG disparaît |
| 6 minutes écoulées, ou plus aucun joueur hors Préceptes en vie | Eri est définitivement éliminée ; chaque Précepte en vie gagne +1 cœur permanent et +8 % de Force |

{% hint style="info" %}
La barre d'action des joueurs présents dans le QG affiche le temps restant, leur avancée dans le labyrinthe et la progression de la capture.
{% endhint %}
