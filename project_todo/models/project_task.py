# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    use_todo = fields.Boolean("Use ToDo", related='project_id.use_todo')
    todo_list = fields.One2many('project.task.todo', 'task_id', 'ToDo List')
