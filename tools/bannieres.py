# Images du GitBook, générées sans aucun visuel officiel : fond sombre, halo, lignes de vitesse façon manga
# et trame de points aux couleurs du camp.
#   banner(...) : bannière large en haut de page (1990 x 480), texte à gauche
#   card(...)   : image de carte (800 x 450), texte centré
import math, os, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

FONTS = "C:/Windows/Fonts/"
BG = (11, 13, 19)

COLORS = {
    "heros": (74, 222, 128),
    "vilains": (244, 63, 94),
    "preceptes": (168, 85, 247),
    "solitaires": (245, 158, 11),
    "neutre": (52, 211, 153),
}


def title_font(size):
    return ImageFont.truetype(FONTS + "impact.ttf", size)


def text_font(size):
    return ImageFont.truetype(FONTS + "segoeuib.ttf", size)


def background(w, h, color, seed, cx, scale):
    rnd = random.Random(seed)
    cy = h / 2

    # Halo de couleur
    glow = Image.new("RGB", (w, h), BG)
    g = ImageDraw.Draw(glow)
    rmax = int(620 * scale)
    for r in range(rmax, 0, -max(1, int(20 * scale))):
        t = 1 - r / rmax
        c = tuple(int(BG[i] + (color[i] - BG[i]) * (t ** 2) * 0.55) for i in range(3))
        g.ellipse([cx - r * 1.6, cy - r, cx + r * 1.6, cy + r], fill=c)
    img = glow.filter(ImageFilter.GaussianBlur(40 * scale))

    # Lignes de vitesse qui partent du halo
    lines = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(lines)
    for _ in range(140):
        a = rnd.uniform(0, 2 * math.pi)
        r1 = rnd.uniform(140, 260) * scale
        r2 = r1 + rnd.uniform(300, 1100) * scale
        width = max(1, int(rnd.choice([1, 1, 2, 2, 3]) * max(scale, 0.7)))
        d.line([(cx + math.cos(a) * r1 * 1.4, cy + math.sin(a) * r1), (cx + math.cos(a) * r2 * 1.4, cy + math.sin(a) * r2)],
               fill=color + (rnd.randint(25, 80),), width=width)
    img.paste(lines, (0, 0), lines)

    # Trame de points, plus marquée près du halo
    dots = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(dots)
    step = max(10, int(22 * scale))
    for y in range(0, h + step, step):
        for x in range(0, w + step, step):
            t = max(0, 1 - abs(x - cx) / (w * 0.55))
            if t <= 0:
                continue
            r = (1 + 4 * t * (0.6 + 0.4 * math.sin(y / 40 + x / 90))) * max(scale, 0.6)
            ox = step / 2 if (y // step) % 2 else 0
            d.ellipse([x + ox - r, y - r, x + ox + r, y + r], fill=(255, 255, 255, int(14 + 26 * t)))
    img.paste(dots, (0, 0), dots)
    return img


def wrap(text, font, width):
    rows, row = [], ""
    for word in text.split():
        test = (row + " " + word).strip()
        if font.getlength(test) > width and row:
            rows.append(row)
            row = word
        else:
            row = test
    if row:
        rows.append(row)
    return rows


def fit(text, max_width, size, minimum):
    while title_font(size).getlength(text) > max_width and size > minimum:
        size -= 4
    return title_font(size), size


def banner(path, title, kicker, subtitle, color, seed):
    W, H = 1990, 480
    img = background(W, H, color, seed, W * 0.78, 1)

    # Voile sombre à gauche pour la lisibilité du texte
    shade = Image.new("L", (W, 1))
    for x in range(W):
        shade.putpixel((x, 0), int(235 * max(0, 1 - x / (W * 0.62)) ** 1.4))
    img.paste(Image.new("RGB", (W, H), BG), (0, 0), shade.resize((W, H)))

    d = ImageDraw.Draw(img)
    x0 = 120
    d.rectangle([x0, 118, x0 + 70, 126], fill=color)
    d.text((x0 + 90, 104), kicker.upper(), font=text_font(30), fill=color)

    f, size = fit(title.upper(), W * 0.62, 150, 70)
    y = 150
    d.text((x0 + 6, y + 6), title.upper(), font=f, fill=tuple(int(c * 0.45) for c in color))
    d.text((x0, y), title.upper(), font=f, fill=(245, 247, 250))

    sf = text_font(34)
    for i, row in enumerate(wrap(subtitle, sf, W * 0.55)[:2]):
        d.text((x0, y + size + 28 + i * 46), row, font=sf, fill=(200, 205, 214))

    d.rectangle([0, H - 10, W, H], fill=color)
    img.convert("RGB").save(path, quality=88, optimize=True)


def card(path, title, kicker, color, seed):
    W, H = 800, 450
    img = background(W, H, color, seed, W / 2, 0.55)
    # Assombrit le centre pour que le nom ressorte
    veil = Image.new("L", (W, H), 0)
    ImageDraw.Draw(veil).ellipse([W * 0.12, H * 0.28, W * 0.88, H * 0.72], fill=120)
    img.paste(Image.new("RGB", (W, H), BG), (0, 0), veil.filter(ImageFilter.GaussianBlur(40)))

    d = ImageDraw.Draw(img)
    f, size = fit(title.upper(), W * 0.84, 104, 44)
    tw = f.getlength(title.upper())
    x, y = (W - tw) / 2, H / 2 - size * 0.62
    d.text((x + 5, y + 5), title.upper(), font=f, fill=tuple(int(c * 0.45) for c in color))
    d.text((x, y), title.upper(), font=f, fill=(245, 247, 250))

    kf = text_font(24)
    kw = kf.getlength(kicker.upper())
    d.text(((W - kw) / 2, y - 44), kicker.upper(), font=kf, fill=color)
    d.rectangle([0, H - 8, W, H], fill=color)
    img.convert("RGB").save(path, quality=88, optimize=True)
