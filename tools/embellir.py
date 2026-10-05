# Mise en forme GitBook des pages : icônes, descriptions, encadrés (hints), cartes et couleurs de camp.
# À lancer une seule fois sur des pages brutes : une page qui a déjà un en-tête (---) est laissée telle quelle.
import os, re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

camps = {
    "heros": {"name": "Héros", "color": "green", "icon": "shield-halved", "emoji": "🟢"},
    "vilains": {"name": "Vilains", "color": "red", "icon": "skull", "emoji": "🔴"},
    "preceptes": {"name": "Préceptes", "color": "purple", "icon": "mask", "emoji": "🟣"},
    "solitaires": {"name": "Solitaire", "color": "orange", "icon": "user-ninja", "emoji": "🟠"},
}
camp_by_name = {c["name"]: c for c in camps.values()}

pages = {
    "README.md": ("house", "Le mode de jeu Minecraft Bedrock qui mélange UHC et rôles cachés dans l'univers de My Hero Academia."),
    "regles.md": ("list-check", "Du lobby à la victoire : lancement, chronologie, mort et conditions de victoire."),
    "camps.md": ("users", "Les quatre camps, le duo secret et les changements de camp en cours de partie."),
    "roles/README.md": ("id-card", "Les 31 rôles du mode, classés par camp."),
    "mecaniques/README.md": ("gears", "Les systèmes communs à tous les joueurs."),
    "commandes.md": ("terminal", "Toutes les commandes du chat et les interfaces en jeu."),
    "heberger.md": ("server", "Configurer et lancer une partie quand on est hôte."),
    "glossaire.md": ("book", "Le vocabulaire du mode."),
}
mech_icons = {
    "objets-de-pouvoir": "star", "effets-en-pourcentage": "percent", "combat": "hand-fist",
    "pommes-dorees": "apple-whole", "alters-eparpilles": "dna", "yuei": "school",
    "qg-des-preceptes": "dungeon", "marqueurs-personnels": "location-dot", "lobby-et-carte": "map",
}
# Une description doit tenir sur une seule ligne, sinon l'en-tête YAML de la page est invalide
mech_descriptions = {
    "objets-de-pouvoir": "Comment utiliser un pouvoir actif : étoile du Nether, clic droit et temps de recharge.",
    "effets-en-pourcentage": "Force, Résistance, Vitesse, Régénération et cœurs permanents, avec leurs plafonds.",
    "combat": "Calcul des dégâts, recul, kills et assistances.",
    "pommes-dorees": "Absorption, pénalité en cas d'abus et pommes laissées à la mort.",
    "alters-eparpilles": "Cinq pouvoirs bonus à extraire sur la carte pendant la partie.",
    "yuei": "Le lycée qui apparaît temporairement et cache des bonus d'information.",
    "qg-des-preceptes": "Le labyrinthe où se joue le sort d'Eri quand un Précepte la tue.",
    "marqueurs-personnels": "Poser des marqueurs visibles par soi seul au-dessus des autres joueurs.",
    "lobby-et-carte": "L'île du lobby et la forêt sombre générée pour les parties.",
}
section_emojis = [("Particularités", "✨"), ("Pouvoirs passifs", "🌀"), ("Pouvoir passif", "🌀"),
                  ("Pouvoirs actifs", "⚡"), ("Pouvoir actif", "⚡"), ("Objet spécial", "⏳"),
                  ("Missions", "🎯"), ("Éveil", "🌑"), ("Lien avec Brainless", "🔗")]


def read(path):
    with open(os.path.join(root, path), encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(os.path.join(root, path), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def front(icon, description):
    return f"---\ndescription: >-\n  {description}\nicon: {icon}\n---\n\n"


def hint(style, text):
    return f'{{% hint style="{style}" %}}\n{text.strip()}\n{{% endhint %}}'


def wrap(text, start, style):
    """Met dans un encadré le paragraphe (ou la ligne de liste) qui commence par `start`."""
    def repl(m):
        line = m.group(0)
        body = line[2:] if line.startswith("- ") else line
        return hint(style, body)
    new, count = re.subn(r"^(?:- )?" + re.escape(start) + r".*$", repl, text, count=1, flags=re.M)
    if not count:
        print("encadré introuvable :", start)
    return new


def cards(rows):
    body = "".join(f'<tr><td><strong>{t}</strong></td><td>{d}</td><td><a href="{h}">{os.path.basename(h)}</a></td></tr>'
                   for t, d, h in rows)
    return ('<table data-view="cards"><thead><tr><th></th><th></th>'
            '<th data-hidden data-card-target data-type="content-ref"></th></tr></thead>'
            f"<tbody>{body}</tbody></table>")


# Résumé de chaque rôle, pris dans l'index
resumes = {}
for line in read("roles/README.md").split("\n"):
    m = re.match(r"^\| \[(.+?)\]\((.+?)\) \|.*\| (.+?) \|$", line)
    if m:
        resumes[m.group(2)] = (m.group(1), m.group(3))

# Fiches de rôle
for folder, camp in camps.items():
    for name in sorted(os.listdir(os.path.join(root, "roles", folder))):
        path = f"roles/{folder}/{name}"
        text = read(path)
        if name == "README.md" or text.startswith("---"):
            continue
        title, resume = resumes[f"{folder}/{name}"]

        def meta(m):
            label = m.group(1)
            first = label.split(" (")[0]
            c = camp_by_name.get(first, camp)
            extra = label[len(first):]
            return (f'{c["emoji"]} <mark style="color:{c["color"]};">**{first}**</mark>{extra}'
                    f" · 🩸 Groupe sanguin **{m.group(2)}** · ❤️ **{m.group(3)}**")
        text = re.sub(r"^Camp : (.+?) · Groupe sanguin : (\w+) · (.+)$", meta, text, count=1, flags=re.M)

        def heading(m):
            label = m.group(1)
            emoji = next((e for key, e in section_emojis if label.startswith(key)), "🔹")
            return f"## {emoji} {label}"
        text = re.sub(r"^\*\*([^*]+)\*\*$", heading, text, flags=re.M)

        for start in ("Eri n'a aucun pouvoir actif", "Brainless n'a aucun pouvoir actif"):
            if start in text:
                text = wrap(text, start, "info")
        write(path, front(camp["icon"], resume) + text)

# Pages de camp : cartes des rôles
for folder, camp in camps.items():
    path = f"roles/{folder}/README.md"
    text = read(path)
    if text.startswith("---"):
        continue
    lines = text.split("\n")
    intro = [l for l in lines[1:] if not l.startswith("* [")]
    rows = [(resumes[f"{folder}/{h}"][0], resumes[f"{folder}/{h}"][1], h)
            for h in re.findall(r"^\* \[.+?\]\((.+?)\)$", text, flags=re.M)]
    intro_text = "\n".join(intro).strip()
    body = (hint("info", intro_text) + "\n\n" if intro_text else "") + cards(rows)
    write(path, front(camp["icon"], f"Les rôles du camp {camp['name']}.") + f"{lines[0]}\n\n{body}\n")

# Index des rôles : encadré de conventions et couleur des camps
text = read("roles/README.md")
if not text.startswith("---"):
    text = re.sub(r"Conventions de lecture :\n\n((?:- .*\n)+)", lambda m: hint("info", "**Conventions de lecture**\n\n" + m.group(1)) + "\n", text)
    for c in camp_by_name.values():
        text = text.replace(f"| {c['name']} |", f"| <mark style=\"color:{c['color']};\">{c['name']}</mark> |")
    write("roles/README.md", front(*pages["roles/README.md"]) + text)

# Mécaniques
for slug, icon in mech_icons.items():
    path = f"mecaniques/{slug}.md"
    text = read(path)
    if text.startswith("---"):
        continue
    if slug == "pommes-dorees":
        text = wrap(text, "Enchaîner les pommes dorées", "warning")
    if slug == "alters-eparpilles":
        text = wrap(text, "Chaque alter se recharge", "success")
    if slug == "objets-de-pouvoir":
        text = wrap(text, "Si l'inventaire est plein", "info")
    if slug == "qg-des-preceptes":
        text = wrap(text, "La barre d'action des joueurs", "info")
    write(path, front(icon, mech_descriptions[slug]) + text)

text = read("mecaniques/README.md")
if not text.startswith("---"):
    lines = text.split("\n")
    rows = []
    for title, href in re.findall(r"^\* \[(.+?)\]\((.+?)\)$", text, flags=re.M):
        page = read(f"mecaniques/{href}")
        desc = re.search(r"description: >-\n  (.+)", page).group(1)
        rows.append((title, desc, href))
    intro = "\n".join(l for l in lines[1:] if not l.startswith("* [")).strip()
    write("mecaniques/README.md", front(*pages["mecaniques/README.md"]) + f"{lines[0]}\n\n{intro}\n\n{cards(rows)}\n")

# Pages principales
text = read("regles.md")
if not text.startswith("---"):
    text = wrap(text, "Le chat public est coupé", "warning")
    text = wrap(text, "Le cycle jour/nuit alterne", "info")
    text = wrap(text, "Certains rôles peuvent annuler", "info")
    text = wrap(text, "La victoire est annoncée", "success")
    write("regles.md", front(*pages["regles.md"]) + text)

text = read("camps.md")
if not text.startswith("---"):
    for c in camp_by_name.values():
        text = re.sub(rf"^(\| ){c['name']}( \|)", rf'\1<mark style="color:{c["color"]};">**{c["name"]}**</mark>\2', text, flags=re.M)
        text = re.sub(rf"^## {c['name']}$", f"## {c['emoji']} {c['name']}", text, flags=re.M)
    text = text.replace("## Duo Todoroki (camp secret)", "## 🟠 Duo Todoroki (camp secret)")
    text = wrap(text, "Au bout d'1 minute de jeu, Shoto a 20 %", "warning")
    text = wrap(text, "Un joueur transformé en Brainless", "info")
    write("camps.md", front(*pages["camps.md"]) + text)

text = read("heberger.md")
if not text.startswith("---"):
    text = wrap(text, "La génération remplace tout le terrain", "danger")
    text = wrap(text, "La liste blanche du serveur", "info")
    write("heberger.md", front(*pages["heberger.md"]) + text)

for path in ("commandes.md", "glossaire.md"):
    text = read(path)
    if not text.startswith("---"):
        write(path, front(*pages[path]) + text)

text = read("README.md")
if not text.startswith("---"):
    rows = [
        ("📜 Déroulement d'une partie", pages["regles.md"][1], "regles.md"),
        ("🛡️ Camps et équipes", pages["camps.md"][1], "camps.md"),
        ("🎭 Rôles", pages["roles/README.md"][1], "roles/README.md"),
        ("⚙️ Mécaniques communes", pages["mecaniques/README.md"][1], "mecaniques/README.md"),
        ("⌨️ Commandes", pages["commandes.md"][1], "commandes.md"),
        ("🖥️ Héberger une partie", pages["heberger.md"][1], "heberger.md"),
    ]
    write("README.md", front(*pages["README.md"]) + text.rstrip() + "\n\n## Par où commencer\n\n" + cards(rows) + "\n")
