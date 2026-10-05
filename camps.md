---
description: >-
  Les quatre camps, le duo secret et les changements de camp en cours de partie.
icon: users
---

# Camps et équipes

Le jeu compte quatre camps visibles et un camp secret. Chaque camp gagne en étant le dernier en vie.

| Camp | Couleur en jeu | Rôles | Objectif | Ce que ses membres savent |
| --- | --- | --- | --- | --- |
| <mark style="color:green;">**Héros**</mark> | Vert clair (`§a`, #55FF55) | 17 | Éliminer tous les autres camps | Rien en commun : les Héros ne se connaissent pas, sauf informations propres à certains rôles |
| <mark style="color:red;">**Vilains**</mark> | Rouge (`§c`, #FF5555) | 8 | Éliminer tous les autres camps | Chaque Vilain connaît le pseudo d'All For One et celui d'un autre Vilain au hasard. All For One connaît tous les Vilains |
| <mark style="color:purple;">**Préceptes**</mark> | Violet (`§5`, #AA00AA) | 4 | Éliminer tous les autres camps | La liste complète des Préceptes et le pseudo d'Eri |
| <mark style="color:orange;">**Solitaire**</mark> | Or (`§6`, #FFAA00) | 2 | Gagner seul, en dernier survivant | Rien : chaque Solitaire joue pour lui-même, même contre l'autre Solitaire |
| Duo Todoroki (secret) | Or (`§6`, #FFAA00) | 2 | Éliminer tous les autres joueurs à deux | Shoto et Endeavor se connaissent |

## 🟢 Héros

Le camp le plus nombreux, mais le seul dont les membres ne se connaissent pas. Il dispose d'un bonus de camp, le Symbole de la paix.

- 45 secondes après le lancement, un Héros en vie tiré au hasard est désigné Symbole de la paix. Son pseudo est annoncé à toute la partie et précédé de `[S]` au-dessus de sa tête.
- La Force de ses adversaires ne l'affecte pas.
- Il est soigné de 0,5 cœur chaque fois qu'un joueur mange une pomme dorée à 20 blocs ou moins de lui.
- À sa mort, un nouveau Symbole est désigné 20 secondes plus tard parmi les Héros en vie.

## 🔴 Vilains

Camp organisé autour d'All For One, qui connaît tous ses alliés.

- Hawks, pourtant Héros, apparaît dans la liste des Vilains d'All For One : c'est un infiltré.
- Lien avec Brainless : si Brainless reste 10 minutes au total à moins de 20 blocs d'All For One, ils partagent un chat privé et la commande `!brainless` (1 fois par partie). Une fois activée, le prochain joueur tué par un Vilain ressuscite en Brainless et rejoint les Vilains.

## 🟣 Préceptes

Petit camp soudé : ses membres se connaissent tous et discutent entre eux.

- Chat de camp : un message normal écrit par un Précepte n'est lu que par les Préceptes.
- Manipulation : avec `!manip` (Overhaul, 1 fois par partie), le prochain joueur tué par un Précepte revient à la vie et rejoint les Préceptes en gardant son rôle. Il devient un « manipulable ».
- QG des Préceptes : si un Précepte tue Eri, un événement de 6 minutes se déclenche (voir Mécaniques communes).

## 🟠 Solitaire

Lady Nagant et Stain jouent chacun pour soi. Un Solitaire ne gagne que s'il est le dernier joueur en vie. Deku peut devenir Solitaire en cours de partie.

## 🟠 Duo Todoroki (camp secret)

{% hint style="warning" %}
Au bout d'1 minute de jeu, Shoto a 20 % de chance de quitter les Héros pour former un duo avec Endeavor, si celui-ci est en jeu. Les deux doivent alors éliminer tous les autres joueurs.
{% endhint %}

- Le duo n'apparaît pas dans `!compo`.
- À leur mort, Shoto et Endeavor sont annoncés dans la couleur des Héros, pour ne pas révéler le duo.
- Dabi apprend au bout d'1 minute si le duo s'est formé.

## Changements de camp en cours de partie

| Déclencheur | Joueur concerné | Nouveau camp | Rôle conservé |
| --- | --- | --- | --- |
| Tirage à 1 minute (20 %) | Shoto et Endeavor | Duo Todoroki | Oui |
| Mort d'All Might et de Bakugo | Deku | Solitaire | Oui, renforcé |
| Ochaco à moins de 30 blocs de Deku à ce moment-là | Deku | Reste ou redevient Héros | Oui |
| `!manip` d'Overhaul | Prochain joueur tué par un Précepte (sauf Eri) | Préceptes | Oui |
| `!brainless` d'All For One ou de Brainless | Prochain joueur tué par un Vilain | Vilains | Non : il devient Brainless |

{% hint style="info" %}
Un joueur transformé en Brainless est annoncé à sa mort sous la forme « Brainless (ancien rôle) ».
{% endhint %}
