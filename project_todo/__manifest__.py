# -*- coding: utf-8 -*-

{
    'name': 'Project Task ToDO Lists',
    'version': '1.0',
    'author': 'XFanis',
    'support': 'dev@xfanis.ru',
    'website': 'xfanis.ru',
    'license': 'LGPL-3',
    'category': 'Operations/Project',
    'sequence': 10,
    'summary': 'Add ToDo list for project tasks',
    'depends': [
        'project',
    ],
    'description': """
    This module allows to add ToDo list for tasks and mark list items as done step by step.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/project_todo_views.xml',
    ],
    'images': [
        'static/description/Step_2_ToDo_List_Tab.png',
        'static/description/Step_1_Enable_ToDo_List.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
