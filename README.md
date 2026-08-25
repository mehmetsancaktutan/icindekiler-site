# Yuppa website

Static, GitHub Pages-ready website for Yuppa in English, Turkish, German, French and Spanish.

## Publishing

The GitHub Actions workflow in `.github/workflows/pages.yml` publishes the repository whenever the `main` branch is pushed. Enable **GitHub Pages → GitHub Actions** in the repository settings once.

## Editing

Edit copy and legal content in `build_site.py`, then regenerate the checked-in pages:

```sh
python3 build_site.py
```

The root is English. Turkish, German, French and Spanish are served from `/tr`, `/de`, `/fr` and `/es`. Compatibility routes under `/apps/yuppa/` and `/apps/yukka/` keep legal links in released app builds working.
