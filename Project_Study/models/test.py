from odoo import models, fields, api, _


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"
    _description = 'Sale.order'

    name_customer = fields.Char(string='name_customer')


class Student(models.Model):
    _name = "student"
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string='name')
    description = fields.Text(string='description', translate=True)
    dateline = fields.Date(string='dateline')
    student_id = fields.Many2one("class", string='assign to')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('student.sequence') or _('New')
        result = super(student, self).create(vals)
        return result
