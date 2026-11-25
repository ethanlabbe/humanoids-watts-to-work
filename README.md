# Humanoids: Watts to Work

A source-backed engineering library on humanoid robots, from battery power and sensing to motion, useful work, and deployment.

Read it at https://ethanlabbe.github.io/humanoids-watts-to-work/

The book is written in an Obsidian vault and published here with [Quartz](https://quartz.jzhao.xyz/) (MIT licence). `content/` is generated: edit the vault, not this folder.

## Publishing an update

```sh
uv run sync_from_vault.py      # copy the book from the vault into content/
git add -A && git commit -m "Sync from vault" && git push
```

Pushing to `v5` runs `.github/workflows/deploy.yml`, which builds the site and deploys it to GitHub Pages.

Local preview needs Node 22 or later: `npm ci`, then `npx quartz build --serve` (http://localhost:8080).
