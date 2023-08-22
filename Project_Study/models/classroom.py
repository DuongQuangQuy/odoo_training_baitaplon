from odoo import models, fields, api, _


class Student(models.Model):
    _name = 'class'
    _description = 'class'
    name = fields.Char(string='name')
