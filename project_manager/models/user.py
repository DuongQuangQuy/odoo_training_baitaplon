from odoo import models, fields, api, _

class user(models.Model):
    _name = "user"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'User'

    name = fields.Char(string = 'name')
    description = fields.Text(string = 'description', translate = True)
    dateline = fields.Date(string = 'dateline')
    product_ids = fields.One2many(comodel_name = "product", inverse_name="user_id", string='assign project')
    product_id = fields.Many2one(comodel_name = "product",string = 'task assign')