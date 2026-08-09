# -*- coding: utf-8 -*-
# MOTORE DI RENDERING GENERICO — non contiene nulla di specifico alla singola settimana.
# Tutto il contenuto (Vangelo, glosse, santi, ecc.) viene da build_apparato.py e build_document.py,
# che vanno rigenerati ogni volta con i dati della domenica/festa corrente.
import html as H
from build_apparato import GOSPEL_SEGMENTS, ANCHORS
from build_document import (
    author_sequence, SOURCE_NAMES, SOURCE_LETTERS, SOURCE_COLORS, CONCEPTS, THREADS, SAINTS, APPROFONDIMENTI,
    SOURCE_ORDER, GOSPEL_REF, LITURGICAL_LABEL, FOOTER_CREDITS, DOC_TITLE,
)

CSS = """
:root {
  --paper: #faf9f6;
  --panel: #efede7;
  --panel-line: #d8d4ca;
  --ink: #1c1a17;
  --ink-soft: #4a4640;
  --muted-solid: #78726A;
  --rule: #2c2924;
  --badge-ink: #f5f3ee;

  /* scala tipografica unica per tutto il documento */
  --fs-h1: 17pt;
  --fs-h2: 13.5pt;
  --fs-thesis: 11.8pt;
  --fs-body: 10.6pt;
  --fs-caption: 8.3pt;
  --lh-body: 1.52;
}
* { box-sizing: border-box; }
html, body { background: var(--paper); color: var(--ink); margin: 0; }
body { font-family: -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif; }
.page {
  width: 162.56mm;
  padding: 15mm 9.5mm 15mm;
  page-break-after: always;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
}
.page:last-child { page-break-after: auto; }
.concept, .thread { break-inside: avoid; }
footer.credits { break-inside: avoid; }

.eyebrow { font-size: var(--fs-caption); letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted-solid); font-weight: 600; margin: 0 0 2.5mm; }
h1 { font-family: Palatino, "Palatino Linotype", "Iowan Old Style", Georgia, serif; font-size: var(--fs-h1); font-weight: 600; line-height: 1.25; margin: 0 0 2mm; }
h2 { font-family: Palatino, "Palatino Linotype", "Iowan Old Style", Georgia, serif; font-size: var(--fs-h2); font-weight: 600; margin: 0 0 3mm; }
.sub { font-size: var(--fs-caption); color: var(--ink-soft); margin: 0 0 4.5mm; line-height: var(--lh-body); }
hr.rule { border: none; border-top: 0.5pt solid var(--rule); margin: 3mm 0 5mm; }

.badge {
  width: 5.4mm; height: 5.4mm; flex: none;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 7.6pt; font-weight: 700; border-radius: 50%;
  background: var(--rule); color: var(--badge-ink);
}

/* ---- Author page: row grid, gospel left / glosses right ---- */
.author-grid { display: grid; grid-template-columns: 46mm 1fr; column-gap: 4mm; }
.g-row { display: contents; }
.g-left, .g-right { padding-bottom: 4.5mm; }
.g-left {
  font-family: Palatino, "Palatino Linotype", "Iowan Old Style", Georgia, serif;
  font-size: var(--fs-body); line-height: var(--lh-body); color: var(--ink); text-align: left;
  border-right: 0.5pt solid var(--panel-line);
  padding-right: 3.5mm; padding-top: 0.3mm;
}
.g-left .nn { font-weight: 700; font-size: 7pt; color: var(--muted-solid); vertical-align: super; }
.anchor-link { color: inherit; text-decoration: none; border-bottom: 0.6pt dotted var(--muted-solid); }
.back-link { font-size: var(--fs-caption); color: var(--muted-solid); text-decoration: none; border-bottom: 0.5pt dotted var(--muted-solid); }
.toc-link { color: var(--ink); text-decoration: none; }
.toc-link:hover { text-decoration: underline; }
.g-right { padding-top: 0.3mm; }
.g-right.empty { padding-bottom: 4.5mm; }
.connector { font-style: italic; font-size: var(--fs-caption); color: var(--muted-solid); margin: 0 0 1.2mm; }
.thesis { font-weight: 700; font-size: var(--fs-thesis); line-height: 1.32; margin: 0 0 1mm; color: var(--ink); }
.body-text { font-size: var(--fs-body); line-height: var(--lh-body); color: var(--ink-soft); margin: 0; }
.row-divider { border-top: 0.4pt dotted var(--panel-line); }

/* ---- Concepts page ---- */
.concept { margin-bottom: 8mm; }
.concept-title { font-family: Palatino, Georgia, serif; font-weight: 700; font-size: var(--fs-h2); margin: 0 0 1.6mm; }
.concept-intro { font-size: var(--fs-body); color: var(--ink-soft); line-height: var(--lh-body); margin: 0 0 3.2mm; }
.view-row { display: grid; grid-template-columns: 6mm 1fr; gap: 0 3mm; margin-bottom: 2.6mm; align-items: start; }
.view-row .source-name { font-size: var(--fs-caption); letter-spacing: 0.05em; text-transform: uppercase; color: var(--muted-solid); font-weight: 700; margin: 0 0 0.6mm; }
.view-row .view-text { font-size: var(--fs-body); line-height: var(--lh-body); color: var(--ink-soft); margin: 0; }

/* ---- Threads page ---- */
.thread { margin-bottom: 7.5mm; }
.thread-title { font-family: Palatino, Georgia, serif; font-weight: 700; font-size: var(--fs-h2); margin: 0 0 2mm; }
.thread-path { font-size: var(--fs-thesis); font-weight: 600; margin: 0 0 2.4mm; display: flex; align-items: center; gap: 1.8mm; flex-wrap: wrap; }
.thread-path .num-tag { font-family: Palatino, Georgia, serif; font-weight: 700; border: 0.6pt solid var(--rule); border-radius: 50%; width: 6.2mm; height: 6.2mm; display: inline-flex; align-items: center; justify-content: center; font-size: 9pt; color: var(--ink); text-decoration: none; }
.thread-path .arrow { color: var(--muted-solid); }
.thread-note { font-size: var(--fs-body); line-height: var(--lh-body); color: var(--ink-soft); margin: 0 0 2mm; text-align: justify; }
.thread-saint { font-size: var(--fs-caption); color: var(--muted-solid); margin: 0; }
.thread-saint a { color: var(--muted-solid); }

/* ---- Saints page ---- */
.saint-head { display: flex; align-items: baseline; gap: 3.5mm; margin-bottom: 1.5mm; }
.saint-name { font-family: Palatino, Georgia, serif; font-weight: 700; font-size: var(--fs-h1); }
.saint-dates { font-size: var(--fs-body); color: var(--muted-solid); }
.saint-theme { font-size: var(--fs-body); font-style: italic; color: var(--ink-soft); margin: 0 0 5mm; }
.saint-block-label { font-size: var(--fs-caption); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted-solid); font-weight: 700; margin: 0 0 1.6mm; }
.saint-episode { font-size: var(--fs-body); line-height: var(--lh-body); color: var(--ink); margin: 0 0 5.5mm; text-align: justify; }
.saint-connection {
  font-size: var(--fs-body); line-height: var(--lh-body); color: var(--ink-soft); margin: 0 0 4mm;
  background: var(--panel); border-left: 1mm solid var(--rule); border-radius: 1mm;
  padding: 4mm 4.5mm;
}
.saint-source { font-size: var(--fs-caption); color: var(--muted-solid); font-style: italic; }

/* ---- Approfondimenti ---- */
.approf-index { columns: 1; margin-bottom: 6mm; }
.approf-index-item { display: block; font-size: var(--fs-body); line-height: 1.9; }
.approf-index-item .num-tag {
  font-family: Palatino, Georgia, serif; font-weight: 700; border: 0.5pt solid var(--rule);
  border-radius: 50%; width: 5.5mm; height: 5.5mm; display: inline-flex; align-items: center;
  justify-content: center; font-size: 8pt; margin-right: 2mm;
}
.approfondimento { margin-bottom: 7mm; break-inside: avoid; }
.approfondimento .a-title { font-family: Palatino, Georgia, serif; font-weight: 700; font-size: var(--fs-h2); margin: 0 0 2.2mm; }
.approfondimento .a-text { font-size: var(--fs-body); line-height: var(--lh-body); color: var(--ink); text-align: justify; margin: 0 0 2.2mm; }
.approfondimento .a-footer { display: flex; flex-direction: column; align-items: flex-start; gap: 1mm; }
.vedi-anche { font-size: var(--fs-caption); color: var(--muted-solid); }
.vedi-anche a { color: var(--muted-solid); }

footer.credits { margin-top: 7mm; padding-top: 3mm; border-top: 0.5pt solid var(--panel-line); font-size: var(--fs-caption); color: var(--muted-solid); line-height: var(--lh-body); }

@page { size: 162.56mm 216.75mm; margin: 0; }
"""


def esc(s):
    return H.escape(s, quote=False)


def badge_html(slug):
    letter = SOURCE_LETTERS[slug]
    colors = SOURCE_COLORS.get(slug, {"bg": "#2c2924", "text": "#f5f3ee"})
    return f'<span class="badge" style="background:{colors["bg"]}; color:{colors["text"]};">{letter}</span>'


def gospel_structured_by_anchor():
    """Per ogni numero di ancora, lista di segmenti (pre, ancorato, post) - piu' di uno se
    l'ancora compare su piu' porzioni del Vangelo. 'ancorato' va reso in grassetto/link."""
    out = {}
    for pre, anchored, post, num, mark in GOSPEL_SEGMENTS:
        out.setdefault(num, []).append((pre or "", anchored, post or ""))
    return out


def gospel_plain_by_anchor(structured):
    """Solo testo piano (per le stime di altezza riga)."""
    out = {}
    for num, segs in structured.items():
        out[num] = " ".join((pre + anchored + post).strip() for pre, anchored, post in segs)
    return out


def gospel_html_for_anchor(num, link_target=None):
    segs = GOSPEL_STRUCTURED.get(num, [])
    parts = []
    for j, (pre, anchored, post) in enumerate(segs):
        if j > 0:
            parts.append(" ")
        if pre:
            parts.append(esc(pre))
        bold = f'<b>{esc(anchored)}</b>'
        if link_target:
            parts.append(f'<a class="anchor-link" href="#{link_target}">{bold}</a>')
        else:
            parts.append(bold)
        if post:
            parts.append(esc(post))
    return "".join(parts)


GOSPEL_STRUCTURED = gospel_structured_by_anchor()
GOSPEL_BY_ANCHOR = gospel_plain_by_anchor(GOSPEL_STRUCTURED)
ANCHOR_LABELS = {a["num"]: a["label"] for a in ANCHORS}
ANCHOR_ORDER = [a["num"] for a in ANCHORS]
SAINT_NAMES_BY_SLUG = {s["slug"]: s["name"] for s in SAINTS}

# ancore -> lista di (lettera_filo, titolo_filo), per i link di ritorno negli approfondimenti
THREADS_BY_ANCHOR = {}
for _t in THREADS:
    _letter = _t["title"].split()[1]
    for _n in _t["path"]:
        THREADS_BY_ANCHOR.setdefault(_n, []).append(_letter)


MM_PER_PT = 0.3528
FS_BODY, LH_BODY = 10.6, 1.52
FS_THESIS, LH_THESIS = 11.8, 1.32
FS_CAPTION, LH_CAPTION = 8.3, 1.3
LEFT_CHARS_PER_LINE = 25
THESIS_CHARS_PER_LINE = 46
BODY_CHARS_PER_LINE = 52
CAPTION_CHARS_PER_LINE = 61
ROW_PAD_MM = 4.2
SAFETY_MARGIN_MM = 6  # margine di sicurezza contro sottostima altezza riga

PAGE_H_MM = 216.75
PAGE_PAD_MM = 30  # 15 top + 15 bottom
HEADER_FULL_MM = 24  # eyebrow + h1 + sub (2 righe) + hr
HEADER_CONT_MM = 8   # solo eyebrow "continua"


def _lines(text, chars_per_line):
    import math
    return max(1, math.ceil(len(text) / chars_per_line))


def _line_h_mm(fs, lh):
    return fs * lh * MM_PER_PT


def row_height_mm(gospel_chunk, connector, thesis, body):
    left_h = _lines(gospel_chunk, LEFT_CHARS_PER_LINE) * _line_h_mm(FS_BODY, LH_BODY)
    right_h = 0.0
    if connector:
        right_h += _lines(connector, CAPTION_CHARS_PER_LINE) * _line_h_mm(FS_CAPTION, LH_CAPTION) + 1.2
    if thesis:
        right_h += _lines(thesis, THESIS_CHARS_PER_LINE) * _line_h_mm(FS_THESIS, LH_THESIS) + 1.0
    if body:
        right_h += _lines(body, BODY_CHARS_PER_LINE) * _line_h_mm(FS_BODY, LH_BODY)
    return max(left_h, right_h) + ROW_PAD_MM


def paginate_rows(row_specs):
    """row_specs: lista di (num, gospel_chunk, connector, thesis, body). Ritorna lista di chunk (liste di row_specs)."""
    chunks = []
    current = []
    budget = PAGE_H_MM - PAGE_PAD_MM - HEADER_FULL_MM - SAFETY_MARGIN_MM
    used = 0.0
    for spec in row_specs:
        num, gospel_chunk, connector, thesis, body = spec
        h = row_height_mm(gospel_chunk, connector, thesis, body)
        if current and used + h > budget:
            chunks.append(current)
            current = []
            used = 0.0
            budget = PAGE_H_MM - PAGE_PAD_MM - HEADER_CONT_MM - SAFETY_MARGIN_MM
        current.append(spec)
        used += h
    if current:
        chunks.append(current)
    return chunks


def render_author_page(slug):
    name = SOURCE_NAMES[slug]
    seq = author_sequence(slug)
    seq_by_num = {n: (label, connector, thesis, body) for n, label, connector, thesis, body in seq}

    row_specs = []
    for num in ANCHOR_ORDER:
        gospel_chunk = GOSPEL_BY_ANCHOR.get(num, "")
        if num in seq_by_num:
            _, connector, thesis, body = seq_by_num[num]
        else:
            connector, thesis, body = None, None, None
        row_specs.append((num, gospel_chunk, connector, thesis, body))

    chunks = paginate_rows(row_specs)
    parts = []
    for i, chunk in enumerate(chunks):
        parts.append('<div class="page">')
        if i == 0:
            parts.append(f'<p class="eyebrow">{esc(LITURGICAL_LABEL)} · {esc(GOSPEL_REF)} · pensiero di un solo autore</p>')
            parts.append(f'<h1>{esc(name)}</h1>')
        else:
            parts.append(f'<p class="eyebrow">{esc(name)} · segue</p>')
        parts.append('<hr class="rule">')
        parts.append('<div class="author-grid">')
        for num, gospel_chunk, connector, thesis, body in chunk:
            gospel_html = gospel_html_for_anchor(num, link_target=f"approf-{num}")
            parts.append('<div class="g-row">')
            parts.append(f'<div class="g-left" id="gospel-{slug}-{num}">{gospel_html}<span class="nn"> {num}</span></div>')
            if thesis:
                parts.append('<div class="g-right">')
                if connector:
                    parts.append(f'<p class="connector">↳ {esc(connector)}</p>')
                parts.append(f'<p class="thesis">{esc(thesis)}</p>')
                parts.append(f'<p class="body-text">{esc(body)}</p>')
                parts.append('</div>')
            else:
                parts.append('<div class="g-right empty"></div>')
            parts.append('</div>')
        parts.append('</div>')  # .author-grid
        parts.append('</div>')  # .page
    return "".join(parts)


def render_concepts_page():
    parts = ['<div class="page">']
    parts.append('<p class="eyebrow">Tra le fonti</p>')
    parts.append('<h1>Concetti ricorrenti</h1>')
    parts.append('<p class="sub">Temi su cui più fonti convergono, con lo sguardo proprio di ciascuna affiancato.</p>')
    parts.append('<hr class="rule">')
    for c in CONCEPTS:
        parts.append('<div class="concept">')
        parts.append(f'<p class="concept-title">{esc(c["title"])}</p>')
        parts.append(f'<p class="concept-intro">{esc(c["intro"])}</p>')
        for slug, text in c["views"]:
            name = SOURCE_NAMES[slug]
            parts.append('<div class="view-row">')
            parts.append(badge_html(slug))
            parts.append(f'<div><p class="source-name">{esc(name)}</p><p class="view-text">{esc(text)}</p></div>')
            parts.append('</div>')
        parts.append('</div>')
    parts.append('</div>')
    return "".join(parts)


def render_threads_page():
    parts = ['<div class="page">']
    parts.append('<p class="eyebrow">Per la predicazione</p>')
    parts.append('<h1>Sintesi — fili logici</h1>')
    parts.append('<p class="sub">Percorsi che ricombinano gli ancoraggi tra le fonti in una possibile narrazione. Sono ipotesi di lavoro: la scelta e l\'ordine restano da vagliare.</p>')
    parts.append('<hr class="rule">')
    for t in THREADS:
        letter = t["title"].split()[1]  # "Filo A — ..." -> "A"
        parts.append(f'<div class="thread" id="filo-{letter.lower()}">')
        parts.append(f'<p class="thread-title">{esc(t["title"])}</p>')
        parts.append('<div class="thread-path">')
        for i, n in enumerate(t["path"]):
            if i > 0:
                parts.append('<span class="arrow">&#8594;</span>')
            parts.append(f'<a class="num-tag" href="#approf-{n}">{n}</a>')
        parts.append('</div>')
        parts.append(f'<p class="thread-note">{esc(t["note"])}</p>')
        saint_link = t.get("saint_link")
        if saint_link:
            parts.append(
                f'<p class="thread-saint">{saint_link["emoji"]} '
                f'<a href="#santo-{saint_link["slug"]}">Eco in {esc(SAINT_NAMES_BY_SLUG.get(saint_link["slug"], saint_link["slug"]))}</a>'
                f' — {esc(saint_link["phrase"])}</p>'
            )
        parts.append('</div>')
    parts.append('</div>')
    return "".join(parts)


def linked_text(text, link_phrases):
    """Escapa il testo e trasforma le frasi indicate in link verso l'approfondimento."""
    html = esc(text)
    for phrase, num in (link_phrases or []):
        escaped_phrase = esc(phrase)
        link = f'<a class="anchor-link" href="#approf-{num}">{escaped_phrase}</a>'
        html = html.replace(escaped_phrase, link, 1)
    return html


def render_saints_page(saint, is_last=False):
    parts = [f'<div class="page" id="santo-{saint["slug"]}">']
    parts.append('<p class="eyebrow">Un episodio, per la predicazione</p>')
    parts.append('<div class="saint-head">')
    parts.append(f'<span class="saint-name">{esc(saint["name"])}</span>')
    parts.append(f'<span class="saint-dates">{esc(saint["dates"])}</span>')
    parts.append('</div>')
    parts.append(f'<p class="saint-theme">{esc(saint["theme"])}</p>')
    parts.append('<hr class="rule">')
    parts.append('<p class="saint-block-label">Episodio</p>')
    parts.append(f'<p class="saint-episode">{esc(saint["episode"])}</p>')
    parts.append('<p class="saint-block-label">Collegamento con il Vangelo</p>')
    connection_html = linked_text(saint["connection"], saint.get("link_phrases"))
    parts.append(f'<p class="saint-connection">{connection_html}</p>')
    parts.append(f'<p class="saint-source">Fonte: {esc(saint["source"])}</p>')
    if is_last:
        parts.append(f'<footer class="credits">{esc(FOOTER_CREDITS)}</footer>')
    parts.append('</div>')
    return "".join(parts)


def render_approfondimenti_section():
    parts = ['<div class="page">']
    parts.append('<p class="eyebrow">Per capire meglio</p>')
    parts.append('<h1 id="indice-approfondimenti">Approfondimenti</h1>')
    parts.append('<p class="sub">Uno per ciascuno dei dieci ancoraggi usati in tutto il documento: contesto biblico e teologico più esteso, per chi vuole andare oltre la sintesi.</p>')
    parts.append('<hr class="rule">')
    parts.append('<div class="approf-index">')
    for num in ANCHOR_ORDER:
        title = APPROFONDIMENTI[num]["title"]
        parts.append(f'<a class="approf-index-item toc-link" href="#approf-{num}"><span class="num-tag">{num}</span>{esc(title)}</a>')
    parts.append('</div>')
    parts.append('<hr class="rule">')
    for num in ANCHOR_ORDER:
        entry = APPROFONDIMENTI[num]
        parts.append(f'<div class="approfondimento" id="approf-{num}">')
        parts.append(f'<p class="a-title">{num}. {esc(entry["title"])}</p>')
        parts.append(f'<p class="a-text">{esc(entry["text"])}</p>')
        parts.append('<div class="a-footer">')
        parts.append(f'<a class="back-link" href="#indice-approfondimenti">↑ indice</a>')
        gospel_links = [f'<a href="#gospel-{slug}-{num}">{esc(SOURCE_NAMES[slug])}</a>' for slug in SOURCE_ORDER]
        parts.append(f'<span class="vedi-anche">↩ Vangelo: {" · ".join(gospel_links)}</span>')
        vedi_anche = entry.get("vedi_anche")
        if vedi_anche:
            saint_by_slug = {s["slug"]: s["name"] for s in SAINTS}
            links = [f'<a href="#santo-{slug}">{esc(saint_by_slug[slug])}</a>' for slug in vedi_anche if slug in saint_by_slug]
            if links:
                parts.append(f'<span class="vedi-anche">↩ Santi: {" · ".join(links)}</span>')
        thread_letters = THREADS_BY_ANCHOR.get(num)
        if thread_letters:
            thread_links = [f'<a href="#filo-{l.lower()}">Filo {l}</a>' for l in thread_letters]
            parts.append(f'<span class="vedi-anche">↩ Fili logici: {" · ".join(thread_links)}</span>')
        parts.append('</div>')
        parts.append('</div>')
    parts.append(f'<footer class="credits">{esc(FOOTER_CREDITS)}</footer>')
    parts.append('</div>')
    return "".join(parts)


def build():
    body_parts = []
    for slug in SOURCE_ORDER:
        body_parts.append(render_author_page(slug))
    body_parts.append(render_concepts_page())
    body_parts.append(render_threads_page())
    for saint in SAINTS:
        body_parts.append(render_saints_page(saint, is_last=False))
    body_parts.append(render_approfondimenti_section())
    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>{esc(DOC_TITLE)}</title>
<style>{CSS}</style>
</head>
<body>
{''.join(body_parts)}
</body>
</html>"""
    return html


if __name__ == "__main__":
    out = build()
    with open("vangelo_documento_finale.html", "w", encoding="utf-8") as f:
        f.write(out)
    print("scritto vangelo_documento_finale.html —", len(out), "caratteri")
