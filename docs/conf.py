import os
import sys
from datetime import datetime

# make autodoc find your package in src/
sys.path.insert(0, os.path.abspath("../src"))

project = "ci-exercise"
author = "APC524"
year = datetime.now().year
copyright = f"{year}, {author}"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx_markdown_builder",
]

# allow both .rst and .md sources
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = "furo"

# speed up autodoc (optional)
autodoc_default_options = {"members": True, "undoc-members": True}
