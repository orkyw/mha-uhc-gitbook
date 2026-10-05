# Deuxième passe de design, à lancer après embellir.py :
#   - bannière générée en haut de chaque page (le titre GitBook est masqué, la bannière le porte)
#   - cartes illustrées (accueil, rôles, camps, mécaniques)
#   - fiches de rôle : tableau d'identité, un sous-titre par pouvoir et un badge pour son temps de recharge
# Une page déjà traitée (en-tête "layout:") est laissée telle quelle.
import os, re, shutil
from bannieres import COLORS, banner, card

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
assets = os.path.join(root, ".gitbook", "assets")
for sub in ("banners", "cards"):
    shutil.rmtree(os.path.join(assets, sub), ignore_errors=True)
    os.makedirs(os.path.join(assets, sub))

CAMPS = {
    "heros": ("Héros", "🟢", "green"),
    "vilains": ("Vilains", "🔴", "red"),
    "preceptes": ("Préceptes", "🟣", "purple"),
    "solitaires": ("Solitaires", "🟠", "orange"),
}
SINGULAR = {"heros": "Héros", "vilains": "Vilain", "preceptes": "Précepte", "solitaires": "Solitaire"}
SECTIONS = {
    "regles.md": ("📜", "Règles"),
    "camps.md": ("🛡️", "Camps"),
    "roles/README.md": ("🎭", "Rôles"),
    "mecaniques/README.md": ("⚙️", "Mécaniques"),
    "commandes.md": ("⌨️", "Commandes"),
    "heberger.md": ("🖥️", "Hôte"),
}
seed = 0


def read(path):
    with open(os.path.join(root, path), encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(os.path.join(root, path), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def split_page(path):
    text = read(path)
    m = re.match(r"^---\ndescription: >-\n  (.+)\nicon: (.+)\n(?:layout:\n(?:  .*\n)*)?---\n\n# (.+)\n\n?", text)
    return m.group(1), m.group(2), m.group(3), text[m.end():]


def rel(path, target):
    return os.path.relpath(os.path.join(root, target), os.path.dirname(os.path.join(root, path))).replace("\\", "/")


def image_name(path):
    return re.sub(r"[/\\]", "-", path[:-3]).replace("-README", "").replace("README", "accueil")


def make_banner(path, title, kicker, subtitle, color):
    global seed
    seed += 1
    name = image_name(path) + ".jpg"
    banner(os.path.join(assets, "banners", name), title, kicker, subtitle, COLORS[color], seed)
    return f".gitbook/assets/banners/{name}"


def make_card(key, title, kicker, color):
    global seed
    seed += 1
    name = key + ".jpg"
    card(os.path.join(assets, "cards", name), title, kicker, COLORS[color], seed)
    return f".gitbook/assets/cards/{name}"


def front(description, icon, wide=False, outline=True):
    return (f"---\ndescription: >-\n  {description}\nicon: {icon}\nlayout:\n"
            + ("  width: wide\n" if wide else "")
            + "  title:\n    visible: false\n  description:\n    visible: false\n"
            f"  tableOfContents:\n    visible: true\n  outline:\n    visible: {'true' if outline else 'false'}\n"
            "  pagination:\n    visible: true\n---\n\n")


def cards(path, rows):
    """rows = [(titre, description, image, page cible)]"""
    body = "".join(
        f'<tr><td><strong>{t}</strong></td><td>{d}</td>'
        f'<td><a href="{rel(path, img)}">{os.path.basename(img)}</a></td>'
        f'<td><a href="{rel(path, target)}">{os.path.basename(target)}</a></td></tr>'
        for t, d, img, target in rows)
    return ('<table data-view="cards"><thead><tr><th></th><th></th>'
            '<th data-hidden data-card-cover data-type="files"></th>'
            '<th data-hidden data-card-target data-type="content-ref"></th></tr></thead>'
            f"<tbody>{body}</tbody></table>")


def finish(path, title, description, icon, body, kicker, color, wide=False, outline=True):
    img = make_banner(path, title, kicker, description, color)
    # Un titre doit toujours être précédé d'une ligne vide
    body = re.sub(r"([^\n])\n(#{2,4} )", r"\1\n\n\2", body.strip())
    write(path, front(description, icon, wide, outline) + f"# {title}\n\n![{title}]({rel(path, img)})\n\n{body}\n")


def badge(info):
    if "x/" in info or "temps de recharge" in info or "utilisations" in info:
        return f'<mark style="color:orange;">**⏱️ {info}**</mark>'
    if "!" in info:
        return f'<mark style="color:blue;">**⌨️ {info}**</mark>'
    return f'<mark style="color:blue;">**🔁 {info}**</mark>'


def power_blocks(section):
    """Dans une section de pouvoirs au pluriel, chaque puce « Nom (recharge) : texte » devient un sous-titre."""
    def repl(m):
        name, info, desc = m.group(1), m.group(2), m.group(3)
        if len(name) > 40:
            return m.group(0)
        return f"### {name}\n\n" + (badge(info) + "\n\n" if info else "") + desc[0].upper() + desc[1:]
    return re.sub(r"^- ([^:\n(]+?)(?: \(([^)\n]+)\))? : (.+)$", repl, section, flags=re.M)


def role_page(path, folder):
    description, icon, title, body = split_page(path)
    camp, emoji, color = CAMPS[folder]

    # Tableau d'identité à la place de la ligne « Camp · Groupe sanguin · cœurs »
    def identity(m):
        camp_cell, blood, hearts = m.group(1), m.group(2), m.group(3)
        hm = re.match(r"(\d+) cœurs(.*)", hearts)
        hearts_cell = f"❤️ **{hm.group(1)}**{hm.group(2)}" if hm else f"❤️ {hearts}"
        return ("| Camp | Groupe sanguin | Cœurs de départ |\n| --- | --- | --- |\n"
                f"| {camp_cell} | 🩸 **{blood}** | {hearts_cell} |")
    body = re.sub(r"^(.+?) · 🩸 Groupe sanguin \*\*(\w+)\*\* · ❤️ \*\*(.+?)\*\*$", identity, body, count=1, flags=re.M)

    # « ## ⚡ Pouvoir actif : Nom (recharge) » -> « ## ⚡ Pouvoir actif » + « ### Nom » + badge
    def single(m):
        emoji_, kind, name, info = m.group(1), m.group(2), m.group(3), m.group(4)
        return f"## {emoji_} {kind}\n\n### {name}" + (f"\n\n{badge(info)}" if info else "")
    body = re.sub(r"^## (\S+) (Pouvoir (?:actif|passif)) : ([^(\n]+?)(?: \(([^)\n]+)\))?$", single, body, flags=re.M)

    # Sections au pluriel : un sous-titre par pouvoir
    parts = re.split(r"(?m)^(?=## )", body)
    body = "".join(power_blocks(p) if re.match(r"## \S+ Pouvoirs (actifs|passifs)", p) else p for p in parts)

    finish(path, title, description, icon, body, f"Rôle · {camp}", folder)
    return title, description


# Fiches de rôle et pages de camp
role_rows = {}
camp_cards = {}
for folder, (camp, emoji, color) in CAMPS.items():
    rows = []
    for name in sorted(os.listdir(os.path.join(root, "roles", folder))):
        path = f"roles/{folder}/{name}"
        if name == "README.md" or "layout:" in read(path)[:400]:
            continue
        title, description = role_page(path, folder)
        img = make_card(f"{folder}-{name[:-3]}", title, SINGULAR[folder], folder)
        rows.append((title, description, img, path))
    role_rows[folder] = rows

    path = f"roles/{folder}/README.md"
    description, icon, title, body = split_page(path)
    intro = body.split("<table")[0].strip()
    camp_cards[folder] = (f"{emoji} {camp}", description, make_card(f"camp-{folder}", camp, "Camp", folder), path)
    finish(path, title, description, icon, (intro + "\n\n" if intro else "") + cards(path, rows), "Camp", folder, wide=True)

# Index des rôles : cartes des camps au-dessus du tableau
path = "roles/README.md"
description, icon, title, body = split_page(path)
body = body.replace("## Index des rôles", "## Les camps\n\n" + cards(path, list(camp_cards.values())) + "\n\n## Index des rôles", 1)
finish(path, title, description, icon, body, "MHA UHC · Guide", "neutre", wide=True)

# Mécaniques
mech_colors = {"qg-des-preceptes": "preceptes", "alters-eparpilles": "heros", "yuei": "heros", "combat": "vilains"}
path = "mecaniques/README.md"
description, icon, title, body = split_page(path)
rows = []
for t, href in re.findall(r'<strong>(.+?)</strong>.*?<a href="(.+?\.md)"', body):
    mpath = f"mecaniques/{href}"
    md, mi, mt, mb = split_page(mpath)
    color = mech_colors.get(href[:-3], "neutre")
    finish(mpath, mt, md, mi, mb, "Mécanique", color)
    rows.append((mt, md, make_card(f"mecanique-{href[:-3]}", mt, "Mécanique", color), mpath))
intro = body.split("<table")[0].strip()
finish(path, title, description, icon, intro + "\n\n" + cards(path, rows), "MHA UHC · Guide", "neutre", wide=True)

# Camps : cartes des camps en tête de page
path = "camps.md"
description, icon, title, body = split_page(path)
body = body.replace("## 🟢 Héros", "## Les rôles par camp\n\n" + cards(path, list(camp_cards.values())) + "\n\n## 🟢 Héros", 1)
finish(path, title, description, icon, body, "MHA UHC · Guide", "neutre")

# Autres pages de section
for path in ("regles.md", "commandes.md", "heberger.md", "glossaire.md"):
    description, icon, title, body = split_page(path)
    finish(path, title, description, icon, body, "MHA UHC · Guide", "neutre")

# Accueil : boutons, sections en cartes illustrées, camps
path = "README.md"
description, icon, title, body = split_page(path)
intro = body.split("## Par où commencer")[0].strip()
section_rows = []
for target, (emoji, short) in SECTIONS.items():
    sd = split_page(target)[0]
    st = split_page(target)[2]
    section_rows.append((f"{emoji} {st}", sd, make_card(f"section-{image_name(target)}", short, "Guide", "neutre"), target))
buttons = ('<a href="roles/README.md" class="button primary">🎭 Voir les 31 rôles</a> '
           '<a href="regles.md" class="button secondary">📜 Lire les règles</a> '
           '<a href="commandes.md" class="button secondary">⌨️ Commandes</a>')
home = (f"{buttons}\n\n{intro}\n\n## Par où commencer\n\n{cards(path, section_rows)}\n\n"
        f"## Les camps\n\n{cards(path, list(camp_cards.values()))}")
img = make_banner(path, "MHA UHC", "Minecraft Bedrock · Serveur NEXORA", description, "neutre")
write(path, front(description, icon, wide=True, outline=False) + f"# {title}\n\n![MHA UHC]({img})\n\n{home}\n")
print("ok")
