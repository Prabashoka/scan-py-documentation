project = "scan-py"
author = "scan-py contributors"
copyright = "2026, scan-py contributors"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_book_theme"
html_title = "scan-py documentation"
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/Prabashoka/scan-py-documentation",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs",
    "home_page_in_toc": True,
}

myst_heading_anchors = 3
