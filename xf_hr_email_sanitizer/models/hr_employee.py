# -*- coding: utf-8 -*-
import re
from email.utils import parseaddr

from odoo import models, api, _
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _inherit = "hr.employee"

    def sanitize_email_address(self, email):
        # get config parameters
        email_regex = self.env['ir.config_parameter'].get_param('hr.work.email.regex')
        work_email_domain = self.env['ir.config_parameter'].get_param('hr.work.email.domain')

        # parse email address
        addr = parseaddr(email)
        email_address = addr[1].lower()

        # step 1 - check whether the email address is parsed correctly
        if not email_address:
            raise ValidationError(_('Please enter correct email address!'))

        # step 2 - check if the email address matches the regular expression
        if email_regex and not (re.search(email_regex, email_address)):
            raise ValidationError(_('Please enter correct email address!'))

        # step 3 - check if the email address contains the correct domain
        domain = email_address.split('@')[1]
        if work_email_domain and domain != work_email_domain:
            raise ValidationError(_('The correct working email address must contain the corporate domain "@%s"') % work_email_domain)

        return email_address

    @api.model
    def create(self, vals):
        if 'work_email' in vals:
            vals['work_email'] = self.sanitize_email_address(vals['work_email'])
        return super(Employee, self).create(vals)

    def write(self, vals):
        if 'work_email' in vals:
            vals['work_email'] = self.sanitize_email_address(vals['work_email'])
        return super(Employee, self).write(vals)
