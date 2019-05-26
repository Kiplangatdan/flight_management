# -*- coding: utf-8 -*-
# © 2018 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class FlightBooking(models.Model):
    _name = "flight.booking"
    _description = "Flight Bookings"
    _rec_name = 'flight_id'

    flight_id = fields.Char("Flight ID", compute='_compute_flight_id')
    plane_id = fields.Many2one(
        'airplane.airplane', string="Plane", required=True)
    dep_airport_id = fields.Many2one(
        'airport.airport', string="Departure", required=True)
    arr_airport_id = fields.Many2one(
        'airport.airport', string="Arrival", required=True)
    dep_time = fields.Datetime("DepTime", required=True)
    arr_time = fields.Datetime("ArrTime", required=True)
    booking_ids = fields.One2many(
        'booking.booking', 'flight_id', string="Bookings")
    connection_ids = fields.One2many(
        'flight.connection', 'second_flight_id', "Connections")
    count_bookings = fields.Integer(
        'Bookings', compute='_compute_bookings_connections')
    count_connections = fields.Integer(
        'Connections', compute='_compute_bookings_connections')

    @api.multi
    def _compute_bookings_connections(self):
        for this in self:
            this.count_bookings = len(this.booking_ids)
            this.count_connections = len(this.connection_ids)

    @api.multi
    @api.depends('plane_id', 'dep_airport_id', 'arr_airport_id')
    def _compute_flight_id(self):
        for this in self:
            dep_code = this.dep_airport_id.code
            arr_code = this.arr_airport_id.code
            code = "{}-{}-{}".format(
                dep_code if dep_code else '', arr_code if arr_code else '',
                this.plane_id.name if this.plane_id else '')
            this.flight_id = code

    @api.constrains('dep_airport_id', 'dep_airport_id')
    def _check_airports(self):
        for this in self:
            if this.dep_airport_id == this.arr_airport_id:
                raise ValidationError(
                    _('Departure and Arrival cannot be the same. '
                      'Choose another airport!'))
