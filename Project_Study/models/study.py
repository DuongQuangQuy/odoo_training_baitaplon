from odoo import models, fields, api, _


class ProjectStudy(models.Model):
    _name = "project.study"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Study'

    study_name = fields.Char(string='Name', tracking=True, required=True)
    start_date = fields.Date(string='Start Date', tracking=True, required=True)
    end_date = fields.Date(string='End Date', tracking=True, required=True )
    deadline = fields.Datetime(string='Deadline', tracking=True, required=True)
    assign_to = fields.Many2many(comodel_name = 'res.partner',string = 'Assigned to')
    customer = fields.Many2one(comodel_name = 'res.partner', string='Customer')
    state = fields.Selection(selection=[
        ('to do', 'To Do'),
        ('in progress', 'In Progress'),
        ('review', 'Review'),
        ('done', 'Done'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='to do')

    def action_to_do(self):
        for rec in self:
            rec.state = 'to do'

    def action_in_progress(self):
        for rec in self:
            rec.state = 'in progress'

    def action_review(self):
        for rec in self:
            rec.state = 'review'

    def action_done(self):
        for rec in self:
            rec.state = 'done'
