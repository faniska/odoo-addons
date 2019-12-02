# -*- coding: utf-8 -*-
{
    'name': 'Hide Action Buttons',
    'version': '1.0',
    'category': 'Hidden',
    'author': 'XFanis',
    'support': 'dev@xfanis.ru',
    'website': 'xfanis.ru',
    'license': 'LGPL-3',
    'description': """
    This module provides ability to hide action buttons (Create/Edit) in form views based on conditions of record.

    ##Steps:##    
    1. install module    
    2. add computable boolean field named as "hide_action_buttons" for model
    3. implement computation by your business process for field hide_action_buttons
    4. insert the field "hide_action_buttons" in the form view of the model

    More details in the readme.md
    """,
    'depends': ['web'],
    'data': ['backend_assets.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
