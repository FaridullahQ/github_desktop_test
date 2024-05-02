from odoo import fields, models, api


class InheritedJob(models.Model):
    _inherit = "hr.job"

    organization_year = fields.Char(string='Year', required='True')
    code = fields.Char(string='Code')
    position_rank_id = fields.Many2one('position.rank', string='Rank')
    position_status_id = fields.Many2one('position.status', string='Status')
    color = fields.Integer(string='Color')
    work_location_id = fields.Many2one('hr.work.location', string='Work Location')
    report_from = fields.Many2many(
        comodel_name='hr.job',
        relation='hr_job_report_from_rel',
        column1='job_id',
        column2='report_id',
        string='Report From',
        help='Select job positions to associate as reports',
    )
    report_to_id = fields.Many2one('hr.job', string='Report To')
    view_type = fields.Selection([('kanban', 'Kanban')], default='kanban')


class InheritedApplicant(models.Model):
    _inherit = "hr.applicant"






