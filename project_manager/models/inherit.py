import string

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class User_inherit(models.Model):
    _inherit = "user"
    _description = 'Fix_User'

    assign_update = fields.Datetime(string='Assign update')
    customer = fields.Many2one('res.partner',string = 'Customer')

    @api.model 
    def _default_assignee_to(self):
        product_learn_id = self.env['product'].search([('name', '=', 'New Feature')], limit=1)
        if not product_learn_id:
            vals = {
                'name': 'New Feature',
            }
            product_learn_id = self.env['product'].create(vals)
        return product_learn_id

    assignee_to = fields.Many2many("product", 'user_rel', string='Assignee to', default=_default_assignee_to)

    # @api.depends('assignee_to')
    # def assign_update_time(self):
    #     for rec in self:
    #         if rec.assignee_to:
    #             rec.assign_update = rec.write_date


    @api.onchange('assignee_to')
    def onchange_assignee_to(self):
        for record in self:
            if record.assignee_to:
                record.assign_update = record.write_date


    @api.onchange('customer')
    def onchange_customer(self):
        for record in self:
            if record.customer:
                customer_id = self.env['user'].search([('customer','=',record.customer.id)],limit=1 )
                if customer_id:
                    raise ValidationError(_('This customer is existed at another task. Please choose another customer'))

