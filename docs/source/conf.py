# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('.'))

project = 'sf311'
copyright = '2023, Desmond L Molloy'
author = 'Desmond L Molloy'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['autoapi.extension', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.duration', 'sphinx.ext.viewcode', 'sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

autodoc_typehints = 'both'
autodoc_default_options = {'members': True, 'undoc-members': True, 'show-inheritance': True, 'show-module-summary': True, 'special-members': '__init__'}
autoapi_type = 'python'
autoapi_dirs = ['../../sf311']
autoapi_template_dir = '_templates/autoapi'
autoapi_options = ['members', 'undoc-members', 'show-inheritance', 'show-module-summary', 'special-members', 'imported-members']

autosummary_generate = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
rst_prolog = """
.. |project_name| replace:: {project_name}
""".format(project_name=project)

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

html_css_files = [
    'css/custom.css',
]

html_js_files = [
    'js/custom.js',
]

html_theme_options = {
    'logo': 'logo.png',
    'logo_name': True,
    'logo_text_align': 'center',
    'description': 'Put your repo description here.',
    'github_button': True,
    'github_banner': True,
    'show_powered_by': False}

def contains(seq, item):
    return item in seq

def prepare_jinja_env(jinja_env)->None:
    jinja_env.tests['contains'] = contains

autoapi_prepare_jinja_env = prepare_jinja_env
