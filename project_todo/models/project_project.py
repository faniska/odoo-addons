# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields


class Project(models.Model):
    _inherit = 'project.project'

    use_todo = fields.Boolean("Use ToDo")
