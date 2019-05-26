# -*- coding: utf-8 -*-
# Copyright 2018 Sunflower IT <http://sunflowerweb.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, tools, exceptions


class Airport(models.Model):
    _name = 'airport.airport'
    _description = 'Airports'

    name = fields.Char('Name', track_visibility='always', required=True)
    code = fields.Char('Airport Code', required=True)
    city = fields.Char("City")
    country_id = fields.Many2one('res.country', required=True, string="Country")
