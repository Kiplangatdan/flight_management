# -*- coding: utf-8 -*-
# Copyright 2018 Sunflower IT <http://sunflowerweb.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, tools, exceptions


class Airplane(models.Model):
    _name = 'airplane.airplane'
    _description = 'Airplane registration'

    name = fields.Char('Reg.', track_visibility='always', required=True)
    type = fields.Char('Aircraft Type')
    operator = fields.Char('Operator')
    status = fields.Selection(
        [('active', "Active"), ('retired', "Retired")],
        default='active', string="Status")
