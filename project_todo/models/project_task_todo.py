# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ProjectTaskToDo(models.Model):
    _name = 'project.task.todo'
    _order = 'date DESC, id DESC'
    task_id = fields.Many2one('project.task', 'Task', required=True)
    name = fields.Char('ToDo', required=True)
    date = fields.Datetime('Date')

    @api.multi
    def action_done(self):
        return self.write({'date': fields.Datetime.now()})

    @api.multi
    def action_new(self):
        return self.write({'date': False})
