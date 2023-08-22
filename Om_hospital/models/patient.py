from odoo import models, fields, api, _

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    name_customer = fields.Char(string='name_customer')

class HospitalPatient(models.Model):
    _name = "patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string ='Name')
    patient_age = fields.Integer('Age')
    note = fields.Text(string = 'Note')
    image = fields.Binary(string = "image")
    name = fields.Char(string = 'Test')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result