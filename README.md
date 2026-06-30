# scan-py documentation website

This repository builds a Sphinx documentation website with the `sphinx-book-theme`, similar to the structure used by the `sdt-python` documentation.

## Local preview

Install the documentation dependencies and build the site:

```bash
python -m pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` to preview the generated site.

## Publish on GitHub Pages

1. Commit and push these files to the `main` branch.
2. In the GitHub repository, open **Settings** > **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Push to `main`, or run the **Build and deploy documentation** workflow manually from the **Actions** tab.

After GitHub finishes building the site, it will be available at:

```text
https://prabashoka.github.io/scan-py-documentation/
```

The Sphinx home page is `docs/index.md`. Add more pages to `docs/` and list them in the `{toctree}` block in `docs/index.md`.
