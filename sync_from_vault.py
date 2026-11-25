# /// script
# requires-python = ">=3.11"
# ///
"""Copy the textbook from the Obsidian vault into content/ for Quartz.

The vault stays the working copy; this repo only publishes it. Run:

    uv run sync_from_vault.py [VAULT_BOOK_DIR]

What it changes on the way (the vault itself is never written):
- leaves out working files (EXCLUDE below);
- publishes "00 Home.md" as index.md and points [[00 Home]] links at it;
- turns links to left-out notes into plain text;
- moves each note's first "# Heading" into frontmatter `title`, so Quartz
  shows it once (as the page title) instead of twice;
- sets frontmatter `modified` to the vault file's date, since this repo's
  git dates are only publish dates;
- on the home page, drops list items and sections that only pointed at
  left-out notes.
It then lists any wikilink that does not resolve to a published note.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent
CONTENT = REPO / "content"
DEFAULT_SOURCE = Path(
    r"C:\repos\Tracker\Development\P2 - Humanoid Robot Development Map\Humanoids - Watts to Work"
)

HOME = "00 Home"
# Paths relative to the book folder, matched as prefixes.
EXCLUDE = ("99 Templates/", "00 Library/Review Queue.md")

# Target stops at "#", "|" or a table-escaped "\|", so the backslash is not part of it.
WIKILINK = re.compile(r"(!?)\[\[((?:[^\]|#\\]|\\(?!\|))*)(#(?:[^\]|\\]|\\(?!\|))*)?(\\?\|[^\]]*)?\]\]")
H1 = re.compile(r"^# (.+?)\s*$", re.M)


def excluded(rel: str) -> bool:
    return any(rel == p or rel.startswith(p) for p in EXCLUDE)


def rewrite_links(text: str, dropped: set[str], stats: dict) -> str:
    def sub(m: re.Match) -> str:
        bang, target, anchor, alias = m.group(1), m.group(2).strip(), m.group(3) or "", m.group(4) or ""
        if target == HOME:
            stats["home_links"] += 1
            return f"{bang}[[index{anchor}{alias}]]"
        if target in dropped:
            stats["unlinked"] += 1
            return alias.lstrip("\\|") if alias else target
        return m.group(0)

    return WIKILINK.sub(sub, text)


def set_frontmatter(text: str, modified: str) -> str:
    """Move the first H1 into frontmatter `title` (removing it from the body) and
    add `modified` (the vault file's date), keeping any value the note already sets."""
    fm, body = "", text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            fm, body = text[4:end + 1], text[end + 5:]
    m = H1.search(body)
    if m and not re.search(r"^title:", fm, re.M):
        body = body[: m.start()] + body[m.end():].lstrip("\n")
        fm = f"title: {json.dumps(m.group(1), ensure_ascii=False)}\n" + fm
    if not re.search(r"^modified:", fm, re.M):
        fm += f"modified: {modified}\n"
    return f"---\n{fm}---\n\n{body.lstrip(chr(10))}"


def prune_home(text: str, dropped: set[str]) -> str:
    """Drop home-page list items that only linked to left-out notes, then empty sections."""
    names = "|".join(re.escape(n) for n in dropped)
    item = re.compile(rf"^- \[\[({names})(\|[^\]]*)?\]\].*\n", re.M)
    text = item.sub("", text)
    # A heading followed only by blank lines up to the next heading or end of file.
    return re.sub(r"^#{2,6} [^\n]*\n\s*(?=^#{1,6} |\Z)", "", text, flags=re.M)


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    if not (src / f"{HOME}.md").is_file():
        sys.exit(f"not the book folder (no {HOME}.md): {src}")

    notes = sorted(p for p in src.rglob("*.md") if ".obsidian" not in p.parts)
    keep = [p for p in notes if not excluded(p.relative_to(src).as_posix())]
    dropped = {p.stem for p in notes} - {p.stem for p in keep}
    published = {p.stem for p in keep} - {HOME} | {"index"}

    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir()

    stats = {"home_links": 0, "unlinked": 0}
    unresolved: dict[str, set[str]] = {}
    for p in keep:
        rel = p.relative_to(src)
        out = CONTENT / ("index.md" if p.stem == HOME and rel.parent == Path(".") else rel)
        text = p.read_text(encoding="utf-8")
        if p.stem == HOME:
            text = prune_home(text, dropped)
        text = rewrite_links(text, dropped, stats)
        text = set_frontmatter(text, date.fromtimestamp(p.stat().st_mtime).isoformat())
        for m in WIKILINK.finditer(text):
            t = m.group(2).strip()
            if t and t not in published:
                unresolved.setdefault(t, set()).add(rel.as_posix())
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8", newline="\n")

    print(f"source:    {src}")
    print(f"published: {len(keep)} notes  (left out {len(notes) - len(keep)}: {', '.join(sorted(dropped))})")
    print(f"links:     {stats['home_links']} home links -> index, {stats['unlinked']} links to left-out notes made plain text")
    if unresolved:
        print(f"UNRESOLVED wikilinks ({len(unresolved)}):")
        for t, files in sorted(unresolved.items()):
            print(f"  [[{t}]] in {', '.join(sorted(files))}")
    else:
        print("unresolved wikilinks: 0")


if __name__ == "__main__":
    main()
