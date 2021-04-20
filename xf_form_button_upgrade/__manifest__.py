# -*- coding: utf-8 -*-
{
    'name': 'Form Button Upgrade',
    'version': '1.0.0',
    'category': 'Extra Tools',
    'author': 'XFanis',
    'support': 'dev@xfanis.ru',
    'website': 'https://xfanis.ru',
    'license': 'LGPL-3',
    'summary': 'Skip required field validation when the action button is clicked',
    'description': """
    This module provides ability to skip/bypass validation of required/mandatory fields when the action button is clicked.
    Just add the special context value for the button and use.
    """,
    'depends': ['web'],
    'data': ['views/assets.xml'],
    'images': [
        'static/description/thumbnail_1.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
