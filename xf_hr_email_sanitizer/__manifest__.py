# -*- coding: utf-8 -*-
{
    'name': 'Sanitize Working Email Address',
    'version': '11.0.1.0.0',
    'category': 'Human Resources',
    'author': 'XFanis',
    'support': 'dev@xfanis.ru',
    'website': 'https://xfanis.ru',
    'license': 'LGPL-3',
    'summary': 'Strict validation of employee email addresses to prevent mistakes',
    'description': """
    This module provides ability to check if working email address is correct and contains corporate domain.
    """,
    'depends': ['hr'],
    'data': ['data/config_parameter.xml'],
    'images': [
        'static/description/xf_email_sanitizer_image_1.png',
        'static/description/xf_email_sanitizer_image_2.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
