from odoo import models, fields, api


class PositionStatus(models.Model):
    _name = 'position.status'
    _description = 'Position Status'
    _rec_name = 'position_status'

    position_status = fields.Char(string='Status', required=True)
