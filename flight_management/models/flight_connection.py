# -*- coding: utf-8 -*-
# © 2018 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class FlightConnection(models.Model):
    _name = "flight.connection"
    _description = "Flight Connection"

    name = fields.Char(compute='_compute_name')
    passenger_id = fields.Many2one(
        'booking.booking', string="Passenger ID", required=True)
    first_flight_id = fields.Many2one(
        related='passenger_id.flight_id', string="First Flight ID", readonly=1)
    second_flight_id = fields.Many2one(
        'flight.booking', "Second Flight ID", required=1)
    airport_id = fields.Many2one(
        'airport.airport', "Airport", required=True)

    @api.multi
    @api.depends('passenger_id')
    def _compute_name(self):
        for this in self:
            if this.passenger_id:
                this.name = "CONN-%s" % this.passenger_id.booking_number

    @api.constrains('first_flight_id', 'second_flight_id')
    def _check_flights(self):
        for this in self:
            if this.first_flight_id == this.second_flight_id:
                raise ValidationError(
                    'Second Flight Cannot be the same as the first Flight!')
