# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # pour que Sphinx trouve elabforms

# -- Project information -----------------------------------------------------

project = 'elabforms'
copyright = '2025, Fatai Idrissou, Sylvain Takerkart'
author = 'Fatai Idrissou, Sylvain Takerkart'
release = '0.0.6'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',     # Pour docstrings style Google/Numpy
    'sphinx.ext.viewcode',     # Ajoute les liens vers le code source
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # Tu peux aussi essayer 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Language ----------------------------------------------------------------
language = 'en'
