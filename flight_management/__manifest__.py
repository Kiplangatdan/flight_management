# -*- coding: utf-8 -*-
# Copyright 2018 Sunflower IT <http://sunflowerweb.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Flight Management",
    "version": "10.0.1.0.0",
    "category": "Tools",
    "author": "Sunflower IT",
    "website": "https://sunflowerweb.nl",
    "license": "AGPL-3",
    "summary": "Simple flight management ",
    "depends": [
        'base',
    ],
    "data": [
        "data/flight_data.xml",
        "views/menu.xml",
        "views/airplane_airplane.xml",
        "views/airport_airport.xml",
        "views/flight_booking.xml",
        "views/bookings.xml",
        "views/flight_connection.xml",
    ],
    "installable": True,
}
