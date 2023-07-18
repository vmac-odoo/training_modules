from odoo import models, fields

class MotorcycleRegistry(models.Model):

    _name = 'motorcycle.registry'

    registry_number = fields.Char(
        string='Registry Number',
        required=True,
        _rec_name=
