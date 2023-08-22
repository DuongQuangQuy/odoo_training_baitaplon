from odoo import models, fields, api, _

class product(models.Model):
    _name = "product"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Product'

    name = fields.Char(string = 'name')
    user_id = fields.Many2one(comodel_name = "user", string='assign project')
    user_ids = fields.One2many(comodel_name="user", inverse_name="product_id", string='task assign')
    user_product_ids = fields.Many2many("user", string='assign project test')