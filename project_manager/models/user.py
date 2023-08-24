from odoo import models, fields, api, _


class user(models.Model):
    _name = "user"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'User'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description', translate=True)
    dateline = fields.Date(string='Dateline')
    assignee = fields.Char(string='Assignee')
    product_ids = fields.One2many(comodel_name="product", inverse_name="user_id", string='Assign Project Managers')
    # product_id = fields.Many2one(comodel_name = "product",string = 'Task Attendees')
