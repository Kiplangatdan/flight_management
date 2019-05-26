# -*- coding: utf-8 -*-
# © 2018 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class Bookings(models.Model):
    _name = "booking.booking"
    _description = "Bookings per flight"
    _rec_name = 'booking_number'

    flight_id = fields.Many2one(
        'flight.booking', string="Flight ID", required=True)
    booking_number = fields.Char('Passenger ID', default='New')
    passenger_ids = fields.Many2many(
        'res.partner', 'booking_id', 'bookings', string="Passengers")
    connection_ids = fields.One2many('flight.connection', 'passenger_id', "Connections")

    @api.model
    def create(self, vals):
        if vals.get('booking_number', 'New') == 'New':
            vals['booking_number'] = self.env['ir.sequence'].next_by_code(
                'booking.booking') or '/'
        return super(Bookings, self).create(vals)
