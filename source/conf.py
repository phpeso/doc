from datetime import datetime
import os

author = 'Anton Smirnov'
copyright = '{}'.format(datetime.now().year)
language = 'en'

html_title = 'Peso for PHP'
html_theme = 'sphinx_book_theme'
templates_path = ["_templates"]
html_sidebars = {
    "**": [
        "navbar-logo.html",
        "icon-links.html",
        "rtd-version.html",
        "search-button-field.html",
        "sbt-sidebar-nav.html",
    ]
}
html_theme_options = {
    'use_edit_page_button': True,
    'icon_links': [
        {
            "name": "GitHub",
            "url": "https://github.com/phpeso/",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "GitLab",
            "url": "https://gitlab.com/phpeso/",
            "icon": "fa-brands fa-square-gitlab",
            "type": "fontawesome",
        },
        {
            "name": "Codeberg",
            "url": "https://codeberg.org/phpeso/",
            "icon": "fa-solid fa-mountain",
            "type": "fontawesome",
        },
        {
            "name": "Gitea",
            "url": "https://sandfox.org/phpeso/",
            "icon": "fa-solid fa-mug-hot",
            "type": "fontawesome",
        },
        {
            "name": "Packagist",
            "url": "https://packagist.org/packages/peso/",
            "icon": "https://img.shields.io/packagist/dm/peso/core?style=flat-square",
            "type": "url",
        }
   ]
}

html_context = {
    'current_version': os.environ.get("READTHEDOCS_VERSION_NAME"),
    'github_user': "phpeso",
    'github_repo': "doc",
    'github_version': "v1.x",
    'doc_path': "source",
}

html_favicon = '../logo/logo.png'
